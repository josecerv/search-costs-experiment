#!/usr/bin/env python3
"""
Improved Analysis of Database Treatment Effect with Better Matching

Key improvements:
1. Fuzzy name matching using multiple strategies
2. University normalization using the core normalization module
3. LLM-based matching for ambiguous cases
4. Discipline-aware matching
5. Detailed logging of matches and near-misses
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json
from typing import Dict, List, Set, Tuple, Optional
from collections import defaultdict
import warnings
import logging
from fuzzywuzzy import fuzz
import asyncio
import aiohttp
import os
from datetime import datetime
import hashlib

warnings.filterwarnings('ignore')

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import the standardization module
import sys
sys.path.append('/mnt/c/Users/jcerv/Jose/search-costs')
sys.path.append('/mnt/c/Users/jcerv/Jose/search-costs/03_data_collection/scripts')
from standardize_universities import UniversityStandardizer

# Import the peer analyzer
from identify_peer_urm_speakers import URMPeerAnalyzer

class ImprovedDatabaseAnalyzer(URMPeerAnalyzer):
    def __init__(self):
        super().__init__()
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        
        # Initialize university standardizer
        self.university_standardizer = UniversityStandardizer()
        
        # Cache for LLM results
        self.cache_dir = self.output_dir / "matching_cache"
        self.cache_dir.mkdir(exist_ok=True)
        
        # Track all matches for review
        self.match_log = []
        
        print("\nInitializing improved treatment effect analysis with better matching...")
        
    async def check_name_match_llm(self, name1: str, name2: str, discipline: str) -> Tuple[bool, float]:
        """Use LLM to check if two names likely refer to the same person"""
        # Create cache key
        cache_key = hashlib.md5(f"{name1}|{name2}|{discipline}".encode()).hexdigest()
        cache_file = self.cache_dir / f"name_match_{cache_key}.json"
        
        # Check cache
        if cache_file.exists():
            with open(cache_file, 'r') as f:
                result = json.load(f)
                return result['match'], result['confidence']
        
        prompt = f"""Are these two names likely the same person in {discipline}?

Name 1: {name1}
Name 2: {name2}

Consider:
- Common variations (Bob/Robert, nicknames)
- Middle names/initials
- Hyphenated names
- Cultural naming variations

