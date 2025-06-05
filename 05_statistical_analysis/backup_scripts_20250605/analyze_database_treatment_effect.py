#!/usr/bin/env python3
"""
Comprehensive Analysis of URM Database Treatment Effect

This script analyzes whether the RCT's effect on URM/Black representation came from
direct selection from the provided databases or through indirect mechanisms.

Key analyses:
1. Overall URM database matches
2. Black speaker specific analysis  
3. Breakdown by semester and discipline
4. Department-level treatment effects
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json
import logging
from typing import Dict, List, Tuple, Optional
from collections import defaultdict
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class DatabaseTreatmentAnalyzer:
    """Main analyzer for database treatment effects"""
    
    def __init__(self):
        self.data_dir = Path("/mnt/c/Users/jcerv/Jose/search-costs")
        self.output_dir = Path("/mnt/c/Users/jcerv/Jose/search-costs/05_statistical_analysis/outputs")
        self.output_dir.mkdir(exist_ok=True)
        
        logger.info("Initializing Database Treatment Analyzer")
        self.load_all_data()
        
    def load_all_data(self) -> None:
        """Load all necessary data files"""
        logger.info("Loading data files...")
        
        # 1. Load master data
        self.master_data = pd.read_csv(
            self.data_dir / "03_data_collection/processed/master-data-final.csv",
            low_memory=False
        )
        logger.info(f"Loaded master data: {self.master_data.shape}")
        
        # 2. Load URM databases
        self.load_urm_databases()
        
        # 3. Load speaker demographics
        self.speaker_demographics = pd.read_csv(
            self.data_dir / "04_demographic_analysis/outputs/people_combined_analysis.csv"
        )
        logger.info(f"Loaded {len(self.speaker_demographics)} unique speakers with demographics")
        
        # 4. Load randomization
        self.randomization = pd.read_csv(self.data_dir / "01_experiment_design/randomized_data.csv")
        self.randomization['university'] = self.randomization['department'].str.split('-').str[0]
        self.randomization['discipline'] = self.randomization['department'].str.split('-').str[1]
        
        # 5. Extract speakers from master data
        self.speakers_df = self.extract_all_speakers()
        logger.info(f"Extracted {len(self.speakers_df)} speaker appearances")
        
    def load_urm_databases(self) -> None:
        """Load URM faculty databases"""
        self.urm_databases = {}
        self.black_faculty_databases = {}
        
        db_dir = self.data_dir / "02_intervention_materials/databases"
        discipline_map = {
            'chemistry': 'Chemistry',
            'physics': 'Physics', 
            'mathematics': 'Mathematics',
            'computerScience': 'Computer Science',
            'mechanicalEngineering': 'Mechanical Engineering'
        }
        
        total_urm = 0
        total_black = 0
        
        for file_name, discipline in discipline_map.items():
            df = pd.read_csv(db_dir / f"{file_name}.csv")
            self.urm_databases[discipline] = df
            
            # Extract Black faculty
            black_df = df[df['Race'] == 'Black'].copy()
            self.black_faculty_databases[discipline] = black_df
            
            total_urm += len(df)
            total_black += len(black_df)
            
            logger.info(f"  {discipline}: {len(df)} URM faculty ({len(black_df)} Black)")
            
        logger.info(f"Total: {total_urm} URM faculty, {total_black} Black faculty")
        
    def extract_all_speakers(self) -> pd.DataFrame:
        """Extract speakers from wide format to long format"""
        speakers_list = []
        
        for _, row in self.master_data.iterrows():
            seminar_info = {
                'seminar_id': row['seminar_id'],
                'university': row['university'],
                'discipline': row['discipline'],
                'condition': row['condition'],
                'semester': 'Fall' if any(str(row.get(f'date_{i}', '')).startswith(('8/', '9/', '10/', '11/', '12/'))
                                         for i in range(1, 129)) else 'Spring'
            }
            
            # Extract each speaker
            for i in range(1, 129):
                first_name_col = f'First Name_{i}'
                last_name_col = f'Last Name_{i}'
                
                if first_name_col in row and pd.notna(row.get(first_name_col)):
                    first_name = str(row.get(first_name_col, '')).strip()
                    last_name = str(row.get(last_name_col, '')).strip()
                    
                    if first_name and last_name:
                        speaker_data = {
                            **seminar_info,
                            'speaker_num': i,
                            'first_name': first_name,
                            'last_name': last_name,
                            'full_name': f"{first_name} {last_name}",
                            'date': row.get(f'date_{i}'),
                            'speaker_university': row.get(f'university_{i}_standardized', 
                                                        row.get(f'university_{i}')),
                            'rank': row.get(f'rank_{i}_standardized')
                        }
                        speakers_list.append(speaker_data)
                        
        return pd.DataFrame(speakers_list)
    
    def match_speakers_to_demographics(self) -> pd.DataFrame:
        """Match speakers to their demographic information"""
        # Normalize names for matching
        self.speaker_demographics['name_normalized'] = (
            self.speaker_demographics['name'].str.lower().str.strip()
        )
        self.speakers_df['name_normalized'] = (
            self.speakers_df['full_name'].str.lower().str.strip()
        )
        
        # Merge demographics
        speakers_with_demo = self.speakers_df.merge(
            self.speaker_demographics[['name_normalized', 'combined_race', 
                                      'combined_gender', 'is_urm']],
            on='name_normalized',
            how='left'
        )
        
        return speakers_with_demo
    
    def match_to_urm_databases(self, speakers_df: pd.DataFrame) -> pd.DataFrame:
        """Match speakers to URM databases"""
        all_matches = []
        
        for discipline, urm_df in self.urm_databases.items():
            disc_speakers = speakers_df[speakers_df['discipline'] == discipline]
            
            if len(disc_speakers) == 0:
                continue
                
            # Normalize URM names
            urm_df['name_normalized'] = urm_df['Name'].str.lower().str.strip()
            
            for _, urm in urm_df.iterrows():
                urm_name = urm['name_normalized']
                urm_parts = urm_name.split()
                
                # Match speakers
                matches = disc_speakers[
                    disc_speakers['name_normalized'].str.contains(urm_name, case=False, na=False) |
                    disc_speakers['name_normalized'].str.contains(urm_parts[-1], case=False, na=False)
                ]
                
                if len(matches) > 0:
                    for _, match in matches.iterrows():
                        all_matches.append({
                            'urm_name': urm['Name'],
                            'urm_university': urm['Schools'],
                            'urm_race': urm['Race'],
                            'speaker_name': match['full_name'],
                            'speaker_university': match['speaker_university'],
                            'seminar_university': match['university'],
                            'discipline': discipline,
                            'condition': match['condition'],
                            'semester': match['semester'],
                            'date': match['date'],
                            'speaker_race': match.get('combined_race', 'unknown')
                        })
                        
        return pd.DataFrame(all_matches)
    
    def analyze_by_department(self, speakers_df: pd.DataFrame, 
                            matches_df: pd.DataFrame) -> pd.DataFrame:
        """Analyze at department level"""
        dept_stats = []
        
        for _, dept in self.randomization.iterrows():
            university = dept['university']
            discipline = dept['discipline']
            condition = dept['condition']
            
            # Get department speakers
            dept_speakers = speakers_df[
                (speakers_df['university'] == university) & 
                (speakers_df['discipline'] == discipline)
            ]
            
            if len(dept_speakers) == 0:
                continue
                
            # Overall stats
            total_unique = len(dept_speakers['full_name'].unique())
            
            # URM stats
            urm_speakers = dept_speakers[dept_speakers['is_urm'] == 1]
            unique_urm = len(urm_speakers['full_name'].unique())
            
            # Black stats
            black_speakers = dept_speakers[dept_speakers['combined_race'] == 'black']
            unique_black = len(black_speakers['full_name'].unique())
            
            # Database matches
            dept_matches = matches_df[
                (matches_df['seminar_university'] == university) & 
                (matches_df['discipline'] == discipline)
            ] if len(matches_df) > 0 else pd.DataFrame()
            
            unique_from_db = len(dept_matches['speaker_name'].unique()) if len(dept_matches) > 0 else 0
            
            # Black from database
            black_matches = dept_matches[dept_matches['speaker_race'] == 'black'] if len(dept_matches) > 0 else pd.DataFrame()
            unique_black_from_db = len(black_matches['speaker_name'].unique()) if len(black_matches) > 0 else 0
            
            # Semester breakdown
            fall_speakers = dept_speakers[dept_speakers['semester'] == 'Fall']
            spring_speakers = dept_speakers[dept_speakers['semester'] == 'Spring']
            
            dept_stats.append({
                'university': university,
                'discipline': discipline,
                'condition': condition,
                'treatment': 1 if condition == 'treatment' else 0,
                # Overall
                'total_speakers': total_unique,
                'urm_speakers': unique_urm,
                'black_speakers': unique_black,
                'speakers_from_db': unique_from_db,
                'black_from_db': unique_black_from_db,
                # Percentages
                'pct_urm': unique_urm / total_unique if total_unique > 0 else 0,
                'pct_black': unique_black / total_unique if total_unique > 0 else 0,
                'pct_from_db': unique_from_db / total_unique if total_unique > 0 else 0,
                'pct_black_from_db': unique_black_from_db / unique_black if unique_black > 0 else 0,
                # Binary indicators
                'any_urm': 1 if unique_urm > 0 else 0,
                'any_black': 1 if unique_black > 0 else 0,
                'any_from_db': 1 if unique_from_db > 0 else 0,
                # Semester
                'fall_speakers': len(fall_speakers['full_name'].unique()),
                'spring_speakers': len(spring_speakers['full_name'].unique()),
                'fall_black': len(fall_speakers[fall_speakers['combined_race'] == 'black']['full_name'].unique()),
                'spring_black': len(spring_speakers[spring_speakers['combined_race'] == 'black']['full_name'].unique())
            })
            
        return pd.DataFrame(dept_stats)
    
    def calculate_treatment_effects(self, dept_stats_df: pd.DataFrame) -> Dict:
        """Calculate treatment effects with proper statistics"""
        results = {}
        
        # Filter to departments with speakers
        dept_stats_df = dept_stats_df[dept_stats_df['total_speakers'] > 0]
        
        treatment = dept_stats_df[dept_stats_df['treatment'] == 1]
        control = dept_stats_df[dept_stats_df['treatment'] == 0]
        
        # Metrics to analyze
        metrics = [
            ('pct_urm', 'URM share'),
            ('pct_black', 'Black share'),
            ('pct_from_db', 'Share from database'),
            ('any_black', 'Probability of any Black speaker'),
            ('any_from_db', 'Probability of any speaker from database')
        ]
        
        for metric, description in metrics:
            treat_vals = treatment[metric]
            ctrl_vals = control[metric]
            
            # Calculate stats
            result = {
                'metric': metric,
                'description': description,
                'treatment_mean': treat_vals.mean(),
                'control_mean': ctrl_vals.mean(),
                'treatment_n': len(treat_vals),
                'control_n': len(ctrl_vals),
                'difference': treat_vals.mean() - ctrl_vals.mean()
            }
            
            # Percentage change
            if ctrl_vals.mean() > 0:
                result['pct_change'] = result['difference'] / ctrl_vals.mean() * 100
            else:
                result['pct_change'] = np.nan
                
            # T-test
            if treat_vals.std() > 0 or ctrl_vals.std() > 0:
                t_stat, p_value = stats.ttest_ind(treat_vals, ctrl_vals)
                result['t_stat'] = t_stat
                result['p_value'] = p_value
                result['significant'] = p_value < 0.05
            else:
                result['t_stat'] = np.nan
                result['p_value'] = np.nan
                result['significant'] = False
                
            results[metric] = result
            
        return results
    
    def analyze_by_discipline(self, dept_stats_df: pd.DataFrame) -> pd.DataFrame:
        """Analyze treatment effects by discipline with full statistics"""
        discipline_results = []
        
        for discipline in dept_stats_df['discipline'].unique():
            disc_data = dept_stats_df[dept_stats_df['discipline'] == discipline]
            
            if len(disc_data) < 10:  # Skip if too few departments
                continue
                
            treat = disc_data[disc_data['treatment'] == 1]
            ctrl = disc_data[disc_data['treatment'] == 0]
            
            if len(treat) > 0 and len(ctrl) > 0:
                result = {
                    'discipline': discipline,
                    'n_treatment': len(treat),
                    'n_control': len(ctrl),
                    'total_speakers': disc_data['total_speakers'].sum(),
                    'total_urm': disc_data['urm_speakers'].sum(),
                    'total_black': disc_data['black_speakers'].sum()
                }
                
                # Calculate statistics for multiple metrics
                metrics = [
                    ('pct_black', 'black_share'),
                    ('pct_urm', 'urm_share'),
                    ('pct_from_db', 'db_share'),
                    ('any_black', 'any_black'),
                    ('any_urm', 'any_urm'),
                    ('any_from_db', 'any_db')
                ]
                
                for metric, prefix in metrics:
                    treat_vals = treat[metric]
                    ctrl_vals = ctrl[metric]
                    
                    result[f'{prefix}_treatment'] = treat_vals.mean()
                    result[f'{prefix}_control'] = ctrl_vals.mean()
                    result[f'{prefix}_diff'] = treat_vals.mean() - ctrl_vals.mean()
                    
                    # Percentage change
                    if ctrl_vals.mean() > 0:
                        result[f'{prefix}_pct_change'] = (treat_vals.mean() - ctrl_vals.mean()) / ctrl_vals.mean() * 100
                    else:
                        result[f'{prefix}_pct_change'] = np.nan
                    
                    # T-test
                    if treat_vals.std() > 0 or ctrl_vals.std() > 0:
                        t_stat, p_value = stats.ttest_ind(treat_vals, ctrl_vals)
                        result[f'{prefix}_pvalue'] = p_value
                    else:
                        result[f'{prefix}_pvalue'] = np.nan
                
                discipline_results.append(result)
                
        return pd.DataFrame(discipline_results)
    
    def analyze_by_semester(self, speakers_df: pd.DataFrame) -> Dict:
        """Analyze treatment effects by semester"""
        semester_results = {}
        
        for semester in ['Fall', 'Spring']:
            sem_speakers = speakers_df[speakers_df['semester'] == semester]
            
            # Aggregate by department and semester
            dept_sem_stats = []
            for _, dept in self.randomization.iterrows():
                university = dept['university']
                discipline = dept['discipline']
                condition = dept['condition']
                
                dept_sem_speakers = sem_speakers[
                    (sem_speakers['university'] == university) & 
                    (sem_speakers['discipline'] == discipline)
                ]
                
                if len(dept_sem_speakers) > 0:
                    total_unique = len(dept_sem_speakers['full_name'].unique())
                    urm_unique = len(dept_sem_speakers[dept_sem_speakers['is_urm'] == 1]['full_name'].unique())
                    black_unique = len(dept_sem_speakers[dept_sem_speakers['combined_race'] == 'black']['full_name'].unique())
                    
                    dept_sem_stats.append({
                        'treatment': 1 if condition == 'treatment' else 0,
                        'total_speakers': total_unique,
                        'urm_speakers': urm_unique,
                        'black_speakers': black_unique,
                        'pct_urm': urm_unique / total_unique if total_unique > 0 else 0,
                        'pct_black': black_unique / total_unique if total_unique > 0 else 0,
                        'any_urm': 1 if urm_unique > 0 else 0,
                        'any_black': 1 if black_unique > 0 else 0
                    })
            
            if dept_sem_stats:
                sem_df = pd.DataFrame(dept_sem_stats)
                treat = sem_df[sem_df['treatment'] == 1]
                ctrl = sem_df[sem_df['treatment'] == 0]
                
                # Calculate statistics
                result = {
                    'semester': semester,
                    'n_treatment': len(treat),
                    'n_control': len(ctrl)
                }
                
                metrics = [
                    ('pct_black', 'black_share'),
                    ('pct_urm', 'urm_share'),
                    ('any_black', 'any_black'),
                    ('any_urm', 'any_urm')
                ]
                
                for metric, prefix in metrics:
                    if len(treat) > 0 and len(ctrl) > 0:
                        treat_mean = treat[metric].mean()
                        ctrl_mean = ctrl[metric].mean()
                        
                        result[f'{prefix}_treatment'] = treat_mean
                        result[f'{prefix}_control'] = ctrl_mean
                        result[f'{prefix}_diff'] = treat_mean - ctrl_mean
                        
                        if ctrl_mean > 0:
                            result[f'{prefix}_pct_change'] = (treat_mean - ctrl_mean) / ctrl_mean * 100
                        else:
                            result[f'{prefix}_pct_change'] = np.nan
                        
                        # T-test
                        if treat[metric].std() > 0 or ctrl[metric].std() > 0:
                            t_stat, p_value = stats.ttest_ind(treat[metric], ctrl[metric])
                            result[f'{prefix}_pvalue'] = p_value
                        else:
                            result[f'{prefix}_pvalue'] = np.nan
                
                semester_results[semester] = result
                
        return semester_results
    
    def run_comprehensive_analysis(self) -> None:
        """Run the complete analysis"""
        logger.info("\n=== RUNNING COMPREHENSIVE ANALYSIS ===")
        
        # 1. Match speakers to demographics
        speakers_with_demo = self.match_speakers_to_demographics()
        
        # 2. Match to URM databases
        matches_df = self.match_to_urm_databases(speakers_with_demo)
        logger.info(f"Found {len(matches_df)} total database matches")
        
        # 3. Department-level analysis
        dept_stats = self.analyze_by_department(speakers_with_demo, matches_df)
        
        # 4. Calculate treatment effects
        treatment_effects = self.calculate_treatment_effects(dept_stats)
        
        # 5. Discipline analysis
        discipline_stats = self.analyze_by_discipline(dept_stats)
        
        # 6. Semester analysis
        semester_stats = self.analyze_by_semester(speakers_with_demo)
        
        # 7. Display results
        self.display_results(treatment_effects, dept_stats, matches_df, discipline_stats, semester_stats)
        
        # 8. Save outputs
        self.save_results(dept_stats, matches_df, discipline_stats, semester_stats)
        
    def display_results(self, treatment_effects: Dict, dept_stats: pd.DataFrame,
                       matches_df: pd.DataFrame, discipline_stats: pd.DataFrame,
                       semester_stats: Dict) -> None:
        """Display comprehensive results with all statistics"""
        print("\n" + "="*80)
        print("COMPREHENSIVE DATABASE TREATMENT EFFECT ANALYSIS")
        print("="*80)
        
        # Overall statistics
        print("\n1. OVERALL STATISTICS:")
        print(f"   - Total speaker appearances: {len(self.speakers_df):,}")
        print(f"   - Unique speakers: {len(self.speakers_df['full_name'].unique()):,}")
        print(f"   - URM faculty in databases: {sum(len(df) for df in self.urm_databases.values())}")
        print(f"   - Black faculty in databases: {sum(len(df) for df in self.black_faculty_databases.values())}")
        print(f"   - Total database matches: {len(matches_df)}")
        
        # Treatment effects
        print("\n2. TREATMENT EFFECTS:")
        for metric_name, result in treatment_effects.items():
            print(f"\n   {result['description']}:")
            print(f"     Treatment: {result['treatment_mean']:.3f} (N={result['treatment_n']})")
            print(f"     Control:   {result['control_mean']:.3f} (N={result['control_n']})")
            print(f"     Difference: {result['difference']:.3f}", end="")
            if not pd.isna(result.get('pct_change')):
                print(f" ({result['pct_change']:+.1f}%)")
            else:
                print()
            if not pd.isna(result.get('p_value')):
                sig = "***" if result['p_value'] < 0.01 else "**" if result['p_value'] < 0.05 else "*" if result['p_value'] < 0.1 else "ns"
                print(f"     p-value: {result['p_value']:.4f} {sig}")
        
        # Black speaker deep dive
        print("\n3. BLACK SPEAKER ANALYSIS:")
        black_effect = treatment_effects['pct_black']
        print(f"   Treatment increased Black representation by {black_effect['pct_change']:.1f}%")
        
        # Calculate contribution from database
        treatment_depts = dept_stats[dept_stats['treatment'] == 1]
        control_depts = dept_stats[dept_stats['treatment'] == 0]
        
        total_black_treat = treatment_depts['black_speakers'].sum()
        total_black_ctrl = control_depts['black_speakers'].sum()
        black_from_db_treat = treatment_depts['black_from_db'].sum()
        black_from_db_ctrl = control_depts['black_from_db'].sum()
        
        black_increase = total_black_treat - total_black_ctrl
        db_contribution = black_from_db_treat - black_from_db_ctrl
        
        print(f"\n   Absolute numbers:")
        print(f"     Treatment: {total_black_treat} Black speakers total")
        print(f"                {black_from_db_treat} from database")
        print(f"     Control:   {total_black_ctrl} Black speakers total")
        print(f"                {black_from_db_ctrl} from database")
        print(f"\n   Database contribution to increase:")
        print(f"     Total increase: {black_increase} Black speakers")
        print(f"     From database:  {db_contribution} speakers")
        if black_increase > 0:
            print(f"     Percentage:     {db_contribution/black_increase*100:.1f}% of increase from database")
            print(f"     Implication:    {100 - db_contribution/black_increase*100:.1f}% from indirect effects")
        
        # Discipline breakdown
        print("\n4. DISCIPLINE BREAKDOWN WITH FULL STATISTICS:")
        print("\n   A. Black Speaker Share (% of all speakers)")
        print("   " + "-"*70)
        print("   Discipline      | Treatment | Control | Diff (pp) | % Change | p-value")
        print("   " + "-"*70)
        
        for _, disc in discipline_stats.iterrows():
            sig = self._get_significance(disc['black_share_pvalue'])
            print(f"   {disc['discipline']:15s} | {disc['black_share_treatment']*100:8.1f}% | "
                  f"{disc['black_share_control']*100:7.1f}% | {disc['black_share_diff']*100:+9.1f} | "
                  f"{disc['black_share_pct_change']:+7.1f}% | {disc['black_share_pvalue']:.4f} {sig}")
        
        print("\n   B. Probability of ANY Black Speaker (binary)")
        print("   " + "-"*70)
        print("   Discipline      | Treatment | Control | Diff (pp) | % Change | p-value")
        print("   " + "-"*70)
        
        for _, disc in discipline_stats.iterrows():
            sig = self._get_significance(disc['any_black_pvalue'])
            print(f"   {disc['discipline']:15s} | {disc['any_black_treatment']*100:8.1f}% | "
                  f"{disc['any_black_control']*100:7.1f}% | {disc['any_black_diff']*100:+9.1f} | "
                  f"{disc['any_black_pct_change']:+7.1f}% | {disc['any_black_pvalue']:.4f} {sig}")
        
        print("\n   C. Database Usage (% departments using database)")
        print("   " + "-"*70)
        print("   Discipline      | Treatment | Control | Diff (pp) | % Change | p-value")
        print("   " + "-"*70)
        
        for _, disc in discipline_stats.iterrows():
            sig = self._get_significance(disc['any_db_pvalue'])
            print(f"   {disc['discipline']:15s} | {disc['any_db_treatment']*100:8.1f}% | "
                  f"{disc['any_db_control']*100:7.1f}% | {disc['any_db_diff']*100:+9.1f} | "
                  f"{disc['any_db_pct_change']:+7.1f}% | {disc['any_db_pvalue']:.4f} {sig}")
        
        # Semester analysis
        print("\n5. SEMESTER ANALYSIS:")
        
        for semester, sem_stats in semester_stats.items():
            print(f"\n   {semester} Semester:")
            print("   " + "-"*70)
            print("   Metric               | Treatment | Control | Diff (pp) | % Change | p-value")
            print("   " + "-"*70)
            
            metrics = [
                ('black_share', 'Black share'),
                ('any_black', 'Any Black speaker'),
                ('urm_share', 'URM share'),
                ('any_urm', 'Any URM speaker')
            ]
            
            for prefix, desc in metrics:
                treat = sem_stats.get(f'{prefix}_treatment', 0)
                ctrl = sem_stats.get(f'{prefix}_control', 0)
                diff = sem_stats.get(f'{prefix}_diff', 0)
                pct_change = sem_stats.get(f'{prefix}_pct_change', 0)
                pval = sem_stats.get(f'{prefix}_pvalue', 1)
                sig = self._get_significance(pval)
                
                print(f"   {desc:20s} | {treat*100:8.1f}% | {ctrl*100:7.1f}% | "
                      f"{diff*100:+9.1f} | {pct_change:+7.1f}% | {pval:.4f} {sig}")
    
    def _get_significance(self, p_value: float) -> str:
        """Get significance stars for p-value"""
        if pd.isna(p_value):
            return ""
        elif p_value < 0.001:
            return "***"
        elif p_value < 0.01:
            return "**"
        elif p_value < 0.05:
            return "*"
        elif p_value < 0.1:
            return "+"
        else:
            return ""
    
    def save_results(self, dept_stats: pd.DataFrame, matches_df: pd.DataFrame,
                    discipline_stats: pd.DataFrame, semester_stats: Dict) -> None:
        """Save all results to files"""
        # Department statistics
        dept_stats.to_csv(self.output_dir / "database_effect_dept_stats.csv", index=False)
        
        # All matches
        matches_df.to_csv(self.output_dir / "database_matches_all.csv", index=False)
        
        # Discipline breakdown
        discipline_stats.to_csv(self.output_dir / "database_effect_by_discipline.csv", index=False)
        
        # Semester results
        semester_df = pd.DataFrame(semester_stats).T
        semester_df.to_csv(self.output_dir / "database_effect_by_semester.csv")
        
        # Summary JSON
        summary = {
            'total_speakers': len(self.speakers_df),
            'unique_speakers': len(self.speakers_df['full_name'].unique()),
            'total_matches': len(matches_df),
            'unique_matched_speakers': len(matches_df['speaker_name'].unique()) if len(matches_df) > 0 else 0,
            'analysis_date': pd.Timestamp.now().isoformat()
        }
        
        with open(self.output_dir / "database_effect_summary.json", 'w') as f:
            json.dump(summary, f, indent=2)
            
        logger.info(f"\nResults saved to {self.output_dir}")


def main():
    """Run the analysis"""
    analyzer = DatabaseTreatmentAnalyzer()
    analyzer.run_comprehensive_analysis()
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80)


if __name__ == "__main__":
    main()