"""
Add email recipient demographic variables to the master analysis dataset.
"""
import pandas as pd
import numpy as np
from pathlib import Path

def main():
    # Load master analysis dataset
    master_file = Path(__file__).parent.parent / "outputs" / "master_analysis_dataset.csv"
    master_df = pd.read_csv(master_file)
    print(f"Loaded master dataset with {len(master_df)} seminars")
    
    # Load email recipient demographics
    recipient_file = Path(__file__).parent.parent / "outputs" / "email_recipient_demographics_by_dept.csv"
    recipient_df = pd.read_csv(recipient_file)
    print(f"Loaded recipient demographics for {len(recipient_df)} departments")
    
    # Merge on department name
    # Need to match format: master has "University-Department", recipient has original "University-Department"
    # Use the original 'department' column from recipient data, not department_clean
    master_df['merge_key'] = master_df['department_std']
    recipient_df['merge_key'] = recipient_df['department']
    
    # Select columns to merge
    merge_cols = [
        'merge_key',
        'num_email_recipients',
        'pct_female_recipients', 
        'pct_urm_recipients',
        'pct_black_recipients',
        'pct_hispanic_recipients',
        'pct_assistant_prof_recipients'
    ]
    
    # Merge
    merged_df = master_df.merge(
        recipient_df[merge_cols], 
        on='merge_key', 
        how='left',
        suffixes=('', '_new')
    )
    
    # Check merge quality
    matched = merged_df['num_email_recipients'].notna().sum()
    print(f"Matched {matched}/{len(merged_df)} seminars ({matched/len(merged_df)*100:.1f}%)")
    
    # Handle any conflicts with existing num_recipients column
    if 'num_recipients' in merged_df.columns:
        print(f"Original num_recipients range: {merged_df['num_recipients'].min()}-{merged_df['num_recipients'].max()}")
        print(f"New num_email_recipients range: {merged_df['num_email_recipients'].min()}-{merged_df['num_email_recipients'].max()}")
        # Keep original num_recipients, add email-specific count as separate column
        merged_df['num_email_recipients_analyzed'] = merged_df['num_email_recipients']
        merged_df.drop('num_email_recipients', axis=1, inplace=True)
    
    # Clean up
    merged_df.drop('merge_key', axis=1, inplace=True)
    
    # Calculate number of distinct seminars per department
    seminars_per_dept = merged_df.groupby('department_std')['seminar_id'].nunique().reset_index()
    seminars_per_dept.columns = ['department_std', 'num_distinct_seminars']
    
    # Merge back
    merged_df = merged_df.merge(seminars_per_dept, on='department_std', how='left')
    
    # Save updated dataset
    output_file = Path(__file__).parent.parent / "outputs" / "master_analysis_dataset_with_recipients.csv"
    merged_df.to_csv(output_file, index=False)
    print(f"Saved updated dataset to {output_file}")
    
    # Print summary of new variables
    print("\nNew variables added:")
    print(f"- pct_female_recipients: Mean = {merged_df['pct_female_recipients'].mean():.3f}")
    print(f"- pct_urm_recipients: Mean = {merged_df['pct_urm_recipients'].mean():.3f}")
    print(f"- pct_assistant_prof_recipients: Mean = {merged_df['pct_assistant_prof_recipients'].mean():.3f}")
    print(f"- num_distinct_seminars: Mean = {merged_df['num_distinct_seminars'].mean():.1f}")
    
if __name__ == "__main__":
    main()