"""
Stable Face Analysis with Process Isolation
Runs DeepFace in separate processes to avoid memory corruption
"""

import pandas as pd
import numpy as np
import cv2
import os
import multiprocessing as mp
from multiprocessing import Queue, Process
import queue
import time
import sys
from pathlib import Path
import warnings
import json

warnings.filterwarnings('ignore')

# Add config to path
sys.path.append(str(Path(__file__).parent.parent.parent / "03_data_collection"))
sys.path.append(str(Path(__file__).parent))
from config.settings import config
from speaker_database import speaker_db
from photo_manager import photo_manager

def analyze_image_in_subprocess(image_path, speaker_id, result_queue):
    """Run DeepFace analysis in an isolated subprocess"""
    try:
        # Import DeepFace here to avoid issues with multiprocessing
        from deepface import DeepFace
        
        # Read image
        image = cv2.imread(str(image_path))
        if image is None:
            result_queue.put({
                'speaker_id': speaker_id,
                'success': False,
                'error': 'Could not read image file'
            })
            return
        
        # Convert BGR to RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Try different backends in order of stability
        backends = ['opencv', 'retinaface', 'mtcnn', 'skip']
        
        for backend in backends:
            try:
                if backend == 'skip':
                    # If all backends fail, use skip
                    analysis = DeepFace.analyze(
                        image,
                        actions=['gender', 'race'],
                        detector_backend='skip',
                        enforce_detection=False,
                        silent=True
                    )
                else:
                    analysis = DeepFace.analyze(
                        image,
                        actions=['gender', 'race'],
                        detector_backend=backend,
                        enforce_detection=False,
                        silent=True
                    )
                
                # Success - parse results
                if isinstance(analysis, list):
                    analysis = analysis[0]
                
                # Extract gender
                gender_data = analysis.get('gender', {})
                if isinstance(gender_data, dict) and gender_data:
                    gender = max(gender_data.items(), key=lambda x: x[1])
                    face_gender = gender[0]
                    face_gender_confidence = gender[1] / 100.0
                else:
                    face_gender = 'unknown'
                    face_gender_confidence = 0.0
                
                # Extract race
                race_data = analysis.get('race', {})
                if isinstance(race_data, dict) and race_data:
                    race = max(race_data.items(), key=lambda x: x[1])
                    face_race = race[0]
                    face_race_confidence = race[1] / 100.0
                else:
                    face_race = 'unknown'
                    face_race_confidence = 0.0
                
                # Put result in queue
                result_queue.put({
                    'speaker_id': speaker_id,
                    'success': True,
                    'face_gender': face_gender,
                    'face_gender_confidence': face_gender_confidence,
                    'face_race': face_race,
                    'face_race_confidence': face_race_confidence,
                    'backend_used': backend
                })
                return
                
            except Exception as e:
                if backend == backends[-1]:  # Last backend
                    result_queue.put({
                        'speaker_id': speaker_id,
                        'success': False,
                        'error': f'All backends failed: {str(e)}'
                    })
                continue
                
    except Exception as e:
        result_queue.put({
            'speaker_id': speaker_id,
            'success': False,
            'error': f'Subprocess error: {str(e)}'
        })

