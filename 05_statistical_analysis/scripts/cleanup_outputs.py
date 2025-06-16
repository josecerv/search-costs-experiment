#!/usr/bin/env python3
"""
Clean up unnecessary CSV files from the outputs directory
"""
import os
from pathlib import Path
import shutil

def main():
    """Remove unnecessary intermediate CSV files"""
    outputs_dir = Path(__file__).parent.parent / "outputs"
    
    # Files to remove (intermediate versions that are no longer needed)
    files_to_remove = [
        "master_analysis_dataset_final.csv",
        "master_analysis_dataset_with_recipients.csv",
        "female_urm_recipient_stats.csv",  # Redundant with detailed demographics
        "llm_database_speaker_matches.csv"  # Superseded by comprehensive version
    ]
    
    # Files to keep (essential for analysis)
    essential_files = [
        "master_analysis_dataset.csv",  # Main dataset (now integrated)
        "master_analysis_dataset_metadata.json",  # Metadata for main dataset
        "seminar_batch_mapping.csv",  # Required for experimental design
        "llm_database_speaker_matches_comprehensive.csv",  # Database matching
        "database_impact_final.csv",  # For Figure 5
        "database_impact_final.json",  # Supporting data
        "database_impact_summary_final.csv",  # Summary stats
        "email_recipient_demographics_by_dept.csv",  # Email recipient analysis
        "email_recipient_demographics_detailed.csv",  # Detailed recipient data
        "email_recipient_demographics_cache.json",  # Cache file
        "DATABASE_ANALYSIS_SUMMARY.md",  # Documentation
        "balance_checks_results.xlsx",  # Balance check results
        "comprehensive_summary_statistics.xlsx",  # Summary statistics
        "latex_tables/",  # Keep entire directory
        "llm_matching_comprehensive_analysis.json",  # LLM analysis
        "llm_matching_comprehensive_report.txt",  # LLM report
        "phd_years_moderation_analysis.json",  # PhD years analysis
        "phd_years_moderation_report.md"  # PhD years report
    ]
    
    print("Cleaning up unnecessary CSV files from outputs directory...")
    print("="*60)
    
    removed_count = 0
    
    for file_name in files_to_remove:
        file_path = outputs_dir / file_name
        if file_path.exists():
            # Create backup directory if it doesn't exist
            backup_dir = outputs_dir / "_removed_files"
            backup_dir.mkdir(exist_ok=True)
            
            # Move file to backup instead of deleting
            backup_path = backup_dir / file_name
            shutil.move(str(file_path), str(backup_path))
            print(f"✓ Moved to backup: {file_name}")
            removed_count += 1
        else:
            print(f"  Already removed: {file_name}")
    
    print("="*60)
    print(f"Moved {removed_count} files to _removed_files/ backup directory")
    
    # List remaining CSV files
    print("\nRemaining CSV files in outputs directory:")
    remaining_csvs = sorted(outputs_dir.glob("*.csv"))
    for csv_file in remaining_csvs:
        file_size = csv_file.stat().st_size / 1024 / 1024  # MB
        print(f"  - {csv_file.name} ({file_size:.1f} MB)")
    
    print(f"\nTotal CSV files remaining: {len(remaining_csvs)}")
    
    # Print summary of what each remaining file is used for
    print("\nPurpose of remaining files:")
    print("  - master_analysis_dataset.csv: Main integrated dataset with all variables")
    print("  - seminar_batch_mapping.csv: Maps seminars to experimental batches")
    print("  - llm_database_speaker_matches_comprehensive.csv: Database speaker matching results")
    print("  - database_impact_*.csv: Database impact analysis for Figure 5")
    print("  - email_recipient_demographics_*.csv: Email recipient demographic analysis")

if __name__ == "__main__":
    main()