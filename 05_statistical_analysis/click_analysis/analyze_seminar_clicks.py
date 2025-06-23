#!/usr/bin/env python3
"""
CORRECTED click analysis - fixes double-counting issue.
Each click is counted only once, but properly attributed to all relevant seminars.
"""

import json
import pandas as pd
import numpy as np
from pathlib import Path
from collections import defaultdict
from datetime import datetime

def load_seminar_mapping():
    """Load the mapping of seminar IDs to seminar names from speaker appearances."""
    print("Loading seminar ID to name mapping...")
    speaker_path = Path("/Users/josecervantez/Documents/Jose-CODE/search-costs/04_demographic_analysis/outputs/speaker_appearances_analysis.csv")
    
    df = pd.read_csv(speaker_path)
    seminar_cols = ['seminar_id', 'university', 'discipline', 'seminar_name', 'Link']
    seminar_mapping = df[seminar_cols].drop_duplicates()
    
    print(f"Found {len(seminar_mapping)} unique seminars with names")
    return seminar_mapping

def load_master_seminars():
    """Load the master seminar dataset."""
    print("Loading master seminar dataset...")
    master_path = Path("/Users/josecervantez/Documents/Jose-CODE/search-costs/05_statistical_analysis/outputs/master_analysis_dataset.csv")
    master_df = pd.read_csv(master_path)
    print(f"Total seminars in master dataset: {len(master_df)}")
    return master_df

def load_email_campaign():
    """Load email campaign data."""
    print("Loading email campaign data...")
    email_path = Path("/Users/josecervantez/Documents/Jose-CODE/search-costs/02_intervention_materials/email_campaigns/email-launch.csv")
    email_df = pd.read_csv(email_path)
    print(f"Total emails sent: {len(email_df)}")
    return email_df

def load_click_data():
    """Load bitly click data."""
    print("Loading click data...")
    bitly_path = Path("/Users/josecervantez/Documents/Jose-CODE/search-costs/01_experiment_design/bitly_cache.json")
    with open(bitly_path, 'r') as f:
        bitly_data = json.load(f)
    
    total_clicks = sum(d['total'] for d in bitly_data.values())
    links_with_clicks = sum(1 for d in bitly_data.values() if d['total'] > 0)
    print(f"Total clicks across all links: {total_clicks}")
    print(f"Links with at least one click: {links_with_clicks}")
    
    return bitly_data

