#!/usr/bin/env python3
"""
Show the structure of the master analysis dataset
"""

import pandas as pd
from pathlib import Path
import json

base_dir = Path("/mnt/c/Users/jcerv/Jose/search-costs")
output_dir = base_dir / "05_statistical_analysis/outputs"

print("=== MASTER ANALYSIS DATASET STRUCTURE ===\n")

# Check if dataset exists
dataset_file = output_dir / "master_analysis_dataset.csv"
metadata_file = output_dir / "master_analysis_dataset_metadata.json"

if not dataset_file.exists():
    print(f"Dataset not found at: {dataset_file}")
    print("\nExpected columns would include:")
    
    # List expected columns
    expected_columns = {
        "Identifiers": [
            "seminar_id", "university", "discipline", "department", 
            "department_std", "condition", "treatment"
        ],
        "Outcomes - Full Year": [
            "total_speakers", "speakers_with_demographics",
            "num_urm", "num_black", "num_hispanic", "num_native_american", 
            "num_female", "num_male", "num_white", "num_asian",
            "pct_urm", "pct_black", "pct_hispanic", "pct_native_american",
            "pct_female", "pct_male", "pct_white", "pct_asian",
            "has_any_urm", "has_any_black", "has_any_hispanic", 
            "has_any_native_american", "has_any_female"
        ],
        "Outcomes - Fall Semester": [
            "has_fall_speakers", "fall_total_speakers", "fall_speakers_with_demographics",
            "fall_num_urm", "fall_num_black", "fall_num_hispanic", "fall_num_female",
            "fall_pct_urm", "fall_pct_black", "fall_pct_hispanic", "fall_pct_female"
        ],
        "Outcomes - Spring Semester": [
            "has_spring_speakers", "spring_total_speakers", "spring_speakers_with_demographics",
            "spring_num_urm", "spring_num_black", "spring_num_hispanic", "spring_num_female",
            "spring_pct_urm", "spring_pct_black", "spring_pct_hispanic", "spring_pct_female"
        ],
        "Control Variables - Model 1": [
            "bin_category", "batch_number", "batch_date",
            "bin_[0,1]", "bin_(1,3]", "bin_(3,5]", "bin_(5,7]", "bin_(7,11]", "bin_(17,26]",
            "batch_1", "batch_2", "batch_3", "batch_4", "batch_5", 
            "batch_6", "batch_7", "batch_8", "batch_9",
            "disc_mathematics", "disc_physics", "disc_computer_science", "disc_mechanical_engineering"
        ],
        "Control Variables - Model 2 (Additional)": [
            "total_faculty", "urm_faculty", "women_faculty",
            "frac_urm_faculty", "frac_women_faculty",
            "dept_ranking", "general_ranking", "missing_dept_rank",
            "num_recipients",
            "total_peer_departments", "total_urm_peer_faculty"
        ]
    }
    
    for category, columns in expected_columns.items():
        print(f"\n{category}:")
        for col in columns:
            print(f"  - {col}")
    
else:
    # Load and show actual structure
    print(f"Loading dataset from: {dataset_file}")
    
    # Load metadata if exists
    if metadata_file.exists():
        with open(metadata_file, 'r') as f:
            metadata = json.load(f)
        
        print(f"\nDataset created: {metadata['creation_date']}")
        print(f"Total seminars: {metadata['n_seminars']}")
        print(f"Treatment: {metadata['n_treatment']}")
        print(f"Control: {metadata['n_control']}")
        
        print("\nControl variable coverage:")
        for var, coverage in metadata['control_variable_coverage'].items():
            print(f"  {var}: {coverage*100:.1f}%")
    
    # Load dataset to show columns
    df = pd.read_csv(dataset_file, nrows=5)  # Just load first 5 rows
    
    print(f"\nDataset has {len(df.columns)} columns")
    
    # Categorize columns
    id_cols = [c for c in df.columns if c in ['seminar_id', 'university', 'discipline', 'department', 'department_std', 'condition', 'treatment']]
    outcome_cols = [c for c in df.columns if any(x in c for x in ['num_', 'pct_', 'has_any_', 'total_speakers', 'speakers_with_demographics']) and not c.startswith('bin_') and not c.startswith('batch_')]
    control_cols = [c for c in df.columns if c.startswith('bin_') or c.startswith('batch_') or c.startswith('disc_')]
    other_control_cols = [c for c in df.columns if c in ['total_faculty', 'urm_faculty', 'women_faculty', 'frac_urm_faculty', 'frac_women_faculty', 
                                                          'dept_ranking', 'general_ranking', 'missing_dept_rank', 'num_recipients',
                                                          'total_peer_departments', 'total_urm_peer_faculty']]
    
    print("\nColumn categories:")
    print(f"\nIdentifiers ({len(id_cols)} columns):")
    for col in id_cols:
        print(f"  - {col}")
    
    print(f"\nOutcome variables ({len(outcome_cols)} columns):")
    # Group by type
    full_year = [c for c in outcome_cols if not c.startswith('fall_') and not c.startswith('spring_')]
    fall = [c for c in outcome_cols if c.startswith('fall_')]
    spring = [c for c in outcome_cols if c.startswith('spring_')]
    
    print(f"\n  Full year ({len(full_year)}):")
    for col in sorted(full_year):
        print(f"    - {col}")
    
    print(f"\n  Fall semester ({len(fall)}):")
    for col in sorted(fall):
        print(f"    - {col}")
    
    print(f"\n  Spring semester ({len(spring)}):")
    for col in sorted(spring):
        print(f"    - {col}")
    
    print(f"\nControl variables - Model 1 ({len(control_cols)} columns):")
    bin_vars = sorted([c for c in control_cols if c.startswith('bin_')])
    batch_vars = sorted([c for c in control_cols if c.startswith('batch_')])
    disc_vars = sorted([c for c in control_cols if c.startswith('disc_')])
    
    print(f"\n  Bin indicators ({len(bin_vars)}):")
    for col in bin_vars:
        print(f"    - {col}")
    
    print(f"\n  Batch indicators ({len(batch_vars)}):")
    for col in batch_vars:
        print(f"    - {col}")
    
    print(f"\n  Discipline indicators ({len(disc_vars)}):")
    for col in disc_vars:
        print(f"    - {col}")
    
    print(f"\nControl variables - Model 2 additional ({len(other_control_cols)} columns):")
    for col in other_control_cols:
        value_info = ""
        if col in df.columns:
            if df[col].dtype in ['float64', 'int64']:
                non_zero = (df[col] != 0).sum()
                if len(df) > 0:
                    value_info = f" (non-zero in {non_zero}/{len(df)} rows shown)"
        print(f"  - {col}{value_info}")
    
    # Show any other columns
    all_shown = set(id_cols + outcome_cols + control_cols + other_control_cols)
    other_cols = [c for c in df.columns if c not in all_shown]
    if other_cols:
        print(f"\nOther columns ({len(other_cols)}):")
        for col in sorted(other_cols):
            print(f"  - {col}")

print("\n✓ Dataset structure review complete!")