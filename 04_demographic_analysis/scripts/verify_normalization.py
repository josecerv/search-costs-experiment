#!/usr/bin/env python3
"""
Verify that university normalization is working correctly
Shows sample of standardized affiliations from the data
"""

import pandas as pd
import sys
from pathlib import Path

# Add parent directories to path
sys.path.append(str(Path(__file__).parent.parent.parent / "03_data_collection"))

def verify_normalization():
    """Check that GPT-standardized affiliations are being used"""
    
    # Load the master data
    data_path = Path(__file__).parent.parent.parent / "03_data_collection/processed/master-data-final.csv"
    print(f"Loading data from: {data_path}")
    df = pd.read_csv(data_path, low_memory=False)
    
    print("\n=== Verification of University Normalization ===\n")
    
    # Check if standardized columns exist
    std_cols = [col for col in df.columns if col.endswith('_standardized')]
    uni_std_cols = [col for col in std_cols if 'university' in col]
    
    print(f"Found {len(uni_std_cols)} standardized university columns")
    
    # Sample some standardized affiliations
    print("\n--- Sample of Raw vs Standardized Affiliations ---")
    
    samples_shown = 0
    for i in range(1, 20):  # Check first 20 speaker slots
        raw_col = f'university_{i}'
        std_col = f'university_{i}_standardized'
        
        if raw_col in df.columns and std_col in df.columns:
            # Get non-empty samples
            mask = (df[raw_col].notna()) & (df[raw_col] != '') & (df[std_col].notna()) & (df[std_col] != '')
            samples = df[mask][[raw_col, std_col]].drop_duplicates().head(5)
            
            if len(samples) > 0:
                print(f"\nSpeaker slot {i}:")
                for _, row in samples.iterrows():
                    raw = row[raw_col]
                    std = row[std_col]
                    if raw != std:  # Only show when different
                        print(f"  '{raw}' → '{std}'")
                        samples_shown += 1
                        
            if samples_shown >= 20:
                break
    
    # Check for problematic patterns
    print("\n--- Checking for Old Bug Patterns ---")
    
    bug_patterns = ['universityersity', 'instituteitute', 'technologynology', 'collegeege']
    bug_found = False
    
    for col in uni_std_cols:
        values = df[col].dropna().astype(str).unique()
        for val in values:
            for pattern in bug_patterns:
                if pattern in val.lower():
                    print(f"❌ BUG FOUND in {col}: '{val}' (contains '{pattern}')")
                    bug_found = True
    
    if not bug_found:
        print("✅ No bug patterns found in standardized columns!")
    
    # Show most common standardized affiliations
    print("\n--- Top 20 Most Common Standardized Affiliations ---")
    
    all_affiliations = []
    for col in uni_std_cols:
        if col != 'university_standardized':  # Skip seminar universities
            affiliations = df[col].dropna().astype(str)
            affiliations = affiliations[affiliations != '']
            all_affiliations.extend(affiliations.tolist())
    
    from collections import Counter
    affiliation_counts = Counter(all_affiliations)
    
    for affiliation, count in affiliation_counts.most_common(20):
        print(f"{count:4d} - {affiliation}")
    
    print("\n✅ Verification complete!")
    
    # Now test the demographic analysis data transformation
    print("\n=== Testing Demographic Analysis Data Transformation ===")
    
    # Import the demographic analysis module
    sys.path.append(str(Path(__file__).parent))
    from run_analysis import DemographicAnalyzer
    
    analyzer = DemographicAnalyzer()
    
    # Extract just a few speaker appearances to test
    test_df = df.head(5)  # Just first 5 seminars
    appearances = analyzer._extract_speaker_appearances(test_df)
    
    print(f"\nExtracted {len(appearances)} speaker appearances from 5 seminars")
    
    # Check if affiliations are properly standardized
    print("\n--- Sample Speaker Appearances with Affiliations ---")
    
    for i, (_, speaker) in enumerate(appearances.head(10).iterrows()):
        if pd.notna(speaker.get('name')) and speaker.get('name').strip():
            print(f"\nSpeaker {i+1}: {speaker.get('name')}")
            print(f"  Raw affiliation: {speaker.get('affiliation_raw', 'N/A')}")
            print(f"  Standardized: {speaker.get('affiliation', 'N/A')}")
            print(f"  From seminar at: {speaker.get('university', 'N/A')}")

if __name__ == "__main__":
    verify_normalization()