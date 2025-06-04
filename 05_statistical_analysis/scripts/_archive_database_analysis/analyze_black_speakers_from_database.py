#!/usr/bin/env python3
"""
Analyze if Black speakers specifically were selected from the URM databases

This addresses the main finding that treatment increased Black speaker representation.
We want to know: Did this come from the database, or from other sources?
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json
import asyncio
from typing import Dict, List, Tuple
import warnings
warnings.filterwarnings('ignore')

# Import the improved analyzer to reuse its matching logic
import sys
sys.path.append('/mnt/c/Users/jcerv/Jose/search-costs/05_statistical_analysis/scripts')
from analyze_database_treatment_effect_improved import ImprovedDatabaseAnalyzer

class BlackSpeakerDatabaseAnalyzer(ImprovedDatabaseAnalyzer):
    def __init__(self):
        super().__init__()
        print("\nInitializing Black speaker database analysis...")
        
        # Load the full speaker appearances with demographics
        self.load_demographic_data()
        
    def load_demographic_data(self):
        """Load speaker appearances with demographic coding"""
        # This file has the combined_race field we need
        demographics_path = self.base_dir / "04_demographic_analysis/outputs/speaker_appearances_analysis.csv"
        self.demographics_df = pd.read_csv(demographics_path)
        
        # Count Black speakers
        black_speakers = self.demographics_df[
            self.demographics_df['combined_race'].str.contains('Black', case=False, na=False)
        ]
        print(f"Found {len(black_speakers)} Black speaker appearances")
        print(f"Unique Black speakers: {len(black_speakers['speaker_id'].unique())}")
        
    async def analyze_black_speakers_from_database(self):
        """Main analysis focused on Black speakers"""
        results = []
        black_matches_detailed = []
        
        # Get all departments
        dept_groups = self.randomization.groupby(['university', 'discipline'])
        
        print(f"\nAnalyzing {len(dept_groups)} departments for Black speaker selection...")
        
        for (university, discipline), dept_data in dept_groups:
            treatment = 1 if dept_data['condition'].iloc[0] == 'treatment' else 0
            
            # Get peer universities and URM faculty
            peers = self.get_peer_universities(university, discipline)
            if not peers:
                continue
                
            # Get URM faculty from database
            potential_urm_faculty = self.get_urm_faculty_for_peers(peers, discipline)
            if potential_urm_faculty.empty:
                continue
            
            # Filter for Black faculty in the database
            black_urm_faculty = potential_urm_faculty[
                potential_urm_faculty['Race'].str.contains('Black', case=False, na=False)
            ]
            
            # Get actual seminars for this department
            dept_seminars = self.speaker_appearances[
                (self.speaker_appearances['university'] == university) &
                (self.speaker_appearances['discipline'] == discipline)
            ].copy()
            
            if dept_seminars.empty:
                continue
            
            # Get demographic info for these seminars
            dept_demographics = self.demographics_df[
                (self.demographics_df['university'] == university) &
                (self.demographics_df['discipline'] == discipline)
            ].copy()
            
            # Identify Black speakers in the seminars
            black_speakers_in_seminars = dept_demographics[
                dept_demographics['combined_race'].str.contains('Black', case=False, na=False)
            ]
            
            # Match Black URM faculty to Black seminar speakers
            if not black_urm_faculty.empty and not black_speakers_in_seminars.empty:
                matches = await self.match_speakers_improved(
                    black_urm_faculty, black_speakers_in_seminars, discipline
                )
                
                if not matches.empty:
                    matches['focal_university'] = university
                    matches['focal_discipline'] = discipline
                    matches['treatment'] = treatment
                    matches['speaker_race'] = 'Black'
                    black_matches_detailed.append(matches)
            else:
                matches = pd.DataFrame()
            
            # Calculate metrics
            total_speakers = len(dept_demographics['speaker_id'].unique())
            total_black_speakers = len(black_speakers_in_seminars['speaker_id'].unique())
            black_speakers_from_database = len(matches['speaker_id'].unique()) if not matches.empty else 0
            
            result = {
                'university': university,
                'discipline': discipline,
                'treatment': treatment,
                'num_peer_universities': len(peers),
                'num_black_urm_in_database': len(black_urm_faculty),
                'total_speakers': total_speakers,
                'total_black_speakers': total_black_speakers,
                'black_speakers_from_database': black_speakers_from_database,
                'pct_black_speakers': total_black_speakers / total_speakers if total_speakers > 0 else np.nan,
                'pct_black_from_database': black_speakers_from_database / total_black_speakers if total_black_speakers > 0 else np.nan,
                'any_black_from_database': 1 if black_speakers_from_database > 0 else 0
            }
            
            results.append(result)
        
        # Convert to DataFrame
        results_df = pd.DataFrame(results)
        results_df = results_df[results_df['total_speakers'] > 0]
        
        print(f"\nAnalyzed {len(results_df)} departments with speakers")
        
        # Save detailed Black speaker matches
        if black_matches_detailed:
            all_matches_df = pd.concat(black_matches_detailed, ignore_index=True)
            matches_path = self.output_dir / "black_speaker_database_matches.csv"
            all_matches_df.to_csv(matches_path, index=False)
            print(f"Saved {len(all_matches_df)} Black speaker matches to: {matches_path}")
        
        # Calculate and display results
        self.analyze_treatment_effects_black_speakers(results_df)
        
        # Save main results
        output_path = self.output_dir / "black_speaker_database_analysis.csv"
        results_df.to_csv(output_path, index=False)
        print(f"\nResults saved to: {output_path}")
        
        return results_df
    
    def analyze_treatment_effects_black_speakers(self, results_df):
        """Analyze treatment effects specifically for Black speakers"""
        print("\n" + "="*60)
        print("BLACK SPEAKER DATABASE SELECTION ANALYSIS")
        print("="*60)
        
        # Remove departments with no Black speakers for some analyses
        results_with_black = results_df[results_df['total_black_speakers'] > 0]
        
        # Split by treatment/control
        treatment_df = results_df[results_df['treatment'] == 1]
        control_df = results_df[results_df['treatment'] == 0]
        
        treatment_with_black = results_with_black[results_with_black['treatment'] == 1]
        control_with_black = results_with_black[results_with_black['treatment'] == 0]
        
        print(f"\nSample sizes:")
        print(f"  All departments:")
        print(f"    Treatment: {len(treatment_df)}")
        print(f"    Control: {len(control_df)}")
        print(f"  Departments with Black speakers:")
        print(f"    Treatment: {len(treatment_with_black)}")
        print(f"    Control: {len(control_with_black)}")
        
        # Key metrics
        metrics = [
            ('pct_black_speakers', 'Overall Black speaker share', results_df),
            ('any_black_from_database', 'Probability of selecting ANY Black speaker from database', results_df),
            ('pct_black_from_database', 'Share of Black speakers from database (among depts with Black speakers)', results_with_black),
            ('black_speakers_from_database', 'Average number of Black speakers from database', results_df)
        ]
        
        print("\n" + "-"*60)
        print("MAIN RESULTS:")
        print("-"*60)
        
        for metric, description, df_to_use in metrics:
            # Split data
            treat_data = df_to_use[df_to_use['treatment'] == 1]
            control_data = df_to_use[df_to_use['treatment'] == 0]
            
            # Get values
            treatment_vals = treat_data[metric].dropna()
            control_vals = control_data[metric].dropna()
            
            if len(treatment_vals) == 0 or len(control_vals) == 0:
                continue
                
            # Calculate statistics
            treatment_mean = treatment_vals.mean()
            control_mean = control_vals.mean()
            treatment_se = treatment_vals.sem()
            control_se = control_vals.sem()
            diff = treatment_mean - control_mean
            
            # T-test
            from scipy import stats
            t_stat, p_value = stats.ttest_ind(treatment_vals, control_vals)
            
            print(f"\n{description}:")
            print(f"  Treatment: {treatment_mean:.3f} (SE: {treatment_se:.3f}, N={len(treatment_vals)})")
            print(f"  Control:   {control_mean:.3f} (SE: {control_se:.3f}, N={len(control_vals)})")
            print(f"  Difference: {diff:.3f} ({diff/control_mean*100:.1f}% increase)" if control_mean > 0 else f"  Difference: {diff:.3f}")
            print(f"  p-value: {p_value:.4f}")
            print(f"  Significant: {'Yes' if p_value < 0.05 else 'Marginally' if p_value < 0.1 else 'No'}")
        
        # Additional analysis: departments with Black faculty in database
        print("\n" + "-"*60)
        print("DEPARTMENTS WITH BLACK FACULTY IN DATABASE:")
        print("-"*60)
        
        has_black_in_db = results_df[results_df['num_black_urm_in_database'] > 0]
        print(f"\nDepartments with Black faculty in their peer database:")
        print(f"  Treatment: {len(has_black_in_db[has_black_in_db['treatment'] == 1])}")
        print(f"  Control: {len(has_black_in_db[has_black_in_db['treatment'] == 0])}")
        
        # Among those with Black faculty available, how many selected any?
        if len(has_black_in_db) > 0:
            selected_any = has_black_in_db[has_black_in_db['black_speakers_from_database'] > 0]
            print(f"\nAmong departments with Black faculty in database, those who selected any:")
            print(f"  Treatment: {len(selected_any[selected_any['treatment'] == 1])} / {len(has_black_in_db[has_black_in_db['treatment'] == 1])}")
            print(f"  Control: {len(selected_any[selected_any['treatment'] == 0])} / {len(has_black_in_db[has_black_in_db['treatment'] == 0])}")

async def main():
    analyzer = BlackSpeakerDatabaseAnalyzer()
    results = await analyzer.analyze_black_speakers_from_database()
    
    print("\n" + "="*60)
    print("INTERPRETATION:")
    print("="*60)
    print("""
This analysis specifically examines whether the increased Black speaker
representation in treatment departments came from the personalized databases.

Key questions:
1. Did treatment departments select more Black speakers from their databases?
2. What fraction of Black speakers came from the shown databases?
3. Does this explain the overall increase in Black representation?
""")

if __name__ == "__main__":
    asyncio.run(main())