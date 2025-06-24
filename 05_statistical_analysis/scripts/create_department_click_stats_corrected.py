#!/usr/bin/env python3
"""
Create CORRECTED department-level email click statistics using the comprehensive mapping.
This uses the accurate mapping from email-list.csv to avoid comma-splitting errors.

Output: email_clicks_from_bitly_cache_corrected.csv with columns:
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
    base_dir = Path("/mnt/c/Users/jcerv/Jose/search-costs")
    mapping_path = base_dir / "comprehensive_email_seminar_mapping.csv"
    email_data_path = base_dir / "02_intervention_materials" / "email_campaigns" / "email-launch.csv"
    bitly_cache_path = base_dir / "01_experiment_design" / "bitly_cache.json"
    output_path = base_dir / "05_statistical_analysis" / "outputs" / "email_clicks_from_bitly_cache_corrected.csv"
    
    logger.info("Loading comprehensive mapping...")
    mapping_df = pd.read_csv(mapping_path)
    logger.info(f"Loaded {len(mapping_df)} mapping records")
    
    logger.info("Loading email campaign data...")
    email_df = pd.read_csv(email_data_path)
    email_df = email_df[email_df['sent'] == 1].copy()
    logger.info(f"Processing {len(email_df)} sent emails")
    
    logger.info("Loading bitly cache...")
    with open(bitly_cache_path, 'r') as f:
        bitly_cache = json.load(f)
    
    # Get unique department-link combinations from mapping
    dept_links = mapping_df[['department', 'link', 'condition']].drop_duplicates()
    
    # Add click data
    dept_links['clicks'] = dept_links['link'].map(lambda x: bitly_cache.get(x, {}).get('total', 0))
    dept_links['clicked'] = (dept_links['clicks'] > 0).astype(int)
    
    # Aggregate by department
    logger.info("Aggregating clicks by department...")
    dept_stats = dept_links.groupby(['department', 'condition']).agg({
        'clicked': 'max',  # 1 if any email in department was clicked
        'clicks': 'sum',   # total clicks for department
        'link': 'nunique'  # number of unique links/emails
    }).reset_index()
    
    # Rename columns
    dept_stats.rename(columns={
        'clicks': 'total_clicks',
        'link': 'num_emails'
    }, inplace=True)
    
    # Ensure correct data types
    dept_stats['clicked'] = dept_stats['clicked'].astype(int)
    dept_stats['total_clicks'] = dept_stats['total_clicks'].astype(int)
    
    # Sort by department
    dept_stats = dept_stats.sort_values('department').reset_index(drop=True)
    
    # Save to CSV
    logger.info(f"Saving corrected department-level click statistics to {output_path}")
    dept_stats.to_csv(output_path, index=False)
    
    # Also overwrite the original file that the Rmd uses
    original_output = base_dir / "05_statistical_analysis" / "outputs" / "email_clicks_from_bitly_cache.csv"
    dept_stats.to_csv(original_output, index=False)
    logger.info(f"Also updated original file at {original_output}")
    
    # Print summary statistics
    logger.info("\n=== CORRECTED Summary Statistics ===")
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