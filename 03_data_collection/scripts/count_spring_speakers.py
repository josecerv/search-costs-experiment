#!/usr/bin/env python3
import pandas as pd
import numpy as np

# Read the Spring data file
file_path = '/mnt/c/Users/jcerv/Jose/search-costs/03_data_collection/raw/master-data-spring.csv'
df = pd.read_csv(file_path, encoding='utf-8-sig')

# Count rows (excluding header)
total_rows = len(df)
print(f"Total rows (excluding header): {total_rows}")

# Count non-empty speaker entries
speaker_count = 0
for i in range(1, 101):  # Check columns 1-100
    first_name_col = f'First Name_{i}'
    if first_name_col in df.columns:
        # Count non-empty first names
        non_empty = df[first_name_col].notna() & (df[first_name_col] != '') & (df[first_name_col].astype(str).str.strip() != '')
        speaker_count += non_empty.sum()

print(f"Total non-empty speaker entries: {speaker_count}")

# Also check how many seminars have at least one speaker
seminars_with_speakers = 0
for idx, row in df.iterrows():
    has_speaker = False
    for i in range(1, 101):
        first_name_col = f'First Name_{i}'
        if first_name_col in df.columns:
            if pd.notna(row[first_name_col]) and str(row[first_name_col]).strip() != '':
                has_speaker = True
                break
    if has_speaker:
        seminars_with_speakers += 1

print(f"Seminars with at least one speaker: {seminars_with_speakers}")

# Get some statistics about speakers per seminar
speakers_per_seminar = []
for idx, row in df.iterrows():
    count = 0
    for i in range(1, 101):
        first_name_col = f'First Name_{i}'
        if first_name_col in df.columns:
            if pd.notna(row[first_name_col]) and str(row[first_name_col]).strip() != '':
                count += 1
    if count > 0:
        speakers_per_seminar.append(count)

if speakers_per_seminar:
    print(f"\nSpeaker statistics for seminars with speakers:")
    print(f"  Average speakers per seminar: {np.mean(speakers_per_seminar):.2f}")
    print(f"  Max speakers in a seminar: {max(speakers_per_seminar)}")
    print(f"  Min speakers in a seminar: {min(speakers_per_seminar)}")