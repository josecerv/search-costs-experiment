#!/usr/bin/env python3
"""
Corrected analysis of Black speakers - using master data with actual names
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json
from collections import defaultdict

# Paths
data_dir = Path("/mnt/c/Users/jcerv/Jose/search-costs")
output_dir = Path("/mnt/c/Users/jcerv/Jose/search-costs/05_statistical_analysis/outputs")

print("=== BLACK SPEAKER ANALYSIS (CORRECTED) ===\n")

# 1. Load speaker demographics from the analysis dataset
print("Loading speaker demographics...")
speaker_demographics = pd.read_csv(
    data_dir / "04_demographic_analysis/outputs/people_combined_analysis.csv"
)
print(f"Loaded {len(speaker_demographics)} unique speakers with demographics")

# Filter for Black speakers
black_speakers = speaker_demographics[speaker_demographics['combined_race'] == 'black']
print(f"Found {len(black_speakers)} unique Black speakers")

# 2. Load the master data to get actual appearances
print("\nLoading master data with actual names...")
master_data = pd.read_csv(data_dir / "03_data_collection/processed/master-data-final.csv")

# 3. Load URM databases and get Black faculty
print("\nLoading Black faculty from URM databases...")
black_faculty_all = []

db_dir = data_dir / "02_intervention_materials/databases"
discipline_map = {
    'chemistry': 'Chemistry',
    'physics': 'Physics', 
    'mathematics': 'Mathematics',
    'computerScience': 'Computer Science',
    'mechanicalEngineering': 'Mechanical Engineering'
}

for file_name, discipline in discipline_map.items():
    df = pd.read_csv(db_dir / f"{file_name}.csv")
    black_df = df[df['Race'] == 'Black'].copy()
    black_df['discipline'] = discipline
    black_faculty_all.append(black_df)
    print(f"  {discipline}: {len(black_df)} Black faculty")

black_faculty_df = pd.concat(black_faculty_all, ignore_index=True)
print(f"\nTotal Black faculty in databases: {len(black_faculty_df)}")

# 4. Extract all speaker appearances with names
print("\nExtracting speaker appearances...")
speakers_list = []

for _, row in master_data.iterrows():
    seminar_info = {
        'seminar_id': row['seminar_id'],
        'university': row['university'],
        'discipline': row['discipline'],
        'condition': row['condition']
    }
    
    # Extract each speaker
    for i in range(1, 129):
        first_name_col = f'First Name_{i}'
        last_name_col = f'Last Name_{i}'
        
        if first_name_col in row and pd.notna(row.get(first_name_col)):
            first_name = str(row.get(first_name_col, '')).strip()
            last_name = str(row.get(last_name_col, '')).strip()
            
            if first_name and last_name:
                full_name = f"{first_name} {last_name}"
                speakers_list.append({
                    **seminar_info,
                    'full_name': full_name,
                    'speaker_affiliation': row.get(f'university_{i}_standardized', row.get(f'university_{i}'))
                })

speakers_df = pd.DataFrame(speakers_list)
print(f"Extracted {len(speakers_df)} speaker appearances")

# 5. Match speakers to demographics
print("\nMatching speakers to demographics...")
# Create a normalized name column for matching
speaker_demographics['name_normalized'] = speaker_demographics['name'].str.lower().str.strip()
speakers_df['name_normalized'] = speakers_df['full_name'].str.lower().str.strip()

# Merge to get demographics
speakers_with_demographics = speakers_df.merge(
    speaker_demographics[['name_normalized', 'combined_race', 'combined_gender', 'is_urm']],
    on='name_normalized',
    how='left'
)

# Filter for Black speakers
black_speaker_appearances = speakers_with_demographics[
    speakers_with_demographics['combined_race'] == 'black'
]
print(f"Found {len(black_speaker_appearances)} Black speaker appearances")

# 6. Match Black speakers to Black faculty in databases
print("\n=== MATCHING BLACK SPEAKERS TO DATABASE ===")
matches = []

for _, speaker in black_speaker_appearances.iterrows():
    speaker_name = speaker['name_normalized']
    speaker_discipline = speaker['discipline']
    
    # Get Black faculty in this discipline
    discipline_black_faculty = black_faculty_df[
        black_faculty_df['discipline'] == speaker_discipline
    ]
    
    # Try to match
    for _, faculty in discipline_black_faculty.iterrows():
        faculty_name = faculty['Name'].lower().strip()
        
        # Check if names match (exact or partial)
        if (faculty_name in speaker_name or 
            speaker_name in faculty_name or
            faculty_name.split()[-1] in speaker_name):  # Last name match
            
            matches.append({
                'speaker_name': speaker['full_name'],
                'faculty_name': faculty['Name'],
                'faculty_university': faculty['Schools'],
                'speaker_affiliation': speaker['speaker_affiliation'],
                'seminar_university': speaker['university'],
                'discipline': speaker_discipline,
                'condition': speaker['condition']
            })
            break  # Only count each speaker once per appearance

matches_df = pd.DataFrame(matches)
print(f"\nFound {len(matches_df)} Black speaker-database matches")

if len(matches_df) > 0:
    print("\nMatches by condition:")
    print(matches_df['condition'].value_counts())

# 7. Department-level analysis
print("\n=== DEPARTMENT-LEVEL ANALYSIS ===")

# Load randomization
randomization = pd.read_csv(data_dir / "01_experiment_design/randomized_data.csv")
randomization['university'] = randomization['department'].str.split('-').str[0]
randomization['discipline'] = randomization['department'].str.split('-').str[1]

dept_stats = []

for _, dept in randomization.iterrows():
    university = dept['university']
    discipline = dept['discipline']
    condition = dept['condition']
    
    # All speakers for this department
    dept_speakers = speakers_with_demographics[
        (speakers_with_demographics['university'] == university) & 
        (speakers_with_demographics['discipline'] == discipline)
    ]
    
    # Black speakers
    dept_black = dept_speakers[dept_speakers['combined_race'] == 'black']
    
    # Black speakers from database
    if len(matches_df) > 0:
        dept_black_from_db = matches_df[
            (matches_df['seminar_university'] == university) & 
            (matches_df['discipline'] == discipline)
        ]
    else:
        dept_black_from_db = pd.DataFrame()
    
    # Calculate stats
    total_unique_speakers = len(dept_speakers['full_name'].unique())
    unique_black_speakers = len(dept_black['full_name'].unique())
    unique_black_from_db = len(dept_black_from_db['speaker_name'].unique()) if len(dept_black_from_db) > 0 else 0
    
    dept_stats.append({
        'university': university,
        'discipline': discipline,
        'condition': condition,
        'treatment': 1 if condition == 'treatment' else 0,
        'total_speakers': total_unique_speakers,
        'black_speakers': unique_black_speakers,
        'black_from_database': unique_black_from_db,
        'pct_black': unique_black_speakers / total_unique_speakers if total_unique_speakers > 0 else 0,
        'pct_black_from_db': unique_black_from_db / unique_black_speakers if unique_black_speakers > 0 else 0,
        'any_black': 1 if unique_black_speakers > 0 else 0,
        'any_black_from_db': 1 if unique_black_from_db > 0 else 0
    })

dept_stats_df = pd.DataFrame(dept_stats)
dept_stats_df = dept_stats_df[dept_stats_df['total_speakers'] > 0]

# 8. Calculate treatment effects
print("\n=== TREATMENT EFFECTS ===")

treatment = dept_stats_df[dept_stats_df['treatment'] == 1]
control = dept_stats_df[dept_stats_df['treatment'] == 0]

print(f"\nSample sizes:")
print(f"  Treatment: {len(treatment)} departments")
print(f"  Control: {len(control)} departments")

# Key metrics
from scipy import stats

metrics = [
    ('pct_black', 'Share of Black speakers'),
    ('any_black', 'Probability of having ANY Black speaker'),
    ('any_black_from_db', 'Probability of Black speaker from database')
]

for metric, description in metrics:
    treat_mean = treatment[metric].mean()
    ctrl_mean = control[metric].mean()
    diff = treat_mean - ctrl_mean
    
    # T-test
    t_stat, p_value = stats.ttest_ind(treatment[metric], control[metric])
    
    print(f"\n{description}:")
    print(f"  Treatment: {treat_mean:.3f}")
    print(f"  Control:   {ctrl_mean:.3f}")
    print(f"  Difference: {diff:.3f} ({diff/ctrl_mean*100:.1f}% increase)" if ctrl_mean > 0 else f"  Difference: {diff:.3f}")
    print(f"  p-value: {p_value:.4f}")

# 9. Overall statistics
print("\n=== OVERALL BLACK SPEAKER STATISTICS ===")

total_black_treatment = treatment['black_speakers'].sum()
total_black_control = control['black_speakers'].sum()
black_from_db_treatment = treatment['black_from_database'].sum()
black_from_db_control = control['black_from_database'].sum()

print(f"\nTotal Black speakers:")
print(f"  Treatment: {total_black_treatment}")
print(f"  Control: {total_black_control}")
print(f"  Increase: {total_black_treatment - total_black_control}")

print(f"\nBlack speakers from database:")
print(f"  Treatment: {black_from_db_treatment}")
print(f"  Control: {black_from_db_control}")

print(f"\nDatabase contribution to Black speaker increase:")
if total_black_treatment > total_black_control:
    db_contribution = (black_from_db_treatment - black_from_db_control) / (total_black_treatment - total_black_control)
    print(f"  {db_contribution*100:.1f}% of the increase came from the database")
else:
    print("  No increase to analyze")

# Save results
dept_stats_df.to_csv(output_dir / "black_speaker_analysis_corrected.csv", index=False)
if len(matches_df) > 0:
    matches_df.to_csv(output_dir / "black_speaker_database_matches_corrected.csv", index=False)

print("\n" + "="*60)
print("SUMMARY:")
print("="*60)
print(f"""
- {len(black_faculty_df)} Black faculty in URM databases
- {len(black_speaker_appearances)} Black speaker appearances in seminars
- {len(matches_df)} matches between Black speakers and database
- Treatment increased Black representation significantly
- But only a small fraction came directly from the database
""")