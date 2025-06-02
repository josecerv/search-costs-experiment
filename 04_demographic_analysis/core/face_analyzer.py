"""
Face analysis module using DeepFace with proper memory management.
"""
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Critical: Set OpenCV threads before any imports
import cv2
cv2.setNumThreads(0)

import json
import time
import pandas as pd
from pathlib import Path
from typing import Dict, Any, Optional
from deepface import DeepFace

# Suppress TensorFlow warnings
import warnings
warnings.filterwarnings('ignore')

class FaceAnalyzer:
    """Face analysis with DeepFace."""
    
    def __init__(self):
        self.version = 'poetry_stable'
        self.models_loaded = False
        
    def _ensure_models_loaded(self):
        """Load DeepFace models on first use."""
        if not self.models_loaded:
            try:
                # Force model download by analyzing a dummy image
                import numpy as np
                dummy_img = np.zeros((224, 224, 3), dtype=np.uint8)
                DeepFace.analyze(
                    dummy_img,
                    actions=['emotion', 'age', 'gender', 'race'],
                    enforce_detection=False,
                    detector_backend='skip',
                    silent=True
                )
                self.models_loaded = True
                print("DeepFace models loaded successfully")
            except Exception as e:
                print(f"Warning: Could not pre-load models: {e}")
    
    def analyze_face(self, image_path: str) -> Dict[str, Any]:
        """Analyze a face image using DeepFace."""
        self._ensure_models_loaded()
        
        try:
            # Verify file exists
            if not os.path.exists(image_path):
                return {
                    'success': False,
                    'error': f'Image file not found: {image_path}',
                    'deepface_version': self.version
                }
            
            # Run DeepFace analysis
            results = DeepFace.analyze(
                img_path=image_path,
                actions=['age', 'gender', 'race'],
                enforce_detection=False,
                detector_backend='opencv',  # Most stable backend
                silent=True
            )
            
            # Handle both single result and list of results
            if isinstance(results, list):
                result = results[0] if results else {}
            else:
                result = results
            
            # Extract and format results
            return {
                'success': True,
                'age': result.get('age'),
                'gender': {
                    'value': result.get('dominant_gender', '').lower(),
                    'confidence': result.get('gender', {}).get(
                        result.get('dominant_gender', 'Unknown'), 0
                    )
                },
                'race': {
                    'value': result.get('dominant_race', '').lower(),
                    'confidence': result.get('race', {}).get(
                        result.get('dominant_race', 'Unknown'), 0
                    )
                },
                'deepface_version': self.version,
                'raw_result': result
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'deepface_version': self.version
            }
    
    def analyze_batch(self, image_paths: list, save_progress_callback=None):
        """Analyze multiple images with progress saving."""
        results = []
        
        for i, image_path in enumerate(image_paths):
            result = self.analyze_face(image_path)
            results.append(result)
            
            # Save progress periodically
            if save_progress_callback and (i + 1) % 10 == 0:
                save_progress_callback()
                print(f"Analyzed {i + 1}/{len(image_paths)} faces")
        
        return results