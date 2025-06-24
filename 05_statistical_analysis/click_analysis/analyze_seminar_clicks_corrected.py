#!/usr/bin/env python3
"""
Corrected click analysis using email-list.csv as ground truth.
This properly handles seminars with commas in their names.
"""

import pandas as pd
import json
import numpy as np
from collections import defaultdict
from datetime import datetime
from pathlib import Path

def analyze_clicks():
    """Analyze seminar clicks using the comprehensive correct mapping."""
    print("\n" + "="*80)
    print("SEMINAR CLICK ANALYSIS (CORRECTED)")
    print("Using email-list.csv ground truth")
    print("="*80 + "\n")
    
    # Load data
    print("Loading data...")
    base_path = Path("/mnt/c/Users/jcerv/Jose/search-costs")
    
    # Use the comprehensive mapping created from email-list.csv
    mapping_df = pd.read_csv(base_path / "comprehensive_email_seminar_mapping.csv")
    master_df = pd.read_csv(base_path / "05_statistical_analysis/outputs/master_analysis_dataset.csv")
    
    with open(base_path / "01_experiment_design/bitly_cache.json", 'r') as f:
        bitly_data = json.load(f)
    
    print(f"Loaded {len(mapping_df)} email-seminar mappings")
    print(f"Master dataset has {len(master_df)} seminars")
    
    # Initialize results for all seminars
    seminar_results = {}
    for _, seminar in master_df.iterrows():
        sid = seminar['seminar_id']
        seminar_results[sid] = {
            'clicked': False,
            'click_sources': [],
            'treatment': seminar['treatment'],
            'university': seminar['university'],
            'discipline': seminar['discipline']
        }
    
    # Process mappings - each link counted only once
    print("\nProcessing click data...")
    for link, group in mapping_df.groupby('link'):
        clicks = group.iloc[0]['clicks']
        
        if clicks > 0:
            # Mark all seminars in this group as clicked
            for _, mapping in group.iterrows():
                sid = mapping['seminar_id']
                if sid in seminar_results:
                    seminar_results[sid]['clicked'] = True
                    seminar_results[sid]['click_sources'].append({
                        'email_type': mapping['contact_type'],
                        'match_type': mapping['match_type']
                    })
    
    # Calculate statistics
    print("\n" + "="*60)
    print("RESULTS")
    print("="*60)
    
    total_seminars = len(master_df)
    seminars_clicked = sum(1 for data in seminar_results.values() if data['clicked'])
    total_clicks = sum(d['total'] for d in bitly_data.values())
    
    print(f"\nOVERALL:")
    print(f"  Total seminars: {total_seminars}")
    print(f"  Seminars clicked: {seminars_clicked}")
    print(f"  Seminar click rate: {seminars_clicked/total_seminars*100:.1f}%")
    print(f"  Total Bit.ly clicks: {total_clicks}")
    
    # By treatment condition
    treatment_seminars = [sid for sid, data in seminar_results.items() if data['treatment'] == 1]
    control_seminars = [sid for sid, data in seminar_results.items() if data['treatment'] == 0]
    
    treatment_clicked = sum(1 for sid in treatment_seminars if seminar_results[sid]['clicked'])
    control_clicked = sum(1 for sid in control_seminars if seminar_results[sid]['clicked'])
    
    print(f"\nTREATMENT GROUP:")
    print(f"  Total seminars: {len(treatment_seminars)}")
    print(f"  Seminars clicked: {treatment_clicked}")
    print(f"  Click rate: {treatment_clicked/len(treatment_seminars)*100:.1f}%")
    
    print(f"\nCONTROL GROUP:")
    print(f"  Total seminars: {len(control_seminars)}")  
    print(f"  Seminars clicked: {control_clicked}")
    print(f"  Click rate: {control_clicked/len(control_seminars)*100:.1f}%")
    
    # Contact type analysis
    reach_by_type = defaultdict(set)
    for sid, data in seminar_results.items():
        if data['clicked']:
            for source in data['click_sources']:
                reach_by_type[source['email_type']].add(sid)
    
    print(f"\nSEMINARS REACHED BY CONTACT TYPE:")
    for contact_type in ['department_chair', 'faculty', 'seminar_contact']:
        if contact_type in reach_by_type:
            count = len(reach_by_type[contact_type])
            pct = count / seminars_clicked * 100
            print(f"  {contact_type}: {count} seminars ({pct:.1f}% of clicked)")
    
    # Save results
    results = {
        'summary': {
            'total_seminars': int(total_seminars),
            'seminars_clicked': int(seminars_clicked),
            'click_rate': round(seminars_clicked/total_seminars*100, 1),
            'total_clicks': int(total_clicks)
        },
        'treatment': {
            'total_seminars': len(treatment_seminars),
            'seminars_clicked': int(treatment_clicked),
            'click_rate': round(treatment_clicked/len(treatment_seminars)*100, 1)
        },
        'control': {
            'total_seminars': len(control_seminars),
            'seminars_clicked': int(control_clicked),
            'click_rate': round(control_clicked/len(control_seminars)*100, 1)
        },
        'timestamp': datetime.now().isoformat()
    }
    
    output_path = base_path / "05_statistical_analysis/click_analysis/results.json"
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Save seminar details
    seminar_details = []
    for sid, data in seminar_results.items():
        seminar_details.append({
            'seminar_id': sid,
            'university': data['university'],
            'discipline': data['discipline'],
            'treatment': data['treatment'],
            'clicked': int(data['clicked']),
            'num_click_sources': len(data['click_sources'])
        })
    
    details_df = pd.DataFrame(seminar_details)
    details_path = base_path / "05_statistical_analysis/click_analysis/seminar_click_details.csv"
    details_df.to_csv(details_path, index=False)
    
    print(f"\n✓ Results saved to results.json")
    print(f"✓ Seminar details saved to seminar_click_details.csv")
    
    return results

if __name__ == "__main__":
    results = analyze_clicks()