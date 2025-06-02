#!/usr/bin/env python3
"""
Fix corrupted photo_downloaded column in speaker database
"""

import pandas as pd
import sys
from pathlib import Path
from datetime import datetime

# Add paths
sys.path.append(str(Path(__file__).parent.parent.parent / "03_data_collection"))
sys.path.append(str(Path(__file__).parent.parent / "core"))

from config.settings import config
from speaker_database import speaker_db

def fix_photo_database():
    """
    Fix the photo_downloaded column by checking actual photo files
    """
    
    print("=== Fixing Photo Database ===")
    print(f"Started at: {datetime.now()}")
    
    # Get all existing photos
    photos_dir = config.SPEAKER_PHOTOS_DIR
    existing_photo_files = set(p.stem.split('_')[0] for p in photos_dir.glob("*.jpg"))
    print(f"Found {len(existing_photo_files)} unique speaker IDs with photos on disk")
    
    # Load current speaker database
    speakers_df = speaker_db.speakers_db.copy()
    print(f"Loaded {len(speakers_df)} speakers from database")
    
    # Check current state
    print("\nCurrent photo_downloaded values:")
    print(speakers_df['photo_downloaded'].value_counts(dropna=False))
    
    # Fix the photo_downloaded column
    fixed_count = 0
    for idx, speaker in speakers_df.iterrows():
        speaker_id = speaker['speaker_id']
        
        # Check if photo exists on disk
        has_photo = speaker_id in existing_photo_files
        
        # Update if different from current value or if current value is not boolean
        current_value = speaker['photo_downloaded']
        if not isinstance(current_value, bool) or current_value != has_photo:
            speaker_db.speakers_db.loc[idx, 'photo_downloaded'] = has_photo
            fixed_count += 1
    
    # Save the updated database
    speaker_db.save_all()
    
    # Verify the fix
    speakers_with_photos = speaker_db.speakers_db['photo_downloaded'].sum()
    speakers_without_photos = (~speaker_db.speakers_db['photo_downloaded']).sum()
    
    print(f"\n=== Fix Complete ===")
    print(f"Fixed {fixed_count} entries")
    print(f"Speakers with photos: {speakers_with_photos}")
    print(f"Speakers without photos: {speakers_without_photos}")
    print(f"Total photo files: {len(existing_photo_files)}")
    
    # Show the new distribution
    print("\nNew photo_downloaded values:")
    print(speaker_db.speakers_db['photo_downloaded'].value_counts(dropna=False))
    
    # Check for any discrepancies
    db_with_photos = set(speaker_db.speakers_db[speaker_db.speakers_db['photo_downloaded']]['speaker_id'])
    missing_from_db = existing_photo_files - db_with_photos
    missing_from_disk = db_with_photos - existing_photo_files
    
    if missing_from_db:
        print(f"\n⚠️  {len(missing_from_db)} photos on disk not marked in database")
    if missing_from_disk:
        print(f"\n⚠️  {len(missing_from_disk)} speakers marked as having photos but files missing")

if __name__ == "__main__":
    fix_photo_database()