Respond with JSON: {{"match": true/false, "confidence": 0.0-1.0, "reasoning": "brief explanation"}}"""

        async with aiohttp.ClientSession() as session:
            try:
                async with session.post(
                    'https://api.openai.com/v1/chat/completions',
                    headers={'Authorization': f'Bearer {self.api_key}'},
                    json={
                        'model': 'gpt-4o-mini',
                        'messages': [{'role': 'user', 'content': prompt}],
                        'temperature': 0,
                        'response_format': {'type': 'json_object'}
                    }
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        result = json.loads(data['choices'][0]['message']['content'])
                        
                        # Cache result
                        with open(cache_file, 'w') as f:
                            json.dump(result, f)
                        
                        return result['match'], result['confidence']
                    else:
                        logger.error(f"LLM API error: {response.status}")
                        return False, 0.0
            except Exception as e:
                logger.error(f"LLM matching error: {e}")
                return False, 0.0
    
    def fuzzy_name_match(self, name1: str, name2: str) -> Tuple[bool, float, str]:
        """
        Check if two names match using multiple strategies
        Returns: (is_match, confidence, match_type)
        """
        # Normalize names
        n1 = self.normalize_name(name1)
        n2 = self.normalize_name(name2)
        
        # Exact match
        if n1 == n2:
            return True, 1.0, "exact"
        
        # Check if one is substring of the other (e.g., "John Smith" in "John A. Smith")
        if n1 in n2 or n2 in n1:
            return True, 0.9, "substring"
        
        # Split names into parts
        parts1 = set(n1.split())
        parts2 = set(n2.split())
        
        # Check if last names match and first name is initial or partial
        if len(parts1) >= 2 and len(parts2) >= 2:
            # Get likely last names (usually the longest parts)
            last1 = max(parts1, key=len)
            last2 = max(parts2, key=len)
            
            if last1 == last2:
                # Check if first names are compatible
                first1 = min(parts1 - {last1}, key=len) if len(parts1) > 1 else ""
                first2 = min(parts2 - {last2}, key=len) if len(parts2) > 1 else ""
                
                if first1 and first2:
                    # Check if one is initial of the other
                    if first1[0] == first2[0]:
                        return True, 0.8, "last_match_first_initial"
                    # Check if one contains the other
                    if first1 in first2 or first2 in first1:
                        return True, 0.85, "last_match_first_partial"
        
        # Fuzzy string matching
        ratio = fuzz.ratio(n1, n2)
        token_sort_ratio = fuzz.token_sort_ratio(n1, n2)  # Handles reordered names
        
        # High confidence fuzzy match
        if ratio >= 85 or token_sort_ratio >= 90:
            return True, ratio/100, "fuzzy_high"
        
        # Medium confidence fuzzy match
        if ratio >= 75 or token_sort_ratio >= 80:
            return True, ratio/100, "fuzzy_medium"
        
        return False, ratio/100, "no_match"
    
    async def match_speakers_improved(self, urm_faculty_df: pd.DataFrame, 
                                    seminar_speakers_df: pd.DataFrame,
                                    discipline: str) -> pd.DataFrame:
        """Improved speaker matching with fuzzy logic and LLM fallback"""
        matches = []
        potential_matches = []
        
        # Normalize all names once
        urm_faculty_df['normalized_name'] = urm_faculty_df['Name'].apply(self.normalize_name)
        seminar_speakers_df['normalized_speaker_name'] = seminar_speakers_df['name'].apply(self.normalize_name)
        
        # Normalize universities in URM data
        logger.info(f"Normalizing {len(urm_faculty_df)} URM faculty universities...")
        
        # Get unique universities to normalize
        unique_universities = urm_faculty_df['Schools'].unique().tolist()
        
        # Standardize universities in batch
        standardized = await self.university_standardizer.standardize_universities_batch(unique_universities)
        
        # Map back to dataframe
        urm_faculty_df['normalized_university'] = urm_faculty_df['Schools'].map(standardized)
        
        # For each URM faculty member
        for _, urm in urm_faculty_df.iterrows():
            # First, filter by university if possible
            university_matches = seminar_speakers_df[
                seminar_speakers_df['affiliation'].str.contains(
                    urm['normalized_university'], case=False, na=False
                ) |
                seminar_speakers_df['affiliation'].str.contains(
                    urm['Schools'], case=False, na=False
                )
            ]
            
            # If no university matches, search all speakers
            search_pool = university_matches if len(university_matches) > 0 else seminar_speakers_df
            
            # Check each potential match
            for _, speaker in search_pool.iterrows():
                is_match, confidence, match_type = self.fuzzy_name_match(
                    urm['Name'], speaker['name']
                )
                
                if is_match and confidence >= 0.75:
                    match_record = {
                        'urm_name': urm['Name'],
                        'urm_university': urm['Schools'],
                        'urm_normalized_university': urm['normalized_university'],
                        'urm_title': urm['Title'],
                        'seminar_speaker_name': speaker['name'],
                        'seminar_university': speaker['university'],
                        'seminar_affiliation': speaker['affiliation'],
                        'seminar_date': speaker['date'],
                        'seminar_discipline': speaker['discipline'],
                        'speaker_id': speaker['speaker_id'],
                        'match_confidence': confidence,
                        'match_type': match_type
                    }
                    
                    if confidence >= 0.85:
                        matches.append(match_record)
                    else:
                        potential_matches.append(match_record)
                
                # Log near misses for debugging
                elif confidence >= 0.6:
                    self.match_log.append({
                        'urm_name': urm['Name'],
                        'speaker_name': speaker['name'],
                        'confidence': confidence,
                        'match_type': match_type,
                        'discipline': discipline
                    })
        
        # For potential matches with medium confidence, use LLM
        if potential_matches and len(potential_matches) < 50:  # Limit LLM calls
            logger.info(f"Checking {len(potential_matches)} potential matches with LLM...")
            
            # Run LLM checks asynchronously
            tasks = []
            for pm in potential_matches:
                task = self.check_name_match_llm(
                    pm['urm_name'], 
                    pm['seminar_speaker_name'],
                    discipline
                )
                tasks.append(task)
            
            llm_results = await asyncio.gather(*tasks)
            
            # Add confirmed matches
            for pm, (is_match, llm_confidence) in zip(potential_matches, llm_results):
                if is_match:
                    pm['match_confidence'] = max(pm['match_confidence'], llm_confidence)
                    pm['match_type'] = f"{pm['match_type']}_llm_confirmed"
                    matches.append(pm)
        
        return pd.DataFrame(matches)
    
    async def analyze_treatment_effect_improved(self):
        """Main analysis with improved matching"""
        results = []
        all_matches_detailed = []
        
        # Get all departments
        dept_groups = self.randomization.groupby(['university', 'discipline'])
        
        print(f"\nAnalyzing {len(dept_groups)} departments with improved matching...")
        
        for (university, discipline), dept_data in dept_groups:
            treatment = 1 if dept_data['condition'].iloc[0] == 'treatment' else 0
            
            # Get peer universities and URM faculty
            peers = self.get_peer_universities(university, discipline)
            if not peers:
                continue
                
            potential_urm_faculty = self.get_urm_faculty_for_peers(peers, discipline)
            if potential_urm_faculty.empty:
                continue
            
            # Get actual seminars
            dept_seminars = self.speaker_appearances[
                (self.speaker_appearances['university'] == university) &
                (self.speaker_appearances['discipline'] == discipline)
            ].copy()
            
            if dept_seminars.empty:
                continue
            
            # Match speakers with improved algorithm
            matches = await self.match_speakers_improved(
                potential_urm_faculty, dept_seminars, discipline
            )
            
            # Log matches for this department
            if not matches.empty:
                matches['focal_university'] = university
                matches['focal_discipline'] = discipline
                matches['treatment'] = treatment
                all_matches_detailed.append(matches)
            
            # Calculate metrics
            total_speakers = len(dept_seminars['speaker_id'].unique())
            total_urm_speakers = len(dept_seminars[dept_seminars['is_urm'] == 1]['speaker_id'].unique())
            speakers_from_database = len(matches['speaker_id'].unique()) if not matches.empty else 0
            
            result = {
                'university': university,
                'discipline': discipline,
                'treatment': treatment,
                'num_peer_universities': len(peers),
                'num_potential_urm_in_database': len(potential_urm_faculty),
                'total_speakers': total_speakers,
                'total_urm_speakers': total_urm_speakers,
                'speakers_from_database': speakers_from_database,
                'pct_speakers_from_database': speakers_from_database / total_speakers if total_speakers > 0 else np.nan,
                'pct_urm_from_database': speakers_from_database / total_urm_speakers if total_urm_speakers > 0 else np.nan,
                'any_speaker_from_database': 1 if speakers_from_database > 0 else 0,
                'urm_share_overall': total_urm_speakers / total_speakers if total_speakers > 0 else np.nan,
            }
            
            results.append(result)
            
            # Progress update
            if len(results) % 50 == 0:
                print(f"  Processed {len(results)} departments...")
        
        # Convert to DataFrame
        results_df = pd.DataFrame(results)
        results_df = results_df[results_df['total_speakers'] > 0]
        
        print(f"\nAnalyzed {len(results_df)} departments with speakers")
        
        # Save detailed matches
        if all_matches_detailed:
            all_matches_df = pd.concat(all_matches_detailed, ignore_index=True)
            matches_path = self.output_dir / "peer_urm_matches_improved.csv"
            all_matches_df.to_csv(matches_path, index=False)
            print(f"Saved {len(all_matches_df)} matches to: {matches_path}")
        
        # Save match log for review
        if self.match_log:
            log_df = pd.DataFrame(self.match_log)
            log_path = self.output_dir / "matching_near_misses.csv"
            log_df.to_csv(log_path, index=False)
            print(f"Saved {len(log_df)} near misses for review")
        
        # Calculate and display results
        self.calculate_and_display_treatment_effects(results_df)
        
        # Save main results
        output_path = self.output_dir / "database_treatment_effect_improved.csv"
        results_df.to_csv(output_path, index=False)
        print(f"\nResults saved to: {output_path}")
        
        return results_df
    
    def calculate_and_display_treatment_effects(self, results_df):
        """Calculate and display treatment effects with proper statistics"""
        print("\n" + "="*60)
        print("IMPROVED TREATMENT EFFECT ANALYSIS")
        print("="*60)
        
        # Split by treatment/control
        treatment_df = results_df[results_df['treatment'] == 1]
        control_df = results_df[results_df['treatment'] == 0]
        
        print(f"\nSample sizes:")
        print(f"  Treatment departments: {len(treatment_df)}")
        print(f"  Control departments: {len(control_df)}")
        
        # Key metrics
        metrics = [
            ('pct_speakers_from_database', 'Share of ALL speakers from the URM database'),
            ('pct_urm_from_database', 'Share of URM speakers from the database'),
            ('any_speaker_from_database', 'Probability of selecting ANY speaker from database'),
            ('urm_share_overall', 'Overall URM share')
        ]
        
        print("\n" + "-"*60)
        print("MAIN RESULTS (WITH IMPROVED MATCHING):")
        print("-"*60)
        
        for metric, description in metrics:
            # Remove NaN values
            treatment_vals = treatment_df[metric].dropna()
            control_vals = control_df[metric].dropna()
            
            if len(treatment_vals) == 0 or len(control_vals) == 0:
                continue
                
            # Calculate statistics
            treatment_mean = treatment_vals.mean()
            control_mean = control_vals.mean()
            treatment_se = treatment_vals.sem()
            control_se = control_vals.sem()
            diff = treatment_mean - control_mean
            
            # T-test
            from scipy import stats
            t_stat, p_value = stats.ttest_ind(treatment_vals, control_vals)
            
            # Effect size
            pooled_std = np.sqrt(((len(treatment_vals)-1)*treatment_vals.std()**2 + 
                                 (len(control_vals)-1)*control_vals.std()**2) / 
                                (len(treatment_vals) + len(control_vals) - 2))
            cohens_d = diff / pooled_std if pooled_std > 0 else 0
            
            print(f"\n{description}:")
            print(f"  Treatment: {treatment_mean:.3f} (SE: {treatment_se:.3f}, N={len(treatment_vals)})")
            print(f"  Control:   {control_mean:.3f} (SE: {control_se:.3f}, N={len(control_vals)})")
            print(f"  Difference: {diff:.3f} ({diff/control_mean*100:.1f}% increase)" if control_mean > 0 else f"  Difference: {diff:.3f}")
            print(f"  t-statistic: {t_stat:.2f}, p-value: {p_value:.4f}")
            print(f"  Cohen's d: {cohens_d:.3f}")
            print(f"  Significant: {'Yes' if p_value < 0.05 else 'No' if p_value < 0.1 else 'No'}")

async def main():
    analyzer = ImprovedDatabaseAnalyzer()
    results = await analyzer.analyze_treatment_effect_improved()
    
    print("\n" + "="*60)
    print("INTERPRETATION:")
    print("="*60)
    print("""
The improved matching algorithm:
1. Uses fuzzy string matching for names (handles variations, initials, etc.)
2. Normalizes university names in both datasets
3. Uses GPT-4 for ambiguous cases
4. Considers discipline context

This should capture many more matches than simple exact string matching,
giving us a more accurate picture of the treatment effect.
""")

if __name__ == "__main__":
    asyncio.run(main())