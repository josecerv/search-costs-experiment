import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest
from statsmodels.stats.meta_analysis import combine_effects
from statsmodels.regression.linear_model import OLS
from statsmodels.tools.tools import add_constant
import warnings
warnings.filterwarnings('ignore')

# Load the data
master_data = pd.read_csv('/mnt/c/Users/jcerv/Jose/search-costs/05_statistical_analysis/outputs/master_analysis_dataset_final.csv')
randomization = pd.read_csv('/mnt/c/Users/jcerv/Jose/search-costs/01_experiment_design/randomized_data.csv')
speaker_appearances = pd.read_csv('/mnt/c/Users/jcerv/Jose/search-costs/04_demographic_analysis/outputs/speaker_appearances_analysis.csv')
email_demographics = pd.read_csv('/mnt/c/Users/jcerv/Jose/search-costs/05_statistical_analysis/outputs/email_recipient_demographics_by_dept.csv')

# Load full speaker data to calculate appearances properly
people_data = pd.read_csv('/mnt/c/Users/jcerv/Jose/search-costs/04_demographic_analysis/outputs/people_combined_analysis.csv')

# The master data already has bin_category, so we don't need to merge
df = master_data.copy()

# Define stratification bins
bins = ['[0,1]', '(1,3]', '(3,5]', '(5,7]', '(7,11]', '(11,17]', '(17,26]']

def stratified_t_test(data, var, treatment_col='treatment', strata_col='bin_category'):
    """
    Performs stratified t-test accounting for randomization within bins
    Uses Cochran-Mantel-Haenszel approach for continuous variables
    """
    strata_results = []
    
    for stratum in data[strata_col].unique():
        if pd.isna(stratum):
            continue
            
        stratum_data = data[data[strata_col] == stratum]
        
        control = stratum_data[stratum_data[treatment_col] == 0][var].dropna()
        treatment = stratum_data[stratum_data[treatment_col] == 1][var].dropna()
        
        if len(control) > 0 and len(treatment) > 0:
            # Calculate stratum-specific statistics
            n_c = len(control)
            n_t = len(treatment)
            mean_c = control.mean()
            mean_t = treatment.mean()
            var_c = control.var()
            var_t = treatment.var()
            
            # Pooled variance
            pooled_var = ((n_c - 1) * var_c + (n_t - 1) * var_t) / (n_c + n_t - 2)
            
            # Weight by stratum size
            weight = (n_c * n_t) / (n_c + n_t)
            
            strata_results.append({
                'stratum': stratum,
                'diff': mean_t - mean_c,
                'se': np.sqrt(pooled_var * (1/n_c + 1/n_t)) if pooled_var > 0 else 0,
                'weight': weight,
                'n_control': n_c,
                'n_treatment': n_t
            })
    
    if not strata_results:
        return np.nan
    
    # Combine across strata using inverse variance weighting
    strata_df = pd.DataFrame(strata_results)
    weights = strata_df['weight'] / strata_df['weight'].sum()
    
    # Weighted mean difference
    weighted_diff = (strata_df['diff'] * weights).sum()
    
    # Weighted standard error
    weighted_se = np.sqrt((weights**2 * strata_df['se']**2).sum())
    
    # Test statistic
    if weighted_se > 0:
        z_stat = weighted_diff / weighted_se
        p_value = 2 * (1 - stats.norm.cdf(abs(z_stat)))
    else:
        p_value = np.nan
    
    return p_value

def regression_based_test(data, var, treatment_col='treatment', strata_col='bin_category'):
    """
    Regression-based test with stratum fixed effects
    More efficient than stratified t-test when many strata
    """
    # Remove missing values
    clean_data = data[[var, treatment_col, strata_col]].dropna()
    
    if len(clean_data) < 10:
        return np.nan
    
    # Create dummy variables for strata
    strata_dummies = pd.get_dummies(clean_data[strata_col], prefix='stratum', drop_first=True)
    
    # Combine with treatment
    X = pd.concat([clean_data[[treatment_col]], strata_dummies], axis=1)
    X = add_constant(X)
    y = clean_data[var]
    
    try:
        model = OLS(y, X).fit(cov_type='HC3')  # Robust standard errors
        return model.pvalues[treatment_col]
    except:
        return np.nan

# Calculate % URM among female recipients properly
# First, get department-level email recipient data
dept_female_urm = email_demographics.copy()
dept_female_urm['female_recipients'] = dept_female_urm['num_email_recipients'] * dept_female_urm['pct_female_recipients']
dept_female_urm['urm_female_recipients'] = dept_female_urm['num_urm_recipients'] * (dept_female_urm['pct_female_recipients'] if 'pct_urm_among_female' in dept_female_urm.columns else dept_female_urm['pct_urm_recipients'])
dept_female_urm['pct_urm_among_female_calc'] = np.where(
    dept_female_urm['female_recipients'] > 0.5,  # At least 0.5 female recipients
    dept_female_urm['urm_female_recipients'] / dept_female_urm['female_recipients'],
    np.nan
)

