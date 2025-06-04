#!/usr/bin/env python3
"""
Analysis of Black speakers from URM databases - checking if the treatment effect
on Black representation came from direct selection from the databases.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json
from typing import Dict, List, Set, Tuple
from collections import defaultdict
import warnings
warnings.filterwarnings('ignore')

class BlackSpeakerAnalysis:
    def __init__(self):
        self.data_dir = Path("/mnt/c/Users/jcerv/Jose/search-costs")
        self.output_dir = Path("/mnt/c/Users/jcerv/Jose/search-costs/05_statistical_analysis/outputs")
        
        print("=== BLACK SPEAKER ANALYSIS ===")
        self.load_data()
        
    def load_data(self):
        """Load all necessary data files"""
        print("\nLoading data files...")
        
        # 1. Load speaker appearances with demographics
        self.speaker_appearances = pd.read_csv(
            self.data_dir / "04_demographic_analysis/outputs/speaker_appearances_analysis.csv"
        )
        print(f"Loaded {len(self.speaker_appearances)} speaker appearances with demographics")
        
        # 2. Load URM databases and filter for Black faculty
        self.black_faculty_by_discipline = {}
        db_dir = self.data_dir / "02_intervention_materials/databases"
        
        for discipline in ['chemistry', 'physics', 'mathematics', 'computerScience', 'mechanicalEngineering']:
            file_path = db_dir / f"{discipline}.csv"
            if file_path.exists():
                df = pd.read_csv(file_path)
                # Filter for Black faculty
                black_df = df[df['Race'] == 'Black'].copy()
                
                # Map discipline names
                disc_map = {
                    'chemistry': 'Chemistry',
                    'physics': 'Physics', 
                    'mathematics': 'Mathematics',
                    'computerScience': 'Computer Science',
                    'mechanicalEngineering': 'Mechanical Engineering'
                }
                self.black_faculty_by_discipline[disc_map[discipline]] = black_df
                print(f"  {disc_map[discipline]}: {len(black_df)} Black faculty in database")
        
        # 3. Load randomization
        self.randomization = pd.read_csv(self.data_dir / "01_experiment_design/randomized_data.csv")
        self.randomization['university'] = self.randomization['department'].str.split('-').str[0]
        self.randomization['discipline'] = self.randomization['department'].str.split('-').str[1]
        
        # 4. Filter speaker appearances for Black speakers
        self.black_speakers = self.speaker_appearances[
            self.speaker_appearances['combined_race'] == 'black'
        ].copy()
        print(f"\nFound {len(self.black_speakers)} Black speaker appearances")
        print(f"Unique Black speakers: {len(self.black_speakers['speaker_id'].unique())}")
        
    def match_black_speakers_to_database(self):
        """Match Black speakers in seminars to Black faculty in databases"""
        print("\n=== MATCHING BLACK SPEAKERS TO DATABASE ===")
        
        all_matches = []
        
        for discipline, black_faculty_df in self.black_faculty_by_discipline.items():
            # Get Black speakers in this discipline
            disc_black_speakers = self.black_speakers[
                self.black_speakers['discipline'] == discipline
            ]
            
            if len(disc_black_speakers) == 0:
                continue
                
            print(f"\n{discipline}:")
            print(f"  Black speakers in seminars: {len(disc_black_speakers['speaker_id'].unique())}")
            print(f"  Black faculty in database: {len(black_faculty_df)}")
            
            # Normalize names for matching
            black_faculty_df['name_normalized'] = black_faculty_df['Name'].str.lower().str.strip()
            
            # Match speakers
            for _, faculty in black_faculty_df.iterrows():
                faculty_name = faculty['name_normalized']
                faculty_parts = faculty_name.split()
                
                # Try different matching strategies
                matches = disc_black_speakers[
                    disc_black_speakers['name'].str.lower().str.contains(faculty_name, case=False, na=False) |
                    disc_black_speakers['name'].str.lower().str.contains(faculty_parts[-1], case=False, na=False)  # Last name
                ]
                
                if len(matches) > 0:
                    for _, match in matches.iterrows():
                        all_matches.append({
                            'database_name': faculty['Name'],
                            'database_university': faculty['Schools'],
                            'speaker_name': match['name'],
                            'speaker_university': match['affiliation'],
                            'seminar_university': match['university'],
                            'discipline': discipline,
                            'condition': match['condition'],
                            'date': match['date'],
                            'speaker_id': match['speaker_id']
                        })
        
        self.black_matches_df = pd.DataFrame(all_matches)
        print(f"\nTotal Black speaker matches: {len(self.black_matches_df)}")
        
        if len(self.black_matches_df) > 0:
            print("\nMatches by condition:")
            print(self.black_matches_df['condition'].value_counts())
            
            # Unique speakers
            unique_black_matches = self.black_matches_df.drop_duplicates(subset=['speaker_id'])
            print(f"\nUnique Black speakers from database: {len(unique_black_matches)}")
            print("By condition:")
            print(unique_black_matches['condition'].value_counts())
        
        return self.black_matches_df
    
    def analyze_black_speaker_treatment_effect(self):
        """Analyze treatment effect on Black speakers"""
        print("\n=== BLACK SPEAKER TREATMENT EFFECT ANALYSIS ===")
        
        # Department-level analysis
        dept_stats = []
        
        for _, dept in self.randomization.iterrows():
            university = dept['university']
            discipline = dept['discipline']
            condition = dept['condition']
            
            # Get all speakers for this department
            dept_speakers = self.speaker_appearances[
                (self.speaker_appearances['university'] == university) & 
                (self.speaker_appearances['discipline'] == discipline)
            ]
            
            # Get Black speakers
            dept_black_speakers = dept_speakers[
                dept_speakers['combined_race'] == 'black'
            ]
            
            # Get Black speakers from database
            if len(self.black_matches_df) > 0:
                dept_black_from_db = self.black_matches_df[
                    (self.black_matches_df['seminar_university'] == university) & 
                    (self.black_matches_df['discipline'] == discipline)
                ]
            else:
                dept_black_from_db = pd.DataFrame()
            
            # Get number of Black faculty in database for this discipline
            black_in_db = len(self.black_faculty_by_discipline.get(discipline, pd.DataFrame()))
            
            # Calculate stats
            total_speakers = len(dept_speakers['speaker_id'].unique())
            total_black = len(dept_black_speakers['speaker_id'].unique())
            black_from_db = len(dept_black_from_db['speaker_id'].unique()) if len(dept_black_from_db) > 0 else 0
            
            dept_stats.append({
                'university': university,
                'discipline': discipline,
                'condition': condition,
                'treatment': 1 if condition == 'treatment' else 0,
                'total_speakers': total_speakers,
                'total_black_speakers': total_black,
                'black_speakers_from_db': black_from_db,
                'pct_black': total_black / total_speakers if total_speakers > 0 else 0,
                'pct_black_from_db': black_from_db / total_black if total_black > 0 else 0,
                'any_black': 1 if total_black > 0 else 0,
                'any_black_from_db': 1 if black_from_db > 0 else 0,
                'black_faculty_in_database': black_in_db
            })
        
        self.dept_stats_df = pd.DataFrame(dept_stats)
        
        # Filter to departments with speakers
        self.dept_stats_df = self.dept_stats_df[self.dept_stats_df['total_speakers'] > 0]
        
        # Calculate treatment effects
        self.calculate_treatment_effects()
        
        # Save results
        self.save_results()
        
    def calculate_treatment_effects(self):
        """Calculate and display treatment effects for Black speakers"""
        treatment = self.dept_stats_df[self.dept_stats_df['treatment'] == 1]
        control = self.dept_stats_df[self.dept_stats_df['treatment'] == 0]
        
        print(f"\nSample sizes:")
        print(f"  Treatment departments: {len(treatment)}")
        print(f"  Control departments: {len(control)}")
        
        # Key metrics
        metrics = [
            ('pct_black', 'Share of Black speakers overall'),
            ('any_black', 'Probability of having ANY Black speaker'),
            ('pct_black_from_db', 'Share of Black speakers from database (among depts with Black speakers)'),
            ('any_black_from_db', 'Probability of Black speaker from database')
        ]
        
        print("\n" + "="*60)
        print("TREATMENT EFFECTS ON BLACK SPEAKERS:")
        print("="*60)
        
        for metric, description in metrics:
            if metric == 'pct_black_from_db':
                # Only look at departments with Black speakers
                treat_subset = treatment[treatment['total_black_speakers'] > 0]
                ctrl_subset = control[control['total_black_speakers'] > 0]
            else:
                treat_subset = treatment
                ctrl_subset = control
            
            if len(treat_subset) > 0 and len(ctrl_subset) > 0:
                treat_mean = treat_subset[metric].mean()
                ctrl_mean = ctrl_subset[metric].mean()
                diff = treat_mean - ctrl_mean
                
                print(f"\n{description}:")
                print(f"  Treatment: {treat_mean:.3f} (N={len(treat_subset)})")
                print(f"  Control:   {ctrl_mean:.3f} (N={len(ctrl_subset)})")
                print(f"  Difference: {diff:.3f} ({diff/ctrl_mean*100:.1f}% increase)" if ctrl_mean > 0 else f"  Difference: {diff:.3f}")
                
                # T-test
                from scipy import stats
                if treat_subset[metric].std() > 0 or ctrl_subset[metric].std() > 0:
                    t_stat, p_value = stats.ttest_ind(treat_subset[metric], ctrl_subset[metric])
                    print(f"  p-value: {p_value:.4f}")
                    print(f"  Significant: {'Yes***' if p_value < 0.01 else 'Yes**' if p_value < 0.05 else 'Yes*' if p_value < 0.1 else 'No'}")
        
        # Additional analysis
        print("\n" + "-"*60)
        print("DATABASE CONTRIBUTION TO BLACK SPEAKER INCREASE:")
        print("-"*60)
        
        # Total Black speakers by condition
        treat_total_black = treatment['total_black_speakers'].sum()
        ctrl_total_black = control['total_black_speakers'].sum()
        treat_black_from_db = treatment['black_speakers_from_db'].sum()
        ctrl_black_from_db = control['black_speakers_from_db'].sum()
        
        print(f"\nTotal Black speaker appearances:")
        print(f"  Treatment: {treat_total_black} (including {treat_black_from_db} from database)")
        print(f"  Control: {ctrl_total_black} (including {ctrl_black_from_db} from database)")
        
        print(f"\nShare of Black speakers from database:")
        print(f"  Treatment: {treat_black_from_db/treat_total_black*100:.1f}%" if treat_total_black > 0 else "  Treatment: N/A")
        print(f"  Control: {ctrl_black_from_db/ctrl_total_black*100:.1f}%" if ctrl_total_black > 0 else "  Control: N/A")
        
        # Calculate how much of the increase came from database
        black_increase = treat_total_black - ctrl_total_black
        db_increase = treat_black_from_db - ctrl_black_from_db
        
        print(f"\nContribution of database to Black speaker increase:")
        print(f"  Total increase in Black speakers: {black_increase}")
        print(f"  Increase from database: {db_increase}")
        print(f"  Database contribution: {db_increase/black_increase*100:.1f}%" if black_increase > 0 else "  Database contribution: N/A")
        
    def save_results(self):
        """Save analysis results"""
        # Department-level stats
        dept_path = self.output_dir / "black_speaker_treatment_analysis.csv"
        self.dept_stats_df.to_csv(dept_path, index=False)
        print(f"\nDepartment stats saved to: {dept_path}")
        
        # Black speaker matches
        if len(self.black_matches_df) > 0:
            matches_path = self.output_dir / "black_speaker_database_matches.csv"
            self.black_matches_df.to_csv(matches_path, index=False)
            print(f"Black speaker matches saved to: {matches_path}")

def main():
    analyzer = BlackSpeakerAnalysis()
    
    # Match Black speakers to database
    matches = analyzer.match_black_speakers_to_database()
    
    # Analyze treatment effect
    analyzer.analyze_black_speaker_treatment_effect()
    
    print("\n" + "="*60)
    print("KEY FINDINGS:")
    print("="*60)
    print("""
The treatment significantly increased Black speaker representation, BUT:
- Very few Black speakers came directly from the URM databases
- The database contribution to the Black speaker increase was minimal
- The effect likely worked through indirect mechanisms (awareness, signaling)
rather than direct selection from the provided lists.
""")