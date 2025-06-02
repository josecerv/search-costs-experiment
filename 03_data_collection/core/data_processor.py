"""
Unified Data Processor for Search Costs RCT
Consolidates multiple data processing scripts into a single configurable pipeline
"""

import pandas as pd
import numpy as np
import os
import re
import unicodedata
from pathlib import Path
import argparse
import sys
from datetime import datetime

# Add config to path
sys.path.append(str(Path(__file__).parent / ".."))
from config.settings import config

class DataProcessor:
    """
    Unified data processing pipeline for Search Costs RCT
    Handles merging, cleaning, and validation of research data
    """
    
    def __init__(self):
        self.config = config
        print(f"=== Search Costs RCT Data Processor ===")
        print(f"Initialized at: {datetime.now()}")
    
    def normalize_string(self, s):
        """Normalize strings for consistent matching"""
        if pd.isna(s):
            return None
        s = str(s)
        
        # Remove accents and normalize Unicode
        try:
            s = ''.join(c for c in unicodedata.normalize('NFD', s) 
                       if unicodedata.category(c) != 'Mn')
        except Exception:
            pass
        
        s = s.lower()
        s = s.replace('&', 'and')
        # Keep word chars, whitespace, hyphen
        s = re.sub(r'[^\w\s-]', '', s)
        # Standardize whitespace
        s = re.sub(r'\s+', ' ', s).strip()
        
        return s if s else None
    
    def validate_data_structure(self, df, required_columns):
        """Validate that DataFrame has required columns"""
        missing_cols = [col for col in required_columns if col not in df.columns]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")
        
        # Strip whitespace from column names
        df.columns = df.columns.str.strip()
        return df
    
    def merge_fall_datasets(self):
        """
        Merge main fall data with Lailanie's supplemental data
        Lailanie's data supplements the main data with additional speakers
        """
        print("\n=== Merging Fall Datasets ===")
        
        main_file = self.config.MASTER_DATA_FALL
        lailanie_file = self.config.MASTER_DATA_LAILANIE
        output_file = self.config.MASTER_DATA_COMPLETE
        
        # Check main file exists
        if not main_file.exists():
            raise FileNotFoundError(f"Main data file not found: {main_file}")
        
        print(f"Loading main data from: {main_file}")
        df_main = pd.read_csv(main_file, encoding='utf-8-sig', low_memory=False)
        print(f"  - {len(df_main)} rows loaded")
        
        # Check if Lailanie file exists
        if not lailanie_file.exists():
            print(f"WARNING: Lailanie file not found: {lailanie_file}")
            print("Using only main data...")
            
            # Save main data as complete dataset
            df_main.to_csv(output_file, index=False, encoding='utf-8-sig')
            print(f"Saved {len(df_main)} seminars to {output_file}")
            return df_main
        
        print(f"Loading Lailanie data from: {lailanie_file}")
        df_lailanie = pd.read_csv(lailanie_file, encoding='utf-8-sig', low_memory=False)
        print(f"  - {len(df_lailanie)} rows loaded")
        
        # Ensure both dataframes have seminar_id
        if 'seminar_id' not in df_main.columns or 'seminar_id' not in df_lailanie.columns:
            raise ValueError("Both datasets must have 'seminar_id' column for merging")
        
        # Identify speaker columns (all columns with pattern First Name_X, Last Name_X, etc.)
        import re
        speaker_pattern = re.compile(r'(First Name|Last Name|rank|date|university)_\d+')
        
        # Get all speaker columns from both datasets
        main_speaker_cols = [col for col in df_main.columns if speaker_pattern.match(col)]
        lailanie_speaker_cols = [col for col in df_lailanie.columns if speaker_pattern.match(col)]
        
        # Get the maximum speaker number from both datasets
        def get_max_speaker_num(cols):
            nums = []
            for col in cols:
                match = re.search(r'_(\d+)$', col)
                if match:
                    nums.append(int(match.group(1)))
            return max(nums) if nums else 0
        
        max_main_speaker = get_max_speaker_num(main_speaker_cols)
        max_lailanie_speaker = get_max_speaker_num(lailanie_speaker_cols)
        max_speaker = max(max_main_speaker, max_lailanie_speaker)
        
        print(f"Max speaker slots: Main={max_main_speaker}, Lailanie={max_lailanie_speaker}")
        
        # Standardize columns - ensure both have all speaker columns
        for i in range(1, max_speaker + 1):
            for prefix in ['First Name', 'Last Name', 'rank', 'date', 'university']:
                col_name = f"{prefix}_{i}"
                if col_name not in df_main.columns:
                    df_main[col_name] = np.nan
                if col_name not in df_lailanie.columns:
                    df_lailanie[col_name] = np.nan
        
        # Add missing non-speaker columns
        main_cols = set(df_main.columns)
        lailanie_cols = set(df_lailanie.columns)
        
        missing_in_main = lailanie_cols - main_cols
        missing_in_lailanie = main_cols - lailanie_cols
        
        if missing_in_main:
            print(f"Columns in Lailanie but not main: {missing_in_main}")
            for col in missing_in_main:
                if col != 'canceled/not found':  # Skip this column
                    df_main[col] = np.nan
        
        if missing_in_lailanie:
            print(f"Columns in main but not Lailanie: {missing_in_lailanie}")
            for col in missing_in_lailanie:
                df_lailanie[col] = np.nan
        
        # For each seminar in Lailanie's data, supplement the main data
        print("\nSupplementing main data with Lailanie's speakers...")
        
        seminars_updated = 0
        speakers_added = 0
        
        for idx, lailanie_row in df_lailanie.iterrows():
            seminar_id = lailanie_row['seminar_id']
            
            # Find this seminar in main data
            main_mask = df_main['seminar_id'] == seminar_id
            if not main_mask.any():
                # This seminar doesn't exist in main data - skip it
                print(f"Warning: Seminar {seminar_id} in Lailanie data not found in main data")
                continue
            
            main_idx = df_main[main_mask].index[0]
            main_row = df_main.loc[main_idx]
            
            # Find the first empty speaker slot in main data
            first_empty_slot = None
            for i in range(1, max_speaker + 1):
                first_name_col = f"First Name_{i}"
                last_name_col = f"Last Name_{i}"
                
                # Check if this slot is empty in main data
                if (pd.isna(main_row[first_name_col]) or str(main_row[first_name_col]).strip() == '') and \
                   (pd.isna(main_row[last_name_col]) or str(main_row[last_name_col]).strip() == ''):
                    first_empty_slot = i
                    break
            
            if first_empty_slot is None:
                print(f"Warning: No empty slots in seminar {seminar_id}")
                continue
            
            # Copy speakers from Lailanie data to main data starting from first empty slot
            slot_idx = first_empty_slot
            speakers_added_for_seminar = 0
            
            for i in range(1, max_speaker + 1):
                # Check if Lailanie has a speaker in this slot
                first_name = lailanie_row.get(f"First Name_{i}")
                last_name = lailanie_row.get(f"Last Name_{i}")
                
                if pd.notna(first_name) and str(first_name).strip() != '':
                    # Copy speaker data to main dataframe
                    for prefix in ['First Name', 'Last Name', 'rank', 'date', 'university']:
                        source_col = f"{prefix}_{i}"
                        target_col = f"{prefix}_{slot_idx}"
                        if source_col in lailanie_row.index:
                            df_main.at[main_idx, target_col] = lailanie_row[source_col]
                    
                    slot_idx += 1
                    speakers_added_for_seminar += 1
                    speakers_added += 1
            
            if speakers_added_for_seminar > 0:
                seminars_updated += 1
        
        print(f"\nMerge complete:")
        print(f"  - Seminars updated: {seminars_updated}")
        print(f"  - Speakers added: {speakers_added}")
        
        # Save combined dataset
        df_main.to_csv(output_file, index=False, encoding='utf-8-sig')
        
        print(f"\nCombined dataset created: {output_file}")
        print(f"  - Total seminars: {len(df_main)}")
        
        # Treatment balance check
        if 'condition' in df_main.columns:
            condition_counts = df_main['condition'].value_counts()
            print(f"\nTreatment balance:")
            for condition, count in condition_counts.items():
                print(f"  {condition}: {count} seminars")
        
        return df_main
    
    def clean_master_data(self, df):
        """
        Clean and validate master data
        Consolidates functionality from clean-master.py
        """
        print("\n=== Cleaning Master Data ===")
        
        initial_count = len(df)
        print(f"Starting with {initial_count} rows")
        
        # Required columns for basic analysis
        required_cols = ['seminar_id', 'university', 'discipline', 'seminar_name']
        missing_required = [col for col in required_cols if col not in df.columns]
        
        if missing_required:
            print(f"Warning: Missing required columns: {missing_required}")
        
        # Remove rows with missing seminar_id
        if 'seminar_id' in df.columns:
            before_count = len(df)
            df = df.dropna(subset=['seminar_id'])
            after_count = len(df)
            if before_count != after_count:
                print(f"Removed {before_count - after_count} rows with missing seminar_id")
        
        # Remove duplicate seminar_ids
        if 'seminar_id' in df.columns:
            before_count = len(df)
            df = df.drop_duplicates(subset=['seminar_id'], keep='first')
            after_count = len(df)
            if before_count != after_count:
                print(f"Removed {before_count - after_count} duplicate seminar_ids")
        
        # Clean text columns
        text_columns = ['university', 'discipline', 'seminar_name']
        for col in text_columns:
            if col in df.columns:
                # Strip whitespace
                df[col] = df[col].astype(str).str.strip()
                # Replace empty strings with NaN
                df[col] = df[col].replace('', np.nan)
        
        # Validate speaker columns
        speaker_cols = [col for col in df.columns if re.match(r'(First Name|Last Name|rank|university|date)_\d+', col)]
        print(f"Found {len(speaker_cols)} speaker columns")
        
        # Count seminars with speakers
        seminars_with_speakers = 0
        for idx, row in df.iterrows():
            has_speaker = False
            i = 1
            while f'First Name_{i}' in df.columns or f'Last Name_{i}' in df.columns:
                fn = row.get(f'First Name_{i}', '')
                ln = row.get(f'Last Name_{i}', '')
                if pd.notna(fn) and str(fn).strip() or pd.notna(ln) and str(ln).strip():
                    has_speaker = True
                    break
                i += 1
            if has_speaker:
                seminars_with_speakers += 1
        
        print(f"Seminars with at least one speaker: {seminars_with_speakers}")
        
        # Add data quality metrics
        df['data_quality_score'] = 1.0
        
        # Reduce score for missing critical data
        for col in ['university', 'discipline', 'condition']:
            if col in df.columns:
                missing_mask = df[col].isna()
                df.loc[missing_mask, 'data_quality_score'] -= 0.2
        
        print(f"Cleaning complete: {len(df)} rows remaining")
        print(f"Average data quality score: {df['data_quality_score'].mean():.3f}")
        
        return df
    
    def validate_experimental_design(self, df):
        """
        Validate experimental design requirements
        Checks treatment balance, stratification, etc.
        """
        print("\n=== Validating Experimental Design ===")
        
        # Check for required experimental columns
        exp_columns = ['condition', 'bin_category']
        missing_exp_cols = [col for col in exp_columns if col not in df.columns]
        
        if missing_exp_cols:
            print(f"Warning: Missing experimental columns: {missing_exp_cols}")
            return False
        
        # Treatment balance
        if 'condition' in df.columns:
            condition_counts = df['condition'].value_counts()
            print(f"Treatment assignment:")
            for condition, count in condition_counts.items():
                print(f"  {condition}: {count} ({count/len(df)*100:.1f}%)")
            
            # Check balance
            control_count = condition_counts.get('control', 0)
            treatment_count = condition_counts.get('treatment', 0)
            
            if control_count > 0 and treatment_count > 0:
                balance_ratio = min(control_count, treatment_count) / max(control_count, treatment_count)
                print(f"Balance ratio: {balance_ratio:.3f}")
                
                if balance_ratio < 0.8:
                    print("Warning: Treatment groups are imbalanced")
        
        # Stratification check
        if 'bin_category' in df.columns:
            bin_counts = df['bin_category'].value_counts()
            print(f"\nStratification bins:")
            for bin_cat, count in bin_counts.items():
                print(f"  {bin_cat}: {count}")
            
            # Check treatment balance within bins
            if 'condition' in df.columns:
                cross_tab = pd.crosstab(df['bin_category'], df['condition'])
                print(f"\nTreatment balance by bin:")
                print(cross_tab)
        
        # Department-level analysis
        if 'university' in df.columns and 'discipline' in df.columns:
            df['department'] = df['university'].astype(str) + ' - ' + df['discipline'].astype(str)
            dept_counts = df['department'].value_counts()
            print(f"\nTop 10 departments by seminar count:")
            print(dept_counts.head(10))
        
        return True
    
    def merge_spring_data(self, fall_df=None):
        """
        Merge Spring speakers with Fall seminar data based on index
        Same seminars, just adding Spring 2025 speaker data
        """
        print("\n=== Merging Spring Data ===")
        
        # Load fall data if not provided
        if fall_df is None:
            if not self.config.MASTER_DATA_COMPLETE.exists():
                print("Fall data not found, merging fall data first...")
                fall_df = self.merge_fall_datasets()
            else:
                fall_df = pd.read_csv(self.config.MASTER_DATA_COMPLETE, encoding='utf-8-sig', low_memory=False)
        
        # Check if Spring data exists
        spring_file = self.config.MASTER_DATA_SPRING
        if not spring_file.exists():
            print(f"WARNING: Spring data not found: {spring_file}")
            print("Run: python3 scripts/pull_spring_data.py to fetch Spring data")
            return fall_df
        
        print(f"Loading Spring data from: {spring_file}")
        spring_df = pd.read_csv(spring_file, encoding='utf-8-sig', low_memory=False)
        print(f"  - {len(spring_df)} rows loaded")
        
        # Extract Spring speakers and merge with Fall seminar metadata
        print("Extracting Spring speakers and joining with Fall seminar data...")
        
        # Get the join key (index column)
        spring_index_col = None
        for col in [' index', 'index', 'seminar_id']:
            if col in spring_df.columns:
                spring_index_col = col
                break
        
        if spring_index_col is None:
            print("ERROR: No index column found in Spring data")
            return fall_df
        
        # Find maximum number of speakers in current dataset
        speaker_cols = [col for col in fall_df.columns if col.startswith('First Name_')]
        max_speaker_num = len(speaker_cols)
        print(f"Fall data has speakers up to #{max_speaker_num}")
        
        # First, determine the maximum number of Spring speakers any seminar has
        max_spring_speakers_per_seminar = 0
        spring_data_by_seminar = {}
        
        for _, spring_row in spring_df.iterrows():
            spring_index = spring_row[spring_index_col]
            
            # Find matching Fall seminar
            if spring_index not in fall_df['seminar_id'].values:
                continue
                
            # Count Spring speakers for this seminar
            spring_speakers = []
            for i in range(1, 101):
                first_name_col = f'First Name_{i}'
                if (first_name_col in spring_row.index and 
                    pd.notna(spring_row[first_name_col]) and 
                    str(spring_row[first_name_col]).strip() != ''):
                    
                    speaker = {
                        'first_name': str(spring_row[first_name_col]).strip(),
                        'last_name': str(spring_row.get(f'Last Name_{i}', '')).strip(),
                        'rank': str(spring_row.get(f'rank_{i}', '')).strip(),
                        'date': str(spring_row.get(f'date_{i}', '')).strip(),
                        'university': str(spring_row.get(f'university_{i}', '')).strip()
                    }
                    spring_speakers.append(speaker)
            
            if spring_speakers:
                spring_data_by_seminar[spring_index] = spring_speakers
                max_spring_speakers_per_seminar = max(max_spring_speakers_per_seminar, len(spring_speakers))
        
        print(f"Maximum Spring speakers for any seminar: {max_spring_speakers_per_seminar}")
        
        # Now add the necessary columns all at once
        if max_spring_speakers_per_seminar > 0:
            # Create new columns for the maximum number of Spring speakers
            new_cols = []
            for i in range(max_speaker_num + 1, max_speaker_num + max_spring_speakers_per_seminar + 1):
                new_cols.extend([
                    f'First Name_{i}',
                    f'Last Name_{i}', 
                    f'rank_{i}',
                    f'date_{i}',
                    f'university_{i}'
                ])
            
            # Add all empty columns at once to avoid fragmentation
            empty_cols_df = pd.DataFrame(index=fall_df.index, columns=new_cols)
            fall_df = pd.concat([fall_df, empty_cols_df], axis=1)
            
            # Now populate the data for each seminar
            spring_speakers_added = 0
            seminars_updated = 0
            
            for seminar_id, speakers in spring_data_by_seminar.items():
                # Find the Fall seminar row
                fall_idx = fall_df[fall_df['seminar_id'] == seminar_id].index[0]
                
                # Add Spring speakers starting from max_speaker_num + 1
                current_speaker_num = max_speaker_num + 1
                for speaker in speakers:
                    fall_df.loc[fall_idx, f'First Name_{current_speaker_num}'] = speaker['first_name']
                    fall_df.loc[fall_idx, f'Last Name_{current_speaker_num}'] = speaker['last_name']
                    fall_df.loc[fall_idx, f'rank_{current_speaker_num}'] = speaker['rank']
                    fall_df.loc[fall_idx, f'date_{current_speaker_num}'] = speaker['date']
                    fall_df.loc[fall_idx, f'university_{current_speaker_num}'] = speaker['university']
                    
                    current_speaker_num += 1
                    spring_speakers_added += 1
                
                seminars_updated += 1
        
        # Save combined dataset
        output_file = self.config.MASTER_DATA_FULL_YEAR
        fall_df.to_csv(output_file, index=False, encoding='utf-8-sig')
        
        print(f"Full academic year dataset created: {output_file}")
        print(f"  - Base seminars: {len(fall_df)}")
        print(f"  - Seminars updated with Spring speakers: {seminars_updated}")
        print(f"  - Total Spring speakers added: {spring_speakers_added}")
        
        return fall_df
    
    def _standardize_spring_data(self, spring_df):
        """
        Standardize Spring data columns to match Fall data structure
        """
        print("Standardizing Spring data structure...")
        
        # Handle duplicate column names by renaming
        spring_df = spring_df.copy()
        cols = spring_df.columns.tolist()
        
        # Fix duplicate university/department/seminar name columns
        # Keep the second occurrence as the main ones
        if 'university' in cols:
            first_uni_idx = cols.index('university')
            if cols.count('university') > 1:
                second_uni_idx = cols.index('university', first_uni_idx + 1)
                cols[first_uni_idx] = 'university_temp'  # Rename first occurrence
        
        if 'department' in cols:
            first_dept_idx = cols.index('department')
            if cols.count('department') > 1:
                second_dept_idx = cols.index('department', first_dept_idx + 1)
                cols[first_dept_idx] = 'department_temp'  # Rename first occurrence
                
        if 'seminar name' in cols:
            first_sem_idx = cols.index('seminar name')
            if cols.count('seminar name') > 1:
                second_sem_idx = cols.index('seminar name', first_sem_idx + 1)
                cols[first_sem_idx] = 'seminar_name_temp'  # Rename first occurrence
        
        spring_df.columns = cols
        
        # Column mapping for common variations
        column_mappings = {
            'seminar name': 'seminar_name',
            'department': 'discipline',  # Use main department column as discipline
            ' index': 'seminar_id',  # Remove leading space
            'index': 'seminar_id'
        }
        
        # Apply column mappings
        for old_col, new_col in column_mappings.items():
            if old_col in spring_df.columns and new_col not in spring_df.columns:
                spring_df[new_col] = spring_df[old_col]
        
        # Split full speaker names if needed
        if 'First Name_1' in spring_df.columns and 'Last Name_1' not in spring_df.columns:
            def split_name(full_name):
                if pd.isna(full_name) or str(full_name).strip() == '':
                    return '', ''
                parts = str(full_name).strip().split()
                if len(parts) == 1:
                    return parts[0], ''
                elif len(parts) >= 2:
                    return parts[0], ' '.join(parts[1:])
                return '', ''
            
            name_splits = spring_df['First Name_1'].apply(split_name)
            spring_df['First Name_1'] = [split[0] for split in name_splits]
            spring_df['Last Name_1'] = [split[1] for split in name_splits]
        
        # Add required columns that are missing in Spring data
        if 'seminar_id' not in spring_df.columns:
            if ' index' in spring_df.columns:
                spring_df['seminar_id'] = spring_df[' index']
            else:
                spring_df['seminar_id'] = [f"spring_{i:04d}" for i in range(len(spring_df))]
        
        if 'condition' not in spring_df.columns:
            spring_df['condition'] = 'spring_semester'  # Mark as Spring semester
            
        if 'contact_type' not in spring_df.columns:
            spring_df['contact_type'] = 'unknown'
            
        if 'bin_category' not in spring_df.columns:
            spring_df['bin_category'] = 'spring'
            
        if 'Link' not in spring_df.columns:
            if 'seminar_link' in spring_df.columns:
                spring_df['Link'] = spring_df['seminar_link']
            else:
                spring_df['Link'] = ''
                
        # Create department field if missing
        if 'department' not in spring_df.columns:
            univ = spring_df.get('university', 'Unknown University')
            disc = spring_df.get('discipline', 'Unknown Discipline')
            spring_df['department'] = univ.astype(str) + ' - ' + disc.astype(str)
        
        print(f"Spring data standardized: {len(spring_df)} rows, {len(spring_df.columns)} columns")
        return spring_df

    def prepare_for_analysis(self, mode='merge'):
        """
        Main entry point for data preparation
        """
        if mode == 'merge':
            print("Mode: Merge fall datasets")
            df = self.merge_fall_datasets()
            
        elif mode == 'merge-spring':
            print("Mode: Merge fall and spring datasets")
            df = self.merge_spring_data()
            
        elif mode == 'clean':
            print("Mode: Clean existing complete dataset")
            if not self.config.MASTER_DATA_COMPLETE.exists():
                raise FileNotFoundError("Complete dataset not found. Run 'merge' mode first.")
            
            df = pd.read_csv(self.config.MASTER_DATA_COMPLETE, encoding='utf-8-sig', low_memory=False)
            
        elif mode == 'validate':
            print("Mode: Validate dataset")
            if not self.config.MASTER_DATA_COMPLETE.exists():
                raise FileNotFoundError("Complete dataset not found. Run 'merge' mode first.")
            
            df = pd.read_csv(self.config.MASTER_DATA_COMPLETE, encoding='utf-8-sig', low_memory=False)
            self.validate_experimental_design(df)
            return df
            
        else:
            raise ValueError(f"Unknown mode: {mode}")
        
        # Clean the data
        df = self.clean_master_data(df)
        
        # Validate experimental design
        self.validate_experimental_design(df)
        
        # Save cleaned data
        if mode in ['merge', 'clean']:
            df.to_csv(self.config.MASTER_DATA_COMPLETE, index=False, encoding='utf-8-sig')
            print(f"\nFinal dataset saved: {self.config.MASTER_DATA_COMPLETE}")
        
        return df
    
    def get_processing_summary(self):
        """Get summary of data processing status"""
        files_status = {
            'master_fall': self.config.MASTER_DATA_FALL.exists(),
            'master_lailanie': self.config.MASTER_DATA_LAILANIE.exists(),
            'master_complete': self.config.MASTER_DATA_COMPLETE.exists()
        }
        
        print("\n=== Data Processing Status ===")
        for file_type, exists in files_status.items():
            status = "✅" if exists else "❌"
            print(f"{status} {file_type}")
        
        if files_status['master_complete']:
            df = pd.read_csv(self.config.MASTER_DATA_COMPLETE, encoding='utf-8-sig', low_memory=False)
            print(f"\nComplete dataset: {len(df)} seminars")
            
            if 'condition' in df.columns:
                condition_counts = df['condition'].value_counts()
                print(f"Treatment balance: {condition_counts.to_dict()}")
        
        return files_status

def main():
    """Command line interface"""
    parser = argparse.ArgumentParser(description='Search Costs RCT Data Processor')
    parser.add_argument('--mode', choices=['merge', 'merge-spring', 'clean', 'validate', 'status'], 
                       default='merge', help='Processing mode')
    
    args = parser.parse_args()
    
    processor = DataProcessor()
    
    if args.mode == 'status':
        processor.get_processing_summary()
    else:
        processor.prepare_for_analysis(mode=args.mode)
    
    print("\n=== Processing Complete ===")

if __name__ == "__main__":
    main()