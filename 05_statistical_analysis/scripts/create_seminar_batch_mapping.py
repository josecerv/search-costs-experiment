#!/usr/bin/env python3
"""
FIXED version of seminar batch mapping that correctly extracts batch numbers from filenames.
"""

import os
import sys
import pandas as pd
import numpy as np
import json
from pathlib import Path
from difflib import SequenceMatcher
import glob
import re
from typing import Dict, List, Tuple, Set, Optional
from collections import defaultdict

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent.parent))

class SeminarBatchMapper:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent.parent
        self.batch_path = self.base_path / "02_intervention_materials" / "email_campaigns" / "send-one"
        self.output_path = self.base_path / "05_statistical_analysis" / "outputs"
        self.output_path.mkdir(exist_ok=True)
        
        # Track matched seminars per batch for process of elimination
        self.batch_seminar_counts = defaultdict(int)  # Expected count per batch
        self.batch_seminars_matched = defaultdict(set)  # Actual matched seminars per batch
        
        # Statistics tracking
        self.stats = {
            'total_emails': 0,
            'unique_seminars_in_batches': 0,
            'seminars_matched': 0,
            'seminars_unmatched': 0,
            'match_types': {
                'exact': 0,
                'fuzzy': 0,
                'department': 0
            },
            'emails_by_contact_type': {},
            'seminars_per_batch': {},
            'unmatched_seminars': []
        }
    
    def extract_batch_number(self, filename: str) -> int:
        """Extract batch number from filename like 'batch7-20240627.xlsx'."""
        match = re.search(r'batch(\d+)-', filename)
        if match:
            return int(match.group(1))
        else:
            raise ValueError(f"Could not extract batch number from filename: {filename}")
    
    def load_batch_files(self) -> pd.DataFrame:
        """Load all batch Excel files and combine them."""
        print("\nLoading batch files...")
        batch_files = glob.glob(str(self.batch_path / "batch*.xlsx"))
        
        all_batches = []
        batch_file_map = {}
        
        for file_path in batch_files:
            filename = Path(file_path).name
            batch_num = self.extract_batch_number(filename)
            batch_file_map[batch_num] = file_path
        
        # Process in batch number order
        for batch_num in sorted(batch_file_map.keys()):
            file_path = batch_file_map[batch_num]
            filename = Path(file_path).name
            print(f"  Loading {filename} as batch {batch_num}...")
            
            df = pd.read_excel(file_path)
            df['batch_number'] = batch_num  # Use actual batch number from filename
            df['batch_file'] = filename
            all_batches.append(df)
        
        combined = pd.concat(all_batches, ignore_index=True)
        
        # Statistics
        self.stats['total_emails'] = len(combined)
        self.stats['emails_by_contact_type'] = combined['contact_type'].value_counts().to_dict()
        
        print(f"\nLoaded {len(combined)} emails from {len(batch_files)} batch files")
        print(f"Contact types: {self.stats['emails_by_contact_type']}")
        
        return combined
    
    def _normalize_discipline(self, discipline: str) -> str:
        """Normalize discipline name to match seminar list format."""
        discipline_lower = discipline.lower().strip()
        
        discipline_map = {
            'physics': 'Physics',
            'physical sciences': 'Physics',
            'chemistry': 'Chemistry',
            'chemical': 'Chemistry',
            'chemical sciences': 'Chemistry',
            'math': 'Mathematics',
            'mathematics': 'Mathematics',
            'mathematical sciences': 'Mathematics',
            'applied mathematics': 'Mathematics',
            'applied math': 'Mathematics',
            'mechanical engineering': 'Mechanical Engineering',
            'mechanical': 'Mechanical Engineering',
            'mech eng': 'Mechanical Engineering',
            'meche': 'Mechanical Engineering',
            'me': 'Mechanical Engineering',
            'me department': 'Mechanical Engineering',
            'computer science': 'Computer Science',
            'computer': 'Computer Science',
            'computing': 'Computer Science',
            'cs': 'Computer Science',
            'comp sci': 'Computer Science',
            'computer sciences': 'Computer Science'
        }
        
        for key, value in discipline_map.items():
            if key in discipline_lower:
                return value
        
        return discipline.strip()
    
    def normalize_university_name(self, university: str) -> str:
        """Normalize university names to handle em dashes, hyphens, and other variations."""
        # Replace em dashes with regular hyphens
        normalized = university.replace('–', '-')  # em dash to hyphen
        normalized = normalized.replace('—', '-')  # en dash to hyphen
        return normalized
    
    def universities_match(self, univ1: str, univ2: str) -> bool:
        """Check if two university names match, handling dash variations."""
        norm1 = self.normalize_university_name(univ1).lower().strip()
        norm2 = self.normalize_university_name(univ2).lower().strip()
        
        if norm1 == norm2:
            return True
        
        # Check if one uses em dash and other uses hyphen
        if norm1.replace('-', '') == norm2.replace('-', ''):
            return True
        
        return False
    
    def extract_seminar_info_from_batches(self, batch_df: pd.DataFrame) -> pd.DataFrame:
        """Extract unique seminar-batch mappings from email data."""
        print("\nExtracting seminar information from batch emails...")
        
        seminar_batch_mappings = []
        batch_seminar_sets = defaultdict(set)
        
        for _, row in batch_df.iterrows():
            # Parse department info
            dept_parts = row['department'].rsplit('-', 1)
            if len(dept_parts) == 2:
                university = dept_parts[0].strip()
                discipline = dept_parts[1].strip()
            else:
                university = row['department'].strip()
                discipline = 'Unknown'
                print(f"    Warning: Unexpected department format: {row['department']}")
            
            # Normalize discipline
            discipline = self._normalize_discipline(discipline)
            
            # Parse seminar names
            seminar_names = [s.strip() for s in str(row['seminar_names']).split(',')]
            
            for seminar_name in seminar_names:
                if seminar_name and seminar_name.lower() != 'nan':
                    # Create unique key for tracking
                    seminar_key = (university, discipline, seminar_name)
                    batch_seminar_sets[row['batch_number']].add(seminar_key)
                    
                    mapping = {
                        'university': university,
                        'discipline': discipline,
                        'department': row['department'],
                        'seminar_name': seminar_name,
                        'batch_number': row['batch_number'],
                        'contact_type': row['contact_type'],
                        'condition': row['condition']
                    }
                    seminar_batch_mappings.append(mapping)
        
        # Store expected seminars per batch
        for batch_num, seminars in batch_seminar_sets.items():
            self.batch_seminar_counts[batch_num] = len(seminars)
            print(f"  Batch {batch_num}: {len(seminars)} unique seminars")
        
        # Create DataFrame and remove duplicates
        mapping_df = pd.DataFrame(seminar_batch_mappings)
        
        # Keep one batch per seminar (prioritizing based on contact type)
        contact_priority = {'seminar_contact': 1, 'faculty': 2, 'department_chair': 3}
        mapping_df['priority'] = mapping_df['contact_type'].map(contact_priority)
        
        # Sort and keep first occurrence
        mapping_df = mapping_df.sort_values(['university', 'discipline', 'seminar_name', 'priority'])
        unique_mappings = mapping_df.groupby(['university', 'discipline', 'seminar_name']).first().reset_index()
        
        # Count seminars per batch
        for batch_num in unique_mappings['batch_number'].unique():
            count = len(unique_mappings[unique_mappings['batch_number'] == batch_num])
            self.stats['seminars_per_batch'][int(batch_num)] = count
        
        self.stats['unique_seminars_in_batches'] = len(unique_mappings)
        
        print(f"\nFound {len(unique_mappings)} unique seminars across all batches")
        print(f"Seminars per batch: {dict(sorted(self.stats['seminars_per_batch'].items()))}")
        
        return unique_mappings[['university', 'discipline', 'seminar_name', 'batch_number', 'condition']]
    
    def _fuzzy_score(self, str1: str, str2: str) -> float:
        """Calculate fuzzy match score between two strings."""
        # Normalize strings
        s1 = str1.lower().strip()
        s2 = str2.lower().strip()
        
        # Remove common words that might differ
        common_words = ['seminar', 'seminars', 'colloquium', 'colloquia', 'series', 'lecture', 'lectures']
        for word in common_words:
            s1 = s1.replace(word, '').strip()
            s2 = s2.replace(word, '').strip()
        
        return SequenceMatcher(None, s1, s2).ratio()
    
    def match_seminars_to_batches(self, batch_mappings: pd.DataFrame, seminar_list: pd.DataFrame) -> pd.DataFrame:
        """Match seminars using multiple strategies."""
        print("\nMatching seminars to batches...")
        
        # Initialize all seminars with no batch
        result = seminar_list.copy()
        result['batch_number'] = np.nan
        result['match_type'] = 'unmatched'
        result['match_score'] = 0.0
        result['condition'] = ''
        
        # Reset batch tracking
        self.batch_seminars_matched.clear()
        
        # Strategy 1: Exact matching
        print("\n1. Trying exact matches...")
        for idx, seminar in result.iterrows():
            for _, batch_sem in batch_mappings.iterrows():
                if (self.universities_match(seminar['university'], batch_sem['university']) and
                    seminar['discipline'].lower() == batch_sem['discipline'].lower() and
                    seminar['seminar_name'].lower() == batch_sem['seminar_name'].lower()):
                    
                    result.at[idx, 'batch_number'] = batch_sem['batch_number']
                    result.at[idx, 'match_type'] = 'exact'
                    result.at[idx, 'match_score'] = 1.0
                    result.at[idx, 'condition'] = batch_sem['condition']
                    self.stats['match_types']['exact'] += 1
                    self.batch_seminars_matched[batch_sem['batch_number']].add(seminar['seminar_id'])
                    break
        
        matched = result['batch_number'].notna().sum()
        print(f"  Matched {matched} seminars exactly")
        
        # Strategy 2: Fuzzy matching for unmatched seminars
        print("\n2. Trying fuzzy matches for remaining seminars...")
        unmatched_mask = result['batch_number'].isna()
        
        for idx in result[unmatched_mask].index:
            seminar = result.loc[idx]
            best_match = None
            best_score = 0.7  # Minimum threshold
            
            for _, batch_sem in batch_mappings.iterrows():
                if (self.universities_match(seminar['university'], batch_sem['university']) and
                    seminar['discipline'].lower() == batch_sem['discipline'].lower()):
                    
                    score = self._fuzzy_score(seminar['seminar_name'], batch_sem['seminar_name'])
                    
                    if score > best_score:
                        best_score = score
                        best_match = batch_sem
            
            if best_match is not None:
                result.at[idx, 'batch_number'] = best_match['batch_number']
                result.at[idx, 'match_type'] = 'fuzzy'
                result.at[idx, 'match_score'] = best_score
                result.at[idx, 'condition'] = best_match['condition']
                self.stats['match_types']['fuzzy'] += 1
                self.batch_seminars_matched[best_match['batch_number']].add(seminar['seminar_id'])
        
        matched = result['batch_number'].notna().sum()
        print(f"  Total matched after fuzzy: {matched}")
        
        # Strategy 3: Department-level fallback for remaining
        print("\n3. Using department-level modal batch for remaining seminars...")
        
        dept_modal_data = defaultdict(lambda: {'batches': [], 'conditions': []})
        
        for _, batch_sem in batch_mappings.iterrows():
            key = (self.normalize_university_name(batch_sem['university']), batch_sem['discipline'].lower())
            dept_modal_data[key]['batches'].append(batch_sem['batch_number'])
            dept_modal_data[key]['conditions'].append(batch_sem['condition'])
        
        unmatched_mask = result['batch_number'].isna()
        for idx in result[unmatched_mask].index:
            seminar = result.loc[idx]
            
            sem_key = (self.normalize_university_name(seminar['university']), seminar['discipline'].lower())
            
            if sem_key in dept_modal_data:
                # Get modal batch and condition
                batches = dept_modal_data[sem_key]['batches']
                conditions = dept_modal_data[sem_key]['conditions']
                
                if batches:
                    from collections import Counter
                    batch_counts = Counter(batches)
                    modal_batch = batch_counts.most_common(1)[0][0]
                    
                    condition_counts = Counter(conditions)
                    modal_condition = condition_counts.most_common(1)[0][0]
                    
                    result.at[idx, 'batch_number'] = modal_batch
                    result.at[idx, 'match_type'] = 'department'
                    result.at[idx, 'match_score'] = 0.5
                    result.at[idx, 'condition'] = modal_condition
                    self.stats['match_types']['department'] += 1
        
        matched = result['batch_number'].notna().sum()
        print(f"  Total matched after department fallback: {matched}")
        
        # Final statistics
        self.stats['seminars_matched'] = matched
        self.stats['seminars_unmatched'] = len(result) - matched
        
        return result
    
    def create_batch_mapping(self):
        """Main method to create the batch mapping."""
        # Load batch files
        batch_df = self.load_batch_files()
        
        # Extract seminars from batches
        batch_mappings = self.extract_seminar_info_from_batches(batch_df)
        
        # Load seminar list
        print("\nLoading seminar list...")
        seminar_list = pd.read_csv(self.base_path / "03_data_collection" / "processed" / "master-data-final.csv")
        print(f"Loaded {len(seminar_list)} seminars from master list")
        
        # Match seminars to batches
        result = self.match_seminars_to_batches(batch_mappings, seminar_list)
        
        # Save results
        output_file = self.output_path / "seminar_batch_mapping.csv"
        result[['seminar_id', 'university', 'discipline', 'seminar_name', 
                'batch_number', 'match_type', 'match_score', 'condition']].to_csv(
            output_file, index=False
        )
        
        print(f"\n=== RESULTS SAVED ===")
        print(f"Output file: {output_file}")
        
        # Save diagnostic information
        diagnostic = {
            'summary': {
                'total_seminars': len(seminar_list),
                'seminars_with_batch': int(result['batch_number'].notna().sum()),
                'coverage_rate': float(result['batch_number'].notna().sum() / len(seminar_list) * 100)
            },
            'match_quality': self.stats['match_types'],
            'batch_distribution': dict(result['batch_number'].value_counts().sort_index()),
            'condition_distribution': dict(result[result['batch_number'].notna()]['condition'].value_counts()),
            'match_type_distribution': dict(result['match_type'].value_counts()),
            'average_match_score': float(result[result['batch_number'].notna()]['match_score'].mean()),
            'email_statistics': {
                'total_emails_sent': self.stats['total_emails'],
                'emails_by_contact_type': self.stats['emails_by_contact_type'],
                'unique_seminars_in_batches': self.stats['unique_seminars_in_batches']
            }
        }
        
        diagnostic_file = self.output_path / "batch_mapping_diagnostic.json"
        with open(diagnostic_file, 'w') as f:
            # Convert numpy types to Python types for JSON serialization
            diagnostic_json = json.loads(json.dumps(diagnostic, default=lambda x: int(x) if isinstance(x, np.integer) else float(x)))
            json.dump(diagnostic_json, f, indent=2)
        
        print(f"\nDiagnostic info saved to: {diagnostic_file}")
        
        # Print summary
        print("\n=== SUMMARY ===")
        print(f"Total seminars: {len(seminar_list)}")
        print(f"Seminars matched: {self.stats['seminars_matched']}")
        print(f"Coverage: {self.stats['seminars_matched'] / len(seminar_list) * 100:.1f}%")
        print(f"\nMatch types:")
        for match_type, count in self.stats['match_types'].items():
            if count > 0:
                print(f"  {match_type}: {count}")
        
        return result

def main():
    mapper = SeminarBatchMapper()
    result = mapper.create_batch_mapping()
    
    print("\n=== DOUBLE-CHECKING RESULTS ===")
    
    # Load and verify the saved file
    saved_df = pd.read_csv(mapper.output_path / "seminar_batch_mapping.csv")
    
    print(f"\nTotal seminars in output: {len(saved_df)}")
    print(f"Seminars with batch assignment: {saved_df['batch_number'].notna().sum()}")
    print(f"Seminars without batch: {saved_df['batch_number'].isna().sum()}")
    
    # Check batch distribution
    print("\nBatch distribution:")
    batch_counts = saved_df['batch_number'].value_counts().sort_index()
    for batch, count in batch_counts.items():
        print(f"  Batch {int(batch)}: {count} seminars")
    
    print("\n=== FIXED BATCH MAPPING COMPLETE ===")

if __name__ == "__main__":
    main()