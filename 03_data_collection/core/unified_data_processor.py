"""
Unified Data Processor for Search Costs RCT
Handles data merging, cleaning, and problematic name removal according to CLAUDE.md specifications

Key features:
- Merges Fall + Spring data
- Removes problematic names (TBD, NA, etc.) using LLM validation
- Filters to academic year (Jul 2024 - Jun 2025)
- REMOVES same-day duplicate speakers (same name + university + discipline on same date)
- Counts unique speakers by name + discipline + affiliation
- Preserves data integrity: unique speaker count remains unchanged after duplicate removal
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys
from datetime import datetime
import asyncio
import os
from openai import AsyncOpenAI
import json
from dotenv import load_dotenv

# Load environment variables
env_path = Path(__file__).parent.parent.parent / '.env'
if env_path.exists():
    load_dotenv(env_path)
else:
    # Fallback to absolute path
    env_path = Path('/mnt/c/Users/jcerv/Jose/search-costs/.env')
    if env_path.exists():
        load_dotenv(env_path)

# Add config and core to path
sys.path.append(str(Path(__file__).parent / ".."))
sys.path.append(str(Path(__file__).parent / "../.."))
from config.settings import config
from core.normalization import normalize_text, generate_speaker_id

class UnifiedDataProcessor:
    """
    Single source of truth for data processing pipeline
    Handles Fall + Spring data merge, duplicate detection, and semester assignment
    """
    
    def __init__(self):
        self.config = config
        # Define semester boundaries
        self.fall_start = pd.Timestamp('2024-07-01')
        self.fall_end = pd.Timestamp('2024-12-31')
        self.spring_start = pd.Timestamp('2025-01-01')
        self.spring_end = pd.Timestamp('2025-06-30')
        
    def process_fall_data(self):
        """
        Process Fall data: merge main + lailanie supplement
        Returns DataFrame with combined Fall data
        """
        print("\n=== Processing Fall Data ===")
        
        # Load main Fall data
        main_file = self.config.MASTER_DATA_FALL
        if not main_file.exists():
            raise FileNotFoundError(f"Main Fall data not found: {main_file}")
            
        print(f"Loading main Fall data: {main_file}")
        df_main = pd.read_csv(main_file, encoding='utf-8-sig', low_memory=False)
        print(f"  - {len(df_main)} seminars loaded")
        
        # Check for Lailanie supplement
        lailanie_file = self.config.MASTER_DATA_LAILANIE
        if lailanie_file.exists():
            print(f"\nLoading Lailanie supplement: {lailanie_file}")
            df_lailanie = pd.read_csv(lailanie_file, encoding='utf-8-sig', low_memory=False)
            print(f"  - {len(df_lailanie)} seminars in supplement")
            
            # Merge speakers from Lailanie into main data
            df_main = self._merge_speaker_supplement(df_main, df_lailanie)
        else:
            print("  - No Lailanie supplement found, using main data only")
            
        return df_main
    
    def _merge_speaker_supplement(self, df_main, df_supplement):
        """
        Merge additional speakers from supplement into main data
        """
        print("\nMerging speaker supplement...")
        
        # Get speaker columns pattern
        speaker_cols = [col for col in df_main.columns 
                       if any(prefix in col for prefix in ['First Name_', 'Last Name_', 'rank_', 'date_', 'university_'])]
        
        # Get max speaker number
        max_speaker = max([int(col.split('_')[-1]) for col in speaker_cols 
                          if col.split('_')[-1].isdigit()])
        
        speakers_added = 0
        seminars_updated = 0
        
        # For each seminar in supplement
        for idx, supp_row in df_supplement.iterrows():
            seminar_id = supp_row['seminar_id']
            
            # Find in main data
            main_mask = df_main['seminar_id'] == seminar_id
            if not main_mask.any():
                continue
                
            main_idx = df_main[main_mask].index[0]
            
            # Find first empty slot in main data
            first_empty = None
            for i in range(1, max_speaker + 1):
                first_name = df_main.loc[main_idx, f'First Name_{i}']
                last_name = df_main.loc[main_idx, f'Last Name_{i}']
                
                if pd.isna(first_name) and pd.isna(last_name):
                    first_empty = i
                    break
            
            if first_empty is None:
                continue
            
            # Copy speakers from supplement
            slot_idx = first_empty
            seminar_speakers_added = 0
            
            for i in range(1, max_speaker + 1):
                if slot_idx > max_speaker:
                    break
                    
                first_name = supp_row.get(f'First Name_{i}')
                if pd.notna(first_name) and str(first_name).strip():
                    # Copy all speaker fields
                    for prefix in ['First Name', 'Last Name', 'rank', 'date', 'university']:
                        col_name = f'{prefix}_{i}'
                        if col_name in supp_row.index:
                            df_main.at[main_idx, f'{prefix}_{slot_idx}'] = supp_row[col_name]
                    
                    slot_idx += 1
                    seminar_speakers_added += 1
                    speakers_added += 1
            
            if seminar_speakers_added > 0:
                seminars_updated += 1
        
        print(f"  - Seminars updated: {seminars_updated}")
        print(f"  - Speakers added: {speakers_added}")
        
        return df_main
    
    def process_spring_data(self):
        """
        Process Spring data from Google Sheets or local file
        Returns DataFrame with Spring data
        """
        print("\n=== Processing Spring Data ===")
        
        spring_file = self.config.MASTER_DATA_SPRING
        if not spring_file.exists():
            print("Spring data file not found - attempting to pull from Google Sheets...")
            # Import and use google sheets client
            from core.google_sheets_client import google_sheets_client
            
            sheet_url = 'https://docs.google.com/spreadsheets/d/1k6xDRMJkYGaX0cbXZ3cyJeEUMYJSs6fMIQEn-T--3QQ/edit?gid=1686776172#gid=1686776172'
            sheet_name = "Spring '25 Seminars"
            
            try:
                df_spring = google_sheets_client.fetch_spring_data(sheet_url, sheet_name)
                if df_spring is None:
                    raise ValueError("Failed to fetch Spring data from Google Sheets")
                print(f"  - Retrieved {len(df_spring)} seminars from Google Sheets")
            except Exception as e:
                print(f"ERROR: Could not retrieve Spring data: {e}")
                raise
        else:
            print(f"Loading Spring data: {spring_file}")
            df_spring = pd.read_csv(spring_file, encoding='utf-8-sig', low_memory=False)
            print(f"  - {len(df_spring)} seminars loaded")
            
        return df_spring
    
    def merge_fall_spring_data(self, df_fall, df_spring):
        """
        Merge Fall and Spring data into a unified dataset
        Handles different column structures and preserves all speakers
        """
        print("\n=== Merging Fall and Spring Data ===")
        
        # Standardize column names in Spring data
        df_spring = self._standardize_spring_columns(df_spring)
        
        # Get unique seminar IDs from both
        fall_seminars = set(df_fall['seminar_id'].unique())
        spring_seminars = set(df_spring['seminar_id'].unique())
        
        common_seminars = fall_seminars & spring_seminars
        print(f"  - Fall seminars: {len(fall_seminars)}")
        print(f"  - Spring seminars: {len(spring_seminars)}")
        print(f"  - Common seminars: {len(common_seminars)}")
        
        # Since we're dealing with the same seminars across two semesters,
        # we need to keep ALL speakers from both datasets
        # The Fall data has Fall 2024 speakers, Spring data has Spring 2025 speakers
        
        # Start with Fall data
        df_merged = df_fall.copy()
        
        # For each seminar, we need to find the first available slot to add Spring speakers
        speakers_added_spring = 0
        seminars_updated = 0
        
        for idx, spring_row in df_spring.iterrows():
            seminar_id = spring_row['seminar_id']
            
            # Check if this seminar exists in Fall data
            if seminar_id in fall_seminars:
                # Find this seminar in merged data
                fall_mask = df_merged['seminar_id'] == seminar_id
                if not fall_mask.any():
                    continue
                    
                fall_idx = df_merged[fall_mask].index[0]
                
                # Find the first empty slot after existing speakers
                first_empty = None
                for i in range(1, 204):  # Include both Fall (1-128) and Spring (129-203) speakers
                    first_name_col = f'First Name_{i}'
                    if first_name_col in df_merged.columns:
                        first_name = df_merged.loc[fall_idx, first_name_col]
                        if pd.isna(first_name) or str(first_name).strip() == '':
                            first_empty = i
                            break
                    else:
                        first_empty = i
                        break
                
                if first_empty is None:
                    print(f"Warning: No slots available for seminar {seminar_id}")
                    continue
                
                # Copy all Spring speakers starting from first empty slot
                slot_idx = first_empty
                spring_speakers_for_seminar = 0
                
                for i in range(1, 204):  # Include both Fall (1-128) and Spring (129-203) speakers
                    if slot_idx > 128:
                        break
                    
                    first_name_col = f'First Name_{i}'
                    if first_name_col in spring_row.index:
                        first_name = spring_row[first_name_col]
                        
                        if pd.notna(first_name) and str(first_name).strip():
                            # Copy all speaker data (including canceled ones)
                            for prefix in ['First Name', 'Last Name', 'rank', 'date', 'university']:
                                source_col = f'{prefix}_{i}'
                                target_col = f'{prefix}_{slot_idx}'
                                
                                if source_col in spring_row.index:
                                    # Ensure column exists in merged dataframe with correct dtype
                                    if target_col not in df_merged.columns:
                                        df_merged[target_col] = pd.Series(dtype='object')
                                    
                                    # Ensure the column has object dtype to avoid dtype warnings
                                    if df_merged[target_col].dtype != 'object':
                                        df_merged[target_col] = df_merged[target_col].astype('object')
                                    
                                    df_merged.at[fall_idx, target_col] = spring_row[source_col]
                            
                            slot_idx += 1
                            spring_speakers_for_seminar += 1
                            speakers_added_spring += 1
                
                if spring_speakers_for_seminar > 0:
                    seminars_updated += 1
            else:
                # This is a Spring-only seminar (shouldn't happen with current data)
                print(f"Note: Seminar {seminar_id} exists only in Spring data")
        
        print(f"  - Seminars updated with Spring speakers: {seminars_updated}")
        print(f"  - Total Spring speakers added: {speakers_added_spring}")
        
        return df_merged
    
    def _standardize_spring_columns(self, df_spring):
        """
        Standardize Spring column names to match Fall format
        """
        # First, handle the BOM and leading space in column names
        df_spring.columns = df_spring.columns.str.strip()
        
        # Rename columns to match Fall format
        rename_map = {
            'index': 'seminar_id',
            'seminar_link': 'Link',
            'seminar name': 'seminar_name'
        }
        
        df_spring = df_spring.rename(columns=rename_map)
        
        # Ensure essential columns exist
        essential_cols = ['condition', 'contact_type', 'discipline', 'bin_category']
        for col in essential_cols:
            if col not in df_spring.columns:
                df_spring[col] = np.nan
                
        return df_spring
    
    def normalize_date_for_comparison(self, date_str):
        """Normalize dates for duplicate detection - removes time component"""
        if pd.isna(date_str):
            return None
        
        try:
            # Parse the date
            date_obj = pd.to_datetime(date_str)
            # Return just the date part (no time)
            return date_obj.date()
        except:
            return None
    
    async def check_names_batch_llm(self, names_batch):
        """
        Check multiple names at once with LLM for efficiency
        Returns dict mapping index to is_problematic boolean
        """
        # Initialize OpenAI client
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            # Fallback to simple pattern matching
            results = {}
            for idx, (first_name, last_name) in enumerate(names_batch):
                results[idx] = self.is_problematic_name_simple(first_name, last_name)
            return results
        
        client = AsyncOpenAI(api_key=api_key)
        
        # Build names list for batch checking
        names_list = []
        for idx, (first_name, last_name) in enumerate(names_batch):
            first_clean = str(first_name).strip() if pd.notna(first_name) else ''
            last_clean = str(last_name).strip() if pd.notna(last_name) else ''
            names_list.append(f"{idx}: First: '{first_clean}', Last: '{last_clean}'")
        
        prompt = f"""Analyze these names and determine which are problematic (not real speaker names).