# Merge back to main data
df = df.merge(dept_female_urm[['department', 'pct_urm_among_female_calc']], 
              left_on='department', right_on='department', how='left', suffixes=('', '_dept'))

# Calculate average speaker appearances per seminar
# First count total appearances for each speaker
speaker_counts = speaker_appearances.groupby('speaker_id').size().reset_index(name='total_appearances')

# Get speakers per seminar
seminar_speakers = speaker_appearances.groupby('seminar_id')['speaker_id'].apply(list).reset_index()
seminar_avg_appearances = []

for idx, row in seminar_speakers.iterrows():
    speakers = row['speaker_id']
    # Get appearance counts for speakers in this seminar
    speaker_app_counts = speaker_counts[speaker_counts['speaker_id'].isin(speakers)]['total_appearances']
    if len(speaker_app_counts) > 0:
        avg_appearances = speaker_app_counts.mean()
    else:
        avg_appearances = np.nan
    
    seminar_avg_appearances.append({
        'seminar_id': row['seminar_id'],
        'avg_speaker_appearances_calc': avg_appearances
    })

seminar_avg_df = pd.DataFrame(seminar_avg_appearances)
df = df.merge(seminar_avg_df, on='seminar_id', how='left')

# Use calculated value 
df['avg_speaker_appearances'] = df['avg_speaker_appearances_calc']

# Add derived variables
df['seminars_with_demographics'] = (df['speakers_with_demographics'] > 0).astype(int)
df['total_speakers_analyzed'] = df['speakers_with_demographics']

# Calculate variables
variables = {
    'seminars_with_demographics': 'Final seminars with demographic data (count)',
    'pct_female_recipients': '% Email recipients female',
    'pct_urm_among_female_calc': '% Female recipients URM',
    'frac_women_faculty': 'Department Female % (faculty)',
    'frac_urm_faculty': 'Department URM % (faculty)',
    'total_speakers_analyzed': 'Total speakers analyzed',
    'avg_speaker_appearances': 'Average speaker appearances'
}

print("STRATIFICATION-AWARE BALANCE TABLE WITH CRITICAL STATISTICAL REVIEW")
print("=" * 120)
print(f"{'Variable':<50} {'Control Mean (SD)':<20} {'Treatment Mean (SD)':<20} {'P-value':<12} {'Method':<20}")
print("=" * 120)

# Overall statistics first
print("\nOVERALL STATISTICS (accounting for stratification):")
print("-" * 120)

for var, label in variables.items():
    if var in df.columns:
        control_data = df[df['treatment'] == 0][var].dropna()
        treatment_data = df[df['treatment'] == 1][var].dropna()
        
        control_mean = control_data.mean()
        control_sd = control_data.std()
        treatment_mean = treatment_data.mean()
        treatment_sd = treatment_data.std()
        
        # Use regression-based test for efficiency
        p_value = regression_based_test(df, var)
        
        print(f"{label:<50} {control_mean:>6.3f} ({control_sd:>6.3f})   "
              f"{treatment_mean:>6.3f} ({treatment_sd:>6.3f})   {p_value:>8.3f}    Regression w/ FE")

# Calculate standardized differences (Cohen's d) for effect sizes
print("\n\nSTANDARDIZED DIFFERENCES (Cohen's d):")
print("-" * 120)
print("{:<50} {:<15} {:<30}".format('Variable', "Cohen's d", 'Interpretation'))
print("-" * 120)

for var, label in variables.items():
    if var in df.columns:
        control_data = df[df['treatment'] == 0][var].dropna()
        treatment_data = df[df['treatment'] == 1][var].dropna()
        
        if len(control_data) > 0 and len(treatment_data) > 0:
            pooled_sd = np.sqrt(((len(control_data) - 1) * control_data.var() + 
                                (len(treatment_data) - 1) * treatment_data.var()) / 
                               (len(control_data) + len(treatment_data) - 2))
            
            if pooled_sd > 0:
                cohens_d = (treatment_data.mean() - control_data.mean()) / pooled_sd
                
                if abs(cohens_d) < 0.2:
                    interpretation = "Negligible"
                elif abs(cohens_d) < 0.5:
                    interpretation = "Small"
                elif abs(cohens_d) < 0.8:
                    interpretation = "Medium"
                else:
                    interpretation = "Large"
                
                print(f"{label:<50} {cohens_d:>8.3f}       {interpretation:<30}")

# Joint balance test
print("\n\nJOINT BALANCE TEST (Hotelling's T-squared):")
print("-" * 120)

# Prepare data for multivariate test
test_vars = ['pct_female_recipients', 'frac_women_faculty', 'frac_urm_faculty', 
             'total_speakers_analyzed']
clean_df = df[test_vars + ['treatment', 'bin_category']].dropna()

# Calculate Hotelling's T-squared within each stratum
chi2_stats = []
dfs = []

