#!/usr/bin/env python3
"""
Link existing photos to current speaker database by matching speaker names
"""

import pandas as pd
import os
import sys
from pathlib import Path
from datetime import datetime

# Add paths
sys.path.append(str(Path(__file__).parent.parent.parent / "03_data_collection"))
sys.path.append(str(Path(__file__).parent.parent / "core"))

from config.settings import config
from speaker_database import speaker_db

def link_existing_photos():
    """
    Link existing photos to speakers by:
    1. Building a mapping of old photo IDs to speaker info
    2. Matching to current speaker database
    3. Updating photo metadata
    """
    
    print("=== Linking Existing Photos to Speaker Database ===")
    print(f"Started at: {datetime.now()}")
    
    # Get all existing photos
    photos_dir = config.SPEAKER_PHOTOS_DIR
    existing_photos = list(photos_dir.glob("*_*.jpg"))
    print(f"Found {len(existing_photos)} existing photos")
    
    # Load current speaker database
    speakers_df = speaker_db.speakers_db.copy()
    print(f"Loaded {len(speakers_df)} speakers from database")
    
    # Try to match photos to speakers
    matched = 0
    unmatched_photos = []
    
    # For each speaker, check if any photos might belong to them
    for idx, speaker in speakers_df.iterrows():
        speaker_id = speaker['speaker_id']
        
        # Check if this speaker already has a photo
        if speaker['photo_downloaded']:
            continue
            
        # Look for photos with this speaker_id
        matching_photos = [p for p in existing_photos if p.stem.startswith(speaker_id)]
        
        if matching_photos:
            # Found a direct match!
            photo = matching_photos[0]
            
            # Update speaker database
            speaker_db.mark_photo_downloaded(speaker_id, success=True)
            
            # Add photo metadata
            metadata = {
                'speaker_id': speaker_id,
                'photo_filename': photo.name,
                'photo_url': 'existing_photo',
                'download_timestamp': pd.Timestamp.now().isoformat(),
                'download_success': True,
                'file_size': photo.stat().st_size,
                'image_width': 0,  # Would need to read image to get this
                'image_height': 0,
                'search_query_used': 'linked_existing_photo'
            }
            speaker_db.add_photo_metadata(metadata)
            
            matched += 1
            if matched % 100 == 0:
                print(f"Matched {matched} photos...")
        
    # Save the updated database
    speaker_db.save_all()
    
    print(f"\n=== Linking Complete ===")
    print(f"Successfully linked: {matched} photos")
    print(f"Speakers with photos: {speaker_db.speakers_db['photo_downloaded'].sum()}")
    print(f"Speakers without photos: {(~speaker_db.speakers_db['photo_downloaded']).sum()}")
    
    # Show some examples of linked photos
    linked_examples = speaker_db.photo_metadata[speaker_db.photo_metadata['download_success']].head(5)
    if len(linked_examples) > 0:
        print("\nExample linked photos:")
        for _, row in linked_examples.iterrows():
            speaker = speaker_db.speakers_db[speaker_db.speakers_db['speaker_id'] == row['speaker_id']].iloc[0]
            print(f"  {speaker['name']} -> {row['photo_filename']}")

if __name__ == "__main__":
    link_existing_photos()