def analyze_clicks():
    """Main analysis function - CORRECTED VERSION."""
    print("\n" + "="*80)
    print("CORRECTED GROUND TRUTH CLICK ANALYSIS")
    print("="*80 + "\n")
    
    # Load all data
    seminar_mapping = load_seminar_mapping()
    master_df = load_master_seminars()
    email_df = load_email_campaign()
    bitly_data = load_click_data()
    
    # Merge master with seminar names
    print("\nMerging master dataset with seminar names...")
    master_with_names = master_df.merge(
        seminar_mapping[['seminar_id', 'seminar_name']].drop_duplicates(),
        on='seminar_id',
        how='left'
    )
    
    # Initialize results for each seminar
    seminar_results = defaultdict(lambda: {
        'clicked': False,
        'click_sources': [],
        'treatment': None,
        'university': None,
        'discipline': None,
        'seminar_name': None
    })
    
    # Add seminar metadata
    for _, seminar in master_with_names.iterrows():
        sid = seminar['seminar_id']
        seminar_results[sid]['treatment'] = seminar['treatment']
        seminar_results[sid]['university'] = seminar['university']
        seminar_results[sid]['discipline'] = seminar['discipline']
        seminar_results[sid]['seminar_name'] = seminar.get('seminar_name', '')
    
    # Process email campaign data
    print("\nProcessing email campaign data...")
    emails_processed = 0
    emails_with_clicks = 0
    unmatched_seminars = []
    
    for _, email in email_df.iterrows():
        emails_processed += 1
        link = email['Link']
        department = email['department']
        contact_type = email['contact_type']
        seminar_names_str = str(email['seminar_names'])
        
        # Get click data for this link
        click_data = bitly_data.get(link, {'total': 0})
        clicked = click_data['total'] > 0
        
        if clicked:
            emails_with_clicks += 1
            
        # Parse seminar names from email
        if pd.notna(seminar_names_str) and seminar_names_str.lower() != 'nan':
            email_seminar_names = [s.strip() for s in seminar_names_str.split(',')]
        else:
            email_seminar_names = []
        
        # Track which seminars were matched for this email
        matched_seminars = []
        
        # For department chairs, match ALL seminars in that department
        if contact_type == 'department_chair':
            for sid, sem_data in seminar_results.items():
                if (sem_data['university'] and sem_data['discipline'] and 
                    f"{sem_data['university']}-{sem_data['discipline']}" == department):
                    matched_seminars.append(sid)
                    if clicked:
                        sem_data['clicked'] = True
                        sem_data['click_sources'].append({
                            'type': 'department_chair',
                            'link': link,
                            'clicks': click_data['total']
                        })
        else:
            # For faculty/seminar_contact, match specific seminars
            for email_sem_name in email_seminar_names:
                matched = False
                for sid, sem_data in seminar_results.items():
                    if (sem_data['seminar_name'] and 
                        sem_data['university'] and sem_data['discipline'] and
                        f"{sem_data['university']}-{sem_data['discipline']}" == department):
                        
                        # Normalize names for comparison
                        sem_name_norm = sem_data['seminar_name'].lower().strip()
                        email_sem_norm = email_sem_name.lower().strip()
                        
                        # Check for match
                        if (sem_name_norm == email_sem_norm or 
                            email_sem_norm in sem_name_norm or 
                            sem_name_norm in email_sem_norm):
                            matched = True
                            matched_seminars.append(sid)
                            if clicked:
                                sem_data['clicked'] = True
                                sem_data['click_sources'].append({
                                    'type': contact_type,
                                    'seminar': email_sem_name,
                                    'link': link,
                                    'clicks': click_data['total']
                                })
                            break
                
                if not matched:
                    unmatched_seminars.append((email_sem_name, department, contact_type))
    
    print(f"\nEmails processed: {emails_processed}")
    print(f"Emails with clicks: {emails_with_clicks}")
    print(f"Unmatched seminar references: {len(unmatched_seminars)}")
    
    # Calculate statistics - CORRECTED to avoid double counting
    print("\n" + "="*60)
    print("CLICK STATISTICS BY SEMINAR (CORRECTED)")
    print("="*60)
    
    # Count seminars clicked (this is correct - each seminar counted once)
    total_seminars = len(master_df)
    seminars_clicked = sum(1 for data in seminar_results.values() if data['clicked'])
    
    # For total clicks, we should use the bitly total, not sum across seminars
    total_clicks_actual = sum(d['total'] for d in bitly_data.values())
    
    print(f"\nOVERALL:")
    print(f"  Seminars with at least one click: {seminars_clicked}/{total_seminars}")
    print(f"  Click rate: {seminars_clicked/total_seminars*100:.1f}%")
    print(f"  Total clicks (from bitly): {total_clicks_actual}")
    print(f"  Average clicks per email sent: {total_clicks_actual/len(email_df):.2f}")
    
    # By treatment condition
    treatment_seminars = [sid for sid, data in seminar_results.items() if data['treatment'] == 1]
    control_seminars = [sid for sid, data in seminar_results.items() if data['treatment'] == 0]
    
    treatment_clicked = sum(1 for sid in treatment_seminars if seminar_results[sid]['clicked'])
    control_clicked = sum(1 for sid in control_seminars if seminar_results[sid]['clicked'])
    
    # For clicks by condition, sum the actual bitly clicks for emails in each condition
    treatment_clicks = 0
    control_clicks = 0
    for _, email in email_df.iterrows():
        link = email['Link']
        condition = email['condition']
        clicks = bitly_data.get(link, {'total': 0})['total']
        if condition == 'treatment':
            treatment_clicks += clicks
        else:
            control_clicks += clicks
    
    print(f"\nTREATMENT GROUP:")
    print(f"  Total seminars: {len(treatment_seminars)}")
    print(f"  Seminars clicked: {treatment_clicked}")
    print(f"  Click rate: {treatment_clicked/len(treatment_seminars)*100:.1f}%")
    print(f"  Total clicks: {treatment_clicks}")
    
    print(f"\nCONTROL GROUP:")
    print(f"  Total seminars: {len(control_seminars)}")
    print(f"  Seminars clicked: {control_clicked}")
    print(f"  Click rate: {control_clicked/len(control_seminars)*100:.1f}%")
    print(f"  Total clicks: {control_clicks}")
    
    # Click source breakdown (by seminars reached, not clicks)
    print("\n" + "="*60)
    print("SEMINARS REACHED BY CONTACT TYPE")
    print("="*60)
    
    source_seminars = defaultdict(set)
    for sid, data in seminar_results.items():
        if data['clicked']:
            for source in data['click_sources']:
                source_seminars[source['type']].add(sid)
    
    print("\nUnique seminars reached by each contact type:")
    for source_type in ['department_chair', 'faculty', 'seminar_contact']:
        if source_type in source_seminars:
            count = len(source_seminars[source_type])
            print(f"  {source_type}: {count} seminars")
    
    # Seminars with multiple contact types clicking
    seminars_by_source_count = defaultdict(int)
    for sid, data in seminar_results.items():
        if data['clicked']:
            unique_sources = set(s['type'] for s in data['click_sources'])
            seminars_by_source_count[len(unique_sources)] += 1
    
    print("\nSeminars by number of contact types that clicked:")
    for count in sorted(seminars_by_source_count.keys()):
        print(f"  {count} contact type(s): {seminars_by_source_count[count]} seminars")
    
    # Show some unmatched examples
    if unmatched_seminars:
        print("\n" + "="*60)
        print("SAMPLE UNMATCHED SEMINAR REFERENCES")
        print("="*60)
        unique_unmatched = list(set(unmatched_seminars))[:10]
        for sem_name, dept, contact_type in unique_unmatched:
            print(f"  '{sem_name}' in {dept} ({contact_type})")
    
    # Save corrected results
    results = {
        'summary': {
            'total_seminars': total_seminars,
            'seminars_clicked': seminars_clicked,
            'click_rate': round(seminars_clicked/total_seminars*100, 1),
            'total_clicks_bitly': total_clicks_actual,
            'emails_sent': len(email_df),
            'avg_clicks_per_email': round(total_clicks_actual/len(email_df), 2)
        },
        'treatment': {
            'total_seminars': len(treatment_seminars),
            'seminars_clicked': treatment_clicked,
            'click_rate': round(treatment_clicked/len(treatment_seminars)*100, 1),
            'total_clicks': treatment_clicks
        },
        'control': {
            'total_seminars': len(control_seminars),
            'seminars_clicked': control_clicked,
            'click_rate': round(control_clicked/len(control_seminars)*100, 1),
            'total_clicks': control_clicks
        },
        'seminars_by_source': {k: len(v) for k, v in source_seminars.items()},
        'seminars_by_source_count': dict(seminars_by_source_count),
        'unmatched_seminar_count': len(unmatched_seminars),
        'timestamp': datetime.now().isoformat()
    }
    
    output_path = Path("/Users/josecervantez/Documents/Jose-CODE/search-costs/05_statistical_analysis/click_analysis/corrected_results.json")
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"\n✓ Corrected results saved to: {output_path}")
    
    # Save detailed seminar-level data
    seminar_details = []
    for sid, data in seminar_results.items():
        seminar_details.append({
            'seminar_id': sid,
            'university': data['university'],
            'discipline': data['discipline'],
            'seminar_name': data['seminar_name'] or '',
            'treatment': data['treatment'],
            'clicked': int(data['clicked']),
            'num_click_sources': len(set(s['type'] for s in data['click_sources']))
        })
    
    details_df = pd.DataFrame(seminar_details)
    details_path = Path("/Users/josecervantez/Documents/Jose-CODE/search-costs/05_statistical_analysis/click_analysis/seminar_click_details_corrected.csv")
    details_df.to_csv(details_path, index=False)
    print(f"✓ Seminar details saved to: {details_path}")
    
    return results

if __name__ == "__main__":
    results = analyze_clicks()