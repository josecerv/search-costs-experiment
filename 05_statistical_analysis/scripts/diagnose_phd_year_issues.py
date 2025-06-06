#!/usr/bin/env python3
"""
Diagnose PhD Year Data Quality Issues
Investigate:
1. Why 15.5% of entries have missing PhD years
2. Why there are so many "0" values (current students)
3. Why there are future years (2025)
"""

import pandas as pd
import numpy as np
from pathlib import Path
from collections import Counter

def main():
    print("\n=== PhD Year Data Quality Diagnostic ===")
    
    # Paths
    base_dir = Path("/mnt/c/Users/jcerv/Jose/search-costs")
    appearances_file = base_dir / "04_demographic_analysis/outputs/speaker_appearances_analysis.csv"
    master_data_file = base_dir / "03_data_collection/processed/master-data-final.csv"
    
    # Load data
    print("\nLoading data...")
    appearances_df = pd.read_csv(appearances_file)
    master_df = pd.read_csv(master_data_file, low_memory=False)
    
    # 1. Investigate missing PhD years
    print("\n1. MISSING PhD YEARS ANALYSIS")
    print("="*50)
    
    missing_phd = appearances_df[appearances_df['phd_graduation_year'].isna()]
    print(f"Total missing: {len(missing_phd)} ({len(missing_phd)/len(appearances_df)*100:.1f}%)")
    
    # Check patterns in missing data
    print("\nMissing by discipline:")
    for disc in missing_phd['discipline'].value_counts().head(10).items():
        total_in_disc = len(appearances_df[appearances_df['discipline'] == disc[0]])
        print(f"  {disc[0]}: {disc[1]} ({disc[1]/total_in_disc*100:.1f}% of {total_in_disc})")
    
    print("\nMissing by rank:")
    for rank in missing_phd['rank'].value_counts().head(10).items():
        total_in_rank = len(appearances_df[appearances_df['rank'] == rank[0]])
        if total_in_rank > 0:
            print(f"  {rank[0]}: {rank[1]} ({rank[1]/total_in_rank*100:.1f}% of {total_in_rank})")
    
    print("\nSample of missing PhD year entries:")
    print(missing_phd[['name', 'discipline', 'affiliation', 'rank']].head(10).to_string())
    
    # 2. Investigate "0" values (current students)
    print("\n\n2. CURRENT STUDENTS (0 values) ANALYSIS")
    print("="*50)
    
    current_students = appearances_df[appearances_df['phd_graduation_year'] == 0]
    print(f"Total marked as current students: {len(current_students)} ({len(current_students)/len(appearances_df)*100:.1f}%)")
    
    print("\nCurrent students by rank:")
    rank_counts = current_students['rank'].value_counts()
    for rank, count in rank_counts.head(10).items():
        print(f"  {rank}: {count}")
    
    # Check if professors are marked as students
    professor_ranks = ['professor', 'associate professor', 'assistant professor', 
                      'full professor', 'prof', 'prof.']
    professors_as_students = current_students[
        current_students['rank'].str.lower().str.contains('|'.join(professor_ranks), na=False)
    ]
    print(f"\nProfessors marked as current students: {len(professors_as_students)}")
    if len(professors_as_students) > 0:
        print("Examples:")
        print(professors_as_students[['name', 'rank', 'affiliation']].head(10).to_string())
    
    # 3. Investigate future years (2025+)
    print("\n\n3. FUTURE YEARS ANALYSIS")
    print("="*50)
    
    future_years = appearances_df[appearances_df['phd_graduation_year'] > 2024]
    print(f"Total with future years: {len(future_years)}")
    
    print("\nFuture year distribution:")
    print(future_years['phd_graduation_year'].value_counts().sort_index())
    
    print("\nExamples with future years:")
    print(future_years[['name', 'rank', 'affiliation', 'phd_graduation_year']].head(10).to_string())
    
    # 4. Check enrichment cache to understand the source
    print("\n\n4. ENRICHMENT CACHE ANALYSIS")
    print("="*50)
    
    cache_file = base_dir / "03_data_collection/cache/speaker_enrichment/enrichment_cache.json"
    if cache_file.exists():
        import json
        with open(cache_file, 'r') as f:
            cache = json.load(f)
        
        print(f"Total cached entries: {len(cache)}")
        
        # Sample some problematic cases from cache
        problematic_names = []
        
        # Add some professors marked as students
        if len(professors_as_students) > 0:
            for _, prof in professors_as_students.head(5).iterrows():
                problematic_names.append((prof['name'], prof['discipline'], prof['affiliation']))
        
        # Add some with future years
        if len(future_years) > 0:
            for _, fut in future_years.head(5).iterrows():
                problematic_names.append((fut['name'], fut['discipline'], fut['affiliation']))
        
        print("\nChecking cache for problematic cases:")
        for name, disc, aff in problematic_names[:10]:
            # Try to find in cache
            found = False
            for cache_key, cache_val in cache.items():
                if name.lower() in str(cache_val).lower():
                    print(f"\n{name} ({disc}):")
                    print(f"  PhD year in cache: {cache_val.get('phd_year')}")
                    print(f"  Affiliation in cache: {cache_val.get('affiliation')}")
                    found = True
                    break
            if not found:
                print(f"\n{name}: Not found in cache")
    
    # 5. Recommendations
    print("\n\n5. RECOMMENDATIONS")
    print("="*50)
    
    print("\n1. Missing PhD years (15.5%):")
    print("   - May be due to speakers not found by Perplexity")
    print("   - Could be non-academic speakers without PhDs")
    print("   - Recommendation: Re-run enrichment with improved prompts")
    
    print("\n2. High number of 'current students' (15%):")
    print("   - Likely issue with Perplexity interpretation")
    print("   - Many professors incorrectly marked as students")
    print("   - Recommendation: Add validation based on rank")
    
    print("\n3. Future years (2025):")
    print("   - Likely confusion with expected graduation dates")
    print("   - Recommendation: Filter out future years in validation")
    
    print("\n4. Suggested prompt improvements:")
    print("   - Explicitly state 'past PhD graduation year'")
    print("   - Add examples to clarify expected format")
    print("   - Cross-reference with academic rank for validation")

if __name__ == "__main__":
    main()