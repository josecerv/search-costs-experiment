#!/usr/bin/env python3
"""
Fix PhD Year Data Quality Issues
1. Convert professors/associate/assistant professors from "0" to missing
2. Convert future years (2025+) to missing
3. Update the analysis dataset with corrected values
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import shutil

def fix_phd_years(df):
    """Fix PhD year data quality issues"""
    print("\nFixing PhD year data quality issues...")
    
    # Create a copy to track changes
    df_fixed = df.copy()
    original_zeros = (df_fixed['phd_graduation_year'] == 0).sum()
    original_future = (df_fixed['phd_graduation_year'] > 2024).sum()
    
    # Define professor ranks that shouldn't be students
    professor_ranks = [
        'professor', 'associate professor', 'assistant professor',
        'full professor', 'prof', 'prof.', 'emeritus professor',
        'adjunct professor', 'research professor', 'visiting professor'
    ]
    
    # Fix 1: Convert professors marked as current students to missing
    professor_mask = df_fixed['rank'].str.lower().str.contains('|'.join(professor_ranks), na=False)
    student_mask = df_fixed['phd_graduation_year'] == 0
    
    professors_as_students = professor_mask & student_mask
    df_fixed.loc[professors_as_students, 'phd_graduation_year'] = np.nan
    
    print(f"  Fixed {professors_as_students.sum()} professors incorrectly marked as current students")
    
    # Fix 2: Convert future years to missing
    future_mask = df_fixed['phd_graduation_year'] > 2024
    df_fixed.loc[future_mask, 'phd_graduation_year'] = np.nan
    
    print(f"  Fixed {future_mask.sum()} entries with future PhD years")
    
    # Summary of changes
    final_zeros = (df_fixed['phd_graduation_year'] == 0).sum()
    final_missing = df_fixed['phd_graduation_year'].isna().sum()
    
    print(f"\nSummary of changes:")
    print(f"  Current students (0): {original_zeros} → {final_zeros} (removed {original_zeros - final_zeros})")
    print(f"  Future years: {original_future} → 0 (converted to missing)")
    print(f"  Total missing: {df['phd_graduation_year'].isna().sum()} → {final_missing}")
    
    return df_fixed

def update_analysis_dataset():
    """Update the master analysis dataset with corrected PhD years"""
    print("\nUpdating master analysis dataset with corrected PhD years...")
    
    base_dir = Path("/mnt/c/Users/jcerv/Jose/search-costs")
    
    # Re-run the add_phd_years_to_analysis script with corrected data
    from add_phd_years_to_analysis import calculate_years_from_phd
    
    # Load corrected speaker appearances
    appearances_df = pd.read_csv(base_dir / "04_demographic_analysis/outputs/speaker_appearances_analysis.csv")
    master_df = pd.read_csv(base_dir / "05_statistical_analysis/outputs/master_analysis_dataset.csv")
    
    # Remove old PhD columns if they exist
    phd_columns = [
        'num_speakers_with_phd_year', 'pct_speakers_with_phd_year',
        'mean_years_from_phd', 'median_years_from_phd', 
        'min_years_from_phd', 'max_years_from_phd',
        'num_current_students', 'pct_current_students'
    ]
    
    for col in phd_columns:
        if col in master_df.columns:
            master_df = master_df.drop(columns=[col])
    
    # Calculate years from PhD for each speaker
    appearances_df['years_from_phd'] = appearances_df['phd_graduation_year'].apply(calculate_years_from_phd)
    
    # Aggregate to seminar level
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
    
    # Create dataframe and merge
    phd_stats_df = pd.DataFrame(seminar_phd_stats)
    master_df_enhanced = master_df.merge(phd_stats_df, on='seminar_id', how='left')
    
    # Fill missing values
    for col in phd_columns:
        if col in ['num_speakers_with_phd_year', 'num_current_students']:
            master_df_enhanced[col] = master_df_enhanced[col].fillna(0)
        elif col in ['pct_speakers_with_phd_year', 'pct_current_students']:
            master_df_enhanced[col] = master_df_enhanced[col].fillna(0)
    
    return master_df_enhanced

def main():
    print("\n=== Fixing PhD Year Data Quality Issues ===")
    
    base_dir = Path("/mnt/c/Users/jcerv/Jose/search-costs")
    appearances_file = base_dir / "04_demographic_analysis/outputs/speaker_appearances_analysis.csv"
    
    # Backup original file
    backup_file = appearances_file.with_suffix('.csv.backup')
    if not backup_file.exists():
        shutil.copy(appearances_file, backup_file)
        print(f"Created backup: {backup_file}")
    
    # Load and fix data
    appearances_df = pd.read_csv(appearances_file)
    appearances_df_fixed = fix_phd_years(appearances_df)
    
    # Save corrected data
    appearances_df_fixed.to_csv(appearances_file, index=False)
    print(f"\nSaved corrected data to: {appearances_file}")
    
    # Update analysis dataset
    print("\nUpdating analysis dataset...")
    master_df_enhanced = update_analysis_dataset()
    
    # Save enhanced dataset
    output_file = base_dir / "05_statistical_analysis/outputs/master_analysis_dataset.csv"
    master_df_enhanced.to_csv(output_file, index=False)
    
    # Summary statistics
    print("\nFinal summary of PhD year variables:")
    print(f"  Seminars with PhD data: {(master_df_enhanced['num_speakers_with_phd_year'] > 0).sum()}")
    print(f"  Coverage rate: {(master_df_enhanced['num_speakers_with_phd_year'] > 0).sum() / len(master_df_enhanced) * 100:.1f}%")
    print(f"  Mean years from PhD: {master_df_enhanced['mean_years_from_phd'].mean():.1f}")
    print(f"  % current students: {master_df_enhanced['pct_current_students'].mean():.1f}%")
    
    # Verify fixes
    print("\nVerifying fixes in speaker appearances:")
    appearances_check = pd.read_csv(appearances_file)
    professors_as_students = appearances_check[
        (appearances_check['rank'].str.lower().str.contains('professor', na=False)) & 
        (appearances_check['phd_graduation_year'] == 0)
    ]
    future_years = appearances_check[appearances_check['phd_graduation_year'] > 2024]
    
    print(f"  Professors marked as students: {len(professors_as_students)} (should be 0)")
    print(f"  Future PhD years: {len(future_years)} (should be 0)")
    
    print("\n✅ PhD year data quality issues fixed!")

if __name__ == "__main__":
    main()