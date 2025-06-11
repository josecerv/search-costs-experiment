"""
Add junior/senior speaker subgroup variables based on PhD years.
"""
import pandas as pd
import numpy as np
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    # Load speaker appearances data with PhD years
    appearances_file = Path(__file__).parent.parent.parent / "04_demographic_analysis" / "outputs" / "speaker_appearances_analysis.csv"
    appearances_df = pd.read_csv(appearances_file)
    logger.info(f"Loaded {len(appearances_df)} speaker appearances")
    
    # Calculate years since PhD for each speaker
    appearances_df['years_since_phd'] = 2024 - pd.to_numeric(appearances_df['phd_graduation_year'], errors='coerce')
    
    # Filter to valid PhD years (positive years, not future)
    valid_phd = appearances_df['years_since_phd'] > 0
    logger.info(f"Found {valid_phd.sum()} appearances with valid PhD years")
    
    # Calculate global median years since PhD
    median_years = appearances_df.loc[valid_phd, 'years_since_phd'].median()
    logger.info(f"Global median years since PhD: {median_years:.1f}")
    
    # Classify speakers as junior or senior
    appearances_df['is_junior'] = (appearances_df['years_since_phd'] <= median_years) & valid_phd
    appearances_df['is_senior'] = (appearances_df['years_since_phd'] > median_years) & valid_phd
    
    # Create subgroup demographic variables
    # For Black and Hispanic, derive from combined_race (lowercase values)
    appearances_df['is_black'] = (appearances_df['combined_race'] == 'black').astype(int)
    appearances_df['is_hispanic'] = (appearances_df['combined_race'] == 'latino').astype(int)
    
    for race in ['black', 'hispanic', 'urm']:
        # Junior subgroup
        appearances_df[f'is_{race}_junior'] = (
            (appearances_df[f'is_{race}'] == 1) & 
            appearances_df['is_junior']
        ).astype(int)
        
        # Senior subgroup  
        appearances_df[f'is_{race}_senior'] = (
            (appearances_df[f'is_{race}'] == 1) & 
            appearances_df['is_senior']
        ).astype(int)
    
    # Aggregate to seminar level
    seminar_cols = ['seminar_id']
    
    # Count speakers in each subgroup
    subgroup_counts = appearances_df.groupby(seminar_cols).agg({
        # Total speakers with valid PhD years
        'is_junior': 'sum',
        'is_senior': 'sum',
        # Black subgroups
        'is_black_junior': 'sum',
        'is_black_senior': 'sum',
        # Hispanic subgroups
        'is_hispanic_junior': 'sum', 
        'is_hispanic_senior': 'sum',
        # URM subgroups
        'is_urm_junior': 'sum',
        'is_urm_senior': 'sum'
    }).reset_index()
    
    # Rename count columns
    subgroup_counts.rename(columns={
        'is_junior': 'num_junior_speakers',
        'is_senior': 'num_senior_speakers',
        'is_black_junior': 'num_black_junior',
        'is_black_senior': 'num_black_senior',
        'is_hispanic_junior': 'num_hispanic_junior',
        'is_hispanic_senior': 'num_hispanic_senior',
        'is_urm_junior': 'num_urm_junior',
        'is_urm_senior': 'num_urm_senior'
    }, inplace=True)
    
    # Calculate percentages
    for race in ['black', 'hispanic', 'urm']:
        # Percentage among junior speakers
        subgroup_counts[f'pct_{race}_junior'] = (
            subgroup_counts[f'num_{race}_junior'] / 
            subgroup_counts['num_junior_speakers'].replace(0, np.nan)
        ).fillna(0).round(4)
        
        # Percentage among senior speakers
        subgroup_counts[f'pct_{race}_senior'] = (
            subgroup_counts[f'num_{race}_senior'] / 
            subgroup_counts['num_senior_speakers'].replace(0, np.nan)
        ).fillna(0).round(4)
        
        # Binary indicators
        subgroup_counts[f'has_any_{race}_junior'] = (
            subgroup_counts[f'num_{race}_junior'] > 0
        ).astype(int)
        
        subgroup_counts[f'has_any_{race}_senior'] = (
            subgroup_counts[f'num_{race}_senior'] > 0
        ).astype(int)
    
    # Load master dataset with recipients
    master_file = Path(__file__).parent.parent / "outputs" / "master_analysis_dataset_with_recipients.csv"
    master_df = pd.read_csv(master_file)
    
    # Merge subgroup data
    merged_df = master_df.merge(
        subgroup_counts,
        on='seminar_id',
        how='left',
        suffixes=('', '_subgroup')
    )
    
    # Handle any column conflicts
    for col in ['university', 'discipline', 'department']:
        if f'{col}_subgroup' in merged_df.columns:
            merged_df.drop(f'{col}_subgroup', axis=1, inplace=True)
    
    # Fill missing values with 0 for count/binary variables
    fill_cols = [col for col in merged_df.columns if col.startswith(('num_', 'has_any_')) and 'junior' in col]
    merged_df[fill_cols] = merged_df[fill_cols].fillna(0)
    
    # Save final dataset
    output_file = Path(__file__).parent.parent / "outputs" / "master_analysis_dataset_final.csv"
    merged_df.to_csv(output_file, index=False)
    logger.info(f"Saved final dataset to {output_file}")
    
    # Print summary
    logger.info("\nSubgroup analysis summary:")
    logger.info(f"Seminars with junior speakers: {(merged_df['num_junior_speakers'] > 0).sum()}")
    logger.info(f"Seminars with senior speakers: {(merged_df['num_senior_speakers'] > 0).sum()}")
    logger.info(f"Mean % Black among junior speakers: {merged_df['pct_black_junior'].mean():.3f}")
    logger.info(f"Mean % Black among senior speakers: {merged_df['pct_black_senior'].mean():.3f}")
    
if __name__ == "__main__":
    main()