Names to check:
{chr(10).join(names_list)}

Problematic names include:
- Placeholders (TBD, TBA, NA, N/A, Unknown, Pending)
- Holiday/break indicators (Spring Break, Fall Break, Holiday)
- Seminar status indicators (Cancelled, No Seminar, No Speaker)
- Non-name text (Stop the Bleed Safety Training, etc.)
- Single characters or very short meaningless text
- Empty or near-empty names

Return JSON with format:
{{"results": [{{"index": 0, "is_problematic": true/false}}, ...]}}"""

        try:
            response = await client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                response_format={"type": "json_object"}
            )
            
            result = json.loads(response.choices[0].message.content)
            return {item['index']: item['is_problematic'] for item in result['results']}
            
        except Exception as e:
            print(f"Error checking names batch with LLM: {e}")
            # Fallback to simple pattern matching
            results = {}
            for idx, (first_name, last_name) in enumerate(names_batch):
                results[idx] = self.is_problematic_name_simple(first_name, last_name)
            return results
    
    async def is_problematic_name_llm(self, first_name, last_name):
        """
        Use LLM to check if a name is problematic (TBD, NA, placeholder, etc.)
        Returns True if the name should be removed, False if it's a valid speaker name
        """
        # Quick check for empty names
        first_clean = str(first_name).strip() if pd.notna(first_name) else ''
        last_clean = str(last_name).strip() if pd.notna(last_name) else ''
        
        if len(first_clean) + len(last_clean) < 2:
            return True
        
        # Use batch method for single name
        results = await self.check_names_batch_llm([(first_name, last_name)])
        return results.get(0, False)
    
    def is_obviously_problematic(self, first_name, last_name):
        """Check if name is obviously problematic using strict pattern matching"""
        # Convert to lowercase for checking
        first_clean = str(first_name).strip().lower() if pd.notna(first_name) else ''
        last_clean = str(last_name).strip().lower() if pd.notna(last_name) else ''
        full_clean = f"{first_clean} {last_clean}".strip()
        
        # Check if both names are effectively empty or very short
        if len(first_clean) + len(last_clean) < 2:
            return True
        
        # Exact matches for common problematic entries
        obvious_problematic = [
            'tbd', 'tba', 'na', 'n/a', 'n.a.', 'nan', 'none', 'no', 
            'unknown', 'pending', 'cancelled', 'canceled', 'tbc',
            'holiday', 'spring break', 'fall break', 'winter break', 
            'no seminar', 'no speaker', 'vacant', 'empty', 'blank',
            'test', 'delete', 'remove', 'xxxxx', '????', '---',
            'stop the bleed safety training', 'safety training',
            'placeholder', 'temp', 'temporary', 'filler'
        ]
        
        # Check exact matches
        if first_clean in obvious_problematic or last_clean in obvious_problematic:
            return True
        
        if full_clean in obvious_problematic:
            return True
        
        # Check if name is just numbers or special characters
        if first_clean and first_clean.replace('.', '').replace('-', '').isdigit():
            return True
        if last_clean and last_clean.replace('.', '').replace('-', '').isdigit():
            return True
        
        # Check for repeated characters (e.g., "xxx", "...")
        if first_clean and len(set(first_clean.replace(' ', ''))) == 1:
            return True
        if last_clean and len(set(last_clean.replace(' ', ''))) == 1:
            return True
        
        return False
    
    def is_uncertain_name(self, first_name, last_name):
        """Check if name needs LLM validation (edge cases)"""
        first_clean = str(first_name).strip() if pd.notna(first_name) else ''
        last_clean = str(last_name).strip() if pd.notna(last_name) else ''
        
        # Already checked as obviously problematic
        if self.is_obviously_problematic(first_name, last_name):
            return False
        
        # Single letter names might be initials or problematic
        if (len(first_clean) == 1 and not last_clean) or (len(last_clean) == 1 and not first_clean):
            return True
        
        # Very short combined names (2-3 chars total)
        if 2 <= len(first_clean) + len(last_clean) <= 3:
            return True
        
        # Names that might be abbreviations or codes
        uncertain_patterns = [
            'dr', 'prof', 'mr', 'mrs', 'ms',  # Titles without actual names
            'guest', 'visitor', 'speaker',     # Generic descriptors
            'lunch', 'dinner', 'break',        # Event descriptors
            'meeting', 'seminar', 'talk'       # Event types
        ]
        
        first_lower = first_clean.lower()
        last_lower = last_clean.lower()
        
        # Check if it's ONLY a title or descriptor
        if first_lower in uncertain_patterns and not last_clean:
            return True
        if last_lower in uncertain_patterns and not first_clean:
            return True
        
        # Mixed case single words that might be codes
        if not last_clean and first_clean and any(c.isupper() for c in first_clean[1:]):
            # e.g., "ToBeDetermined", "NoSpeaker"
            return True
        
        return False
    
    def is_problematic_name_simple(self, first_name, last_name):
        """Fallback simple pattern matching for problematic names"""
        problematic_names = ['tbd', 'tba', 'na', 'n/a', 'nan', 'none', 'no', 
                           'stop the bleed safety training', 'unknown', 'pending',
                           'cancelled', 'canceled', 'tbc', 'holiday', 'spring break',
                           'fall break', 'winter break', 'no seminar', 'no speaker']
        
        # Check first name
        if pd.notna(first_name):
            first_clean = str(first_name).strip().lower()
            if first_clean in problematic_names:
                return True
        
        # Check last name
        if pd.notna(last_name):
            last_clean = str(last_name).strip().lower()
            if last_clean in problematic_names:
                return True
        
        # Check if both names are effectively empty
        first_clean = str(first_name).strip() if pd.notna(first_name) else ''
        last_clean = str(last_name).strip() if pd.notna(last_name) else ''
        
        if len(first_clean) + len(last_clean) < 2:
            return True
        
        return False
    
    def is_problematic_name(self, first_name, last_name):
        """Check if a name is TBD, NA, or other problematic entry"""
        problematic_names = ['tbd', 'tba', 'na', 'n/a', 'nan', 'none', 'no', 
                           'stop the bleed safety training', 'unknown', 'pending',
                           'cancelled', 'canceled', 'tbc', 'holiday', 'spring break',
                           'fall break', 'winter break', 'no seminar', 'no speaker']
        
        # Check first name
        if pd.notna(first_name):
            first_clean = str(first_name).strip().lower()
            if first_clean in problematic_names:
                return True
        
        # Check last name
        if pd.notna(last_name):
            last_clean = str(last_name).strip().lower()
            if last_clean in problematic_names:
                return True
        
        # Check if both names are effectively empty
        first_clean = str(first_name).strip() if pd.notna(first_name) else ''
        last_clean = str(last_name).strip() if pd.notna(last_name) else ''
        
        if len(first_clean) + len(last_clean) < 2:
            return True
        
        return False
    
    async def clean_speaker_names(self, df):
        """
        Clean speaker names by removing problematic entries
        NOTE: This step preserves all duplicates initially. Same-day duplicates are removed
        in a separate step after date filtering to ensure data integrity.
        Only removes:
        - Problematic names (TBD, NA, placeholders, etc.)
        - Empty or invalid entries
        
        Optimized to use pattern matching first, LLM only for uncertain cases
        """
        print("\n=== Cleaning Speaker Names (Initial Cleaning) ===")
        
        problematic_names_removed = 0
        uncertain_names = []
        
        # First pass: Remove obvious problematic names with pattern matching
        print("Removing obvious problematic names...")
        for idx, row in df.iterrows():
            for i in range(1, 204):  # Include both Fall (1-128) and Spring (129-203) speakers
                first_name = row.get(f'First Name_{i}')
                last_name = row.get(f'Last Name_{i}')
                
                # Skip empty slots
                if pd.isna(first_name) and pd.isna(last_name):
                    continue
                
                # Use simple pattern matching first
                if self.is_obviously_problematic(first_name, last_name):
                    # Remove this speaker
                    for prefix in ['First Name', 'Last Name', 'rank', 'date', 'university']:
                        col_name = f'{prefix}_{i}'
                        if col_name in df.columns:
                            df.at[idx, col_name] = np.nan
                    problematic_names_removed += 1
                elif self.is_uncertain_name(first_name, last_name):
                    # Add to uncertain list for LLM checking
                    uncertain_names.append({
                        'idx': idx,
                        'position': i,
                        'first_name': first_name,
                        'last_name': last_name
                    })
        
        print(f"  - Removed {problematic_names_removed} obviously problematic names")
        
        # Second pass: Use LLM only for uncertain cases
        if uncertain_names:
            print(f"  - Checking {len(uncertain_names)} uncertain names with LLM...")
            
            # Only check uncertain names with LLM
            batch_size = 50
            llm_removed = 0
            
            for batch_start in range(0, len(uncertain_names), batch_size):
                batch_end = min(batch_start + batch_size, len(uncertain_names))
                batch = uncertain_names[batch_start:batch_end]
                
                # Prepare names for batch checking
                names_for_llm = [(info['first_name'], info['last_name']) for info in batch]
                
                # Check batch with LLM
                problematic_results = await self.check_names_batch_llm(names_for_llm)
                
                # Process results
                for idx_in_batch, name_info in enumerate(batch):
                    if problematic_results.get(idx_in_batch, False):
                        # Remove this speaker
                        idx = name_info['idx']
                        i = name_info['position']
                        
                        for prefix in ['First Name', 'Last Name', 'rank', 'date', 'university']:
                            col_name = f'{prefix}_{i}'
                            if col_name in df.columns:
                                df.at[idx, col_name] = np.nan
                        llm_removed += 1
            
            print(f"  - Removed {llm_removed} additional names flagged by LLM")
            problematic_names_removed += llm_removed
        
        print(f"\n  - Total removed: {problematic_names_removed} problematic name entries")
        print("  - All duplicates preserved at this stage (removed later in pipeline)")
        
        # Count statistics
        total_appearances = 0
        unique_speakers = set()
        
        for idx, row in df.iterrows():
            seminar_discipline = row.get('discipline', '')
            
            for i in range(1, 204):  # Include both Fall (1-128) and Spring (129-203) speakers
                first_name = row.get(f'First Name_{i}')
                last_name = row.get(f'Last Name_{i}')
                
                if pd.notna(first_name) or pd.notna(last_name):
                    total_appearances += 1
                    
                    # Track unique speakers using shared speaker ID generation
                    full_name = f"{first_name or ''} {last_name or ''}".strip()
                    
                    # Get standardized affiliation if available
                    uni_col = f'university_{i}'
                    uni_std_col = f'university_{i}_standardized'
                    if uni_std_col in df.columns and pd.notna(row.get(uni_std_col)):
                        affiliation = row.get(uni_std_col)
                    elif uni_col in df.columns and pd.notna(row.get(uni_col)):
                        affiliation = row.get(uni_col)
                    else:
                        affiliation = row.get('university', '')
                    
                    # Generate speaker ID using shared function
                    speaker_id = generate_speaker_id(full_name, seminar_discipline, affiliation)
                    if speaker_id:  # Only add if valid ID was generated
                        unique_speakers.add(speaker_id)
        
        print(f"  - Total speaker appearances: {total_appearances:,}")
        print(f"  - Unique speakers (by name + discipline + affiliation): {len(unique_speakers):,}")
        
        return df
    
    def filter_speakers_by_academic_year(self, df):
        """
        Filter out speakers who fall outside the academic year (July 2024 - June 2025)
        Keep only speakers with dates within the academic year range
        Remove speakers without dates or with unparseable dates
        """
        print("\n=== Filtering Speakers by Academic Year ===")
        print(f"Academic year: {self.fall_start.strftime('%B %Y')} - {self.spring_end.strftime('%B %Y')}")
        
        speakers_removed_out_of_range = 0
        speakers_removed_no_date = 0
        speakers_removed_bad_date = 0
        speakers_kept_in_range = 0
        
        # Process each seminar
        for idx, row in df.iterrows():
            for i in range(1, 204):  # Include both Fall (1-128) and Spring (129-203) speakers
                first_name = row.get(f'First Name_{i}')
                date = row.get(f'date_{i}')
                
                if pd.notna(first_name) and str(first_name).strip():
                    if pd.notna(date):
                        try:
                            speaker_date = pd.to_datetime(date)
                            
                            # Check if within academic year
                            if speaker_date < self.fall_start or speaker_date > self.spring_end:
                                # Remove this speaker - outside academic year
                                for prefix in ['First Name', 'Last Name', 'rank', 'date', 'university']:
                                    col_name = f'{prefix}_{i}'
                                    if col_name in df.columns:
                                        df.at[idx, col_name] = np.nan
                                speakers_removed_out_of_range += 1
                            else:
                                speakers_kept_in_range += 1
                        except:
                            # Remove speakers with unparseable dates
                            for prefix in ['First Name', 'Last Name', 'rank', 'date', 'university']:
                                col_name = f'{prefix}_{i}'
                                if col_name in df.columns:
                                    df.at[idx, col_name] = np.nan
                            speakers_removed_bad_date += 1
                    else:
                        # Remove speakers with no date
                        for prefix in ['First Name', 'Last Name', 'rank', 'date', 'university']:
                            col_name = f'{prefix}_{i}'
                            if col_name in df.columns:
                                df.at[idx, col_name] = np.nan
                        speakers_removed_no_date += 1
        
        print(f"  - Speakers removed (outside academic year): {speakers_removed_out_of_range:,}")
        print(f"  - Speakers removed (no date): {speakers_removed_no_date:,}")
        print(f"  - Speakers removed (unparseable date): {speakers_removed_bad_date:,}")
        print(f"  - Speakers kept (within academic year): {speakers_kept_in_range:,}")
        print(f"  - Total speakers removed: {speakers_removed_out_of_range + speakers_removed_no_date + speakers_removed_bad_date:,}")
        print(f"  - Total speakers remaining: {speakers_kept_in_range:,}")
        
        return df
    
    def remove_same_day_duplicates(self, df):
        """
        Remove duplicate speakers who appear multiple times on the same day
        A duplicate is defined as same name + university + discipline on the same date
        Keeps the first occurrence and removes subsequent duplicates
        """
        print("\n=== Removing Same-Day Duplicate Speakers ===")
        
        # Track speakers seen on each date
        speakers_by_date = {}
        duplicates_removed = 0
        total_appearances_before = 0
        
        # First pass: identify all speakers and their dates
        for idx, row in df.iterrows():
            seminar_discipline = row.get('discipline', '')
            
            for i in range(1, 204):  # Include both Fall (1-128) and Spring (129-203) speakers
                first_name = row.get(f'First Name_{i}')
                last_name = row.get(f'Last Name_{i}')
                date = row.get(f'date_{i}')
                
                if pd.notna(first_name) and str(first_name).strip():
                    total_appearances_before += 1
                    
                    if pd.notna(date):
                        try:
                            # Normalize date to just the date part (no time)
                            speaker_date = pd.to_datetime(date).date()
                            
                            # Get speaker's university/affiliation
                            uni_col = f'university_{i}'
                            uni_std_col = f'university_{i}_standardized'
                            if uni_std_col in df.columns and pd.notna(row.get(uni_std_col)):
                                affiliation = str(row.get(uni_std_col))
                            elif uni_col in df.columns and pd.notna(row.get(uni_col)):
                                affiliation = str(row.get(uni_col))
                            else:
                                affiliation = str(row.get('university', ''))
                            
                            # Create speaker key
                            full_name = f"{first_name or ''} {last_name or ''}".strip()
                            speaker_key = (full_name.lower(), affiliation.lower(), seminar_discipline.lower(), speaker_date)
                            
                            # Track this speaker occurrence
                            if speaker_key not in speakers_by_date:
                                speakers_by_date[speaker_key] = []
                            speakers_by_date[speaker_key].append((idx, i))
                        except:
                            pass  # Skip speakers with unparseable dates
        
        # Second pass: remove duplicates (keep first occurrence)
        for speaker_key, occurrences in speakers_by_date.items():
            if len(occurrences) > 1:
                # Keep the first occurrence, remove the rest
                for idx, i in occurrences[1:]:
                    # Remove this duplicate speaker
                    for prefix in ['First Name', 'Last Name', 'rank', 'date', 'university']:
                        col_name = f'{prefix}_{i}'
                        if col_name in df.columns:
                            df.at[idx, col_name] = np.nan
                    duplicates_removed += 1
        
        # Count remaining appearances
        total_appearances_after = 0
        unique_speakers = set()
        
        for idx, row in df.iterrows():
            seminar_discipline = row.get('discipline', '')
            
            for i in range(1, 204):
                first_name = row.get(f'First Name_{i}')
                last_name = row.get(f'Last Name_{i}')
                
                if pd.notna(first_name) and str(first_name).strip():
                    total_appearances_after += 1
                    
                    # Track unique speakers
                    full_name = f"{first_name or ''} {last_name or ''}".strip()
                    uni_col = f'university_{i}'
                    uni_std_col = f'university_{i}_standardized'
                    if uni_std_col in df.columns and pd.notna(row.get(uni_std_col)):
                        affiliation = row.get(uni_std_col)
                    elif uni_col in df.columns and pd.notna(row.get(uni_col)):
                        affiliation = row.get(uni_col)
                    else:
                        affiliation = row.get('university', '')
                    
                    speaker_id = generate_speaker_id(full_name, seminar_discipline, affiliation)
                    if speaker_id:
                        unique_speakers.add(speaker_id)
        
        print(f"  - Total appearances before: {total_appearances_before:,}")
        print(f"  - Same-day duplicates removed: {duplicates_removed:,}")
        print(f"  - Total appearances after: {total_appearances_after:,}")
        print(f"  - Reduction: {duplicates_removed/total_appearances_before*100:.1f}%")
        print(f"  - Unique speakers (unchanged): {len(unique_speakers):,}")
        
        return df
    
    def assign_semesters_and_calculate_stats(self, df):
        """
        Assign speakers to correct semesters based on date
        Calculate statistics about speaker distribution
        """
        print("\n=== Assigning Semesters and Calculating Statistics ===")
        
        # Initialize counters
        fall_speakers = 0
        spring_speakers = 0
        undated_speakers = 0
        
        # Process each seminar
        for idx, row in df.iterrows():
            for i in range(1, 204):  # Include both Fall (1-128) and Spring (129-203) speakers
                first_name = row.get(f'First Name_{i}')
                date = row.get(f'date_{i}')
                
                if pd.notna(first_name) and str(first_name).strip():
                    if pd.notna(date):
                        try:
                            speaker_date = pd.to_datetime(date)
                            
                            if self.fall_start <= speaker_date <= self.fall_end:
                                fall_speakers += 1
                            elif self.spring_start <= speaker_date <= self.spring_end:
                                spring_speakers += 1
                            # Note: out_of_range_speakers should be 0 after filtering
                        except:
                            undated_speakers += 1
                    else:
                        undated_speakers += 1
        
        # Add summary columns
        df['data_source'] = 'merged'
        df['last_updated'] = datetime.now().strftime('%Y-%m-%d')
        
        # Print statistics
        total_speakers = fall_speakers + spring_speakers + undated_speakers
        print(f"\n=== Speaker Distribution (After Filtering) ===")
        print(f"  - Total speakers: {total_speakers:,}")
        print(f"  - Fall semester (Jul-Dec 2024): {fall_speakers:,} ({fall_speakers/total_speakers*100:.1f}%)")
        print(f"  - Spring semester (Jan-Jun 2025): {spring_speakers:,} ({spring_speakers/total_speakers*100:.1f}%)")
        if undated_speakers > 0:
            print(f"  - WARNING: Found {undated_speakers:,} speakers without dates ({undated_speakers/total_speakers*100:.1f}%) - these should have been removed!")
        
        # Seminar statistics
        seminars_with_speakers = df.apply(lambda row: any(pd.notna(row.get(f'First Name_{i}', None)) 
                                         for i in range(1, 204)), axis=1).sum()  # Check all speaker slots
        
        print(f"\n=== Seminar Statistics ===")
        print(f"  - Total seminars: {len(df):,}")
        print(f"  - Seminars with speakers: {seminars_with_speakers:,} ({seminars_with_speakers/len(df)*100:.1f}%)")
        print(f"  - Empty seminars: {len(df) - seminars_with_speakers:,}")
        
        return df
    
    async def run_full_pipeline(self):
        """
        Run the complete data processing pipeline
        """
        print("\n" + "="*60)
        print("SEARCH COSTS RCT - DATA PROCESSING PIPELINE (WITH DATE FILTERING + SAME-DAY DUPLICATE REMOVAL)")
        print("="*60)
        print(f"Started at: {datetime.now()}")
        
        # Step 1: Process Fall data
        df_fall = self.process_fall_data()
        
        # Step 2: Process Spring data
        df_spring = self.process_spring_data()
        
        # Step 3: Merge Fall and Spring
        df_merged = self.merge_fall_spring_data(df_fall, df_spring)
        
        # Step 4: Clean speaker names (preserving all duplicates initially)
        df_cleaned = await self.clean_speaker_names(df_merged)
        
        # Step 5: Filter speakers by academic year
        df_filtered = self.filter_speakers_by_academic_year(df_cleaned)
        
        # Step 6: Remove same-day duplicates (NEW)
        df_deduplicated = self.remove_same_day_duplicates(df_filtered)
        
        # Step 7: Calculate statistics and finalize
        df_final = self.assign_semesters_and_calculate_stats(df_deduplicated)
        
        # Step 8: Save final dataset
        output_file = self.config.MASTER_DATA_FINAL
        df_final.to_csv(output_file, index=False, encoding='utf-8-sig')
        print(f"\n✅ Master dataset saved to: {output_file}")
        
        print(f"\nCompleted at: {datetime.now()}")
        print("="*60)
        
        return df_final


if __name__ == "__main__":
    processor = UnifiedDataProcessor()
    asyncio.run(processor.run_full_pipeline())