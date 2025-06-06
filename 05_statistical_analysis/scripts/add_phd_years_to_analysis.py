#!/usr/bin/env python3
"""
Add Years from PhD as a moderator variable to the master analysis dataset
This script calculates the years since PhD graduation for seminar speakers
and adds it as a variable for exploratory analysis.
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

def calculate_years_from_phd(phd_year, reference_year=2025):
    """
    Calculate years from PhD graduation
    
    Args:
        phd_year: PhD graduation year (can be year, 0 for current student, NA for non-PhD)
        reference_year: Year to calculate from (default 2025 for the experiment year)
    
    Returns:
        Years from PhD or None if not applicable
    """
    if pd.isna(phd_year):
        return None
    
    try:
        phd_year = float(phd_year)
        
        # Current students (0) - assign negative value to indicate pre-PhD
        if phd_year == 0:
            return -1  # Indicates current student
        
        # Future years (likely errors) - treat as missing
        if phd_year > reference_year:
            return None
        
        # Valid years - calculate difference
        if 1900 <= phd_year <= reference_year:
            return reference_year - phd_year
        
        return None
    except:
        # NA or other non-numeric values
        return None

def main():
    print("\n=== Adding PhD Years to Master Analysis Dataset ===")
    
    # Paths
    base_dir = Path("/mnt/c/Users/jcerv/Jose/search-costs")
    demographics_file = base_dir / "04_demographic_analysis/outputs/speaker_appearances_analysis.csv"
    master_file = base_dir / "05_statistical_analysis/outputs/master_analysis_dataset.csv"
    
    # Load data
    print("\nLoading data...")
    appearances_df = pd.read_csv(demographics_file)
    master_df = pd.read_csv(master_file)
    
    print(f"  Loaded {len(appearances_df)} speaker appearances")
    print(f"  Loaded {len(master_df)} seminars")
    
    # Calculate years from PhD for each speaker
    print("\nCalculating years from PhD...")
    appearances_df['years_from_phd'] = appearances_df['phd_graduation_year'].apply(calculate_years_from_phd)
    
    # Check distribution
    print("\nYears from PhD distribution:")
    print(f"  Valid values: {appearances_df['years_from_phd'].notna().sum()}")
    print(f"  Missing values: {appearances_df['years_from_phd'].isna().sum()}")
    print(f"  Current students (negative): {(appearances_df['years_from_phd'] == -1).sum()}")
    
    # Aggregate to seminar level
    print("\nAggregating to seminar level...")
    seminar_phd_stats = []
    
    for seminar_id in master_df['seminar_id'].unique():
        # Get speakers for this seminar
        seminar_speakers = appearances_df[appearances_df['seminar_id'] == seminar_id]
        
        if len(seminar_speakers) == 0:
            continue
        
        # Get years from PhD values (excluding missing)
        years_values = seminar_speakers['years_from_phd'].dropna()
        
        # Calculate statistics
        stats = {
            'seminar_id': seminar_id,
            'num_speakers_with_phd_year': len(years_values),
            'pct_speakers_with_phd_year': len(years_values) / len(seminar_speakers) * 100 if len(seminar_speakers) > 0 else 0
        }
        
        if len(years_values) > 0:
            # Exclude current students for mean/median calculations
            years_post_phd = years_values[years_values >= 0]
            
            if len(years_post_phd) > 0:
                stats['mean_years_from_phd'] = years_post_phd.mean()
                stats['median_years_from_phd'] = years_post_phd.median()
                stats['min_years_from_phd'] = years_post_phd.min()
                stats['max_years_from_phd'] = years_post_phd.max()
            else:
                # All speakers are current students
                stats['mean_years_from_phd'] = -1
                stats['median_years_from_phd'] = -1
                stats['min_years_from_phd'] = -1
                stats['max_years_from_phd'] = -1
            
            # Count current students
            stats['num_current_students'] = (years_values == -1).sum()
            stats['pct_current_students'] = stats['num_current_students'] / len(years_values) * 100
        else:
            # No PhD year data
            stats['mean_years_from_phd'] = np.nan
            stats['median_years_from_phd'] = np.nan
            stats['min_years_from_phd'] = np.nan
            stats['max_years_from_phd'] = np.nan
            stats['num_current_students'] = 0
            stats['pct_current_students'] = 0
        
        seminar_phd_stats.append(stats)
    
    # Create dataframe
    phd_stats_df = pd.DataFrame(seminar_phd_stats)
    
    # Merge with master dataset
    print("\nMerging with master dataset...")
    master_df_enhanced = master_df.merge(phd_stats_df, on='seminar_id', how='left')
    
    # Fill missing values with appropriate defaults
    phd_columns = [
        'num_speakers_with_phd_year', 'pct_speakers_with_phd_year',
        'mean_years_from_phd', 'median_years_from_phd', 
        'min_years_from_phd', 'max_years_from_phd',
        'num_current_students', 'pct_current_students'
    ]
    
    for col in phd_columns:
        if col in ['num_speakers_with_phd_year', 'num_current_students']:
            master_df_enhanced[col] = master_df_enhanced[col].fillna(0)
        elif col in ['pct_speakers_with_phd_year', 'pct_current_students']:
            master_df_enhanced[col] = master_df_enhanced[col].fillna(0)
    
    # Summary statistics
    print("\nSummary of PhD year variables:")
    print(f"  Seminars with PhD data: {(master_df_enhanced['num_speakers_with_phd_year'] > 0).sum()}")
    print(f"  Coverage rate: {(master_df_enhanced['num_speakers_with_phd_year'] > 0).sum() / len(master_df_enhanced) * 100:.1f}%")
    print(f"  Mean years from PhD (across seminars): {master_df_enhanced['mean_years_from_phd'].mean():.1f}")
    print(f"  Median years from PhD (across seminars): {master_df_enhanced['median_years_from_phd'].median():.1f}")
    
    # Check treatment vs control
    print("\nPhD years by treatment status:")
    for treatment in [0, 1]:
        subset = master_df_enhanced[master_df_enhanced['treatment'] == treatment]
        print(f"\n  Treatment={treatment}:")
        print(f"    Mean years from PhD: {subset['mean_years_from_phd'].mean():.1f}")
        print(f"    % with PhD data: {subset['pct_speakers_with_phd_year'].mean():.1f}%")
    
    # Save enhanced dataset
    output_file = base_dir / "05_statistical_analysis/outputs/master_analysis_dataset.csv"
    print(f"\nSaving enhanced dataset to: {output_file}")
    master_df_enhanced.to_csv(output_file, index=False)
    
    # Also update the metadata
    import json
    metadata_file = base_dir / "05_statistical_analysis/outputs/master_analysis_dataset_metadata.json"
    if metadata_file.exists():
        with open(metadata_file, 'r') as f:
            metadata = json.load(f)
        
        metadata['phd_year_variables'] = {
            'creation_date': datetime.now().isoformat(),
            'coverage_rate': float((master_df_enhanced['num_speakers_with_phd_year'] > 0).sum() / len(master_df_enhanced)),
            'mean_years_from_phd': float(master_df_enhanced['mean_years_from_phd'].mean()),
            'new_columns': phd_columns
        }
        
        with open(metadata_file, 'w') as f:
            json.dump(metadata, f, indent=2)
    
    print("\n✅ PhD year variables successfully added to master analysis dataset!")
    print("\nNew variables added:")
    for col in phd_columns:
        print(f"  - {col}")
    
    print("\nNote: Use these variables for exploratory analysis as moderators.")
    print("      Negative values (-1) indicate current graduate students.")

if __name__ == "__main__":
    main()