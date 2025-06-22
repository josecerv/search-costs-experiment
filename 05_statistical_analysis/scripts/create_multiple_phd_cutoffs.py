#!/usr/bin/env python3
"""
Create Junior/Senior Speaker Variables for Multiple PhD Year Cutoffs
This script generates speaker count variables using different seniority thresholds (5, 10, 15, 20 years).
Critical for testing robustness of treatment effects to different definitions of "junior" vs "senior".
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json
from datetime import datetime
import logging
import warnings
warnings.filterwarnings('ignore')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

class PHDCutoffProcessor:
    def __init__(self):
        self.base_dir = Path("/mnt/c/Users/jcerv/Jose/search-costs")
        self.demographics_dir = self.base_dir / "04_demographic_analysis/outputs"
        self.analysis_dir = self.base_dir / "05_statistical_analysis/outputs"
        self.current_year = 2025  # Academic year 2024-2025
        
    def load_data(self):
        """Load necessary data files"""
        logger.info("Loading data files...")
        
        # Load speaker appearances with PhD years
        self.appearances_df = pd.read_csv(self.demographics_dir / "speaker_appearances_analysis.csv")
        logger.info(f"Loaded {len(self.appearances_df)} speaker appearances")
        
        # Load current analysis dataset to merge with
        self.master_df = pd.read_csv(self.analysis_dir / "master_analysis_dataset.csv")
        logger.info(f"Loaded {len(self.master_df)} seminars from master dataset")
        
        # Check PhD year coverage
        phd_year_coverage = self.appearances_df['phd_graduation_year'].notna().sum()
        logger.info(f"PhD year data available for {phd_year_coverage}/{len(self.appearances_df)} appearances ({phd_year_coverage/len(self.appearances_df)*100:.1f}%)")
        
    def calculate_years_since_phd(self):
        """Calculate years since PhD for each speaker appearance"""
        logger.info("Calculating years since PhD...")
        
        # Convert PhD year to numeric, handling various formats
        self.appearances_df['phd_year_numeric'] = pd.to_numeric(
            self.appearances_df['phd_graduation_year'], 
            errors='coerce'
        )
        
        # Calculate years since PhD
        # Use the seminar date if available, otherwise use current year
        if 'speaker_date' in self.appearances_df.columns:
            # Extract year from date
            self.appearances_df['seminar_year'] = pd.to_datetime(
                self.appearances_df['speaker_date'], 
                errors='coerce'
            ).dt.year
            # Fill missing with current year
            self.appearances_df['seminar_year'].fillna(self.current_year, inplace=True)
        else:
            self.appearances_df['seminar_year'] = self.current_year
            
        # Calculate years since PhD
        self.appearances_df['years_since_phd'] = (
            self.appearances_df['seminar_year'] - self.appearances_df['phd_year_numeric']
        )
        
        # Filter out unreasonable values (e.g., PhD year = 0 when not a current student)
        # If PhD year is less than 1900 or greater than current year, set to NaN
        self.appearances_df.loc[
            (self.appearances_df['phd_year_numeric'] < 1900) | 
            (self.appearances_df['phd_year_numeric'] > self.current_year),
            'years_since_phd'
        ] = np.nan
        
        # Handle edge cases
        # If PhD year is 0 (current student), set years_since_phd to 0
        self.appearances_df.loc[
            self.appearances_df['phd_graduation_year'] == '0', 
            'years_since_phd'
        ] = 0
        
        # If years_since_phd is negative (future graduation), set to NaN
        self.appearances_df.loc[
            self.appearances_df['years_since_phd'] < 0, 
            'years_since_phd'
        ] = np.nan
        
        # Log distribution
        valid_years = self.appearances_df['years_since_phd'].dropna()
        if len(valid_years) > 0:
            logger.info(f"Years since PhD statistics:")
            logger.info(f"  Mean: {valid_years.mean():.1f} years")
            logger.info(f"  Median: {valid_years.median():.1f} years")
            logger.info(f"  Min: {valid_years.min():.1f} years")
            logger.info(f"  Max: {valid_years.max():.1f} years")
            
    def create_cutoff_variables(self, cutoff_years=[5, 10, 15, 20]):
        """Create junior/senior classification for multiple cutoffs"""
        logger.info(f"Creating variables for cutoffs: {cutoff_years}")
        
        # For each cutoff, create junior/senior flags
        for cutoff in cutoff_years:
            # Junior = <= cutoff years post-PhD
            self.appearances_df[f'is_junior_{cutoff}'] = (
                self.appearances_df['years_since_phd'] <= cutoff
            ).astype(float)  # Float to handle NaN properly
            
            # Senior = > cutoff years post-PhD
            self.appearances_df[f'is_senior_{cutoff}'] = (
                self.appearances_df['years_since_phd'] > cutoff
            ).astype(float)
            
            # Log counts
            junior_count = self.appearances_df[f'is_junior_{cutoff}'].sum()
            senior_count = self.appearances_df[f'is_senior_{cutoff}'].sum()
            total_with_data = junior_count + senior_count
            
            logger.info(f"  {cutoff}-year cutoff: {junior_count:.0f} junior, {senior_count:.0f} senior "
                       f"({junior_count/total_with_data*100:.1f}% junior)")
            
    def aggregate_to_seminar_level(self, cutoff_years=[5, 10, 15, 20]):
        """Aggregate speaker-level data to seminar level"""
        logger.info("Aggregating to seminar level...")
        
        # Group by seminar
        seminar_groups = self.appearances_df.groupby('seminar_id')
        
        # Initialize results dictionary
        results = {}
        
        # Create demographic binary variables from combined_race and combined_gender
        self.appearances_df['is_black'] = (self.appearances_df['combined_race'] == 'black').astype(int)
        self.appearances_df['is_hispanic'] = (self.appearances_df['combined_race'] == 'hispanic').astype(int)
        self.appearances_df['is_urm'] = self.appearances_df['is_black'] | self.appearances_df['is_hispanic']
        self.appearances_df['is_female'] = (self.appearances_df['combined_gender'] == 'woman').astype(int)
        
        # For each demographic group
        for demo in ['black', 'hispanic', 'urm', 'female']:
            logger.info(f"  Processing {demo} speakers...")
            
            # Overall counts (already in master dataset, but recalculate for verification)
            demo_var = f'is_{demo}'
            if demo_var in self.appearances_df.columns:
                results[f'num_{demo}_check'] = seminar_groups[demo_var].sum()
                results[f'pct_{demo}_check'] = seminar_groups[demo_var].mean() * 100
                
                # For each cutoff
                for cutoff in cutoff_years:
                    # Count of junior speakers in this demographic
                    junior_mask = f'is_junior_{cutoff}'
                    results[f'num_{demo}_junior_{cutoff}'] = seminar_groups.apply(
                        lambda x: ((x[demo_var] == 1) & (x[junior_mask] == 1)).sum()
                    )
                    
                    # Count of senior speakers in this demographic
                    senior_mask = f'is_senior_{cutoff}'
                    results[f'num_{demo}_senior_{cutoff}'] = seminar_groups.apply(
                        lambda x: ((x[demo_var] == 1) & (x[senior_mask] == 1)).sum()
                    )
                    
        # Also calculate for all speakers (not demographic-specific)
        results['speakers_with_phd_year'] = seminar_groups['years_since_phd'].apply(
            lambda x: x.notna().sum()
        )
        
        # Convert to DataFrame
        self.seminar_level_df = pd.DataFrame(results)
        self.seminar_level_df.reset_index(inplace=True)
        
        logger.info(f"Created seminar-level dataset with {len(self.seminar_level_df)} seminars")
        
    def merge_with_master_dataset(self):
        """Merge new variables with existing master dataset"""
        logger.info("Merging with master dataset...")
        
        # Check overlap
        common_seminars = set(self.master_df['seminar_id']) & set(self.seminar_level_df['seminar_id'])
        logger.info(f"  Found {len(common_seminars)} seminars in common")
        
        # Merge
        self.final_df = self.master_df.merge(
            self.seminar_level_df,
            on='seminar_id',
            how='left',
            suffixes=('', '_new')
        )
        
        # Fill missing values with 0 for count variables
        count_cols = [col for col in self.final_df.columns if col.startswith(('num_', 'speakers_with_'))]
        self.final_df[count_cols] = self.final_df[count_cols].fillna(0)
        
        # Verify data integrity
        self.verify_data_integrity()
        
    def verify_data_integrity(self):
        """Verify the new variables make sense"""
        logger.info("Verifying data integrity...")
        
        # Check if recalculated totals match original
        for demo in ['black']:  # Just check black for now
            if f'num_{demo}' in self.final_df.columns and f'num_{demo}_check' in self.final_df.columns:
                diff = (self.final_df[f'num_{demo}'] - self.final_df[f'num_{demo}_check']).abs()
                mismatches = diff > 0.01
                if mismatches.any():
                    logger.warning(f"  Found {mismatches.sum()} mismatches in {demo} counts")
                else:
                    logger.info(f"  ✓ {demo} counts match original data")
                    
        # Check that junior + senior <= total for each cutoff
        for cutoff in [5, 10, 15, 20]:
            for demo in ['black']:
                junior_col = f'num_{demo}_junior_{cutoff}'
                senior_col = f'num_{demo}_senior_{cutoff}'
                total_col = f'num_{demo}'
                
                if all(col in self.final_df.columns for col in [junior_col, senior_col, total_col]):
                    sum_junior_senior = self.final_df[junior_col] + self.final_df[senior_col]
                    total = self.final_df[total_col]
                    
                    # Allow for small differences due to missing PhD years
                    issues = sum_junior_senior > total + 0.01
                    if issues.any():
                        logger.warning(f"  Found {issues.sum()} seminars where junior+senior > total for {demo} at {cutoff}-year cutoff")
                    else:
                        logger.info(f"  ✓ Junior+senior counts valid for {demo} at {cutoff}-year cutoff")
                        
    def save_results(self):
        """Save the enhanced dataset"""
        # Create backup of original
        backup_path = self.analysis_dir / f"master_analysis_dataset_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        self.master_df.to_csv(backup_path, index=False)
        logger.info(f"Created backup at {backup_path}")
        
        # Save new dataset
        output_path = self.analysis_dir / "master_analysis_dataset_with_cutoffs.csv"
        
        # Drop check columns before saving
        cols_to_drop = [col for col in self.final_df.columns if col.endswith('_check')]
        self.final_df.drop(columns=cols_to_drop, inplace=True)
        
        self.final_df.to_csv(output_path, index=False)
        logger.info(f"Saved enhanced dataset to {output_path}")
        
        # Save metadata
        metadata = {
            'created_date': datetime.now().isoformat(),
            'n_seminars': len(self.final_df),
            'cutoff_years': [5, 10, 15, 20],
            'new_columns': [col for col in self.final_df.columns if any(
                f'_{cutoff}' in col for cutoff in [5, 10, 15, 20]
            )],
            'phd_year_coverage': {
                'appearances_with_phd_year': int(self.appearances_df['phd_graduation_year'].notna().sum()),
                'total_appearances': len(self.appearances_df),
                'percentage': float(self.appearances_df['phd_graduation_year'].notna().mean() * 100)
            }
        }
        
        metadata_path = self.analysis_dir / "phd_cutoffs_metadata.json"
        with open(metadata_path, 'w') as f:
            json.dump(metadata, f, indent=2)
        logger.info(f"Saved metadata to {metadata_path}")
        
        return output_path
        
    def run(self):
        """Execute the full pipeline"""
        logger.info("Starting PhD cutoff variable creation...")
        logger.info("=" * 80)
        
        self.load_data()
        self.calculate_years_since_phd()
        self.create_cutoff_variables()
        self.aggregate_to_seminar_level()
        self.merge_with_master_dataset()
        output_path = self.save_results()
        
        logger.info("=" * 80)
        logger.info("Pipeline completed successfully!")
        logger.info(f"Enhanced dataset saved to: {output_path}")
        
        # Print summary statistics
        logger.info("\nSummary of new variables:")
        for cutoff in [5, 10, 15, 20]:
            logger.info(f"\n{cutoff}-year cutoff:")
            for demo in ['black']:
                junior_col = f'num_{demo}_junior_{cutoff}'
                senior_col = f'num_{demo}_senior_{cutoff}'
                if junior_col in self.final_df.columns:
                    junior_mean = self.final_df[junior_col].mean()
                    senior_mean = self.final_df[senior_col].mean()
                    logger.info(f"  Average {demo} speakers per seminar: "
                               f"{junior_mean:.2f} junior, {senior_mean:.2f} senior")
                    
                    # Count seminars with any junior/senior speakers
                    has_junior = (self.final_df[junior_col] > 0).sum()
                    has_senior = (self.final_df[senior_col] > 0).sum()
                    logger.info(f"  Seminars with {demo} speakers: "
                               f"{has_junior} have junior, {has_senior} have senior")

if __name__ == "__main__":
    processor = PHDCutoffProcessor()
    processor.run()