class StableFaceAnalyzer:
    """Face analyzer using process isolation to prevent memory corruption"""
    
    def __init__(self):
        # Set multiprocessing start method
        try:
            mp.set_start_method('spawn', force=True)
        except RuntimeError:
            pass  # Already set
        
        print("Initialized Stable Face Analyzer with process isolation")
    
    def analyze_single_image(self, image_path, speaker_id):
        """Analyze a single image in an isolated process"""
        try:
            # Check if already analyzed
            cached_result = speaker_db.get_face_analysis(speaker_id)
            if cached_result:
                return {
                    'speaker_id': speaker_id,
                    'success': True,
                    'cached': True,
                    'result': cached_result
                }
            
            # Check if image exists
            if not image_path.exists():
                return {
                    'speaker_id': speaker_id,
                    'success': False,
                    'cached': False,
                    'error': 'Image file not found'
                }
            
            # Create queue for result
            result_queue = Queue()
            
            # Run analysis in subprocess
            process = Process(
                target=analyze_image_in_subprocess,
                args=(image_path, speaker_id, result_queue)
            )
            process.start()
            
            # Wait for result with timeout
            try:
                result = result_queue.get(timeout=60)  # 60 second timeout
                process.join()
            except queue.Empty:
                process.terminate()
                process.join()
                
                # Save failed result to cache
                failed_result = {
                    'speaker_id': speaker_id,
                    'face_gender': 'unknown',
                    'face_gender_confidence': 0.0,
                    'face_race': 'unknown',
                    'face_race_confidence': 0.0,
                    'face_analysis_success': False,
                    'analysis_timestamp': pd.Timestamp.now().isoformat(),
                    'deepface_version': 'timeout',
                    'error': 'Analysis timeout after 60 seconds'
                }
                speaker_db.add_face_analysis(failed_result)
                
                return {
                    'speaker_id': speaker_id,
                    'success': False,
                    'cached': False,
                    'error': 'Analysis timeout',
                    'result': failed_result
                }
            
            if result['success']:
                # Create analysis result
                analysis_result = {
                    'speaker_id': speaker_id,
                    'face_gender': result['face_gender'],
                    'face_gender_confidence': result['face_gender_confidence'],
                    'face_race': result['face_race'],
                    'face_race_confidence': result['face_race_confidence'],
                    'face_analysis_success': True,
                    'analysis_timestamp': pd.Timestamp.now().isoformat(),
                    'deepface_version': 'stable_isolated',
                    'backend_used': result.get('backend_used', 'unknown')
                }
                
                # Cache the result
                speaker_db.add_face_analysis(analysis_result)
                
                return {
                    'speaker_id': speaker_id,
                    'success': True,
                    'cached': False,
                    'result': analysis_result
                }
            else:
                # Failed analysis
                failed_result = {
                    'speaker_id': speaker_id,
                    'face_gender': 'unknown',
                    'face_gender_confidence': 0.0,
                    'face_race': 'unknown',
                    'face_race_confidence': 0.0,
                    'face_analysis_success': False,
                    'analysis_timestamp': pd.Timestamp.now().isoformat(),
                    'deepface_version': 'stable_isolated',
                    'error': result.get('error', 'Unknown error')
                }
                
                # Cache the failed result
                speaker_db.add_face_analysis(failed_result)
                
                return {
                    'speaker_id': speaker_id,
                    'success': False,
                    'cached': False,
                    'error': result.get('error', 'Unknown error'),
                    'result': failed_result
                }
                
        except Exception as e:
            # Save failed result to cache
            failed_result = {
                'speaker_id': speaker_id,
                'face_gender': 'unknown',
                'face_gender_confidence': 0.0,
                'face_race': 'unknown',
                'face_race_confidence': 0.0,
                'face_analysis_success': False,
                'analysis_timestamp': pd.Timestamp.now().isoformat(),
                'deepface_version': 'error',
                'error': str(e)
            }
            speaker_db.add_face_analysis(failed_result)
            
            return {
                'speaker_id': speaker_id,
                'success': False,
                'cached': False,
                'error': str(e),
                'result': failed_result
            }
    
    def analyze_speakers_sequential(self, speakers_df):
        """Analyze speakers one by one (safer for memory)"""
        print(f"Starting sequential face analysis for {len(speakers_df)} speakers...")
        print("Using process isolation to prevent memory corruption...")
        
        all_results = []
        cached_count = 0
        successful_count = 0
        
        for idx, (_, speaker_row) in enumerate(speakers_df.iterrows()):
            speaker_id = speaker_row['speaker_id']
            
            # Progress update
            if idx % 10 == 0:
                progress = (idx / len(speakers_df)) * 100
                print(f"Face analysis progress: {idx}/{len(speakers_df)} ({progress:.1f}%)")
                # Save cache periodically
                speaker_db.save_all()
            
            # Get photo path
            photo_path = photo_manager.get_photo_path(speaker_id)
            
            if photo_path is None:
                # No photo available
                failed_result = {
                    'speaker_id': speaker_id,
                    'face_gender': 'unknown',
                    'face_gender_confidence': 0.0,
                    'face_race': 'unknown',
                    'face_race_confidence': 0.0,
                    'face_analysis_success': False,
                    'analysis_timestamp': pd.Timestamp.now().isoformat(),
                    'deepface_version': 'no_photo'
                }
                
                speaker_db.add_face_analysis(failed_result)
                
                all_results.append({
                    'speaker_id': speaker_id,
                    'success': False,
                    'cached': False,
                    'error': 'No photo available',
                    'result': failed_result
                })
                continue
            
            # Analyze the image
            result = self.analyze_single_image(photo_path, speaker_id)
            all_results.append(result)
            
            if result.get('cached', False):
                cached_count += 1
            elif result.get('success', False):
                successful_count += 1
                # Small delay between successful analyses
                time.sleep(0.5)
        
        # Save final cache
        speaker_db.save_all()
        
        # Summary
        total_successful = successful_count + cached_count
        print(f"\nFace analysis complete:")
        print(f"  Total speakers: {len(speakers_df)}")
        print(f"  Successful analyses: {total_successful}")
        print(f"  New analyses: {successful_count}")
        print(f"  Already cached: {cached_count}")
        print(f"  Failed analyses: {len(all_results) - total_successful}")
        
        return all_results
    
    def get_analysis_summary(self):
        """Get summary of face analysis results"""
        face_cache = speaker_db.face_cache
        
        if len(face_cache) == 0:
            return "No face analysis results found"
        
        total = len(face_cache)
        successful = face_cache['face_analysis_success'].sum()
        
        # Gender distribution
        gender_counts = face_cache[face_cache['face_analysis_success']]['face_gender'].value_counts()
        
        # Race distribution  
        race_counts = face_cache[face_cache['face_analysis_success']]['face_race'].value_counts()
        
        summary = f"""
Face Analysis Summary:
  Total analyzed: {total}
  Successful: {successful}
  Failed: {total - successful}
  
Gender Distribution:
{gender_counts.to_string() if not gender_counts.empty else 'No data'}

Race Distribution:
{race_counts.to_string() if not race_counts.empty else 'No data'}
        """
        
        return summary

# Use the stable analyzer
face_analyzer = StableFaceAnalyzer()