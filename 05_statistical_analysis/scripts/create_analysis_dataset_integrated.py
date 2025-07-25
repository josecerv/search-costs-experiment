#!/usr/bin/env python3
"""
Create Master Analysis Dataset with All Variables (Integrated Version)
This script generates the complete dataset needed for statistical analysis,
including all pre-registered control variables, email recipient demographics,
and junior/senior speaker subgroups.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json
from datetime import datetime
import warnings
from collections import defaultdict
import hashlib
import logging
warnings.filterwarnings('ignore')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

class AnalysisDatasetCreator:
    def __init__(self):
        self.base_dir = Path("/mnt/c/Users/jcerv/Jose/search-costs")
        self.data_dir = self.base_dir / "03_data_collection/processed"
        self.demographics_dir = self.base_dir / "04_demographic_analysis/outputs"
        self.output_dir = self.base_dir / "05_statistical_analysis/outputs"
        self.archive_dir = self.base_dir / "07_archive"
        self.email_dir = self.base_dir / "02_intervention_materials/email_campaigns"
        self.databases_dir = self.base_dir / "02_intervention_materials/databases"
        self.output_dir.mkdir(exist_ok=True)
        
        # University rankings by discipline (from the JavaScript algorithm)
        self.discipline_rankings = self.load_discipline_rankings()
        
    def load_discipline_rankings(self):
        """Load university rankings for each discipline"""
        # These would be extracted from the Qualtrics scripts, but for now we'll use the ranking data
        rankings_file = self.archive_dir / "05_statistical_analysis_backup_20250530_094227/outputs/university_rankings_processed.csv"
        rankings_df = pd.read_csv(rankings_file)
        
        # Create discipline-specific rankings
        discipline_rankings = {}
        
        # Map discipline names to ranking columns
        discipline_to_rank_col = {
            'Physics': 'physics_rank',
            'Chemistry': 'chemistry_rank',
            'Mathematics': 'mathematics_rank',
            'Computer Science': 'computerScience_rank',
            'Mechanical Engineering': 'mechanicalEngineering_rank'
        }
        
        for discipline, rank_col in discipline_to_rank_col.items():
            # Get universities sorted by rank for this discipline
            disc_ranks = rankings_df[['university', rank_col]].dropna()
            disc_ranks = disc_ranks.sort_values(rank_col)
            discipline_rankings[discipline] = disc_ranks['university'].tolist()
        
        return discipline_rankings
    
    def calculate_peer_departments(self, university, discipline):
        """
        Calculate peer departments using the same algorithm as the experiment.
        Returns the number of peer departments that would be shown.
        """
        if discipline not in self.discipline_rankings:
            return np.nan
        
        ranking = self.discipline_rankings[discipline]
        
        # Find university's position
        try:
            index = ranking.index(university)
        except ValueError:
            # University not in ranking, return NaN
            return np.nan
        
        # Initial window: ±20 ranks
        min_rank = max(0, index - 20)
        max_rank = min(len(ranking) - 1, index + 20)
        peers = ranking[min_rank:max_rank + 1]
        peers = [p for p in peers if p != university]
        
        # Ensure at least 40 peers
        if len(peers) < 40:
            if min_rank == 0:
                # At the top, expand downward
                max_rank = min(len(ranking) - 1, 40)
                peers = ranking[min_rank:max_rank + 1]
            elif max_rank == len(ranking) - 1:
                # At the bottom, expand upward
                min_rank = max(0, len(ranking) - 41)
                peers = ranking[min_rank:max_rank + 1]
            
            peers = [p for p in peers if p != university]
        
        # Cap at 40 peers if more
        if len(peers) > 40:
            peers = peers[:40]
        
        return len(peers)
    
    def load_urm_faculty_data(self):
        """Load URM faculty data from the experiment databases"""
        urm_faculty_by_discipline = {}
        
        # Load each discipline's database
        for csv_file in self.databases_dir.glob("*.csv"):
            discipline = csv_file.stem.title()  # e.g., "physics.csv" -> "Physics"
            
            # Standardize discipline names
            if discipline == "Computerscience":
                discipline = "Computer Science"
            elif discipline == "Mechanicalengineering":
                discipline = "Mechanical Engineering"
            
            try:
                df = pd.read_csv(csv_file)
                # Group by university to get URM faculty count per university
                urm_by_univ = df.groupby('Schools').size().to_dict()
                urm_faculty_by_discipline[discipline] = urm_by_univ
            except Exception as e:
                print(f"  Warning: Could not load {csv_file}: {e}")
        
        return urm_faculty_by_discipline
    
    def calculate_urm_faculty_in_peers(self, university, discipline, peer_count):
        """
        Calculate total URM faculty in peer departments.
        This uses the actual peer universities and counts from the experiment databases.
        """
        if pd.isna(peer_count) or discipline not in self.urm_faculty_by_discipline:
            return np.nan
        
        # Get the peer universities (same algorithm as peer count)
        if discipline not in self.discipline_rankings:
            return np.nan
        
        ranking = self.discipline_rankings[discipline]
        
        try:
            index = ranking.index(university)
        except ValueError:
            return np.nan
        
        # Get peer universities using same algorithm
        min_rank = max(0, index - 20)
        max_rank = min(len(ranking) - 1, index + 20)
        peers = ranking[min_rank:max_rank + 1]
        peers = [p for p in peers if p != university]
        
        if len(peers) < 40:
            if min_rank == 0:
                max_rank = min(len(ranking) - 1, 40)
                peers = ranking[min_rank:max_rank + 1]
            elif max_rank == len(ranking) - 1:
                min_rank = max(0, len(ranking) - 41)
                peers = ranking[min_rank:max_rank + 1]
            peers = [p for p in peers if p != university]
        
        if len(peers) > 40:
            peers = peers[:40]
        
        # Count URM faculty in these peer universities
        urm_data = self.urm_faculty_by_discipline.get(discipline, {})
        total_urm = 0
        for peer in peers:
            total_urm += urm_data.get(peer, 0)
        
        return total_urm
    
    def load_all_data(self):
        """Load all necessary data files"""
        print("\n=== LOADING DATA ===")
        
        # Load master seminar data
        print("Loading master seminar data...")
        self.master_df = pd.read_csv(self.data_dir / "master-data-final.csv", low_memory=False)
        print(f"  Loaded {len(self.master_df)} seminars")
        
        # Load demographic analysis results
        print("\nLoading demographic analysis results...")
        self.demographics_df = pd.read_csv(self.demographics_dir / "people_combined_analysis.csv")
        print(f"  Loaded {len(self.demographics_df)} unique speakers with demographics")
        
        # Load speaker appearances
        print("\nLoading speaker appearances...")
        self.appearances_df = pd.read_csv(self.demographics_dir / "speaker_appearances_analysis.csv")
        print(f"  Loaded {len(self.appearances_df)} speaker appearances")
        
        # Load randomization data for bin categories
        print("\nLoading randomization data...")
        self.randomization_df = pd.read_csv(self.base_dir / "01_experiment_design/randomized_data.csv")
        print(f"  Loaded randomization data for {len(self.randomization_df)} departments")
        
        # Load batch mapping
        print("\nLoading batch mapping...")
        self.batch_mapping_df = pd.read_csv(self.output_dir / "seminar_batch_mapping.csv")
        print(f"  Loaded batch mapping for {len(self.batch_mapping_df)} seminars")
        
        # Load department faculty data
        print("\nLoading department faculty data...")
        self.faculty_df = pd.read_csv(self.archive_dir / "department faculty count.csv")
        print(f"  Loaded faculty data for {len(self.faculty_df)} departments")
        
        # Load university rankings
        print("\nLoading university rankings...")
        rankings_file = self.archive_dir / "05_statistical_analysis_backup_20250530_094227/outputs/university_rankings_processed.csv"
        self.rankings_df = pd.read_csv(rankings_file)
        print(f"  Loaded rankings for {len(self.rankings_df)} universities")
        
        # Load URM faculty data from experiment databases
        print("\nLoading URM faculty databases...")
        self.urm_faculty_by_discipline = self.load_urm_faculty_data()
        print(f"  Loaded URM faculty data for {len(self.urm_faculty_by_discipline)} disciplines")
        
        # Load email recipient demographics if available
        print("\nLoading email recipient demographics...")
        recipient_file = self.output_dir / "email_recipient_demographics_by_dept.csv"
        if recipient_file.exists():
            self.recipient_df = pd.read_csv(recipient_file)
            print(f"  Loaded recipient demographics for {len(self.recipient_df)} departments")
        else:
            self.recipient_df = None
            print("  Warning: email_recipient_demographics_by_dept.csv not found")
        
    def create_speaker_level_data(self):
        """Create speaker-level dataset with all demographics"""
        print("\n=== CREATING SPEAKER-LEVEL DATA ===")
        
        # Use speaker_appearances_analysis.csv which already has demographics matched by speaker_id
        print("Using speaker_appearances_analysis.csv which already has demographics...")
        
        # Calculate years since PhD for each speaker (for junior/senior classification)
        self.appearances_df['years_since_phd'] = 2024 - pd.to_numeric(self.appearances_df['phd_graduation_year'], errors='coerce')
        
        # Calculate global median years since PhD for junior/senior split
        valid_phd = self.appearances_df['years_since_phd'] > 0
        self.median_years_since_phd = self.appearances_df.loc[valid_phd, 'years_since_phd'].median()
        logger.info(f"Global median years since PhD: {self.median_years_since_phd:.1f}")
        
        # Classify speakers as junior or senior
        self.appearances_df['is_junior'] = (self.appearances_df['years_since_phd'] <= self.median_years_since_phd) & valid_phd
        self.appearances_df['is_senior'] = (self.appearances_df['years_since_phd'] > self.median_years_since_phd) & valid_phd
        
        # Create demographic flags for subgroup analysis
        self.appearances_df['is_black'] = (self.appearances_df['combined_race'] == 'black').astype(int)
        self.appearances_df['is_hispanic'] = (self.appearances_df['combined_race'] == 'latino').astype(int)
        
        # Create subgroup demographic variables
        for race in ['black', 'hispanic', 'urm']:
            # Junior subgroup
            self.appearances_df[f'is_{race}_junior'] = (
                (self.appearances_df[f'is_{race}'] == 1) & 
                self.appearances_df['is_junior']
            ).astype(int)
            
            # Senior subgroup  
            self.appearances_df[f'is_{race}_senior'] = (
                (self.appearances_df[f'is_{race}'] == 1) & 
                self.appearances_df['is_senior']
            ).astype(int)
        
        # Group appearances by seminar to calculate seminar-level statistics
        seminar_groups = self.appearances_df.groupby('seminar_id')
        
        # Process each seminar and create seminar-level statistics
        seminar_stats = []
        
        print(f"Processing {len(seminar_groups)} seminars...")
        
        for sem_idx, (seminar_id, appearances) in enumerate(seminar_groups):
            if sem_idx % 100 == 0:
                print(f"  Processed {sem_idx}/{len(seminar_groups)} seminars...")
            
            # Get seminar info from the first appearance
            seminar_info = appearances.iloc[0]
            
            # Initialize counters
            total_speakers = len(appearances)
            speakers_with_demographics = 0
            is_urm = 0
            is_black = 0
            is_hispanic = 0
            is_native_american = 0
            is_female = 0
            is_male = 0
            is_white = 0
            is_asian = 0
            
            # Junior/Senior counters
            num_junior_speakers = 0
            num_senior_speakers = 0
            num_black_junior = 0
            num_black_senior = 0
            num_hispanic_junior = 0
            num_hispanic_senior = 0
            num_urm_junior = 0
            num_urm_senior = 0
            
            # Semester-specific counters
            fall_total = 0
            fall_with_demographics = 0
            fall_urm = 0
            fall_black = 0
            fall_hispanic = 0
            fall_female = 0
            
            spring_total = 0
            spring_with_demographics = 0
            spring_urm = 0
            spring_black = 0
            spring_hispanic = 0
            spring_female = 0
            
            # Date ranges for semesters
            fall_start = pd.Timestamp('2024-07-01')
            fall_end = pd.Timestamp('2024-12-31')
            spring_start = pd.Timestamp('2025-01-01')
            spring_end = pd.Timestamp('2025-06-30')
            
            # Initialize PhD year tracking
            phd_years = []
            
            # Process each speaker appearance
            for _, speaker in appearances.iterrows():
                # Parse date for semester classification
                semester = None
                if pd.notna(speaker['date']):
                    try:
                        date = pd.to_datetime(speaker['date'])
                        if fall_start <= date <= fall_end:
                            semester = 'Fall'
                            fall_total += 1
                        elif spring_start <= date <= spring_end:
                            semester = 'Spring'
                            spring_total += 1
                    except:
                        pass
                
                # Extract PhD year and calculate years from PhD
                if pd.notna(speaker.get('phd_graduation_year')):
                    try:
                        phd_year = float(speaker['phd_graduation_year'])
                        if phd_year == 0:  # Current student
                            phd_years.append(-1)
                        elif 1900 <= phd_year <= 2024:  # Valid past year
                            years_from_phd = 2025 - phd_year
                            phd_years.append(years_from_phd)
                    except:
                        pass
                
                # Count junior/senior speakers
                if speaker.get('is_junior', False):
                    num_junior_speakers += 1
                if speaker.get('is_senior', False):
                    num_senior_speakers += 1
                
                # Check if speaker has demographics (already matched by speaker_id)
                if speaker.get('has_demographics', False) or pd.notna(speaker.get('combined_race')):
                    speakers_with_demographics += 1
                    
                    # Check race (using the demographics already in speaker_appearances)
                    race = str(speaker.get('combined_race', '')).lower()
                    if race in ['black', 'latino', 'native american']:
                        is_urm += 1
                    if race == 'black':
                        is_black += 1
                    if race == 'latino':
                        is_hispanic += 1
                    if race == 'native american':
                        is_native_american += 1
                    if race == 'white':
                        is_white += 1
                    if race == 'asian':
                        is_asian += 1
                    
                    # Check gender
                    gender = str(speaker.get('combined_gender', '')).lower()
                    if gender == 'woman':
                        is_female += 1
                    elif gender == 'man':
                        is_male += 1
                    
                    # Count subgroups
                    if speaker.get('is_black_junior', False):
                        num_black_junior += 1
                    if speaker.get('is_black_senior', False):
                        num_black_senior += 1
                    if speaker.get('is_hispanic_junior', False):
                        num_hispanic_junior += 1
                    if speaker.get('is_hispanic_senior', False):
                        num_hispanic_senior += 1
                    if speaker.get('is_urm_junior', False):
                        num_urm_junior += 1
                    if speaker.get('is_urm_senior', False):
                        num_urm_senior += 1
                    
                    # Update semester-specific counts
                    if semester == 'Fall':
                        fall_with_demographics += 1
                        if race in ['black', 'latino', 'native american']:
                            fall_urm += 1
                        if race == 'black':
                            fall_black += 1
                        if race == 'latino':
                            fall_hispanic += 1
                        if gender == 'woman':
                            fall_female += 1
                    elif semester == 'Spring':
                        spring_with_demographics += 1
                        if race in ['black', 'latino', 'native american']:
                            spring_urm += 1
                        if race == 'black':
                            spring_black += 1
                        if race == 'latino':
                            spring_hispanic += 1
                        if gender == 'woman':
                            spring_female += 1
            
            # Calculate percentages for full year
            pct_urm = (is_urm / speakers_with_demographics * 100) if speakers_with_demographics > 0 else 0
            pct_black = (is_black / speakers_with_demographics * 100) if speakers_with_demographics > 0 else 0
            pct_hispanic = (is_hispanic / speakers_with_demographics * 100) if speakers_with_demographics > 0 else 0
            pct_native_american = (is_native_american / speakers_with_demographics * 100) if speakers_with_demographics > 0 else 0
            pct_female = (is_female / speakers_with_demographics * 100) if speakers_with_demographics > 0 else 0
            pct_male = (is_male / speakers_with_demographics * 100) if speakers_with_demographics > 0 else 0
            pct_white = (is_white / speakers_with_demographics * 100) if speakers_with_demographics > 0 else 0
            pct_asian = (is_asian / speakers_with_demographics * 100) if speakers_with_demographics > 0 else 0
            
            # Calculate percentages for semesters
            fall_pct_urm = (fall_urm / fall_with_demographics * 100) if fall_with_demographics > 0 else 0
            fall_pct_black = (fall_black / fall_with_demographics * 100) if fall_with_demographics > 0 else 0
            fall_pct_hispanic = (fall_hispanic / fall_with_demographics * 100) if fall_with_demographics > 0 else 0
            fall_pct_female = (fall_female / fall_with_demographics * 100) if fall_with_demographics > 0 else 0
            
            spring_pct_urm = (spring_urm / spring_with_demographics * 100) if spring_with_demographics > 0 else 0
            spring_pct_black = (spring_black / spring_with_demographics * 100) if spring_with_demographics > 0 else 0
            spring_pct_hispanic = (spring_hispanic / spring_with_demographics * 100) if spring_with_demographics > 0 else 0
            spring_pct_female = (spring_female / spring_with_demographics * 100) if spring_with_demographics > 0 else 0
            
            # Calculate junior/senior percentages
            pct_black_junior = (num_black_junior / num_junior_speakers * 100) if num_junior_speakers > 0 else 0
            pct_black_senior = (num_black_senior / num_senior_speakers * 100) if num_senior_speakers > 0 else 0
            pct_hispanic_junior = (num_hispanic_junior / num_junior_speakers * 100) if num_junior_speakers > 0 else 0
            pct_hispanic_senior = (num_hispanic_senior / num_senior_speakers * 100) if num_senior_speakers > 0 else 0
            pct_urm_junior = (num_urm_junior / num_junior_speakers * 100) if num_junior_speakers > 0 else 0
            pct_urm_senior = (num_urm_senior / num_senior_speakers * 100) if num_senior_speakers > 0 else 0
            
            # Calculate PhD year statistics
            num_speakers_with_phd_year = len(phd_years)
            pct_speakers_with_phd_year = (num_speakers_with_phd_year / total_speakers * 100) if total_speakers > 0 else 0
            
            if num_speakers_with_phd_year > 0:
                # Separate current students from those with PhDs
                phd_years_array = np.array(phd_years)
                current_students = (phd_years_array == -1).sum()
                phd_holders = phd_years_array[phd_years_array >= 0]
                
                if len(phd_holders) > 0:
                    mean_years_from_phd = float(np.mean(phd_holders))
                    median_years_from_phd = float(np.median(phd_holders))
                    min_years_from_phd = float(np.min(phd_holders))
                    max_years_from_phd = float(np.max(phd_holders))
                else:
                    # All speakers are current students
                    mean_years_from_phd = -1.0
                    median_years_from_phd = -1.0
                    min_years_from_phd = -1.0
                    max_years_from_phd = -1.0
                
                num_current_students = int(current_students)
                pct_current_students = (num_current_students / num_speakers_with_phd_year * 100)
            else:
                # No PhD year data
                mean_years_from_phd = np.nan
                median_years_from_phd = np.nan
                min_years_from_phd = np.nan
                max_years_from_phd = np.nan
                num_current_students = 0
                pct_current_students = 0.0
            
            # Store seminar statistics
            seminar_stats.append({
                'seminar_id': seminar_id,
                'university': seminar_info['university'],
                'discipline': seminar_info['discipline'],
                'department': f"{seminar_info['university']}-{seminar_info['discipline']}",
                'condition': seminar_info['condition'],
                
                # Full year counts
                'total_speakers': total_speakers,
                'speakers_with_demographics': speakers_with_demographics,
                'num_urm': is_urm,
                'num_black': is_black,
                'num_hispanic': is_hispanic,
                'num_native_american': is_native_american,
                'num_female': is_female,
                'num_male': is_male,
                'num_white': is_white,
                'num_asian': is_asian,
                
                # Full year percentages
                'pct_urm': pct_urm,
                'pct_black': pct_black,
                'pct_hispanic': pct_hispanic,
                'pct_native_american': pct_native_american,
                'pct_female': pct_female,
                'pct_male': pct_male,
                'pct_white': pct_white,
                'pct_asian': pct_asian,
                
                # Binary indicators
                'has_any_urm': int(is_urm > 0),
                'has_any_black': int(is_black > 0),
                'has_any_hispanic': int(is_hispanic > 0),
                'has_any_native_american': int(is_native_american > 0),
                'has_any_female': int(is_female > 0),
                
                # Junior/Senior counts
                'num_junior_speakers': num_junior_speakers,
                'num_senior_speakers': num_senior_speakers,
                'num_black_junior': num_black_junior,
                'num_black_senior': num_black_senior,
                'num_hispanic_junior': num_hispanic_junior,
                'num_hispanic_senior': num_hispanic_senior,
                'num_urm_junior': num_urm_junior,
                'num_urm_senior': num_urm_senior,
                
                # Junior/Senior percentages
                'pct_black_junior': pct_black_junior,
                'pct_black_senior': pct_black_senior,
                'pct_hispanic_junior': pct_hispanic_junior,
                'pct_hispanic_senior': pct_hispanic_senior,
                'pct_urm_junior': pct_urm_junior,
                'pct_urm_senior': pct_urm_senior,
                
                # Junior/Senior binary indicators
                'has_any_black_junior': int(num_black_junior > 0),
                'has_any_black_senior': int(num_black_senior > 0),
                'has_any_hispanic_junior': int(num_hispanic_junior > 0),
                'has_any_hispanic_senior': int(num_hispanic_senior > 0),
                'has_any_urm_junior': int(num_urm_junior > 0),
                'has_any_urm_senior': int(num_urm_senior > 0),
                
                # Semester indicators
                'has_fall_speakers': int(fall_total > 0),
                'has_spring_speakers': int(spring_total > 0),
                
                # Fall semester
                'fall_total_speakers': fall_total,
                'fall_speakers_with_demographics': fall_with_demographics,
                'fall_num_urm': fall_urm,
                'fall_num_black': fall_black,
                'fall_num_hispanic': fall_hispanic,
                'fall_num_female': fall_female,
                'fall_pct_urm': fall_pct_urm,
                'fall_pct_black': fall_pct_black,
                'fall_pct_hispanic': fall_pct_hispanic,
                'fall_pct_female': fall_pct_female,
                
                # Spring semester
                'spring_total_speakers': spring_total,
                'spring_speakers_with_demographics': spring_with_demographics,
                'spring_num_urm': spring_urm,
                'spring_num_black': spring_black,
                'spring_num_hispanic': spring_hispanic,
                'spring_num_female': spring_female,
                'spring_pct_urm': spring_pct_urm,
                'spring_pct_black': spring_pct_black,
                'spring_pct_hispanic': spring_pct_hispanic,
                'spring_pct_female': spring_pct_female,
                
                # PhD year statistics
                'num_speakers_with_phd_year': num_speakers_with_phd_year,
                'pct_speakers_with_phd_year': pct_speakers_with_phd_year,
                'mean_years_from_phd': mean_years_from_phd,
                'median_years_from_phd': median_years_from_phd,
                'min_years_from_phd': min_years_from_phd,
                'max_years_from_phd': max_years_from_phd,
                'num_current_students': num_current_students,
                'pct_current_students': pct_current_students
            })
        
        self.seminar_df = pd.DataFrame(seminar_stats)
        
        # Add treatment indicator
        self.seminar_df['treatment'] = (self.seminar_df['condition'] == 'treatment').astype(int)
        
        print(f"\nCreated seminar-level dataset:")
        print(f"  Total seminars: {len(self.seminar_df)}")
        print(f"  Treatment: {self.seminar_df['treatment'].sum()}")
        print(f"  Control: {len(self.seminar_df) - self.seminar_df['treatment'].sum()}")
        
    def add_email_recipient_demographics(self):
        """Add email recipient demographic variables"""
        if self.recipient_df is None:
            print("\n=== SKIPPING EMAIL RECIPIENT DEMOGRAPHICS (file not found) ===")
            return
        
        print("\n=== ADDING EMAIL RECIPIENT DEMOGRAPHICS ===")
        
        # Merge on department name
        self.seminar_df['merge_key'] = self.seminar_df['department_std']
        self.recipient_df['merge_key'] = self.recipient_df['department']
        
        # Select columns to merge
        merge_cols = [
            'merge_key',
            'num_email_recipients',
            'pct_female_recipients', 
            'pct_urm_recipients',
            'pct_black_recipients',
            'pct_hispanic_recipients',
            'pct_assistant_prof_recipients'
        ]
        
        # Merge
        self.seminar_df = self.seminar_df.merge(
            self.recipient_df[merge_cols], 
            on='merge_key', 
            how='left',
            suffixes=('', '_new')
        )
        
        # Check merge quality
        matched = self.seminar_df['num_email_recipients'].notna().sum()
        print(f"  Matched {matched}/{len(self.seminar_df)} seminars ({matched/len(self.seminar_df)*100:.1f}%)")
        
        # Handle any conflicts with existing num_recipients column
        if 'num_recipients' in self.seminar_df.columns:
            print(f"  Original num_recipients range: {self.seminar_df['num_recipients'].min()}-{self.seminar_df['num_recipients'].max()}")
            print(f"  New num_email_recipients range: {self.seminar_df['num_email_recipients'].min()}-{self.seminar_df['num_email_recipients'].max()}")
            # Keep original num_recipients, add email-specific count as separate column
            self.seminar_df['num_email_recipients_analyzed'] = self.seminar_df['num_email_recipients']
            self.seminar_df.drop('num_email_recipients', axis=1, inplace=True)
        
        # Clean up
        self.seminar_df.drop('merge_key', axis=1, inplace=True)
        
        # Calculate number of distinct seminars per department
        seminars_per_dept = self.seminar_df.groupby('department_std')['seminar_id'].nunique().reset_index()
        seminars_per_dept.columns = ['department_std', 'num_distinct_seminars']
        
        # Merge back
        self.seminar_df = self.seminar_df.merge(seminars_per_dept, on='department_std', how='left')
        
        # Print summary of new variables
        print("\n  Email recipient variables added:")
        if 'pct_female_recipients' in self.seminar_df.columns:
            print(f"    - pct_female_recipients: Mean = {self.seminar_df['pct_female_recipients'].mean():.3f}")
            print(f"    - pct_urm_recipients: Mean = {self.seminar_df['pct_urm_recipients'].mean():.3f}")
            print(f"    - pct_black_recipients: Mean = {self.seminar_df['pct_black_recipients'].mean():.3f}")
            print(f"    - pct_hispanic_recipients: Mean = {self.seminar_df['pct_hispanic_recipients'].mean():.3f}")
            print(f"    - pct_assistant_prof_recipients: Mean = {self.seminar_df['pct_assistant_prof_recipients'].mean():.3f}")
            print(f"    - num_distinct_seminars: Mean = {self.seminar_df['num_distinct_seminars'].mean():.1f}")
        
    def add_all_controls(self):
        """Add all control variables"""
        print("\n=== ADDING CONTROL VARIABLES ===")
        
        # Create standardized department name
        self.seminar_df['department_std'] = self.seminar_df['university'] + '-' + self.seminar_df['discipline']
        
        # 1. Bin categories from randomization
        print("  Adding bin categories...")
        self.seminar_df = self.seminar_df.merge(
            self.randomization_df[['department', 'bin_category']].rename(columns={'department': 'department_std'}),
            on='department_std',
            how='left'
        )
        
        # 2. Batch information
        print("  Adding batch information...")
        # Check which columns are available in batch mapping
        batch_cols = ['seminar_id', 'batch_number']
        if 'batch_date' in self.batch_mapping_df.columns:
            batch_cols.append('batch_date')
        
        self.seminar_df = self.seminar_df.merge(
            self.batch_mapping_df[batch_cols],
            on='seminar_id',
            how='left'
        )
        
        # 3. Department faculty data
        print("  Adding department faculty data...")
        faculty_df = self.faculty_df.copy()
        faculty_df['Department_norm'] = faculty_df['Department'].str.lower()
        faculty_lookup = {}
        for _, row in faculty_df.iterrows():
            key = (row['University'], row['Department_norm'])
            faculty_lookup[key] = {
                'total_faculty': row['Total Faculty Count (2024-2025)'],
                'urm_faculty': row['URM (Black, Latino, NativeAmerican) Faculty Count (2024-2025)'],
                'women_faculty': row['Women Faculty Count (2024-2025)']
            }
        
        # Apply faculty data
        self.seminar_df['total_faculty'] = 0
        self.seminar_df['urm_faculty'] = 0
        self.seminar_df['women_faculty'] = 0
        self.seminar_df['frac_urm_faculty'] = 0
        self.seminar_df['frac_women_faculty'] = 0
        
        for idx, row in self.seminar_df.iterrows():
            key = (row['university'], row['discipline'].lower())
            if key in faculty_lookup:
                data = faculty_lookup[key]
                self.seminar_df.loc[idx, 'total_faculty'] = data['total_faculty']
                self.seminar_df.loc[idx, 'urm_faculty'] = data['urm_faculty']
                self.seminar_df.loc[idx, 'women_faculty'] = data['women_faculty']
                
                if data['total_faculty'] > 0:
                    self.seminar_df.loc[idx, 'frac_urm_faculty'] = data['urm_faculty'] / data['total_faculty']
                    self.seminar_df.loc[idx, 'frac_women_faculty'] = data['women_faculty'] / data['total_faculty']
        
        # 4. University rankings
        print("  Adding university rankings...")
        discipline_to_rank_col = {
            'Mathematics': 'mathematics_rank',
            'Physics': 'physics_rank',
            'Chemistry': 'chemistry_rank',
            'Computer Science': 'computerScience_rank',
            'Mechanical Engineering': 'mechanicalEngineering_rank'
        }
        
        rankings_df = self.rankings_df.copy()
        rankings_df['university_norm'] = rankings_df['university'].str.strip()
        ranking_lookup = {}
        for _, row in rankings_df.iterrows():
            ranking_lookup[row['university_norm']] = row.to_dict()
        
        self.seminar_df['dept_ranking'] = np.nan
        self.seminar_df['general_ranking'] = np.nan
        self.seminar_df['missing_dept_rank'] = 0
        
        for idx, row in self.seminar_df.iterrows():
            university = row['university']
            discipline = row['discipline']
            
            if university in ranking_lookup:
                rank_data = ranking_lookup[university]
                
                # Get discipline-specific ranking
                if discipline in discipline_to_rank_col:
                    rank_col = discipline_to_rank_col[discipline]
                    if rank_col in rank_data and pd.notna(rank_data[rank_col]):
                        self.seminar_df.loc[idx, 'dept_ranking'] = rank_data[rank_col]
                    else:
                        self.seminar_df.loc[idx, 'missing_dept_rank'] = 1
                        # Use general ranking as fallback
                        if 'general_rank' in rank_data and pd.notna(rank_data['general_rank']):
                            self.seminar_df.loc[idx, 'dept_ranking'] = rank_data['general_rank']
                
                # Get general ranking
                if 'general_rank' in rank_data and pd.notna(rank_data['general_rank']):
                    self.seminar_df.loc[idx, 'general_ranking'] = rank_data['general_rank']
        
        # 5. Email recipient counts (original from email-launch.csv)
        print("  Adding email recipient counts...")
        email_df = pd.read_csv(self.email_dir / "email-launch.csv")
        recipient_counts = email_df.groupby('department').size().reset_index(name='num_recipients')
        self.seminar_df = self.seminar_df.merge(
            recipient_counts.rename(columns={'department': 'department_std'}),
            on='department_std',
            how='left'
        )
        
        # 6. Peer department variables
        print("  Calculating peer department variables...")
        print("    This uses the same algorithm as the experiment (±20 ranks, min 40 peers)...")
        
        # Calculate for each unique department (not each seminar, to avoid redundant computation)
        unique_depts = self.seminar_df[['university', 'discipline', 'department_std']].drop_duplicates()
        peer_data = {}
        
        for _, dept in unique_depts.iterrows():
            university = dept['university']
            discipline = dept['discipline']
            dept_key = dept['department_std']
            
            # Calculate number of peer departments
            peer_count = self.calculate_peer_departments(university, discipline)
            
            # Calculate total URM faculty in peer departments
            if pd.notna(peer_count):
                urm_in_peers = self.calculate_urm_faculty_in_peers(university, discipline, peer_count)
            else:
                urm_in_peers = np.nan
            
            peer_data[dept_key] = {
                'total_peer_departments': peer_count,
                'total_urm_peer_faculty': urm_in_peers
            }
        
        # Apply to all seminars
        self.seminar_df['total_peer_departments'] = 0
        self.seminar_df['total_urm_peer_faculty'] = 0
        
        for idx, row in self.seminar_df.iterrows():
            dept_key = row['department_std']
            if dept_key in peer_data:
                self.seminar_df.loc[idx, 'total_peer_departments'] = peer_data[dept_key]['total_peer_departments']
                self.seminar_df.loc[idx, 'total_urm_peer_faculty'] = peer_data[dept_key]['total_urm_peer_faculty']
        
        # Print summary
        print(f"\n  Control variable coverage:")
        print(f"    Bin categories: {self.seminar_df['bin_category'].notna().sum()}/{len(self.seminar_df)} ({self.seminar_df['bin_category'].notna().sum()/len(self.seminar_df)*100:.1f}%)")
        print(f"    Batch numbers: {self.seminar_df['batch_number'].notna().sum()}/{len(self.seminar_df)} ({self.seminar_df['batch_number'].notna().sum()/len(self.seminar_df)*100:.1f}%)")
        print(f"    Faculty data: {(self.seminar_df['total_faculty'] > 0).sum()}/{len(self.seminar_df)} ({(self.seminar_df['total_faculty'] > 0).sum()/len(self.seminar_df)*100:.1f}%)")
        print(f"    Rankings: {self.seminar_df['dept_ranking'].notna().sum()}/{len(self.seminar_df)} ({self.seminar_df['dept_ranking'].notna().sum()/len(self.seminar_df)*100:.1f}%)")
        print(f"    Email recipients: {self.seminar_df['num_recipients'].notna().sum()}/{len(self.seminar_df)} ({self.seminar_df['num_recipients'].notna().sum()/len(self.seminar_df)*100:.1f}%)")
        print(f"    Peer departments: {(self.seminar_df['total_peer_departments'] > 0).sum()}/{len(self.seminar_df)} ({(self.seminar_df['total_peer_departments'] > 0).sum()/len(self.seminar_df)*100:.1f}%)")
        print(f"    URM in peer depts: {(self.seminar_df['total_urm_peer_faculty'] > 0).sum()}/{len(self.seminar_df)} ({(self.seminar_df['total_urm_peer_faculty'] > 0).sum()/len(self.seminar_df)*100:.1f}%)")
        
    def create_indicator_variables(self):
        """Create indicator variables for regression"""
        print("\n=== CREATING INDICATOR VARIABLES ===")
        
        # Create bin indicator variables
        present_bins = self.seminar_df['bin_category'].dropna().unique()
        bin_counts = self.seminar_df['bin_category'].value_counts()
        largest_bin = bin_counts.idxmax()
        
        print(f"  Creating bin indicators (reference: '{largest_bin}' with n={bin_counts[largest_bin]})...")
        for bin_cat in present_bins:
            if bin_cat != largest_bin:
                col_name = f'bin_{bin_cat.replace("[", "").replace("]", "").replace("(", "").replace(")", "").replace(",", "_")}'
                self.seminar_df[col_name] = (self.seminar_df['bin_category'] == bin_cat).astype(int)
        
        # Create batch indicator variables
        present_batches = sorted(self.seminar_df['batch_number'].dropna().unique())
        print(f"  Creating batch indicators (reference: batch 10)...")
        for batch_num in present_batches:
            if batch_num != 10:
                col_name = f'batch_{int(batch_num)}'
                self.seminar_df[col_name] = (self.seminar_df['batch_number'] == batch_num).astype(int)
        
        # Create discipline indicator variables
        print(f"  Creating discipline indicators (reference: Chemistry)...")
        for disc in ['Mathematics', 'Physics', 'Computer Science', 'Mechanical Engineering']:
            col_name = f'disc_{disc.lower().replace(" ", "_")}'
            self.seminar_df[col_name] = (self.seminar_df['discipline'] == disc).astype(int)
    
    def check_for_issues(self):
        """Check for NA values and collinearity issues"""
        print("\n=== CHECKING FOR DATA ISSUES ===")
        
        # Check for NA values in key variables
        key_vars = [
            'treatment', 'bin_category', 'batch_number', 'total_faculty', 
            'frac_urm_faculty', 'frac_women_faculty', 'dept_ranking', 
            'num_recipients', 'total_peer_departments', 'total_urm_peer_faculty'
        ]
        
        print("\n  NA values in key variables:")
        for var in key_vars:
            if var in self.seminar_df.columns:
                na_count = self.seminar_df[var].isna().sum()
                if var in ['total_faculty', 'frac_urm_faculty', 'frac_women_faculty']:
                    # These use 0 for missing
                    na_count = (self.seminar_df[var] == 0).sum()
                if na_count > 0:
                    print(f"    {var}: {na_count} ({na_count/len(self.seminar_df)*100:.1f}%)")
        
        # Check for potential collinearity
        print("\n  Checking for potential collinearity:")
        
        # Check if peer variables vary within departments
        dept_peer_vars = self.seminar_df.groupby('department_std')[['total_peer_departments', 'total_urm_peer_faculty']].nunique()
        constant_peer_depts = (dept_peer_vars['total_peer_departments'] == 1).sum()
        constant_urm_peers = (dept_peer_vars['total_urm_peer_faculty'] == 1).sum()
        
        print(f"    Departments with constant peer counts: {constant_peer_depts}/{len(dept_peer_vars)} ({constant_peer_depts/len(dept_peer_vars)*100:.1f}%)")
        print(f"    → This is EXPECTED: peer variables are determined at department level")
        
        # Check correlation between peer variables
        if 'total_peer_departments' in self.seminar_df.columns and 'total_urm_peer_faculty' in self.seminar_df.columns:
            valid_data = self.seminar_df[
                (self.seminar_df['total_peer_departments'] > 0) & 
                (self.seminar_df['total_urm_peer_faculty'] > 0)
            ]
            if len(valid_data) > 0:
                corr = valid_data['total_peer_departments'].corr(valid_data['total_urm_peer_faculty'])
                print(f"    Correlation between peer departments and URM in peers: {corr:.3f}")
    
    def save_dataset(self):
        """Save the complete analysis dataset"""
        print("\n=== SAVING DATASET ===")
        
        output_file = self.output_dir / "master_analysis_dataset.csv"
        self.seminar_df.to_csv(output_file, index=False)
        print(f"  Saved to: {output_file}")
        
        # Also save metadata
        metadata = {
            'creation_date': datetime.now().isoformat(),
            'n_seminars': len(self.seminar_df),
            'n_treatment': int(self.seminar_df['treatment'].sum()),
            'n_control': int(len(self.seminar_df) - self.seminar_df['treatment'].sum()),
            'n_seminars_with_fall': int(self.seminar_df['has_fall_speakers'].sum()),
            'n_seminars_with_spring': int(self.seminar_df['has_spring_speakers'].sum()),
            'n_seminars_with_junior': int((self.seminar_df['num_junior_speakers'] > 0).sum()),
            'n_seminars_with_senior': int((self.seminar_df['num_senior_speakers'] > 0).sum()),
            'control_variable_coverage': {
                'bin_categories': float(self.seminar_df['bin_category'].notna().sum() / len(self.seminar_df)),
                'batch_numbers': float(self.seminar_df['batch_number'].notna().sum() / len(self.seminar_df)),
                'faculty_data': float((self.seminar_df['total_faculty'] > 0).sum() / len(self.seminar_df)),
                'rankings': float(self.seminar_df['dept_ranking'].notna().sum() / len(self.seminar_df)),
                'email_recipients': float(self.seminar_df['num_recipients'].notna().sum() / len(self.seminar_df)),
                'peer_departments': float((self.seminar_df['total_peer_departments'] > 0).sum() / len(self.seminar_df)),
                'urm_in_peers': float((self.seminar_df['total_urm_peer_faculty'] > 0).sum() / len(self.seminar_df))
            },
            'phd_year_statistics': {
                'seminars_with_phd_data': int((self.seminar_df['num_speakers_with_phd_year'] > 0).sum()),
                'coverage_rate': float((self.seminar_df['num_speakers_with_phd_year'] > 0).sum() / len(self.seminar_df)),
                'mean_years_from_phd': float(self.seminar_df['mean_years_from_phd'].mean()) if not self.seminar_df['mean_years_from_phd'].isna().all() else None,
                'mean_pct_with_phd': float(self.seminar_df['pct_speakers_with_phd_year'].mean()),
                'mean_pct_current_students': float(self.seminar_df['pct_current_students'].mean()),
                'median_years_for_split': float(self.median_years_since_phd)
            },
            'email_recipient_demographics': {
                'seminars_with_recipient_data': int(self.seminar_df['pct_female_recipients'].notna().sum()) if 'pct_female_recipients' in self.seminar_df.columns else 0,
                'mean_pct_female_recipients': float(self.seminar_df['pct_female_recipients'].mean()) if 'pct_female_recipients' in self.seminar_df.columns else None,
                'mean_pct_urm_recipients': float(self.seminar_df['pct_urm_recipients'].mean()) if 'pct_urm_recipients' in self.seminar_df.columns else None,
                'mean_pct_black_recipients': float(self.seminar_df['pct_black_recipients'].mean()) if 'pct_black_recipients' in self.seminar_df.columns else None
            },
            'columns': list(self.seminar_df.columns),
            'total_columns': len(self.seminar_df.columns)
        }
        
        with open(self.output_dir / "master_analysis_dataset_metadata.json", 'w') as f:
            json.dump(metadata, f, indent=2)
        
        print(f"  Saved metadata to: {self.output_dir / 'master_analysis_dataset_metadata.json'}")
        
        # Print column summary
        print(f"\n  Dataset contains {len(self.seminar_df.columns)} columns:")
        print(f"    - Identifiers: seminar_id, university, discipline, department, etc.")
        print(f"    - Treatment: treatment (0/1)")
        print(f"    - Outcomes: pct_urm, pct_black, pct_hispanic, num_urm, etc.")
        print(f"    - Junior/Senior breakdowns: num_black_junior, pct_urm_senior, etc.")
        print(f"    - Email recipient demographics: pct_female_recipients, pct_black_recipients, etc.")
        print(f"    - Semester outcomes: fall_pct_urm, spring_pct_urm, etc.")
        print(f"    - Control variables: all pre-registered controls including peer variables")
        print(f"    - Indicator variables: bin_*, batch_*, disc_*")
    
    def create_dataset(self):
        """Main method to create the complete analysis dataset"""
        print("\n" + "="*60)
        print("CREATING MASTER ANALYSIS DATASET (INTEGRATED VERSION)")
        print("="*60)
        
        # Check if dataset already exists
        output_file = self.output_dir / "master_analysis_dataset.csv"
        if output_file.exists():
            print(f"\nDataset already exists at: {output_file}")
            user_input = input("Overwrite existing dataset? (y/n): ")
            if user_input.lower() != 'y':
                print("Exiting without overwriting.")
                return False
        
        # Load all data
        self.load_all_data()
        
        # Create speaker-level data with demographics and junior/senior classifications
        self.create_speaker_level_data()
        
        # Add all control variables
        self.add_all_controls()
        
        # Add email recipient demographics
        self.add_email_recipient_demographics()
        
        # Create indicator variables
        self.create_indicator_variables()
        
        # Check for issues
        self.check_for_issues()
        
        # Save dataset
        self.save_dataset()
        
        print("\n" + "="*60)
        print("INTEGRATED DATASET CREATION COMPLETE")
        print("="*60)
        
        # Print subgroup analysis summary
        print("\n=== SUBGROUP ANALYSIS SUMMARY ===")
        print(f"  Junior/Senior split at median years since PhD: {self.median_years_since_phd:.1f}")
        print(f"  Seminars with junior speakers: {(self.seminar_df['num_junior_speakers'] > 0).sum()}")
        print(f"  Seminars with senior speakers: {(self.seminar_df['num_senior_speakers'] > 0).sum()}")
        print(f"  Mean % Black among junior speakers: {self.seminar_df['pct_black_junior'].mean():.3f}")
        print(f"  Mean % Black among senior speakers: {self.seminar_df['pct_black_senior'].mean():.3f}")
        
        return True


if __name__ == "__main__":
    import time
    start_time = time.time()
    
    creator = AnalysisDatasetCreator()
    creator.create_dataset()
    
    elapsed_time = time.time() - start_time
    print(f"\nTotal runtime: {elapsed_time:.2f} seconds")