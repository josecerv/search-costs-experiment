#!/usr/bin/env python3
"""
Analyze PhD Years as a Moderator in the Search Costs RCT
Tests whether treatment effects vary by speaker seniority (years from PhD)
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from pathlib import Path
import json
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

def load_data():
    """Load the master analysis dataset"""
    print("\n=== Loading Master Analysis Dataset ===")
    
    base_dir = Path("/Users/josecervantez/Documents/Jose-CODE/search-costs")
    master_file = base_dir / "05_statistical_analysis/outputs/master_analysis_dataset.csv"
    
    if not master_file.exists():
        raise FileNotFoundError(f"Master dataset not found at {master_file}")
    
    df = pd.read_csv(master_file)
    print(f"Loaded {len(df)} seminars")
    
    # Check PhD year coverage
    has_phd_data = df['num_speakers_with_phd_year'] > 0
    print(f"Seminars with PhD year data: {has_phd_data.sum()} ({has_phd_data.mean()*100:.1f}%)")
    
    return df

def create_seniority_bins(df):
    """Create seniority bins for analysis"""
    print("\n=== Creating Seniority Bins ===")
    
    # Filter to seminars with PhD data
    df_with_phd = df[df['num_speakers_with_phd_year'] > 0].copy()
    
    # Create seniority categories based on mean years from PhD
    # Using quartiles of the distribution
    quartiles = df_with_phd['mean_years_from_phd'].quantile([0.25, 0.5, 0.75])
    
    def categorize_seniority(years):
        if pd.isna(years):
            return 'Unknown'
        elif years < quartiles[0.25]:
            return 'Early Career'  # Bottom quartile
        elif years < quartiles[0.5]:
            return 'Mid Career'    # Second quartile
        elif years < quartiles[0.75]:
            return 'Senior'        # Third quartile
        else:
            return 'Very Senior'   # Top quartile
    
    df_with_phd['seniority_category'] = df_with_phd['mean_years_from_phd'].apply(categorize_seniority)
    
    # Also create a continuous centered variable
    mean_years = df_with_phd['mean_years_from_phd'].mean()
    df_with_phd['years_from_phd_centered'] = df_with_phd['mean_years_from_phd'] - mean_years
    
    print(f"Mean years from PhD: {mean_years:.1f}")
    print(f"Seniority distribution:")
    print(df_with_phd['seniority_category'].value_counts().sort_index())
    
    return df_with_phd, quartiles

def run_moderation_analysis(df):
    """Run moderation analysis with years from PhD"""
    print("\n=== Running Moderation Analysis ===")
    
    results = {}
    
    # 1. Main effect model (for comparison)
    print("\n1. Main Effect Model (no moderation):")
    main_model = smf.ols('pct_urm ~ treatment + C(bin_category)', data=df).fit()
    main_effect = main_model.params['treatment']
    main_pvalue = main_model.pvalues['treatment']
    print(f"   Treatment effect: {main_effect:.4f} (p={main_pvalue:.4f})")
    
    results['main_effect'] = {
        'coefficient': main_effect,
        'p_value': main_pvalue,
        'n': int(main_model.nobs)
    }
    
    # 2. Continuous moderation model
    print("\n2. Continuous Moderation Model:")
    cont_model = smf.ols('pct_urm ~ treatment * years_from_phd_centered + C(bin_category)', 
                        data=df).fit()
    
    treatment_coef = cont_model.params.get('treatment', np.nan)
    interaction_coef = cont_model.params.get('treatment:years_from_phd_centered', np.nan)
    interaction_pvalue = cont_model.pvalues.get('treatment:years_from_phd_centered', np.nan)
    
    print(f"   Treatment main effect: {treatment_coef:.4f}")
    print(f"   Treatment × Years from PhD: {interaction_coef:.4f} (p={interaction_pvalue:.4f})")
    
    results['continuous_moderation'] = {
        'treatment': treatment_coef,
        'years_from_phd': cont_model.params.get('years_from_phd_centered', np.nan),
        'interaction': interaction_coef,
        'interaction_p': interaction_pvalue,
        'n': int(cont_model.nobs)
    }
    
    # 3. Categorical moderation model
    print("\n3. Categorical Moderation Model:")
    cat_model = smf.ols('pct_urm ~ treatment * C(seniority_category) + C(bin_category)', 
                       data=df).fit()
    
    # Extract interaction effects for each category
    cat_results = {}
    for param, value in cat_model.params.items():
        if 'treatment:C(seniority_category)' in param:
            category = param.split('[T.')[1].rstrip(']')
            p_value = cat_model.pvalues[param]
            cat_results[category] = {
                'interaction_coef': value,
                'p_value': p_value
            }
    
    results['categorical_moderation'] = cat_results
    
    # 4. Simple slopes analysis - treatment effect at different seniority levels
    print("\n4. Simple Slopes Analysis:")
    seniority_levels = [-10, -5, 0, 5, 10, 15, 20]  # Years from mean
    
    simple_slopes = []
    for level in seniority_levels:
        # Calculate treatment effect at this seniority level
        effect = treatment_coef + interaction_coef * level
        
        # Calculate standard error using delta method
        # Var(a + b*x) = Var(a) + x^2*Var(b) + 2*x*Cov(a,b)
        var_treatment = cont_model.cov_params().loc['treatment', 'treatment']
        var_interaction = cont_model.cov_params().loc['treatment:years_from_phd_centered', 
                                                     'treatment:years_from_phd_centered']
        cov_treatment_int = cont_model.cov_params().loc['treatment', 
                                                       'treatment:years_from_phd_centered']
        
        se = np.sqrt(var_treatment + level**2 * var_interaction + 2 * level * cov_treatment_int)
        z_score = effect / se
        from scipy import stats
        p_value = 2 * (1 - stats.norm.cdf(abs(z_score)))
        
        actual_years = level + df['mean_years_from_phd'].mean()
        
        simple_slopes.append({
            'years_from_phd': actual_years,
            'treatment_effect': effect,
            'std_error': se,
            'p_value': p_value,
            'significant': p_value < 0.05
        })
        
        print(f"   At {actual_years:.0f} years from PhD: β={effect:.4f} (SE={se:.4f}, p={p_value:.4f})")
    
    results['simple_slopes'] = simple_slopes
    
    # 5. Additional outcomes
    print("\n5. Moderation Effects on Other Outcomes:")
    
    other_outcomes = {
        'num_urm': 'Count of URM speakers',
        'pct_female': 'Percentage female speakers',
        'num_female': 'Count of female speakers'
    }
    
    other_results = {}
    for outcome, label in other_outcomes.items():
        if outcome in df.columns:
            model = smf.ols(f'{outcome} ~ treatment * years_from_phd_centered + C(bin_category)', 
                          data=df).fit()
            interaction = model.params.get('treatment:years_from_phd_centered', np.nan)
            p_value = model.pvalues.get('treatment:years_from_phd_centered', np.nan)
            
            other_results[outcome] = {
                'label': label,
                'interaction': interaction,
                'p_value': p_value
            }
            
            print(f"   {label}: interaction β={interaction:.4f} (p={p_value:.4f})")
    
    results['other_outcomes'] = other_results
    
    return results

def analyze_by_seniority_subgroups(df, quartiles):
    """Analyze treatment effects within seniority subgroups"""
    print("\n=== Treatment Effects by Seniority Subgroups ===")
    
    subgroup_results = {}
    
    # Define subgroups
    subgroups = [
        ('Early Career', lambda x: x < quartiles[0.25]),
        ('Mid Career', lambda x: (x >= quartiles[0.25]) & (x < quartiles[0.5])),
        ('Senior', lambda x: (x >= quartiles[0.5]) & (x < quartiles[0.75])),
        ('Very Senior', lambda x: x >= quartiles[0.75])
    ]
    
    for name, condition in subgroups:
        subset = df[condition(df['mean_years_from_phd'])]
        
        if len(subset) > 20:  # Only analyze if sufficient sample size
            model = smf.ols('pct_urm ~ treatment + C(bin_category)', data=subset).fit()
            
            treatment_effect = model.params.get('treatment', np.nan)
            p_value = model.pvalues.get('treatment', np.nan)
            
            subgroup_results[name] = {
                'n': len(subset),
                'n_treatment': subset['treatment'].sum(),
                'n_control': len(subset) - subset['treatment'].sum(),
                'treatment_effect': treatment_effect,
                'p_value': p_value,
                'mean_years_from_phd': subset['mean_years_from_phd'].mean()
            }
            
            print(f"\n{name} (mean {subset['mean_years_from_phd'].mean():.1f} years from PhD):")
            print(f"  N = {len(subset)} ({subset['treatment'].sum()} treatment, {len(subset) - subset['treatment'].sum()} control)")
            print(f"  Treatment effect: {treatment_effect:.4f} (p={p_value:.4f})")
            
            # Also show mean outcomes by treatment
            print(f"  Mean % URM:")
            print(f"    Control: {subset[subset['treatment']==0]['pct_urm'].mean():.3f}")
            print(f"    Treatment: {subset[subset['treatment']==1]['pct_urm'].mean():.3f}")
    
    return subgroup_results

def create_visualization_data(df, results):
    """Create data for visualization of moderation effects"""
    print("\n=== Creating Visualization Data ===")
    
    # Prepare data for plotting
    viz_data = {
        'seniority_distribution': {
            'treatment': df[df['treatment']==1]['mean_years_from_phd'].describe().to_dict(),
            'control': df[df['treatment']==0]['mean_years_from_phd'].describe().to_dict()
        },
        'simple_slopes': pd.DataFrame(results['simple_slopes']),
        'subgroup_effects': pd.DataFrame(results['subgroup_analysis']).T
    }
    
    return viz_data

def save_results(results, df):
    """Save analysis results"""
    print("\n=== Saving Results ===")
    
    base_dir = Path("/Users/josecervantez/Documents/Jose-CODE/search-costs")
    output_dir = base_dir / "05_statistical_analysis/outputs"
    
    # Save detailed results as JSON
    output_file = output_dir / "phd_years_moderation_analysis.json"
    with open(output_file, 'w') as f:
        # Convert numpy types for JSON serialization
        def convert_types(obj):
            if isinstance(obj, (np.integer, np.int64, np.int32)):
                return int(obj)
            elif isinstance(obj, (np.floating, np.float64, np.float32)):
                return float(obj)
            elif isinstance(obj, (np.bool_, bool)):
                return bool(obj)
            elif isinstance(obj, np.ndarray):
                return obj.tolist()
            elif isinstance(obj, dict):
                return {k: convert_types(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert_types(v) for v in obj]
            elif hasattr(obj, 'to_dict'):  # For pandas objects
                return obj.to_dict()
            return obj
        
        json.dump(convert_types(results), f, indent=2)
    
    print(f"Saved detailed results to: {output_file}")
    
    # Create summary report
    report_file = output_dir / "phd_years_moderation_report.md"
    with open(report_file, 'w') as f:
        f.write("# PhD Years as Moderator Analysis\n\n")
        f.write(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write("## Summary\n\n")
        f.write(f"- Seminars analyzed: {len(df)}\n")
        f.write(f"- Mean years from PhD: {df['mean_years_from_phd'].mean():.1f}\n")
        f.write(f"- Coverage: {(df['num_speakers_with_phd_year'] > 0).mean()*100:.1f}% of seminars have PhD year data\n\n")
        
        f.write("## Key Findings\n\n")
        
        # Main moderation effect
        cont_mod = results['moderation_analysis']['continuous_moderation']
        f.write(f"### Continuous Moderation\n")
        f.write(f"- Interaction coefficient: {cont_mod['interaction']:.4f} (p={cont_mod['interaction_p']:.4f})\n")
        if cont_mod['interaction_p'] < 0.05:
            f.write("- **Significant moderation effect detected**\n")
            if cont_mod['interaction'] > 0:
                f.write("- Treatment effect increases with speaker seniority\n")
            else:
                f.write("- Treatment effect decreases with speaker seniority\n")
        else:
            f.write("- No significant moderation by years from PhD\n")
        
        f.write("\n### Treatment Effects by Seniority Level\n\n")
        f.write("| Years from PhD | Treatment Effect | Std Error | P-value | Significant |\n")
        f.write("|----------------|------------------|-----------|---------|-------------|\n")
        
        for slope in results['moderation_analysis']['simple_slopes']:
            sig = "Yes" if slope['significant'] else "No"
            f.write(f"| {slope['years_from_phd']:.0f} | {slope['treatment_effect']:.4f} | "
                   f"{slope['std_error']:.4f} | {slope['p_value']:.4f} | {sig} |\n")
        
        f.write("\n### Subgroup Analysis\n\n")
        f.write("| Seniority Group | N | Treatment Effect | P-value |\n")
        f.write("|-----------------|---|------------------|----------|\n")
        
        for group, data in results['subgroup_analysis'].items():
            f.write(f"| {group} | {data['n']} | {data['treatment_effect']:.4f} | {data['p_value']:.4f} |\n")
        
        f.write("\n### Other Outcomes\n\n")
        for outcome, data in results['moderation_analysis']['other_outcomes'].items():
            f.write(f"- {data['label']}: interaction = {data['interaction']:.4f} (p={data['p_value']:.4f})\n")
    
    print(f"Saved summary report to: {report_file}")

def main():
    """Main analysis function"""
    print("\n=== PhD Years as Moderator Analysis ===")
    print(f"Started at: {datetime.now()}")
    
    try:
        # Load data
        df = load_data()
        
        # Create seniority bins
        df_with_phd, quartiles = create_seniority_bins(df)
        
        # Run moderation analysis
        moderation_results = run_moderation_analysis(df_with_phd)
        
        # Analyze by subgroups
        subgroup_results = analyze_by_seniority_subgroups(df_with_phd, quartiles)
        
        # Compile all results
        all_results = {
            'data_summary': {
                'n_seminars': len(df),
                'n_with_phd_data': len(df_with_phd),
                'mean_years_from_phd': float(df_with_phd['mean_years_from_phd'].mean()),
                'quartiles': quartiles.to_dict()
            },
            'moderation_analysis': moderation_results,
            'subgroup_analysis': subgroup_results
        }
        
        # Save results
        save_results(all_results, df_with_phd)
        
        print("\n✅ Analysis completed successfully!")
        
    except Exception as e:
        print(f"\n❌ Analysis failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    main()