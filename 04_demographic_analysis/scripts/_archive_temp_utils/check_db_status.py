#!/usr/bin/env python3
"""Quick database status check"""

import pandas as pd
from pathlib import Path

# Load databases directly
cache_dir = Path(__file__).parent.parent / "cache"
speakers_db = pd.read_csv(cache_dir / "speakers_database.csv")
face_cache = pd.read_csv(cache_dir / "face_analysis_cache.csv") if (cache_dir / "face_analysis_cache.csv").exists() else pd.DataFrame()

print("=== Database Status ===")
print(f"Total speakers: {len(speakers_db)}")
print(f"With photos: {speakers_db['photo_downloaded'].sum()}")
print(f"Without photos: {(~speakers_db['photo_downloaded']).sum()}")
print(f"Face analyzed: {len(face_cache)}")

# Check photo files
photos_dir = Path(__file__).parent.parent / "speaker_photos"
photo_count = len(list(photos_dir.glob("*.jpg")))
print(f"\nPhoto files on disk: {photo_count}")

# Check for mismatches
speakers_with_photos_db = speakers_db['photo_downloaded'].sum()
if speakers_with_photos_db != photo_count:
    print(f"\n⚠️  Mismatch: Database shows {speakers_with_photos_db} but {photo_count} files exist")
else:
    print("\n✅ Database and disk are in sync!")