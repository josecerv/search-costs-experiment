"""
Name Analysis with Caching for Search Costs RCT
Uses GPT-4o with intelligent caching to avoid duplicate analysis
"""

import pandas as pd
import numpy as np
import openai
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import time
import json
import sys
from pathlib import Path

# Add config to path
sys.path.append(str(Path(__file__).parent.parent.parent / "03_data_collection"))
from config.settings import config
sys.path.append(str(Path(__file__).parent))
from speaker_database import speaker_db

class NameAnalyzer:
    """
    Handles name-based demographic analysis with intelligent caching
    """
    
    def __init__(self):
        try:
            from openai import OpenAI
            self.client = OpenAI(api_key=config.OPENAI_API_KEY)
            self.api_available = True
            print("OpenAI client initialized successfully")
        except Exception as e:
            print(f"Warning: OpenAI API not available: {e}")
            self.client = None
            self.api_available = False
    
    def create_analysis_prompt(self, name):
        """Create the analysis prompt for GPT-4o"""
        return f"""Analyze the demographic characteristics based solely on this name:

Name: {name}

Please provide your best assessment of:
1. Gender - Use ONLY these categories:
   - Male
   - Female
   (You MUST choose one - no unknown/non-binary options)

2. Race/Ethnicity - Use ONLY these categories:
   - white (includes European and Middle Eastern origins)
   - black (African or African American origins)
   - latino (Hispanic or Latino origins)
   - asian (includes East Asian, South Asian, and Indian origins)
   - native american (Indigenous peoples of the Americas)
   (You MUST choose one - no unknown/mixed/other options)

CRITICAL REQUIREMENTS:
- You MUST make a determination even if uncertain - NO EXCEPTIONS
- You MUST choose exactly one option from each list above
- DO NOT use any other values like "unknown", "mixed", "other", or "non-binary"
- If uncertain, choose the MOST LIKELY option and use a low confidence score
- Base your assessment ONLY on the name provided
- Mapping rules:
  * Middle Eastern/Arab names → "white"
  * Indian/South Asian names → "asian"
  * Hispanic/Latino/Latina names → "latino"
- For ambiguous names, make your best guess - DO NOT refuse to answer

Respond in this exact JSON format:
{{
    "gender": "your_assessment",
    "gender_confidence": 0.0-1.0,
    "race": "your_assessment", 
    "race_confidence": 0.0-1.0,
    "reasoning": "brief explanation of your assessment based only on the name"
}}

Be conservative with confidence scores - only use high confidence (>0.8) when very certain based on the name alone."""
    
    def analyze_single_name(self, speaker_info):
        """Analyze a single speaker's name"""
        speaker_id = speaker_info['speaker_id']
        
        try:
            # Check if already analyzed
            cached_result = speaker_db.get_name_analysis(speaker_id)
            if cached_result:
                return {
                    'speaker_id': speaker_id,
                    'success': True,
                    'cached': True,
                    'result': cached_result
                }
            
            if not self.api_available:
                # Record as failed due to API unavailability
                failed_result = {
                    'speaker_id': speaker_id,
                    'name_gender': 'unknown',  # Will need special handling
                    'name_gender_confidence': 0.0,
                    'name_race': 'unknown',  # Will need special handling
                    'name_race_confidence': 0.0,
                    'name_analysis_success': False,
                    'analysis_timestamp': pd.Timestamp.now().isoformat(),
                    'gpt_model_used': 'api_unavailable'
                }
                
                speaker_db.add_name_analysis(failed_result)
                
                return {
                    'speaker_id': speaker_id,
                    'success': False,
                    'cached': False,
                    'error': 'OpenAI API not available',
                    'result': failed_result
                }
            
            # Prepare the prompt - only use the name
            name = speaker_info.get('name', '')
            
            if not name.strip():
                # No name to analyze - mark as failed without defaulting
                failed_result = {
                    'speaker_id': speaker_id,
                    'name_gender': 'unknown',  # Will need special handling
                    'name_gender_confidence': 0.0,
                    'name_race': 'unknown',  # Will need special handling
                    'name_race_confidence': 0.0,
                    'name_analysis_success': False,
                    'analysis_timestamp': pd.Timestamp.now().isoformat(),
                    'gpt_model_used': 'no_name'
                }
                
                speaker_db.add_name_analysis(failed_result)
                
                return {
                    'speaker_id': speaker_id,
                    'success': False,
                    'cached': False,
                    'error': 'No name provided',
                    'result': failed_result
                }
            
            prompt = self.create_analysis_prompt(name)
            
            # Make API call
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert in demographic analysis based solely on names and cultural naming patterns. You MUST always provide a definitive answer choosing ONLY from the allowed categories (Male/Female for gender, white/black/latino/asian/native american for race). Never use 'unknown', 'mixed', 'other', or refuse to make a determination. Always choose the most likely option even if uncertain."
                    },
                    {
                        "role": "user", 
                        "content": prompt
                    }
                ],
                temperature=0.1,  # Low temperature for consistency
                max_tokens=300
            )
            
            # Parse response
            content = response.choices[0].message.content.strip()
            
            # Remove markdown code blocks if present
            if content.startswith('```json'):
                content = content[7:]  # Remove ```json
            if content.startswith('```'):
                content = content[3:]  # Remove ```
            if content.endswith('```'):
                content = content[:-3]  # Remove trailing ```
            content = content.strip()
            
            # Try to parse JSON
            try:
                analysis_data = json.loads(content)
            except json.JSONDecodeError:
                # Try to extract JSON from response if it's embedded in text
                import re
                json_match = re.search(r'\{.*\}', content, re.DOTALL)
                if json_match:
                    analysis_data = json.loads(json_match.group())
                else:
                    raise ValueError("Could not parse JSON from response")
            
            # Validate and standardize the response
            gender = analysis_data.get('gender', 'unknown').strip()
            gender_confidence = float(analysis_data.get('gender_confidence', 0.0))
            race = analysis_data.get('race', 'unknown').strip()
            race_confidence = float(analysis_data.get('race_confidence', 0.0))
            reasoning = analysis_data.get('reasoning', '')
            
            # Standardize gender values - ONLY Male/Female allowed
            gender_map = {
                'male': 'Male',
                'female': 'Female',
                'm': 'Male',
                'f': 'Female',
                'man': 'Male',
                'woman': 'Female'
            }
            gender = gender_map.get(gender.lower(), gender)
            # Validate gender is in allowed list
            if gender not in ['Male', 'Female']:
                # Force a retry or log error
                raise ValueError(f"Invalid gender '{gender}' - must be Male or Female")
            
            # Standardize race values - ONLY 5 categories allowed
            race_map = {
                'white': 'white',
                'black': 'black',
                'hispanic': 'latino',
                'hispanic/latino': 'latino',
                'latino': 'latino',
                'latina': 'latino',
                'latinx': 'latino',
                'asian': 'asian',
                'south asian': 'asian',
                'east asian': 'asian',
                'indian': 'asian',
                'native american': 'native american',
                'american indian': 'native american',
                'indigenous': 'native american',
                'middle eastern': 'white',
                'arab': 'white',
                'jewish': 'white',
                'european': 'white'
            }
            race = race_map.get(race.lower(), race.lower())
            # Validate race is in allowed list
            allowed_races = ['white', 'black', 'latino', 'asian', 'native american']
            if race not in allowed_races:
                # Force a retry or log error
                raise ValueError(f"Invalid race '{race}' - must be one of: {', '.join(allowed_races)}")
            
            # Ensure confidence scores are in valid range
            gender_confidence = max(0.0, min(1.0, gender_confidence))
            race_confidence = max(0.0, min(1.0, race_confidence))
            
            # Create analysis result
            analysis_result = {
                'speaker_id': speaker_id,
                'name_gender': gender,
                'name_gender_confidence': gender_confidence,
                'name_race': race,
                'name_race_confidence': race_confidence,
                'name_analysis_success': True,
                'analysis_timestamp': pd.Timestamp.now().isoformat(),
                'gpt_model_used': 'gpt-4o'
            }
            
            # Cache the result
            speaker_db.add_name_analysis(analysis_result)
            
            return {
                'speaker_id': speaker_id,
                'success': True,
                'cached': False,
                'result': analysis_result,
                'reasoning': reasoning
            }
            
        except Exception as e:
            # Record failed analysis
            failed_result = {
                'speaker_id': speaker_id,
                'name_gender': 'unknown',  # Will need special handling
                'name_gender_confidence': 0.0,
                'name_race': 'unknown',  # Will need special handling
                'name_race_confidence': 0.0,
                'name_analysis_success': False,
                'analysis_timestamp': pd.Timestamp.now().isoformat(),
                'gpt_model_used': 'failed'
            }
            
            # Cache the failed result to avoid retrying
            speaker_db.add_name_analysis(failed_result)
            
            return {
                'speaker_id': speaker_id,
                'success': False,
                'cached': False,
                'error': str(e),
                'result': failed_result
            }
    
    def process_speaker_batch(self, speakers_batch):
        """Process a batch of speakers for name analysis"""
        results = []
        
        for _, speaker_row in speakers_batch.iterrows():
            result = self.analyze_single_name(speaker_row)
            results.append(result)
            
            # Rate limiting - OpenAI has strict rate limits
            if not result.get('cached', False):
                time.sleep(config.NAME_BATCH_DELAY)
        
        return results
    
    def analyze_speakers_parallel(self, speakers_df, max_workers=None):
        """Analyze multiple speakers in parallel with caching"""
        if max_workers is None:
            max_workers = config.MAX_WORKERS_NAMES
        
        print(f"Starting parallel name analysis for {len(speakers_df)} speakers...")
        
        # Split into smaller batches for rate limiting
        batch_size = 10  # Smaller batches for API rate limiting
        batches = [
            speakers_df.iloc[i:i + batch_size] 
            for i in range(0, len(speakers_df), batch_size)
        ]
        
        all_results = []
        completed_batches = 0
        total_batches = len(batches)
        cached_count = 0
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all batches
            future_to_batch = {
                executor.submit(self.process_speaker_batch, batch): i
                for i, batch in enumerate(batches)
            }
            
            # Process completed batches
            for future in concurrent.futures.as_completed(future_to_batch):
                batch_num = future_to_batch[future]
                
                try:
                    batch_results = future.result()
                    all_results.extend(batch_results)
                    
                    # Count cached results
                    cached_count += sum(1 for r in batch_results if r.get('cached', False))
                    
                    completed_batches += 1
                    
                    print(f"Name analysis progress: Batch {completed_batches}/{total_batches} "
                          f"({completed_batches/total_batches*100:.1f}%)")
                    
                except Exception as e:
                    print(f"Name analysis batch {batch_num} error: {e}")
                    completed_batches += 1
        
        # Save updated cache
        speaker_db.save_all()
        
        # Summary
        successful = sum(1 for r in all_results if r['success'])
        print(f"\nName analysis complete:")
        print(f"  Total speakers: {len(speakers_df)}")
        print(f"  Successful analyses: {successful}")
        print(f"  Failed analyses: {len(all_results) - successful}")
        print(f"  Already cached: {cached_count}")
        
        return all_results
    
    def get_analysis_summary(self):
        """Get summary of name analysis results"""
        name_cache = speaker_db.name_cache
        
        if len(name_cache) == 0:
            return "No name analysis results found"
        
        total = len(name_cache)
        successful = name_cache['name_analysis_success'].sum()
        
        # Gender distribution
        gender_counts = name_cache[name_cache['name_analysis_success']]['name_gender'].value_counts()
        
        # Race distribution
        race_counts = name_cache[name_cache['name_analysis_success']]['name_race'].value_counts()
        
        # Confidence statistics
        gender_conf_avg = name_cache[name_cache['name_analysis_success']]['name_gender_confidence'].mean()
        race_conf_avg = name_cache[name_cache['name_analysis_success']]['name_race_confidence'].mean()
        
        summary = f"""
Name Analysis Summary:
  Total analyzed: {total}
  Successful: {successful}
  Failed: {total - successful}
  
  Average Confidence:
    Gender: {gender_conf_avg:.3f}
    Race: {race_conf_avg:.3f}
  
Gender Distribution:
{gender_counts.to_string()}

Race Distribution:
{race_counts.to_string()}
        """
        
        return summary

# Global name analyzer instance
name_analyzer = NameAnalyzer()