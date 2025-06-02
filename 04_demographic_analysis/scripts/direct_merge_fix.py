#!/usr/bin/env python3
"""
Direct merge of name analysis cache data into the output files
"""

import pandas as pd
from pathlib import Path

# Paths
base_dir = Path(__file__).parent.parent
cache_dir = base_dir / "cache"
output_dir = base_dir / "outputs"

print("=== Direct Name Analysis Merge Fix ===")

# Load all cache files
print("\nLoading cache files...")
speakers_db = pd.read_csv(cache_dir / "speakers_database.csv", encoding='utf-8-sig')
face_cache = pd.read_csv(cache_dir / "face_analysis_cache.csv", encoding='utf-8-sig')
name_cache = pd.read_csv(cache_dir / "name_analysis_cache.csv", encoding='utf-8-sig')

print(f"  Speakers DB: {len(speakers_db)} records")
print(f"  Face cache: {len(face_cache)} records")
print(f"  Name cache: {len(name_cache)} records")

# Load current output
people_output = pd.read_csv(output_dir / "people_combined_analysis.csv", encoding='utf-8-sig')
appearances_output = pd.read_csv(output_dir / "speaker_appearances_analysis.csv", encoding='utf-8-sig')

print(f"\nCurrent outputs:")
print(f"  People output: {len(people_output)} records")
print(f"  Appearances output: {len(appearances_output)} records")

# Merge name analysis into people output
print("\nMerging name analysis data...")

# First, standardize gender values in name_cache to match expected format
def standardize_gender(gender):
    if pd.isna(gender) or str(gender).lower() == 'unknown':
        return 'unknown'
    gender_str = str(gender).lower()
    if gender_str in ['male', 'man']:
        return 'man'
    elif gender_str in ['female', 'woman']:
        return 'woman'
    else:
        return 'unknown'

# Standardize race values
def standardize_race(race):
    if pd.isna(race) or str(race).lower() == 'unknown':
        return 'unknown'
    race_str = str(race).lower()
    # Map to standard categories
    race_map = {
        'white': 'white',
        'black': 'black', 
        'asian': 'asian',
        'south asian': 'asian',
        'indian': 'asian',
        'hispanic': 'latino',
        'hispanic/latino': 'latino',
        'latino': 'latino',
        'native american': 'native american',
        'middle eastern': 'white',
        'mixed': 'mixed/other',
        'other': 'mixed/other'
    }
    return race_map.get(race_str, 'unknown')

# Apply standardization
name_cache['name_gender'] = name_cache['name_gender'].apply(standardize_gender)
name_cache['name_race'] = name_cache['name_race'].apply(standardize_race)

# Remove existing name analysis columns from people_output
name_cols = ['name_gender', 'name_gender_confidence', 'name_race', 'name_race_confidence', 'name_analysis_success']
for col in name_cols:
    if col in people_output.columns:
        people_output = people_output.drop(columns=[col])

# Merge name cache
people_merged = people_output.merge(
    name_cache[['speaker_id'] + name_cols],
    on='speaker_id',
    how='left'
)

# Fill missing values
people_merged['name_gender'] = people_merged['name_gender'].fillna('unknown')
people_merged['name_race'] = people_merged['name_race'].fillna('unknown')
people_merged['name_gender_confidence'] = people_merged['name_gender_confidence'].fillna(0.0)
people_merged['name_race_confidence'] = people_merged['name_race_confidence'].fillna(0.0)
people_merged['name_analysis_success'] = people_merged['name_analysis_success'].fillna(False)

# Recalculate combined fields
def combine_gender(row):
    valid_genders = ['man', 'woman']
    
    face_gender = standardize_gender(row.get('face_gender', 'unknown'))
    name_gender = row.get('name_gender', 'unknown')
    
    # Prioritize face if high confidence
    if (row.get('face_analysis_success', False) and 
        row.get('face_gender_confidence', 0) > 95 and 
        face_gender in valid_genders):
        return face_gender
    elif name_gender in valid_genders:
        return name_gender
    else:
        return 'unknown'

def combine_race(row):
    valid_races = ['white', 'black', 'latino', 'asian', 'native american']
    
    face_race = standardize_race(row.get('face_race', 'unknown'))
    name_race = row.get('name_race', 'unknown')
    
    # Prioritize face if high confidence
    if (row.get('face_analysis_success', False) and 
        row.get('face_race_confidence', 0) > 99 and 
        face_race in valid_races):
        return face_race
    elif name_race in valid_races:
        return name_race
    else:
        return 'unknown'

people_merged['combined_gender'] = people_merged.apply(combine_gender, axis=1)
people_merged['combined_race'] = people_merged.apply(combine_race, axis=1)

# Recalculate URM status
urm_categories = ['black', 'latino', 'native american']
people_merged['is_urm'] = people_merged['combined_race'].isin(urm_categories)

# Save updated people output
people_merged.to_csv(output_dir / "people_combined_analysis.csv", index=False, encoding='utf-8-sig')
print(f"\nUpdated people analysis saved")
print(f"  Total records: {len(people_merged)}")
print(f"  With name analysis: {(people_merged['name_analysis_success'] == True).sum()}")
print(f"  Combined gender != unknown: {(people_merged['combined_gender'] != 'unknown').sum()}")
print(f"  Combined race != unknown: {(people_merged['combined_race'] != 'unknown').sum()}")

# Update appearances output
print("\nUpdating appearances output...")

# Remove existing demographic columns
demo_cols = ['combined_gender', 'combined_race', 'is_urm', 'face_gender', 'face_gender_confidence', 
             'face_race', 'face_race_confidence', 'name_gender', 'name_gender_confidence', 
             'name_race', 'name_race_confidence', 'face_analysis_success', 'name_analysis_success']

for col in demo_cols:
    if col in appearances_output.columns:
        appearances_output = appearances_output.drop(columns=[col])

# Merge with updated people data
appearances_merged = appearances_output.merge(
    people_merged[['speaker_id'] + demo_cols],
    on='speaker_id',
    how='left'
)

# Save updated appearances output
appearances_merged.to_csv(output_dir / "speaker_appearances_analysis.csv", index=False, encoding='utf-8-sig')
print(f"\nUpdated appearances analysis saved")
print(f"  Total records: {len(appearances_merged)}")
print(f"  With demographics: {appearances_merged['speaker_id'].notna().sum()}")

# Summary statistics
print("\n=== Final Statistics ===")
print(f"\nGender distribution in people data:")
print(people_merged['combined_gender'].value_counts())
print(f"\nRace distribution in people data:")
print(people_merged['combined_race'].value_counts())
print(f"\nURM rate: {people_merged['is_urm'].mean():.1%}")

print("\n✅ Name analysis merge completed successfully!")