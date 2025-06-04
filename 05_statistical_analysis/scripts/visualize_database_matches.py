#!/usr/bin/env python3
"""
Visualize and analyze the database matching results
"""

import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_matches():
    base_dir = Path("/mnt/c/Users/jcerv/Jose/search-costs")
    
    # Load improved matches
    matches_df = pd.read_csv(base_dir / "05_statistical_analysis/outputs/peer_urm_matches_improved.csv")
    
    # Load main results
    results_df = pd.read_csv(base_dir / "05_statistical_analysis/outputs/database_treatment_effect_improved.csv")
    
    print("="*60)
    print("DATABASE MATCHING ANALYSIS")
    print("="*60)
    
    # Basic counts
    print(f"\nTotal matches found: {len(matches_df)}")
    print(f"Treatment matches: {len(matches_df[matches_df['treatment'] == 1])}")
    print(f"Control matches: {len(matches_df[matches_df['treatment'] == 0])}")
    
    # By discipline
    print("\n\nMatches by Discipline:")
    disc_counts = matches_df.groupby(['seminar_discipline', 'treatment']).size().unstack(fill_value=0)
    print(disc_counts)
    
    # By match type
    print("\n\nMatch Quality Distribution:")
    match_types = matches_df['match_type'].value_counts()
    print(match_types)
    
    # Top matched universities
    print("\n\nTop Universities with Matches:")
    top_unis = matches_df['focal_university'].value_counts().head(10)
    print(top_unis)
    
    # Analyze departments with no matches vs with matches
    print("\n\nDepartment Analysis:")
    results_with_matches = results_df[results_df['speakers_from_database'] > 0]
    results_no_matches = results_df[results_df['speakers_from_database'] == 0]
    
    print(f"\nDepartments with matches: {len(results_with_matches)}")
    print(f"  Treatment: {len(results_with_matches[results_with_matches['treatment'] == 1])}")
    print(f"  Control: {len(results_with_matches[results_with_matches['treatment'] == 0])}")
    
    # Average characteristics
    print("\n\nCharacteristics of departments WITH matches:")
    print(f"  Avg total speakers: {results_with_matches['total_speakers'].mean():.1f}")
    print(f"  Avg URM speakers: {results_with_matches['total_urm_speakers'].mean():.1f}")
    print(f"  Avg peer universities: {results_with_matches['num_peer_universities'].mean():.1f}")
    print(f"  Avg potential URMs in database: {results_with_matches['num_potential_urm_in_database'].mean():.1f}")
    
    print("\n\nCharacteristics of departments WITHOUT matches:")
    print(f"  Avg total speakers: {results_no_matches['total_speakers'].mean():.1f}")
    print(f"  Avg URM speakers: {results_no_matches['total_urm_speakers'].mean():.1f}")
    print(f"  Avg peer universities: {results_no_matches['num_peer_universities'].mean():.1f}")
    print(f"  Avg potential URMs in database: {results_no_matches['num_potential_urm_in_database'].mean():.1f}")
    
    # Most successful matches
    print("\n\nMost Frequently Matched URM Faculty:")
    top_urm = matches_df['urm_name'].value_counts().head(10)
    for name, count in top_urm.items():
        urm_info = matches_df[matches_df['urm_name'] == name].iloc[0]
        print(f"  {name} ({urm_info['urm_university']}): {count} appearances")

if __name__ == "__main__":
    analyze_matches()