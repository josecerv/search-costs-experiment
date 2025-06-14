#!/usr/bin/env python3
"""
Comprehensive Summary Statistics for Search Costs RCT
=====================================================

This script generates a complete set of summary statistics for the experiment,
including balance checks, sample characteristics, and additional helpful metrics.

Author: Jose Cervan
Date: December 2024
"""

import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest, proportion_confint
import logging
from pathlib import Path
from typing import Dict, Tuple, List
import warnings
warnings.filterwarnings('ignore')

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define paths
BASE_DIR = Path('/mnt/c/Users/jcerv/Jose/search-costs')
DATA_DIR = BASE_DIR / '05_statistical_analysis' / 'outputs'
DEMOGRAPHICS_DIR = BASE_DIR / '04_demographic_analysis' / 'outputs'


def load_data() -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Load all necessary datasets."""
    logging.info("Loading datasets...")
    
    master_data = pd.read_csv(DATA_DIR / 'master_analysis_dataset_final.csv')
    speaker_appearances = pd.read_csv(DEMOGRAPHICS_DIR / 'speaker_appearances_analysis.csv')
    email_demographics = pd.read_csv(DATA_DIR / 'email_recipient_demographics_detailed.csv')
    
    logging.info(f"Loaded {len(master_data)} seminars, {len(speaker_appearances)} speaker appearances")
    return master_data, speaker_appearances, email_demographics


def calculate_coverage_stats(master_data: pd.DataFrame) -> Dict:
    """Calculate data coverage statistics."""
    # Original seminar counts from documentation
    original_control = 949
    original_treatment = 932
    
    # Current counts
    current_control = len(master_data[master_data['treatment'] == 0])
    current_treatment = len(master_data[master_data['treatment'] == 1])
    
    # Coverage rates
    coverage_control = current_control / original_control
    coverage_treatment = current_treatment / original_treatment
    
    # Test for difference
    count = np.array([current_control, current_treatment])
    nobs = np.array([original_control, original_treatment])
    z_stat, p_value = proportions_ztest(count, nobs)
    
    return {
        'original_control': original_control,
        'original_treatment': original_treatment,
        'current_control': current_control,
        'current_treatment': current_treatment,
        'coverage_control': coverage_control,
        'coverage_treatment': coverage_treatment,
        'coverage_p_value': p_value
    }


def calculate_discipline_distribution(master_data: pd.DataFrame) -> pd.DataFrame:
    """Calculate seminar distribution by discipline."""
    discipline_stats = master_data.groupby(['discipline', 'treatment']).size().unstack(fill_value=0)
    discipline_stats['total'] = discipline_stats.sum(axis=1)
    discipline_stats['pct_treatment'] = discipline_stats[1] / discipline_stats['total']
    
    # Chi-square test for each discipline
    p_values = []
    for disc in discipline_stats.index:
        control = discipline_stats.loc[disc, 0]
        treatment = discipline_stats.loc[disc, 1]
        _, p = stats.chisquare([control, treatment])
        p_values.append(p)
    
    discipline_stats['balance_p_value'] = p_values
    return discipline_stats


def calculate_temporal_distribution(speaker_appearances: pd.DataFrame) -> pd.DataFrame:
    """Calculate temporal distribution of seminars."""
    # Parse dates
    speaker_appearances['date'] = pd.to_datetime(speaker_appearances['date'], errors='coerce')
    speaker_appearances['month'] = speaker_appearances['date'].dt.month
    speaker_appearances['semester'] = speaker_appearances['month'].apply(
        lambda x: 'Fall' if x in [8, 9, 10, 11, 12] else 'Spring' if x in [1, 2, 3, 4, 5] else 'Summer'
    )
    
    # Get unique seminars per semester
    seminar_semester = speaker_appearances.groupby(['seminar_id', 'condition', 'semester']).size().reset_index()[['seminar_id', 'condition', 'semester']]
    
    # Count by condition and semester
    temporal_stats = seminar_semester.groupby(['semester', 'condition']).size().unstack(fill_value=0)
    temporal_stats.columns = ['control', 'treatment']
    temporal_stats['total'] = temporal_stats.sum(axis=1)
    
    return temporal_stats


def calculate_speaker_diversity_metrics(master_data: pd.DataFrame) -> pd.DataFrame:
    """Calculate detailed speaker diversity metrics."""
    diversity_metrics = []
    
    for treatment in [0, 1]:
        data = master_data[master_data['treatment'] == treatment]
        
        metrics = {
            'condition': 'control' if treatment == 0 else 'treatment',
            'n_seminars': len(data),
            
            # Overall diversity
            'pct_with_any_female': (data['has_any_female'] == 1).mean() * 100,
            'pct_with_any_urm': (data['has_any_urm'] == 1).mean() * 100,
            'pct_with_any_black': (data['has_any_black'] == 1).mean() * 100,
            'pct_with_any_hispanic': (data['has_any_hispanic'] == 1).mean() * 100,
            
            # Average percentages
            'avg_pct_female': data['pct_female'].mean(),
            'avg_pct_urm': data['pct_urm'].mean(),
            'avg_pct_black': data['pct_black'].mean(),
            'avg_pct_hispanic': data['pct_hispanic'].mean(),
            
            # Speaker counts
            'total_speakers': data['total_speakers'].sum(),
            'total_urm_speakers': data['num_urm'].sum(),
            'total_female_speakers': data['num_female'].sum(),
            'total_black_speakers': data['num_black'].sum(),
            'total_hispanic_speakers': data['num_hispanic'].sum(),
            
            # Concentration metrics
            'gini_female': calculate_gini(data['pct_female']),
            'gini_urm': calculate_gini(data['pct_urm']),
        }
        
        diversity_metrics.append(metrics)
    
    return pd.DataFrame(diversity_metrics)


def calculate_gini(x: pd.Series) -> float:
    """Calculate Gini coefficient for concentration."""
    x = x.dropna().sort_values()
    n = len(x)
    if n == 0:
        return np.nan
    index = np.arange(1, n + 1)
    return (2 * index * x).sum() / (n * x.sum()) - (n + 1) / n


def calculate_department_characteristics(master_data: pd.DataFrame) -> pd.DataFrame:
    """Calculate department-level characteristics."""
    dept_stats = master_data.groupby('treatment').agg({
        'total_faculty': 'mean',
        'frac_women_faculty': 'mean',
        'frac_urm_faculty': 'mean',
        'dept_ranking': 'mean',
        'general_ranking': 'mean',
        'num_recipients': 'mean',
        'pct_female_recipients': 'mean',
        'pct_urm_recipients': 'mean'
    }).round(3)
    
    # Add standard deviations
    dept_std = master_data.groupby('treatment').agg({
        'total_faculty': 'std',
        'frac_women_faculty': 'std',
        'frac_urm_faculty': 'std',
        'dept_ranking': 'std',
        'general_ranking': 'std',
        'num_recipients': 'std',
        'pct_female_recipients': 'std',
        'pct_urm_recipients': 'std'
    }).round(3)
    
    dept_stats.columns = [f"{col}_mean" for col in dept_stats.columns]
    dept_std.columns = [f"{col}_sd" for col in dept_std.columns]
    
    return pd.concat([dept_stats, dept_std], axis=1)


def calculate_stratification_balance(master_data: pd.DataFrame) -> pd.DataFrame:
    """Check balance within stratification bins."""
    bins = ['[0,1]', '(1,3]', '(3,5]', '(5,7]', '(7,11]', '(11,17]', '(17,26]']
    bin_stats = []
    
    for bin_cat in bins:
        bin_data = master_data[master_data['bin_category'] == bin_cat]
        
        if len(bin_data) > 0:
            n_control = len(bin_data[bin_data['treatment'] == 0])
            n_treatment = len(bin_data[bin_data['treatment'] == 1])
            
            # Key variables
            female_pct_c = bin_data[bin_data['treatment'] == 0]['pct_female'].mean()
            female_pct_t = bin_data[bin_data['treatment'] == 1]['pct_female'].mean()
            urm_pct_c = bin_data[bin_data['treatment'] == 0]['pct_urm'].mean()
            urm_pct_t = bin_data[bin_data['treatment'] == 1]['pct_urm'].mean()
            
            bin_stats.append({
                'bin': bin_cat,
                'n_control': n_control,
                'n_treatment': n_treatment,
                'n_total': n_control + n_treatment,
                'pct_treatment': n_treatment / (n_control + n_treatment) * 100,
                'female_pct_control': female_pct_c,
                'female_pct_treatment': female_pct_t,
                'urm_pct_control': urm_pct_c,
                'urm_pct_treatment': urm_pct_t
            })
    
    return pd.DataFrame(bin_stats)


def generate_latex_tables(results: Dict) -> None:
    """Generate LaTeX tables for the paper."""
    output_dir = DATA_DIR / 'latex_tables'
    output_dir.mkdir(exist_ok=True)
    
    # Table 1: Sample characteristics
    with open(output_dir / 'table1_sample_characteristics.tex', 'w') as f:
        f.write("% Table 1: Sample Characteristics\n")
        f.write("\\begin{table}[htbp]\n")
        f.write("\\centering\n")
        f.write("\\caption{Sample Characteristics}\n")
        f.write("\\begin{tabular}{lcc}\n")
        f.write("\\toprule\n")
        f.write("& Control & Treatment \\\\\n")
        f.write("\\midrule\n")
        
        # Add rows with formatted statistics
        coverage = results['coverage']
        f.write(f"Seminars analyzed & {coverage['current_control']} & {coverage['current_treatment']} \\\\\n")
        f.write(f"Coverage rate & {coverage['coverage_control']:.1%} & {coverage['coverage_treatment']:.1%} \\\\\n")
        
        f.write("\\bottomrule\n")
        f.write("\\end{tabular}\n")
        f.write("\\end{table}\n")
    
    logging.info(f"LaTeX tables saved to {output_dir}")


def main():
    """Run comprehensive summary statistics analysis."""
    logging.info("Starting comprehensive summary statistics analysis...")
    
    # Load data
    master_data, speaker_appearances, email_demographics = load_data()
    
    # Calculate all statistics
    results = {
        'coverage': calculate_coverage_stats(master_data),
        'disciplines': calculate_discipline_distribution(master_data),
        'temporal': calculate_temporal_distribution(speaker_appearances),
        'diversity': calculate_speaker_diversity_metrics(master_data),
        'departments': calculate_department_characteristics(master_data),
        'stratification': calculate_stratification_balance(master_data)
    }
    
    # Print formatted output
    print("\n" + "="*80)
    print("COMPREHENSIVE SUMMARY STATISTICS FOR SEARCH COSTS RCT")
    print("="*80)
    
    # 1. Coverage Statistics
    print("\n1. DATA COVERAGE")
    print("-"*50)
    cov = results['coverage']
    print(f"Original seminars:  Control={cov['original_control']}, Treatment={cov['original_treatment']}")
    print(f"Analyzed seminars:  Control={cov['current_control']}, Treatment={cov['current_treatment']}")
    print(f"Coverage rate:      Control={cov['coverage_control']:.1%}, Treatment={cov['coverage_treatment']:.1%}")
    print(f"Coverage p-value:   {cov['coverage_p_value']:.4f}")
    
    # 2. Discipline Distribution
    print("\n2. DISCIPLINE DISTRIBUTION")
    print("-"*50)
    print(results['disciplines'])
    
    # 3. Temporal Distribution
    print("\n3. TEMPORAL DISTRIBUTION")
    print("-"*50)
    print(results['temporal'])
    
    # 4. Speaker Diversity
    print("\n4. SPEAKER DIVERSITY METRICS")
    print("-"*50)
    div = results['diversity']
    for _, row in div.iterrows():
        print(f"\n{row['condition'].upper()}:")
        print(f"  Seminars with any female speaker: {row['pct_with_any_female']:.1f}%")
        print(f"  Seminars with any URM speaker: {row['pct_with_any_urm']:.1f}%")
        print(f"  Seminars with any Black speaker: {row['pct_with_any_black']:.1f}%")
        print(f"  Seminars with any Hispanic speaker: {row['pct_with_any_hispanic']:.1f}%")
        print(f"  Average % female: {row['avg_pct_female']:.1f}%")
        print(f"  Average % URM: {row['avg_pct_urm']:.1f}%")
        print(f"  Gini coefficient (female): {row['gini_female']:.3f}")
        print(f"  Gini coefficient (URM): {row['gini_urm']:.3f}")
    
    # 5. Department Characteristics
    print("\n5. DEPARTMENT CHARACTERISTICS")
    print("-"*50)
    dept = results['departments']
    print("Control departments:")
    print(f"  Faculty size: {dept.loc[0, 'total_faculty_mean']:.1f} (SD={dept.loc[0, 'total_faculty_sd']:.1f})")
    print(f"  % Female faculty: {dept.loc[0, 'frac_women_faculty_mean']:.1%} (SD={dept.loc[0, 'frac_women_faculty_sd']:.1%})")
    print(f"  % URM faculty: {dept.loc[0, 'frac_urm_faculty_mean']:.1%} (SD={dept.loc[0, 'frac_urm_faculty_sd']:.1%})")
    print(f"  Department ranking: {dept.loc[0, 'dept_ranking_mean']:.1f} (SD={dept.loc[0, 'dept_ranking_sd']:.1f})")
    
    print("\nTreatment departments:")
    print(f"  Faculty size: {dept.loc[1, 'total_faculty_mean']:.1f} (SD={dept.loc[1, 'total_faculty_sd']:.1f})")
    print(f"  % Female faculty: {dept.loc[1, 'frac_women_faculty_mean']:.1%} (SD={dept.loc[1, 'frac_women_faculty_sd']:.1%})")
    print(f"  % URM faculty: {dept.loc[1, 'frac_urm_faculty_mean']:.1%} (SD={dept.loc[1, 'frac_urm_faculty_sd']:.1%})")
    print(f"  Department ranking: {dept.loc[1, 'dept_ranking_mean']:.1f} (SD={dept.loc[1, 'dept_ranking_sd']:.1f})")
    
    # 6. Stratification Balance
    print("\n6. STRATIFICATION BALANCE")
    print("-"*50)
    strat = results['stratification']
    print(f"{'Bin':<10} {'N_C':<8} {'N_T':<8} {'%_T':<8} {'Female_C':<10} {'Female_T':<10} {'URM_C':<8} {'URM_T':<8}")
    print("-"*70)
    for _, row in strat.iterrows():
        print(f"{row['bin']:<10} {row['n_control']:<8} {row['n_treatment']:<8} "
              f"{row['pct_treatment']:<8.1f} {row['female_pct_control']:<10.1f} "
              f"{row['female_pct_treatment']:<10.1f} {row['urm_pct_control']:<8.1f} "
              f"{row['urm_pct_treatment']:<8.1f}")
    
    # Save results
    output_file = DATA_DIR / 'comprehensive_summary_statistics.xlsx'
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        results['disciplines'].to_excel(writer, sheet_name='Disciplines')
        results['temporal'].to_excel(writer, sheet_name='Temporal')
        results['diversity'].to_excel(writer, sheet_name='Diversity')
        results['departments'].to_excel(writer, sheet_name='Departments')
        results['stratification'].to_excel(writer, sheet_name='Stratification')
    
    logging.info(f"Results saved to {output_file}")
    
    # Generate LaTeX tables
    generate_latex_tables(results)
    
    print("\n" + "="*80)
    print("Analysis complete! Check outputs folder for detailed results.")
    

if __name__ == "__main__":
    main()