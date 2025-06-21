#!/usr/bin/env python3
"""
Extract detailed Bit.ly click data from the cache, including daily breakdowns if available.
This script analyzes the bitly_cache.json file and searches for any additional
Bit.ly API response data that might contain daily click information.
"""

import json
import csv
import os
from collections import defaultdict
from datetime import datetime

def analyze_bitly_cache():
    """Analyze the existing bitly cache file."""
    cache_file = '/mnt/c/Users/jcerv/Jose/search-costs/01_experiment_design/bitly_cache.json'
    
    print("Loading Bit.ly cache data...")
    with open(cache_file, 'r') as f:
        cache_data = json.load(f)
    
    print(f"Total links in cache: {len(cache_data)}")
    
    # Analyze click distribution
    email1_total = sum(item['email1'] for item in cache_data.values())
    email2_total = sum(item['email2'] for item in cache_data.values())
    overall_total = sum(item['total'] for item in cache_data.values())
    
    print(f"\nTotal clicks across all links:")
    print(f"  Email 1 period: {email1_total}")
    print(f"  Email 2 period: {email2_total}")
    print(f"  Overall: {overall_total}")
    
    # Create detailed CSV output
    output_file = '/mnt/c/Users/jcerv/Jose/search-costs/01_experiment_design/bitly_detailed_clicks.csv'
    
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['bitly_link', 'email1_clicks', 'email2_clicks', 'total_clicks'])
        
        # Sort by total clicks descending
        sorted_links = sorted(cache_data.items(), key=lambda x: x[1]['total'], reverse=True)
        
        for link, clicks in sorted_links:
            writer.writerow([link, clicks['email1'], clicks['email2'], clicks['total']])
    
    print(f"\nDetailed click data saved to: {output_file}")
    
    # Look for links with significant engagement
    high_engagement = [(link, clicks) for link, clicks in cache_data.items() 
                       if clicks['total'] >= 5]
    
    print(f"\nLinks with 5+ total clicks: {len(high_engagement)}")
    print("\nTop 20 most clicked links:")
    for i, (link, clicks) in enumerate(high_engagement[:20], 1):
        print(f"{i}. {link}: Email1={clicks['email1']}, Email2={clicks['email2']}, Total={clicks['total']}")
    
    return cache_data

def search_for_additional_bitly_data():
    """Search for any additional Bit.ly API response files."""
    search_dirs = [
        '/mnt/c/Users/jcerv/Jose/search-costs/01_experiment_design',
        '/mnt/c/Users/jcerv/Jose/search-costs/02_intervention_materials',
        '/mnt/c/Users/jcerv/Jose/search-costs/03_data_collection'
    ]
    
    print("\n\nSearching for additional Bit.ly data files...")
    
    for directory in search_dirs:
        if os.path.exists(directory):
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if any(keyword in file.lower() for keyword in ['bitly', 'click', 'api']):
                        if file.endswith(('.json', '.csv', '.txt')):
                            file_path = os.path.join(root, file)
                            print(f"Found potential file: {file_path}")

def create_summary_by_condition():
    """Create a summary of clicks by experimental condition."""
    # Load email campaign data to map links to conditions
    email_file = '/mnt/c/Users/jcerv/Jose/search-costs/02_intervention_materials/email_campaigns/email-launch.csv'
    
    if not os.path.exists(email_file):
        print("\nEmail campaign file not found, skipping condition analysis")
        return
    
    print("\n\nAnalyzing clicks by experimental condition...")
    
    # Load email data
    with open(email_file, 'r') as f:
        reader = csv.DictReader(f)
        email_data = list(reader)
    
    # Load cache data
    cache_file = '/mnt/c/Users/jcerv/Jose/search-costs/01_experiment_design/bitly_cache.json'
    with open(cache_file, 'r') as f:
        cache_data = json.load(f)
    
    # Map links to conditions
    link_to_condition = {}
    for row in email_data:
        link_to_condition[row['Link']] = row['condition']
    
    # Aggregate by condition
    condition_stats = defaultdict(lambda: {'email1': 0, 'email2': 0, 'total': 0, 'links': 0})
    
    for link, clicks in cache_data.items():
        condition = link_to_condition.get(link, 'unknown')
        condition_stats[condition]['email1'] += clicks['email1']
        condition_stats[condition]['email2'] += clicks['email2']
        condition_stats[condition]['total'] += clicks['total']
        condition_stats[condition]['links'] += 1
    
    # Print summary
    print("\nClicks by condition:")
    for condition, stats in sorted(condition_stats.items()):
        print(f"\n{condition.upper()}:")
        print(f"  Total links: {stats['links']}")
        print(f"  Email 1 clicks: {stats['email1']}")
        print(f"  Email 2 clicks: {stats['email2']}")
        print(f"  Total clicks: {stats['total']}")
        if stats['links'] > 0:
            print(f"  Average clicks per link: {stats['total'] / stats['links']:.2f}")

def main():
    print("=== Bit.ly Click Data Extraction ===")
    
    # Analyze main cache file
    cache_data = analyze_bitly_cache()
    
    # Search for additional files
    search_for_additional_bitly_data()
    
    # Create condition-based summary
    create_summary_by_condition()
    
    print("\n=== Analysis Complete ===")

if __name__ == "__main__":
    main()