for stratum in bins:
    stratum_data = clean_df[clean_df['bin_category'] == stratum]
    
    if len(stratum_data) > 10:
        control = stratum_data[stratum_data['treatment'] == 0][test_vars]
        treatment = stratum_data[stratum_data['treatment'] == 1][test_vars]
        
        if len(control) > 5 and len(treatment) > 5:
            # Calculate Hotelling's T-squared
            n1, n2 = len(control), len(treatment)
            p = len(test_vars)
            
            mean_diff = treatment.mean() - control.mean()
            pooled_cov = ((n1 - 1) * control.cov() + (n2 - 1) * treatment.cov()) / (n1 + n2 - 2)
            
            try:
                inv_cov = np.linalg.inv(pooled_cov)
                t2 = n1 * n2 / (n1 + n2) * mean_diff.dot(inv_cov).dot(mean_diff)
                
                # Convert to F-statistic
                f_stat = (n1 + n2 - p - 1) / ((n1 + n2 - 2) * p) * t2
                f_df1 = p
                f_df2 = n1 + n2 - p - 1
                
                # Convert to chi-square for combining
                chi2_stats.append(f_stat * f_df1)
                dfs.append(f_df1)
            except:
                continue

# Combine chi-square statistics across strata
if chi2_stats:
    combined_chi2 = sum(chi2_stats)
    combined_df = sum(dfs)
    joint_p = 1 - stats.chi2.cdf(combined_chi2, combined_df)
    
    print(f"Combined chi-square statistic: {combined_chi2:.3f}")
    print(f"Degrees of freedom: {combined_df}")
    print(f"P-value: {joint_p:.4f}")
    print("\nInterpretation: " + ("Significant imbalance detected" if joint_p < 0.05 else "No significant imbalance"))

# Sample sizes and randomization check
print("\n\nRANDOMIZATION INTEGRITY CHECK:")
print("=" * 80)
print(f"{'Bin':<15} {'Control':<10} {'Treatment':<10} {'% Treatment':<15} {'Chi-sq p-value':<15}")
print("-" * 80)

chi2_overall = 0
for bin_cat in bins:
    bin_data = df[df['bin_category'] == bin_cat]
    n_control = len(bin_data[bin_data['treatment'] == 0])
    n_treatment = len(bin_data[bin_data['treatment'] == 1])
    n_total = n_control + n_treatment
    
    if n_total > 0:
        pct_treatment = n_treatment / n_total
        
        # Test if treatment proportion deviates from 0.5
        observed = [n_control, n_treatment]
        expected = [n_total/2, n_total/2]
        chi2, p_val = stats.chisquare(observed, expected)
        chi2_overall += chi2
        
        print(f"{bin_cat:<15} {n_control:<10} {n_treatment:<10} {pct_treatment:<15.3f} {p_val:<15.3f}")

# Overall randomization test
print("-" * 80)
total_control = len(df[df['treatment'] == 0])
total_treatment = len(df[df['treatment'] == 1])
print(f"{'TOTAL':<15} {total_control:<10} {total_treatment:<10} {total_treatment/(total_control+total_treatment):<15.3f}")
print(f"\nOverall randomization test: Chi-square = {chi2_overall:.3f}, p = {1 - stats.chi2.cdf(chi2_overall, len(bins)):.3f}")

# Critical reviewer notes
print("\n\nCRITICAL STATISTICAL REVIEW NOTES:")
print("=" * 120)
print("1. STRATIFICATION VALIDITY:")
print("   - Randomization was conducted within bins, ensuring balance within strata")
print("   - Overall balance may not hold due to different strata sizes")
print("   - P-values correctly account for stratification using regression with fixed effects")
print("\n2. MULTIPLE TESTING CONCERNS:")
print(f"   - Testing {len(variables)} variables increases Type I error probability")
print(f"   - Bonferroni-adjusted significance level: {0.05/len(variables):.4f}")
print(f"   - Consider false discovery rate (FDR) correction for exploratory analyses")
print("\n3. PRACTICAL SIGNIFICANCE:")
print("   - Statistical significance ≠ practical importance")
print("   - Cohen's d provides effect size context")
print("   - Small standardized differences (<0.2) are unlikely to bias results")
print("\n4. MISSING DATA:")
missing_pcts = {}
for var in variables:
    if var in df.columns:
        missing_pct = df[var].isna().mean() * 100
        if missing_pct > 0:
            missing_pcts[var] = missing_pct

if missing_pcts:
    print("   - Variables with missing data:")
    for var, pct in missing_pcts.items():
        print(f"     * {variables[var]}: {pct:.1f}% missing")
else:
    print("   - No missing data detected")

print("\n5. DEPARTMENT-LEVEL CLUSTERING:")
print("   - Standard errors should account for department-level randomization")
print("   - Current analysis uses robust (HC3) standard errors")
print("   - Consider cluster-robust standard errors for final analyses")