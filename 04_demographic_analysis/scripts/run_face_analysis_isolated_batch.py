#!/usr/bin/env python3
"""
Run face analysis in batches with isolation to avoid memory corruption.
This script processes faces in batches within separate processes for better performance.
"""

import subprocess
import sys
import os
import pandas as pd
from pathlib import Path
import json
import time
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent.parent.parent / '.env'
if env_path.exists():
    load_dotenv(env_path)

# Add paths
sys.path.append(str(Path(__file__).parent.parent / "core"))
sys.path.append(str(Path(__file__).parent.parent.parent / "03_data_collection"))
from speaker_database import speaker_db
from photo_manager import photo_manager
from config.settings import config

def analyze_batch_isolated(batch_data):
    """Run face analysis for a batch of images in an isolated subprocess."""
    
    # Convert batch data to JSON for passing to subprocess
    batch_json = json.dumps(batch_data)
    
    # Create a minimal script that runs in isolation
    script_content = f'''
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import cv2
cv2.setNumThreads(0)

from deepface import DeepFace
import json
import sys

batch_data = json.loads('{batch_json}')
results = []

for item in batch_data:
    speaker_id = item['speaker_id']
    image_path = item['image_path']
    
    try:
        result = DeepFace.analyze(
            img_path=image_path,
            actions=['age', 'gender', 'race'],
            enforce_detection=False,
            detector_backend='opencv',
            silent=True
        )
        
        if isinstance(result, list):
            result = result[0] if result else {{}}
        
        output = {{
            'success': True,
            'speaker_id': speaker_id,
            'age': result.get('age'),
            'gender': {{
                'value': result.get('dominant_gender', '').lower(),
                'confidence': result.get('gender', {{}}).get(
                    result.get('dominant_gender', 'Unknown'), 0
                )
            }},
            'race': {{
                'value': result.get('dominant_race', '').lower(),
                'confidence': result.get('race', {{}}).get(
                    result.get('dominant_race', 'Unknown'), 0
                )
            }}
        }}
        
    except Exception as e:
        output = {{
            'success': False,
            'speaker_id': speaker_id,
            'error': str(e)
        }}
    
    results.append(output)

print(json.dumps(results))
'''
    
    # Run in isolated subprocess
    try:
        result = subprocess.run(
            [sys.executable, '-c', script_content],
            capture_output=True,
            text=True,
            timeout=300  # 5 minutes for larger batch size (25 faces)
        )
        
        if result.returncode == 0 and result.stdout:
            return json.loads(result.stdout.strip())
        else:
            # Return individual failures for each item in batch
            return [
                {
                    'success': False,
                    'speaker_id': item['speaker_id'],
                    'error': f'Process failed: {result.stderr}'
                }
                for item in batch_data
            ]
            
    except subprocess.TimeoutExpired:
        return [
            {
                'success': False,
                'speaker_id': item['speaker_id'],
                'error': 'Batch analysis timed out'
            }
            for item in batch_data
        ]
    except Exception as e:
        return [
            {
                'success': False,
                'speaker_id': item['speaker_id'],
                'error': str(e)
            }
            for item in batch_data
        ]

