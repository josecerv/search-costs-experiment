#!/usr/bin/env python3
"""Investigate why some speakers don't have photos"""

import sys
from pathlib import Path
import pandas as pd
sys.path.append(str(Path(__file__).parent.parent.parent / "03_data_collection"))
sys.path.append(str(Path(__file__).parent.parent))

from core.speaker_database import speaker_db

# Get stats
total_speakers = len(speaker_db.speakers_db)
with_photos = speaker_db.speakers_db['photo_downloaded'].sum()
without_photos = total_speakers - with_photos

print(f"Total speakers: {total_speakers}")
print(f"With photos: {with_photos}")
print(f"Without photos: {without_photos}")

# Check photo metadata for failed downloads
failed_downloads = speaker_db.photo_metadata[
    speaker_db.photo_metadata['download_success'] == False
]
print(f"\nFailed photo downloads in metadata: {len(failed_downloads)}")

# Get speakers without photos
speakers_without_photos = speaker_db.speakers_db[
    ~speaker_db.speakers_db['photo_downloaded']
]

print(f"\n=== Sample of speakers without photos ===")
for idx, speaker in speakers_without_photos.head(10).iterrows():
    print(f"  {speaker['name']} | {speaker['university']} | {speaker['discipline']}")

# Check if these speakers have entries in photo metadata
print(f"\n=== Checking photo metadata for these speakers ===")
for idx, speaker in speakers_without_photos.head(5).iterrows():
    metadata = speaker_db.photo_metadata[
        speaker_db.photo_metadata['speaker_id'] == speaker['speaker_id']
    ]
    if len(metadata) > 0:
        print(f"\n{speaker['name']}:")
        print(f"  Download attempts: {len(metadata)}")
        print(f"  Success: {metadata['download_success'].any()}")
        print(f"  Photo URL: {metadata.iloc[0]['photo_url']}")
    else:
        print(f"\n{speaker['name']}: No metadata found")

# Check for duplicate processing
print(f"\n=== Checking for speakers with multiple photo metadata entries ===")
metadata_counts = speaker_db.photo_metadata['speaker_id'].value_counts()
duplicates = metadata_counts[metadata_counts > 1]
print(f"Speakers with multiple metadata entries: {len(duplicates)}")
if len(duplicates) > 0:
    print("Top 5:")
    for speaker_id, count in duplicates.head().items():
        speaker = speaker_db.speakers_db[speaker_db.speakers_db['speaker_id'] == speaker_id]
        if len(speaker) > 0:
            print(f"  {speaker.iloc[0]['name']}: {count} entries")