#!/usr/bin/env python3
"""Pre-download DeepFace models to avoid hanging during analysis"""

print("Downloading DeepFace models...")
print("This may take a few minutes on first run...")

# Set environment to suppress warnings
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

try:
    from deepface import DeepFace
    import cv2
    import numpy as np
    
    # Create a dummy image to trigger model downloads
    dummy_img = np.zeros((224, 224, 3), dtype=np.uint8)
    dummy_img[:] = 128  # Gray image
    
    # Save temporarily
    cv2.imwrite('/tmp/dummy_face.jpg', dummy_img)
    
    print("\nDownloading age, gender, race, and emotion models...")
    
    # This will download all models if not present
    result = DeepFace.analyze(
        img_path='/tmp/dummy_face.jpg',
        actions=['age', 'gender', 'race', 'emotion'],
        detector_backend='skip',
        enforce_detection=False,
        silent=False  # Show download progress
    )
    
    print("\n✅ All models downloaded successfully!")
    print("Face analysis can now run without delays.")
    
    # Clean up
    os.remove('/tmp/dummy_face.jpg')
    
except Exception as e:
    print(f"\n❌ Error downloading models: {e}")
    print("You may need to run this script again or download models manually.")