def main():
    print("=== Isolated Face Analysis (Batch Mode) ===")
    print(f"Started at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Configuration
    BATCH_SIZE = 25  # Increased from 10 for faster processing (still safe with subprocess isolation)
    
    # CRITICAL: Re-link cache before checking who needs analysis
    # This handles the case where main process linked cache but subprocess doesn't see it
    print("🔄 Re-linking face analysis cache...")
    face_linked = 0
    if hasattr(speaker_db, 'face_cache') and len(speaker_db.face_cache) > 0:
        if 'face_analysis_success' in speaker_db.face_cache.columns:
            successful_analyses = speaker_db.face_cache[speaker_db.face_cache['face_analysis_success'] == True]
            for speaker_id in successful_analyses['speaker_id'].unique():
                speaker_mask = speaker_db.speakers_db['speaker_id'] == speaker_id
                if speaker_mask.any() and not speaker_db.speakers_db.loc[speaker_mask, 'face_analyzed'].iloc[0]:
                    speaker_db.speakers_db.loc[speaker_mask, 'face_analyzed'] = True
                    face_linked += 1
            
            if face_linked > 0:
                print(f"  ✅ Re-linked {face_linked} cached face analyses")
                speaker_db._save_speakers_database()
    
    # Get speakers needing face analysis
    speakers_df = speaker_db.get_speakers_needing_face_analysis()
    total_speakers = len(speakers_df)
    
    print(f"Found {total_speakers} speakers needing face analysis")
    print(f"Using batch size: {BATCH_SIZE}")
    
    if total_speakers == 0:
        print("No speakers need face analysis")
        return
    
    # Debug: Show what columns we have
    print(f"\nDebug - DataFrame columns: {speakers_df.columns.tolist()}")
    if len(speakers_df) > 0:
        print(f"Debug - First speaker data: {speakers_df.iloc[0].to_dict()}")
    
    # Process in batches
    processed = 0
    successful = 0
    start_time = time.time()
    batch_data = []
    
    for idx, speaker in speakers_df.iterrows():
        speaker_id = speaker.get('speaker_id', idx)
        
        # Get photo path from photo manager
        photo_path = photo_manager.get_photo_path(speaker_id)
        if not photo_path:
            # Try direct lookup
            pattern = f"{speaker_id}_*.jpg"
            photo_files = list(config.SPEAKER_PHOTOS_DIR.glob(pattern))
            if photo_files:
                photo_path = str(photo_files[0])
            else:
                continue
        else:
            photo_path = str(photo_path)
            
        if not os.path.exists(photo_path):
            continue
        
        batch_data.append({
            'speaker_id': speaker_id,
            'image_path': photo_path
        })
        
        # Process batch when full or at end
        if len(batch_data) >= BATCH_SIZE or idx == speakers_df.index[-1]:
            # Analyze batch in isolation
            batch_results = analyze_batch_isolated(batch_data)
            
            # Process results
            for result in batch_results:
                speaker_id = result['speaker_id']
                
                if result['success']:
                    # Update database
                    speaker_db.add_face_analysis({
                        'speaker_id': speaker_id,
                        'face_gender': result['gender']['value'],
                        'face_gender_confidence': result['gender']['confidence'],
                        'face_race': result['race']['value'], 
                        'face_race_confidence': result['race']['confidence'],
                        'face_analysis_success': True,
                        'analysis_timestamp': pd.Timestamp.now().isoformat(),
                        'deepface_version': 'isolated_subprocess_batch'
                    })
                    speaker_db.mark_face_analyzed(speaker_id, success=True)
                    successful += 1
                else:
                    # Mark as failed
                    speaker_db.add_face_analysis({
                        'speaker_id': speaker_id,
                        'face_gender': 'unknown',
                        'face_gender_confidence': 0.0,
                        'face_race': 'unknown',
                        'face_race_confidence': 0.0,
                        'face_analysis_success': False,
                        'analysis_timestamp': pd.Timestamp.now().isoformat(),
                        'deepface_version': 'isolated_subprocess_batch'
                    })
                    speaker_db.mark_face_analyzed(speaker_id, success=True)
                
                processed += 1
            
            # Clear batch
            batch_data = []
            
            # Progress update
            elapsed = time.time() - start_time
            rate = processed / elapsed if elapsed > 0 else 0
            remaining = (total_speakers - processed) / rate if rate > 0 else 0
            
            print(f"Progress: {processed}/{total_speakers} ({processed/total_speakers*100:.1f}%) "
                  f"| Success: {successful} | "
                  f"Rate: {rate:.1f} faces/sec | "
                  f"ETA: {remaining/3600:.1f} hours")
            
            # Save progress every 50 faces
            if processed % 50 == 0:
                speaker_db.save_all()
                print("All databases saved successfully")
    
    # Final save
    speaker_db.save_all()
    
    # Summary
    elapsed = time.time() - start_time
    print(f"\n=== Analysis Complete ===")
    print(f"Total processed: {processed}")
    print(f"Successful: {successful}")
    print(f"Failed: {processed - successful}")
    print(f"Time elapsed: {elapsed/3600:.1f} hours")
    print(f"Average rate: {processed/elapsed:.1f} faces/sec")

if __name__ == "__main__":
    main()