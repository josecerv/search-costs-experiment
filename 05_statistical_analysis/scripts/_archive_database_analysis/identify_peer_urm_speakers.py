#!/usr/bin/env python3
"""
Identify URM Speakers from Peer Universities that Appeared in Seminars

This script:
1. Calculates peer universities for each department using the experimental algorithm
2. Identifies which URM faculty from peer universities were shown in personalized databases
3. Matches these faculty to actual seminar appearances
4. Outputs analysis of potential vs actual URM speaker selection
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json
import hashlib
from collections import defaultdict
import re
from typing import List, Dict, Set, Tuple
import warnings
warnings.filterwarnings('ignore')

class URMPeerAnalyzer:
    def __init__(self):
        self.base_dir = Path("/mnt/c/Users/jcerv/Jose/search-costs")
        self.output_dir = self.base_dir / "05_statistical_analysis/outputs"
        self.output_dir.mkdir(exist_ok=True)
        
        # Load all necessary data
        self.load_data()
        
    def load_data(self):
        """Load all necessary data files"""
        print("Loading data files...")
        
        # Load university rankings
        self.rankings = self.parse_university_rankings()
        
        # Load URM faculty databases
        self.urm_faculty = self.load_urm_databases()
        
        # Load seminar data with speaker demographics
        self.speaker_appearances = pd.read_csv(
            self.base_dir / "04_demographic_analysis/outputs/speaker_appearances_analysis.csv"
        )
        
        # Load randomization data to identify treatment/control
        self.randomization = pd.read_csv(
            self.base_dir / "01_experiment_design/randomized_data.csv"
        )
        # Split department into university and discipline
        self.randomization[['university', 'discipline']] = self.randomization['department'].str.split('-', n=1, expand=True)
        
    def parse_university_rankings(self) -> Dict[str, List[str]]:
        """Parse the unusual university rankings CSV format"""
        rankings_path = self.base_dir / "06_archive/university_ranks.csv"
        
        # Read the CSV
        df = pd.read_csv(rankings_path)
        
        # The format has universities in first column, then rankings are listed vertically
        # Column names tell us which discipline each ranking column represents
        disciplines = {
            'Physics Ranking': 'Physics',
            'Chemistry Ranking': 'Chemistry', 
            'Math Ranking': 'Mathematics',
            'CS Ranking': 'Computer Science',
            'ME Ranking': 'Mechanical Engineering'
        }
        
        rankings = {}
        
        for col, discipline in disciplines.items():
            # Get the ranking column, skipping empty cells
            ranking_list = df[col].dropna().tolist()
            rankings[discipline] = ranking_list
            
        return rankings
        
    def load_urm_databases(self) -> Dict[str, pd.DataFrame]:
        """Load URM faculty databases for each discipline"""
        databases_dir = self.base_dir / "02_intervention_materials/databases"
        urm_faculty = {}
        
        discipline_mapping = {
            'physics': 'Physics',
            'chemistry': 'Chemistry',
            'mathematics': 'Mathematics',
            'computerScience': 'Computer Science',
            'mechanicalEngineering': 'Mechanical Engineering'
        }
        
        for csv_file in databases_dir.glob("*.csv"):
            discipline_key = csv_file.stem
            discipline = discipline_mapping.get(discipline_key, discipline_key.title())
            
            df = pd.read_csv(csv_file)
            urm_faculty[discipline] = df
            print(f"  Loaded {len(df)} URM faculty for {discipline}")
            
        return urm_faculty
        
    def get_peer_universities(self, university: str, discipline: str) -> List[str]:
        """
        Calculate peer universities using the experimental algorithm
        Returns list of peer universities that would be shown
        """
        if discipline not in self.rankings:
            return []
            
        ranking = self.rankings[discipline]
        
        # Find university's position
        try:
            index = ranking.index(university)
        except ValueError:
            # University not in ranking
            return []
            
        # Initial window: ±20 ranks
        min_rank = max(0, index - 20)
        max_rank = min(len(ranking) - 1, index + 20)
        peers = ranking[min_rank:max_rank + 1]
        peers = [p for p in peers if p != university]
        
        # Ensure at least 40 peers (this part is not working correctly in current implementation)
        # Let's implement the expanding window algorithm from the JavaScript
        urm_data = self.urm_faculty.get(discipline, pd.DataFrame())
        
        if not urm_data.empty:
            # Count URM faculty in current peer set
            faculty_count = urm_data[urm_data['Schools'].isin(peers)].shape[0]
            
            rank_inc = 1
            # Expand window until we have at least 20 URM faculty
            while faculty_count < 20 and len(peers) < len(ranking) - 1:
                # Expand upward
                new_peer_above = index - 20 - rank_inc
                if 0 <= new_peer_above < len(ranking) and ranking[new_peer_above] not in peers:
                    peers.insert(0, ranking[new_peer_above])
                    
                # Expand downward  
                new_peer_below = index + 20 + rank_inc
                if 0 <= new_peer_below < len(ranking) and ranking[new_peer_below] not in peers:
                    peers.append(ranking[new_peer_below])
                    
                # Recount faculty
                faculty_count = urm_data[urm_data['Schools'].isin(peers)].shape[0]
                rank_inc += 1
                
        return peers
        
    def get_urm_faculty_for_peers(self, peers: List[str], discipline: str) -> pd.DataFrame:
        """Get URM faculty from peer universities"""
        if discipline not in self.urm_faculty:
            return pd.DataFrame()
            
        urm_df = self.urm_faculty[discipline]
        return urm_df[urm_df['Schools'].isin(peers)]
        
    def normalize_name(self, name: str) -> str:
        """Normalize name for matching"""
        if pd.isna(name):
            return ""
        # Convert to lowercase, remove extra spaces
        name = str(name).lower().strip()
        # Remove common titles
        name = re.sub(r'^(dr|prof|professor)\.?\s+', '', name)
        # Normalize spaces
        name = re.sub(r'\s+', ' ', name)
        return name
        
    def match_speakers(self, urm_faculty_df: pd.DataFrame, seminar_speakers_df: pd.DataFrame) -> pd.DataFrame:
        """Match URM faculty to seminar speakers"""
        matches = []
        
        # Create normalized name columns
        urm_faculty_df['normalized_name'] = urm_faculty_df['Name'].apply(self.normalize_name)
        seminar_speakers_df['normalized_speaker_name'] = seminar_speakers_df['name'].apply(self.normalize_name)
        
        # For each URM faculty member
        for _, urm in urm_faculty_df.iterrows():
            # Try to find matches in seminar speakers
            # Match by normalized name and affiliation
            potential_matches = seminar_speakers_df[
                (seminar_speakers_df['normalized_speaker_name'] == urm['normalized_name']) |
                (seminar_speakers_df['name'].str.contains(urm['Name'], case=False, na=False))
            ]
            
            # Further filter by affiliation if possible
            if len(potential_matches) > 0 and not pd.isna(urm['Schools']):
                affiliation_matches = potential_matches[
                    potential_matches['affiliation'].str.contains(
                        urm['Schools'].split(',')[0], case=False, na=False
                    )
                ]
                if len(affiliation_matches) > 0:
                    potential_matches = affiliation_matches
                    
            for _, match in potential_matches.iterrows():
                matches.append({
                    'urm_name': urm['Name'],
                    'urm_university': urm['Schools'],
                    'urm_title': urm['Title'],
                    'seminar_speaker_name': match['name'],
                    'seminar_university': match['university'],
                    'seminar_date': match['date'],
                    'seminar_discipline': match['discipline'],
                    'speaker_id': match['speaker_id']
                })
                
        return pd.DataFrame(matches)
        
    def analyze_peer_urm_appearances(self):
        """Main analysis function"""
        results = []
        
        # Get unique university-discipline combinations from randomization data
        dept_groups = self.randomization.groupby(['university', 'discipline'])
        
        print(f"\nAnalyzing {len(dept_groups)} departments...")
        
        for (university, discipline), dept_data in dept_groups:
            # Get treatment status
            treatment = 1 if dept_data['condition'].iloc[0] == 'treatment' else 0
            
            # Get peer universities
            peers = self.get_peer_universities(university, discipline)
            
            if not peers:
                continue
                
            # Get URM faculty that would have been shown
            urm_faculty = self.get_urm_faculty_for_peers(peers, discipline)
            
            if urm_faculty.empty:
                continue
                
            # Get seminars for this department
            dept_seminars = self.speaker_appearances[
                (self.speaker_appearances['university'] == university) &
                (self.speaker_appearances['discipline'] == discipline)
            ]
            
            # Match URM faculty to seminar speakers
            matches = self.match_speakers(urm_faculty, dept_seminars)
            
            # Calculate statistics
            num_urm_matches = len(matches['speaker_id'].unique()) if not matches.empty else 0
            matched_speakers = matches['urm_name'].unique()[:5] if not matches.empty else []
            
            result = {
                'university': university,
                'discipline': discipline,
                'treatment': treatment,
                'num_peer_universities': len(peers),
                'num_urm_faculty_shown': len(urm_faculty),
                'num_seminars': len(dept_seminars['seminar_id'].unique()) if not dept_seminars.empty else 0,
                'num_speakers': len(dept_seminars['speaker_id'].unique()) if not dept_seminars.empty else 0,
                'num_urm_matches': num_urm_matches,
                'match_rate': num_urm_matches / len(urm_faculty) if len(urm_faculty) > 0 else 0,
                'peer_universities': ','.join(peers[:5]) + ('...' if len(peers) > 5 else ''),
                'matched_speakers': ','.join(matched_speakers) + ('...' if len(matched_speakers) == 5 else '')
            }
            
            results.append(result)
            
        # Create results DataFrame
        results_df = pd.DataFrame(results)
        
        # Add summary statistics
        print("\n=== SUMMARY STATISTICS ===")
        print(f"Total departments analyzed: {len(results_df)}")
        print(f"Treatment departments: {len(results_df[results_df['treatment'] == 1])}")
        print(f"Control departments: {len(results_df[results_df['treatment'] == 0])}")
        
        # Compare treatment vs control
        treatment_stats = results_df[results_df['treatment'] == 1]['match_rate'].describe()
        control_stats = results_df[results_df['treatment'] == 0]['match_rate'].describe()
        
        print(f"\nTreatment group match rate: {treatment_stats['mean']:.3f} (SD: {treatment_stats['std']:.3f})")
        print(f"Control group match rate: {control_stats['mean']:.3f} (SD: {control_stats['std']:.3f})")
        
        # Save results
        output_path = self.output_dir / "peer_urm_speaker_analysis.csv"
        results_df.to_csv(output_path, index=False)
        print(f"\nResults saved to: {output_path}")
        
        # Also save detailed matches
        all_matches = []
        for (university, discipline), dept_data in dept_groups:
            peers = self.get_peer_universities(university, discipline)
            if not peers:
                continue
            urm_faculty = self.get_urm_faculty_for_peers(peers, discipline)
            if urm_faculty.empty:
                continue
            dept_seminars = self.speaker_appearances[
                (self.speaker_appearances['university'] == university) &
                (self.speaker_appearances['discipline'] == discipline)
            ]
            matches = self.match_speakers(urm_faculty, dept_seminars)
            if not matches.empty:
                matches['focal_university'] = university
                matches['focal_discipline'] = discipline
                matches['treatment'] = 1 if dept_data['condition'].iloc[0] == 'treatment' else 0
                all_matches.append(matches)
                
        if all_matches:
            all_matches_df = pd.concat(all_matches, ignore_index=True)
            matches_path = self.output_dir / "peer_urm_speaker_matches_detailed.csv"
            all_matches_df.to_csv(matches_path, index=False)
            print(f"Detailed matches saved to: {matches_path}")
            
        return results_df

if __name__ == "__main__":
    analyzer = URMPeerAnalyzer()
    results = analyzer.analyze_peer_urm_appearances()