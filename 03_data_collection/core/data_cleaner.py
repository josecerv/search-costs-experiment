"""
Advanced Data Cleaning for Search Costs RCT
Handles duplicate speaker detection and other data quality issues
"""

import pandas as pd
import numpy as np
import re
import unicodedata
from pathlib import Path
import sys
from datetime import datetime

# Add config to path
sys.path.append(str(Path(__file__).parent / ".."))
from config.settings import config

class DataCleaner:
    """
    Advanced data cleaning for the Search Costs RCT
    Focuses on duplicate detection and data quality improvements
    """
    
    def __init__(self):
        self.config = config
        self.cleaning_report = {
            'duplicates_removed': 0,
            'empty_speakers_removed': 0,
            'data_quality_issues': [],
            'cleaning_timestamp': datetime.now().isoformat()
        }
    
    def normalize_for_matching(self, text):
        """Normalize text for robust duplicate detection"""
        if pd.isna(text):
            return ''
        
        text = str(text).strip()
        
        # Remove accents and normalize Unicode
        try:
            text = ''.join(c for c in unicodedata.normalize('NFD', text) 
                          if unicodedata.category(c) != 'Mn')
        except:
            pass
        
        # Convert to lowercase
        text = text.lower()
        
        # Remove common punctuation and extra spaces
        text = re.sub(r'[^\w\s-]', '', text)
        text = re.sub(r'\s+', ' ', text)
        
        # Handle common name variations
        text = text.replace('dr.', '').replace('prof.', '').replace('professor', '')
        text = text.replace('jr.', 'jr').replace('sr.', 'sr')
        
        return text.strip()
    
    def normalize_date_for_matching(self, date_str):
        """Normalize dates for duplicate detection"""
        if pd.isna(date_str):
            return ''
        
        date_str = str(date_str).strip().lower()
        
        # Remove common date formatting
        date_str = re.sub(r'[^\w\s/-]', '', date_str)
        
        # Try to extract just the date part (remove times)
        date_match = re.search(r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}', date_str)
        if date_match:
            return date_match.group()
        
        # Try other common formats
        date_match = re.search(r'\d{4}-\d{1,2}-\d{1,2}', date_str)
        if date_match:
            return date_match.group()
        
        return date_str
    
    def detect_duplicate_speakers(self, appearances_df):
        """
        Detect duplicate speakers based on name + university + date
        Returns DataFrame with duplicate information
        """
        print("\n=== Detecting Duplicate Speakers ===")
        
        if appearances_df.empty:
            return appearances_df, pd.DataFrame()
        
        # Create normalized columns for matching
        appearances_df['name_normalized'] = appearances_df['name'].apply(self.normalize_for_matching)
        appearances_df['university_normalized'] = appearances_df['university'].apply(self.normalize_for_matching)
        appearances_df['date_normalized'] = appearances_df['date'].apply(self.normalize_date_for_matching)
        
        # Filter out rows with missing critical information
        valid_mask = (
            (appearances_df['name_normalized'] != '') &
            (appearances_df['university_normalized'] != '') &
            (appearances_df['date_normalized'] != '')
        )
        
        valid_appearances = appearances_df[valid_mask].copy()
        invalid_appearances = appearances_df[~valid_mask].copy()
        
        print(f"  - Total appearances: {len(appearances_df)}")
        print(f"  - Valid for duplicate detection: {len(valid_appearances)}")
        print(f"  - Missing critical info: {len(invalid_appearances)}")
        
        if len(valid_appearances) == 0:
            return appearances_df.drop(columns=['name_normalized', 'university_normalized', 'date_normalized']), pd.DataFrame()
        
        # Group by normalized name + university + date to find duplicates
        duplicate_groups = valid_appearances.groupby([
            'name_normalized', 
            'university_normalized', 
            'date_normalized'
        ])
        
        duplicates_found = []
        
        for (name_norm, uni_norm, date_norm), group in duplicate_groups:
            if len(group) > 1:
                # Found duplicates!
                duplicates_found.append({
                    'name_normalized': name_norm,
                    'university_normalized': uni_norm,
                    'date_normalized': date_norm,
                    'duplicate_count': len(group),
                    'seminar_ids': list(group['seminar_id'].unique()),
                    'original_names': list(group['name'].unique()),
                    'original_universities': list(group['university'].unique()),
                    'original_dates': list(group['date'].unique())
                })
        
        duplicates_df = pd.DataFrame(duplicates_found)
        
        print(f"  - Duplicate speaker groups found: {len(duplicates_df)}")
        
        if len(duplicates_df) > 0:
            total_duplicate_appearances = sum(duplicates_df['duplicate_count'])
            print(f"  - Total duplicate appearances: {total_duplicate_appearances}")
            
            # Show examples
            print("\nDuplicate Examples:")
            for i, row in duplicates_df.head(3).iterrows():
                print(f"  {i+1}. '{row['original_names'][0]}' at '{row['original_universities'][0]}' on '{row['original_dates'][0]}'")
                print(f"     Appears {row['duplicate_count']} times in seminars: {row['seminar_ids']}")
        
        return appearances_df, duplicates_df
    
    def remove_duplicate_speakers(self, appearances_df):
        """
        Remove duplicate speakers, keeping only the first occurrence
        """
        print("\n=== Removing Duplicate Speakers ===")
        
        initial_count = len(appearances_df)
        
        # Detect duplicates first
        appearances_df, duplicates_df = self.detect_duplicate_speakers(appearances_df)
        
        if duplicates_df.empty:
            print("✅ No duplicates found")
            # Clean up temporary columns
            cols_to_drop = ['name_normalized', 'university_normalized', 'date_normalized']
            appearances_df = appearances_df.drop(columns=[col for col in cols_to_drop if col in appearances_df.columns])
            return appearances_df
        
        # Remove duplicates by keeping first occurrence of each name+university+date combination
        print("Removing duplicate appearances...")
        
        # Create the duplicate detection key
        appearances_df['duplicate_key'] = (
            appearances_df['name_normalized'].fillna('') + '|' +
            appearances_df['university_normalized'].fillna('') + '|' +
            appearances_df['date_normalized'].fillna('')
        )
        
        # Keep first occurrence of each duplicate key
        appearances_cleaned = appearances_df.drop_duplicates(
            subset=['duplicate_key'], 
            keep='first'
        )
        
        # Clean up temporary columns
        cols_to_drop = ['name_normalized', 'university_normalized', 'date_normalized', 'duplicate_key']
        appearances_cleaned = appearances_cleaned.drop(columns=cols_to_drop)
        
        duplicates_removed = initial_count - len(appearances_cleaned)
        
        print(f"✅ Removed {duplicates_removed} duplicate appearances")
        print(f"  - Before: {initial_count} appearances")
        print(f"  - After: {len(appearances_cleaned)} appearances")
        
        self.cleaning_report['duplicates_removed'] = duplicates_removed
        
        return appearances_cleaned
    
    def remove_empty_speakers(self, appearances_df):
        """Remove speaker appearances with no meaningful name information"""
        print("\n=== Removing Empty Speaker Entries ===")
        
        initial_count = len(appearances_df)
        
        # Define what constitutes a valid speaker
        def is_valid_speaker(row):
            name = str(row.get('name', '')).strip()
            first_name = str(row.get('first_name', '')).strip()
            last_name = str(row.get('last_name', '')).strip()
            
            # Must have at least some name information
            if len(name) >= 2:
                return True
            if len(first_name) >= 1 or len(last_name) >= 1:
                return True
            
            return False
        
        # Filter to valid speakers
        valid_mask = appearances_df.apply(is_valid_speaker, axis=1)
        appearances_cleaned = appearances_df[valid_mask].copy()
        
        empty_removed = initial_count - len(appearances_cleaned)
        
        print(f"✅ Removed {empty_removed} empty speaker entries")
        print(f"  - Before: {initial_count} appearances")
        print(f"  - After: {len(appearances_cleaned)} appearances")
        
        self.cleaning_report['empty_speakers_removed'] = empty_removed
        
        return appearances_cleaned
    
    def clean_speaker_names(self, appearances_df):
        """Clean and standardize speaker names"""
        print("\n=== Cleaning Speaker Names ===")
        
        def clean_name(name):
            if pd.isna(name):
                return ''
            
            name = str(name).strip()
            
            # Remove extra whitespace
            name = re.sub(r'\s+', ' ', name)
            
            # Fix common encoding issues
            name = name.replace('Ã¡', 'á').replace('Ã©', 'é').replace('Ã­', 'í')
            name = name.replace('Ã³', 'ó').replace('Ãº', 'ú').replace('Ã±', 'ñ')
            
            # Remove common prefixes if they're standalone
            prefixes = ['dr.', 'prof.', 'professor', 'dr', 'prof']
            for prefix in prefixes:
                if name.lower().startswith(prefix.lower() + ' '):
                    name = name[len(prefix):].strip()
            
            return name
        
        # Clean names
        for col in ['name', 'first_name', 'last_name']:
            if col in appearances_df.columns:
                appearances_df[col] = appearances_df[col].apply(clean_name)
        
        print("✅ Speaker names cleaned")
        
        return appearances_df
    
    def clean_university_names(self, appearances_df):
        """Clean and standardize university names"""
        print("\n=== Cleaning University Names ===")
        
        def clean_university(uni):
            if pd.isna(uni):
                return ''
            
            uni = str(uni).strip()
            
            # Remove extra whitespace
            uni = re.sub(r'\s+', ' ', uni)
            
            # Standardize common abbreviations
            uni = re.sub(r'\bUniv\b', 'University', uni, flags=re.IGNORECASE)
            uni = re.sub(r'\bU\.\s*of\b', 'University of', uni, flags=re.IGNORECASE)
            uni = re.sub(r'\bInst\b', 'Institute', uni, flags=re.IGNORECASE)
            
            return uni
        
        # Clean university names in relevant columns
        for col in ['university', 'affiliation']:
            if col in appearances_df.columns:
                appearances_df[col] = appearances_df[col].apply(clean_university)
        
        print("✅ University names cleaned")
        
        return appearances_df
    
    def comprehensive_cleaning(self, appearances_df):
        """
        Run comprehensive data cleaning pipeline
        """
        print(f"=== Comprehensive Data Cleaning ===")
        print(f"Started at: {datetime.now()}")
        print(f"Initial data: {len(appearances_df)} speaker appearances")
        
        # Step 1: Remove empty speakers first
        appearances_df = self.remove_empty_speakers(appearances_df)
        
        # Step 2: Clean names and universities
        appearances_df = self.clean_speaker_names(appearances_df)
        appearances_df = self.clean_university_names(appearances_df)
        
        # Step 3: Remove duplicates (after cleaning for better matching)
        appearances_df = self.remove_duplicate_speakers(appearances_df)
        
        # Final summary
        print(f"\n=== Cleaning Summary ===")
        print(f"✅ Duplicate speakers removed: {self.cleaning_report['duplicates_removed']}")
        print(f"✅ Empty speakers removed: {self.cleaning_report['empty_speakers_removed']}")
        print(f"✅ Final clean data: {len(appearances_df)} speaker appearances")
        
        # Save cleaning report
        self._save_cleaning_report()
        
        return appearances_df
    
    def _save_cleaning_report(self):
        """Save cleaning report for documentation"""
        report_path = self.config.PROCESSED_DATA_DIR / "data_cleaning_report.json"
        
        import json
        with open(report_path, 'w') as f:
            json.dump(self.cleaning_report, f, indent=2)
        
        print(f"Cleaning report saved: {report_path}")

# Global data cleaner instance
data_cleaner = DataCleaner()