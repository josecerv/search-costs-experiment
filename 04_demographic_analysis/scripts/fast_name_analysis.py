#!/usr/bin/env python3
"""
Fast parallel name analysis with increased concurrency
"""

import sys
from pathlib import Path
import os
from dotenv import load_dotenv
import asyncio
import aiohttp
from openai import AsyncOpenAI
import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor
import json

# Load environment variables
env_path = Path(__file__).parent.parent.parent / '.env'
if env_path.exists():
    load_dotenv(env_path)

# Add parent directories to path
sys.path.append(str(Path(__file__).parent.parent.parent / "03_data_collection"))
from config.settings import config
sys.path.append(str(Path(__file__).parent.parent / "core"))
from speaker_database import SpeakerDatabase

class FastNameAnalyzer:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.speaker_db = SpeakerDatabase()
        
    async def analyze_name_async(self, speaker_info):
        """Async version of name analysis"""
        speaker_id = speaker_info['speaker_id']
        
        # Check cache first
        cached = self.speaker_db.get_name_analysis(speaker_id)
        if cached and cached.get('name_analysis_success') is not None:
            return {'speaker_id': speaker_id, 'success': True, 'cached': True}
            
        try:
            name = speaker_info.get('name', '')
            if not name.strip():
                # No name - mark as failed
                result = {
                    'speaker_id': speaker_id,
                    'name_gender': 'unknown',
                    'name_gender_confidence': 0.0,
                    'name_race': 'unknown',
                    'name_race_confidence': 0.0,
                    'name_analysis_success': False,
                    'analysis_timestamp': pd.Timestamp.now().isoformat(),
                    'gpt_model_used': 'no_name'
                }
                self.speaker_db.add_name_analysis(result)
                return {'speaker_id': speaker_id, 'success': False, 'error': 'No name'}
                
            # Create prompt
            prompt = f"""Analyze the demographic characteristics based solely on this name:

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
   - native american (Native American origins)
   (You MUST choose one - no unknown/mixed/other options)

IMPORTANT:
- You MUST make a determination even if uncertain - choose the most likely option
- If the name could belong to multiple categories, choose the single most likely one
- Use lower confidence scores (0.3-0.5) when uncertain, but still make a choice

Respond in JSON format:
{{
    "gender": "your_assessment",
    "gender_confidence": 0.0-1.0,
    "race": "your_assessment", 
    "race_confidence": 0.0-1.0,
    "reasoning": "brief explanation"
}}"""

            # Make async API call
            response = await self.client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert in demographic analysis based solely on names. You MUST always provide a definitive answer choosing from the allowed categories only. Never use 'unknown' or refuse to make a determination."
                    },
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
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
            
            analysis_data = json.loads(content)
            
            # Standardize values - ONLY Male/Female allowed
            gender_map = {
                'male': 'Male',
                'female': 'Female',
                'm': 'Male',
                'f': 'Female',
                'man': 'Male',
                'woman': 'Female'
            }
            gender_raw = analysis_data.get('gender', '')
            gender = gender_map.get(gender_raw.lower(), gender_raw)
            # Validate gender is in allowed list
            if gender not in ['Male', 'Female']:
                raise ValueError(f"Invalid gender '{gender}' - must be Male or Female")
            
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
            race_raw = analysis_data.get('race', '')
            race = race_map.get(race_raw.lower(), race_raw.lower())
            # Validate race is in allowed list
            allowed_races = ['white', 'black', 'latino', 'asian', 'native american']
            if race not in allowed_races:
                raise ValueError(f"Invalid race '{race}' - must be one of: {', '.join(allowed_races)}")
            
            # Create result
            result = {
                'speaker_id': speaker_id,
                'name_gender': gender,
                'name_gender_confidence': float(analysis_data.get('gender_confidence', 0)),
                'name_race': race,
                'name_race_confidence': float(analysis_data.get('race_confidence', 0)),
                'name_analysis_success': True,
                'analysis_timestamp': pd.Timestamp.now().isoformat(),
                'gpt_model_used': 'gpt-4o'
            }
            
            # Save to cache
            self.speaker_db.add_name_analysis(result)
            
            return {'speaker_id': speaker_id, 'success': True, 'cached': False}
            
        except Exception as e:
            # Save failed result
            failed_result = {
                'speaker_id': speaker_id,
                'name_gender': 'unknown',
                'name_gender_confidence': 0.0,
                'name_race': 'unknown',
                'name_race_confidence': 0.0,
                'name_analysis_success': False,
                'analysis_timestamp': pd.Timestamp.now().isoformat(),
                'gpt_model_used': 'failed'
            }
            self.speaker_db.add_name_analysis(failed_result)
            
            return {'speaker_id': speaker_id, 'success': False, 'error': str(e)}
    
    async def process_batch_async(self, batch, semaphore):
        """Process a batch with rate limiting"""
        async with semaphore:
            tasks = [self.analyze_name_async(row) for _, row in batch.iterrows()]
            return await asyncio.gather(*tasks)
    
    async def analyze_all_async(self, speakers_df, max_concurrent=150, batch_size=300):
        """Analyze all speakers with high concurrency"""
        print(f"\n🚀 Fast parallel analysis of {len(speakers_df)} speakers")
        print(f"   Concurrency: {max_concurrent} requests")
        print(f"   Batch size: {batch_size}")
        
        # Create semaphore for rate limiting
        semaphore = asyncio.Semaphore(max_concurrent)
        
        # Split into batches
        batches = [
            speakers_df.iloc[i:i + batch_size] 
            for i in range(0, len(speakers_df), batch_size)
        ]
        
        # Process all batches
        start_time = time.time()
        all_results = []
        
        for i, batch in enumerate(batches):
            batch_results = await self.process_batch_async(batch, semaphore)
            all_results.extend(batch_results)
            
            # Progress update
            completed = (i + 1) * batch_size
            progress = min(completed / len(speakers_df) * 100, 100)
            elapsed = time.time() - start_time
            rate = completed / elapsed if elapsed > 0 else 0
            eta = (len(speakers_df) - completed) / rate if rate > 0 else 0
            
            print(f"   Progress: {i+1}/{len(batches)} batches ({progress:.1f}%) "
                  f"| {rate:.1f} speakers/sec | ETA: {eta/60:.1f} min")
            
            # Save progress every 10 batches
            if (i + 1) % 10 == 0:
                self.speaker_db.save_all()
                print("   💾 Progress saved")
                
            # Small delay between batches to respect rate limits
            await asyncio.sleep(0.1)
        
        # Final save
        self.speaker_db.save_all()
        
        # Summary
        elapsed = time.time() - start_time
        successful = sum(1 for r in all_results if r['success'])
        cached = sum(1 for r in all_results if r.get('cached', False))
        
        print(f"\n✅ Analysis complete in {elapsed/60:.1f} minutes")
        print(f"   Total: {len(all_results)}")
        print(f"   Successful: {successful}")
        print(f"   From cache: {cached}")
        print(f"   New analyses: {successful - cached}")
        print(f"   Failed: {len(all_results) - successful}")
        print(f"   Average rate: {len(all_results)/elapsed:.1f} speakers/sec")
        
        return all_results

async def main():
    analyzer = FastNameAnalyzer()
    
    # Get speakers needing analysis
    speakers = analyzer.speaker_db.get_speakers_needing_name_analysis()
    print(f"Found {len(speakers)} speakers needing name analysis")
    
    if len(speakers) == 0:
        print("No speakers need analysis!")
        return
        
    # Run fast async analysis
    results = await analyzer.analyze_all_async(
        speakers,
        max_concurrent=150,  # Increased from 50 for faster processing
        batch_size=300      # Increased from 100 for faster processing
    )
    
    print("\n🎉 Fast name analysis complete!")

if __name__ == "__main__":
    asyncio.run(main())