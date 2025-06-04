#!/usr/bin/env python3
"""
Correct analysis of the peer URM database treatment effect.
Re-analyzing with proper data extraction and matching.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json
from typing import Dict, List, Set, Tuple
from collections import defaultdict
import warnings
warnings.filterwarnings('ignore')

# Load all necessary data
data_dir = Path("/mnt/c/Users/jcerv/Jose/search-costs")
output_dir = Path("/mnt/c/Users/jcerv/Jose/search-costs/05_statistical_analysis/outputs")

print("Loading data files...")

# 1. Load the master data with actual speaker names
master_data = pd.read_csv(data_dir / "03_data_collection/processed/master-data-final.csv")
print(f"Master data shape: {master_data.shape}")

# 2. Load the URM databases
urm_databases = {}
db_dir = data_dir / "02_intervention_materials/databases"
for discipline in ['chemistry', 'physics', 'mathematics', 'computerScience', 'mechanicalEngineering']:
    file_path = db_dir / f"{discipline}.csv"
    if file_path.exists():
        df = pd.read_csv(file_path)
        # Map discipline names
        disc_map = {
            'chemistry': 'Chemistry',
            'physics': 'Physics', 
            'mathematics': 'Mathematics',
            'computerScience': 'Computer Science',
            'mechanicalEngineering': 'Mechanical Engineering'
        }
        urm_databases[disc_map[discipline]] = df
        print(f"Loaded {len(df)} URM faculty for {disc_map[discipline]}")

# 3. Load randomization data to know treatment/control
randomization = pd.read_csv(data_dir / "01_experiment_design/randomized_data.csv")

# 4. Extract all speakers from master data (convert from wide to long format)
print("\nExtracting speakers from master data...")
speakers_list = []

for _, row in master_data.iterrows():
    seminar_info = {
        'seminar_id': row['seminar_id'],
        'university': row['university'],
        'discipline': row['discipline'],
        'condition': row['condition']
    }
    
    # Extract each speaker (up to 128 based on column structure)
    for i in range(1, 129):  # 1 to 128
        first_name_col = f'First Name_{i}'
        last_name_col = f'Last Name_{i}'
        date_col = f'date_{i}'
        university_col = f'university_{i}'
        rank_col = f'rank_{i}_standardized'
        
        if first_name_col in row and pd.notna(row.get(first_name_col)):
            first_name = str(row.get(first_name_col, '')).strip()
            last_name = str(row.get(last_name_col, '')).strip()
            
            if first_name and last_name:  # Only include if we have both names
                speaker_data = {
                    **seminar_info,
                    'speaker_num': i,
                    'first_name': first_name,
                    'last_name': last_name,
                    'full_name': f"{first_name} {last_name}",
                    'date': row.get(date_col),
                    'affiliation': row.get(university_col),
                    'rank': row.get(rank_col)
                }
                speakers_list.append(speaker_data)

speakers_df = pd.DataFrame(speakers_list)
print(f"Extracted {len(speakers_df)} speaker appearances")

# Count unique speakers
speakers_df['name_lower'] = speakers_df['full_name'].str.lower()
unique_speakers = speakers_df.groupby(['name_lower', 'discipline', 'affiliation']).size()
print(f"Found {len(unique_speakers)} unique speakers (by name+discipline+affiliation)")

# 5. Now let's analyze how many speakers came from peer universities
# First, let's understand what universities are in our databases
print("\n=== URM Database Coverage ===")
for discipline, df in urm_databases.items():
    universities = df['Schools'].unique()
    print(f"\n{discipline}: {len(df)} faculty from {len(universities)} universities")
    print(f"Top universities: {universities[:5].tolist()}")

# 6. Calculate what % of all speakers are from peer universities (not just URM)
print("\n=== Analyzing peer university representation ===")

# Load university rankings
rankings = {}
for discipline in ['Chemistry', 'Physics', 'Mathematics', 'Computer Science', 'Mechanical Engineering']:
    rank_file = data_dir / f"06_archive/university_ranks.csv"
    if rank_file.exists():
        ranks_df = pd.read_csv(rank_file)
        # This is a simplified version - you may need to adjust based on actual file structure
        
# For now, let's do a simpler analysis - count matches between database and speakers
print("\n=== Direct matching analysis ===")

all_matches = []
for discipline, urm_df in urm_databases.items():
    # Get speakers from this discipline
    disc_speakers = speakers_df[speakers_df['discipline'] == discipline]
    
    # Create normalized names for matching
    urm_df['name_normalized'] = urm_df['Name'].str.lower().str.strip()
    
    # Try different matching strategies
    for _, urm in urm_df.iterrows():
        urm_name = urm['name_normalized']
        urm_parts = urm_name.split()
        
        # Find potential matches
        matches = disc_speakers[
            disc_speakers['name_lower'].str.contains(urm_name, case=False, na=False) |
            disc_speakers['name_lower'].str.contains(urm_parts[-1], case=False, na=False)  # Last name match
        ]
        
        if len(matches) > 0:
            for _, match in matches.iterrows():
                all_matches.append({
                    'urm_name': urm['Name'],
                    'urm_university': urm['Schools'],
                    'speaker_name': match['full_name'],
                    'speaker_university': match['affiliation'],
                    'seminar_university': match['university'],
                    'discipline': discipline,
                    'condition': match['condition'],
                    'date': match['date']
                })

matches_df = pd.DataFrame(all_matches)
print(f"\nFound {len(matches_df)} total matches between URM databases and speakers")

# Group by treatment/control
if len(matches_df) > 0:
    print("\nMatches by condition:")
    print(matches_df['condition'].value_counts())
    
    # Unique speakers matched
    unique_matches = matches_df.drop_duplicates(subset=['speaker_name', 'discipline'])
    print(f"\nUnique speakers matched: {len(unique_matches)}")
    print("By condition:")
    print(unique_matches['condition'].value_counts())

# 7. Calculate statistics
print("\n=== TREATMENT EFFECT ANALYSIS ===")

# Parse department field to get university and discipline
randomization['university'] = randomization['department'].str.split('-').str[0]
randomization['discipline'] = randomization['department'].str.split('-').str[1]

# Get department-level statistics
dept_stats = []
for _, row in randomization.iterrows():
    university = row['university']
    discipline = row['discipline']
    condition = row['condition']
    
    # Get seminars for this department
    dept_speakers = speakers_df[
        (speakers_df['university'] == university) & 
        (speakers_df['discipline'] == discipline)
    ]
    
    if len(dept_speakers) == 0:
        continue
        
    # Get matches for this department
    dept_matches = matches_df[
        (matches_df['seminar_university'] == university) & 
        (matches_df['discipline'] == discipline)
    ] if len(matches_df) > 0 else pd.DataFrame()
    
    total_speakers = len(dept_speakers['full_name'].unique())
    speakers_from_db = len(dept_matches['speaker_name'].unique()) if len(dept_matches) > 0 else 0
    
    dept_stats.append({
        'university': university,
        'discipline': discipline,
        'condition': condition,
        'treatment': 1 if condition == 'treatment' else 0,
        'total_speakers': total_speakers,
        'speakers_from_database': speakers_from_db,
        'pct_from_database': speakers_from_db / total_speakers if total_speakers > 0 else 0,
        'any_from_database': 1 if speakers_from_db > 0 else 0
    })

dept_stats_df = pd.DataFrame(dept_stats)
dept_stats_df = dept_stats_df[dept_stats_df['total_speakers'] > 0]

print(f"\nAnalyzing {len(dept_stats_df)} departments with speakers")

# Calculate treatment effects
treatment = dept_stats_df[dept_stats_df['treatment'] == 1]
control = dept_stats_df[dept_stats_df['treatment'] == 0]

print(f"\nTreatment departments: {len(treatment)}")
print(f"Control departments: {len(control)}")

# Key metrics
metrics = [
    ('pct_from_database', '% of speakers from URM database'),
    ('any_from_database', 'Probability of selecting ANY speaker from database')
]

for metric, description in metrics:
    treat_mean = treatment[metric].mean()
    ctrl_mean = control[metric].mean()
    diff = treat_mean - ctrl_mean
    
    print(f"\n{description}:")
    print(f"  Treatment: {treat_mean:.3f}")
    print(f"  Control:   {ctrl_mean:.3f}")
    print(f"  Difference: {diff:.3f}")
    
    # T-test
    from scipy import stats
    if treatment[metric].std() > 0 or control[metric].std() > 0:
        t_stat, p_value = stats.ttest_ind(treatment[metric], control[metric])
        print(f"  p-value: {p_value:.4f}")

# Save results
output_path = output_dir / "treatment_effect_analysis_corrected.csv"
dept_stats_df.to_csv(output_path, index=False)
print(f"\nResults saved to: {output_path}")

# Also save detailed matches
if len(matches_df) > 0:
    matches_path = output_dir / "urm_database_matches_detailed.csv"
    matches_df.to_csv(matches_path, index=False)
    print(f"Detailed matches saved to: {matches_path}")