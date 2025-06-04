#!/usr/bin/env python3
"""
Analyze speaker availability from peer universities

Key insight: We want to know if speakers from the URM database were actually
giving talks at peer universities. This tells us about the potential effectiveness
of the database - were these speakers even available/active on the seminar circuit?

We analyze:
1. % of total speakers at peer universities who were in the database
2. % of URM speakers at peer universities who were in the database  
3. % of Black speakers at peer universities who were in the database
4. Binary: Did ANY speaker from the database appear at peer universities?
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json
import asyncio
from typing import Dict, List, Set, Tuple
import warnings
warnings.filterwarnings('ignore')

# Import the improved analyzer
import sys
sys.path.append('/mnt/c/Users/jcerv/Jose/search-costs/05_statistical_analysis/scripts')
from analyze_database_treatment_effect_improved import ImprovedDatabaseAnalyzer

class PeerSpeakerAvailabilityAnalyzer(ImprovedDatabaseAnalyzer):
    def __init__(self):
        super().__init__()
        print("\nInitializing peer speaker availability analysis...")
        
        # Load demographics
        self.demographics_df = pd.read_csv(
            self.base_dir / "04_demographic_analysis/outputs/speaker_appearances_analysis.csv"
        )
        
    async def analyze_peer_speaker_availability(self):
        """Analyze if database speakers were active at peer universities"""
        results = []
        all_peer_matches = []
        
        # Get all departments
        dept_groups = self.randomization.groupby(['university', 'discipline'])
        
        print(f"\nAnalyzing speaker availability at peer universities for {len(dept_groups)} departments...")
        
        for (university, discipline), dept_data in dept_groups:
            treatment = 1 if dept_data['condition'].iloc[0] == 'treatment' else 0
            
            # Get peer universities for this department
            peers = self.get_peer_universities(university, discipline)
            if not peers:
                continue
                
            # Get URM faculty that would be in the database for these peers
            potential_urm_faculty = self.get_urm_faculty_for_peers(peers, discipline)
            if potential_urm_faculty.empty:
                continue
                
            # Get Black faculty subset
            black_urm_faculty = potential_urm_faculty[
                potential_urm_faculty['Race'].str.contains('Black', case=False, na=False)
            ]
            
            # Get ALL seminars at peer universities (not focal university)
            peer_seminars = self.speaker_appearances[
                (self.speaker_appearances['university'].isin(peers)) &
                (self.speaker_appearances['discipline'] == discipline)
            ].copy()
            
            if peer_seminars.empty:
                # No seminars at peer universities
                result = {
                    'focal_university': university,
                    'focal_discipline': discipline,
                    'treatment': treatment,
                    'num_peer_universities': len(peers),
                    'num_urm_in_database': len(potential_urm_faculty),
                    'num_black_in_database': len(black_urm_faculty),
                    'total_speakers_at_peers': 0,
                    'total_urm_at_peers': 0,
                    'total_black_at_peers': 0,
                    'database_speakers_at_peers': 0,
                    'database_urm_at_peers': 0,
                    'database_black_at_peers': 0,
                    'pct_speakers_from_database': np.nan,
                    'pct_urm_from_database': np.nan,
                    'pct_black_from_database': np.nan,
                    'any_speaker_from_database': 0
                }
                results.append(result)
                continue
            
            # Get demographics for peer seminars
            peer_demographics = self.demographics_df[
                (self.demographics_df['university'].isin(peers)) &
                (self.demographics_df['discipline'] == discipline)
            ]
            
            # Count speakers at peer universities
            total_speakers_at_peers = len(peer_seminars['speaker_id'].unique())
            
            # Count URM speakers at peers
            urm_speakers_at_peers = peer_demographics[
                peer_demographics['is_urm'] == 1
            ]['speaker_id'].unique()
            total_urm_at_peers = len(urm_speakers_at_peers)
            
            # Count Black speakers at peers
            black_speakers_at_peers = peer_demographics[
                peer_demographics['combined_race'].str.contains('Black', case=False, na=False)
            ]['speaker_id'].unique()
            total_black_at_peers = len(black_speakers_at_peers)
            
            # Match database faculty to peer seminar speakers
            all_matches = await self.match_speakers_improved(
                potential_urm_faculty, peer_seminars, discipline
            )
            
            # Match Black faculty specifically
            if not black_urm_faculty.empty:
                black_peer_seminars = peer_demographics[
                    peer_demographics['combined_race'].str.contains('Black', case=False, na=False)
                ]
                if not black_peer_seminars.empty:
                    black_matches = await self.match_speakers_improved(
                        black_urm_faculty, black_peer_seminars, discipline
                    )
                else:
                    black_matches = pd.DataFrame()
            else:
                black_matches = pd.DataFrame()
            
            # Count matches
            database_speakers_at_peers = len(all_matches['speaker_id'].unique()) if not all_matches.empty else 0
            database_black_at_peers = len(black_matches['speaker_id'].unique()) if not black_matches.empty else 0
            
            # For URM matches, we need to check which matched speakers are URMs
            if not all_matches.empty:
                matched_speaker_ids = all_matches['speaker_id'].unique()
                database_urm_at_peers = len([sid for sid in matched_speaker_ids if sid in urm_speakers_at_peers])
            else:
                database_urm_at_peers = 0
            
            # Store detailed matches
            if not all_matches.empty:
                all_matches['focal_university'] = university
                all_matches['focal_discipline'] = discipline
                all_matches['treatment'] = treatment
                all_matches['match_location'] = 'peer_university'
                all_peer_matches.append(all_matches)
            
            # Calculate result
            result = {
                'focal_university': university,
                'focal_discipline': discipline,
                'treatment': treatment,
                'num_peer_universities': len(peers),
                'num_urm_in_database': len(potential_urm_faculty),
                'num_black_in_database': len(black_urm_faculty),
                'total_speakers_at_peers': total_speakers_at_peers,
                'total_urm_at_peers': total_urm_at_peers,
                'total_black_at_peers': total_black_at_peers,
                'database_speakers_at_peers': database_speakers_at_peers,
                'database_urm_at_peers': database_urm_at_peers,
                'database_black_at_peers': database_black_at_peers,
                'pct_speakers_from_database': database_speakers_at_peers / total_speakers_at_peers if total_speakers_at_peers > 0 else np.nan,
                'pct_urm_from_database': database_urm_at_peers / total_urm_at_peers if total_urm_at_peers > 0 else np.nan,
                'pct_black_from_database': database_black_at_peers / total_black_at_peers if total_black_at_peers > 0 else np.nan,
                'any_speaker_from_database': 1 if database_speakers_at_peers > 0 else 0
            }
            
            results.append(result)
            
            # Progress update
            if len(results) % 50 == 0:
                print(f"  Processed {len(results)} departments...")
        
        # Convert to DataFrame
        results_df = pd.DataFrame(results)
        
        # Save detailed matches
        if all_peer_matches:
            matches_df = pd.concat(all_peer_matches, ignore_index=True)
            matches_path = self.output_dir / "peer_university_speaker_matches.csv"
            matches_df.to_csv(matches_path, index=False)
            print(f"\nSaved {len(matches_df)} peer university matches")
        
        # Analyze and display results
        self.analyze_results(results_df)
        
        # Save main results
        output_path = self.output_dir / "peer_speaker_availability_analysis.csv"
        results_df.to_csv(output_path, index=False)
        print(f"\nResults saved to: {output_path}")
        
        return results_df
    
    def analyze_results(self, results_df):
        """Analyze speaker availability at peer universities"""
        print("\n" + "="*60)
        print("SPEAKER AVAILABILITY AT PEER UNIVERSITIES")
        print("="*60)
        
        # Remove departments with no peer seminars
        results_with_peers = results_df[results_df['total_speakers_at_peers'] > 0]
        
        print(f"\nDepartments analyzed: {len(results_df)}")
        print(f"Departments with peer seminar data: {len(results_with_peers)}")
        
        # Overall statistics (should be similar for treatment/control)
        print("\n" + "-"*60)
        print("OVERALL SPEAKER AVAILABILITY:")
        print("-"*60)
        
        metrics = [
            ('pct_speakers_from_database', 'Share of ALL peer speakers in database'),
            ('pct_urm_from_database', 'Share of URM peer speakers in database'),
            ('pct_black_from_database', 'Share of Black peer speakers in database'),
            ('any_speaker_from_database', 'Probability ANY database speaker appeared at peers')
        ]
        
        for metric, description in metrics:
            values = results_with_peers[metric].dropna()
            if len(values) > 0:
                print(f"\n{description}:")
                print(f"  Mean: {values.mean():.3f}")
                print(f"  Median: {values.median():.3f}")
                print(f"  Std Dev: {values.std():.3f}")
                print(f"  N: {len(values)}")
        
        # By treatment status (should be similar since peer sets are algorithmic)
        print("\n" + "-"*60)
        print("BY TREATMENT STATUS (should be similar):")
        print("-"*60)
        
        treatment_df = results_with_peers[results_with_peers['treatment'] == 1]
        control_df = results_with_peers[results_with_peers['treatment'] == 0]
        
        for metric, description in metrics:
            treat_vals = treatment_df[metric].dropna()
            control_vals = control_df[metric].dropna()
            
            if len(treat_vals) > 0 and len(control_vals) > 0:
                print(f"\n{description}:")
                print(f"  Treatment: {treat_vals.mean():.3f} (N={len(treat_vals)})")
                print(f"  Control: {control_vals.mean():.3f} (N={len(control_vals)})")
                print(f"  Difference: {treat_vals.mean() - control_vals.mean():.3f}")
        
        # By discipline
        print("\n" + "-"*60)
        print("BY DISCIPLINE:")
        print("-"*60)
        
        for discipline in results_with_peers['focal_discipline'].unique():
            disc_data = results_with_peers[results_with_peers['focal_discipline'] == discipline]
            if len(disc_data) > 10:
                any_match = disc_data['any_speaker_from_database'].mean()
                pct_speakers = disc_data['pct_speakers_from_database'].mean()
                print(f"\n{discipline}:")
                print(f"  Departments with ANY database speaker at peers: {any_match:.1%}")
                print(f"  Average share of speakers from database: {pct_speakers:.3f}")

async def main():
    analyzer = PeerSpeakerAvailabilityAnalyzer()
    results = await analyzer.analyze_peer_speaker_availability()
    
    print("\n" + "="*60)
    print("INTERPRETATION:")
    print("="*60)
    print("""
This analysis examines whether the URM faculty in the personalized databases
were actually giving talks at peer universities. This tells us about:

1. Database Quality: Were these active speakers on the seminar circuit?
2. Availability: What fraction of speakers at peer schools were in our database?
3. Comparability: Treatment and control should be similar (same algorithm)

If very few database speakers appear at peer universities, it suggests the
database contained faculty who weren't actively giving seminars, which would
explain why departments didn't select from it.
""")

if __name__ == "__main__":
    asyncio.run(main())