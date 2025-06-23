#!/usr/bin/env python3
"""
Create department-level email click statistics from bitly_cache.json.
Aggregates clicks by department and filters by recipient type (faculty/organizer).

Output: email_clicks_from_bitly_cache.csv with columns:
- department
- condition
- clicked (1 if any link clicked, 0 otherwise)
- total_clicks (sum of all clicks)
- num_emails (number of unique emails sent to department)
"""

import json
import pandas as pd
import numpy as np
from pathlib import Path
from collections import defaultdict
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    # Define paths
    base_dir = Path("/Users/josecervantez/Documents/Jose-CODE/search-costs")
    bitly_cache_path = base_dir / "01_experiment_design" / "bitly_cache.json"
    email_data_path = base_dir / "02_intervention_materials" / "email_campaigns" / "email-launch.csv"
    output_path = base_dir / "05_statistical_analysis" / "outputs" / "email_clicks_from_bitly_cache.csv"
    
    logger.info("Loading bitly cache data...")
    with open(bitly_cache_path, 'r') as f:
        bitly_cache = json.load(f)
    logger.info(f"Loaded {len(bitly_cache)} links from bitly cache")
    
    logger.info("Loading email campaign data...")
    email_df = pd.read_csv(email_data_path)
    logger.info(f"Loaded {len(email_df)} email records")
    
    # Filter for sent emails only
    email_df = email_df[email_df['sent'] == 1].copy()
    logger.info(f"Filtered to {len(email_df)} sent emails")
    
    # Filter by contact_type if needed
    # The main contact types in the data are: faculty, department_chair, seminar_contact
    # Uncomment and modify the following line to filter by specific contact types:
    # email_df = email_df[email_df['contact_type'].isin(['faculty', 'department_chair'])].copy()
    
    # For filtering only faculty recipients:
    # email_df = email_df[email_df['contact_type'] == 'faculty'].copy()
    
    # Note: The original file appears to include all contact types
    
    # Create department-level aggregation
    logger.info("Aggregating clicks by department...")
    
    # Map links to their click data
    email_df['clicks'] = email_df['Link'].map(lambda x: bitly_cache.get(x, {}).get('total', 0))
    email_df['clicked'] = (email_df['clicks'] > 0).astype(int)
    
    # Group by department
    dept_stats = email_df.groupby(['department', 'condition']).agg({
        'clicked': 'max',  # 1 if any email in department was clicked
        'clicks': 'sum',   # total clicks for department
        'contact_email': 'nunique'  # number of unique emails sent
    }).reset_index()
    
    # Rename columns to match expected output
    dept_stats.rename(columns={
        'clicks': 'total_clicks',
        'contact_email': 'num_emails'
    }, inplace=True)
    
    # Ensure all departments have both clicked and total_clicks columns
    dept_stats['clicked'] = dept_stats['clicked'].astype(int)
    dept_stats['total_clicks'] = dept_stats['total_clicks'].astype(int)
    
    # Sort by department name
    dept_stats = dept_stats.sort_values('department').reset_index(drop=True)
    
    # Save to CSV
    logger.info(f"Saving department-level click statistics to {output_path}")
    dept_stats.to_csv(output_path, index=False)
    
    # Print summary statistics
    logger.info("\n=== Summary Statistics ===")
    logger.info(f"Total departments: {len(dept_stats)}")
    logger.info(f"Departments with clicks: {dept_stats['clicked'].sum()}")
    logger.info(f"Total clicks across all departments: {dept_stats['total_clicks'].sum()}")
    logger.info(f"Average clicks per department: {dept_stats['total_clicks'].mean():.2f}")
    
    # By condition
    for condition in ['control', 'treatment']:
        cond_data = dept_stats[dept_stats['condition'] == condition]
        logger.info(f"\n{condition.capitalize()}:")
        logger.info(f"  Departments: {len(cond_data)}")
        logger.info(f"  With clicks: {cond_data['clicked'].sum()}")
        logger.info(f"  Click rate: {cond_data['clicked'].mean()*100:.1f}%")
        logger.info(f"  Total clicks: {cond_data['total_clicks'].sum()}")
    
    return dept_stats

if __name__ == "__main__":
    dept_stats = main()