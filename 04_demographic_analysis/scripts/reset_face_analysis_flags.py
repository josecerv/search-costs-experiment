#!/usr/bin/env python3
"""
Reset face_analyzed flags in speaker database
"""

import pandas as pd
import sys
from pathlib import Path

# Add paths
sys.path.append(str(Path(__file__).parent.parent.parent / "03_data_collection"))
sys.path.append(str(Path(__file__).parent.parent / "core"))
from config.settings import config

def reset_face_analysis_flags():
    """Reset face_analyzed flags for all speakers"""
    
    database_path = config.SPEAKER_DATABASE
    
    if not database_path.exists():
        print("No speaker database found")
        return
    
    # Load database
    print(f"Loading speaker database from {database_path}")
    speakers_db = pd.read_csv(database_path, encoding='utf-8-sig')
    
    # Count current face_analyzed
    current_analyzed = speakers_db['face_analyzed'].sum() if 'face_analyzed' in speakers_db.columns else 0
    print(f"Current speakers marked as face_analyzed: {current_analyzed}")
    
    # Reset all face_analyzed to False
    if 'face_analyzed' in speakers_db.columns:
        speakers_db['face_analyzed'] = False
    
    # Save database
    speakers_db.to_csv(database_path, index=False, encoding='utf-8-sig')
    print(f"Reset face_analyzed flag for all {len(speakers_db)} speakers")

if __name__ == "__main__":
    reset_face_analysis_flags()