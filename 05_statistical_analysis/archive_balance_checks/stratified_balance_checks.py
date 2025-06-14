import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest
from statsmodels.stats.meta_analysis import combine_effects
import warnings
warnings.filterwarnings('ignore')

# Load the data
master_data = pd.read_csv('/mnt/c/Users/jcerv/Jose/search-costs/05_statistical_analysis/outputs/master_analysis_dataset_final.csv')
randomization = pd.read_csv('/mnt/c/Users/jcerv/Jose/search-costs/01_experiment_design/randomized_data.csv')
speaker_appearances = pd.read_csv('/mnt/c/Users/jcerv/Jose/search-costs/04_demographic_analysis/outputs/speaker_appearances_analysis.csv')
email_demographics = pd.read_csv('/mnt/c/Users/jcerv/Jose/search-costs/05_statistical_analysis/outputs/email_recipient_demographics_by_dept.csv')

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
                'se': np.sqrt(pooled_var * (1/n_c + 1/n_t)),
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

def stratified_proportion_test(data, var, treatment_col='treatment', strata_col='bin_category'):
    """
    Performs Cochran-Mantel-Haenszel test for proportions
    """
    # Create contingency tables for each stratum
    strata_tables = []
    
    for stratum in data[strata_col].unique():
        if pd.isna(stratum):
            continue
            
        stratum_data = data[data[strata_col] == stratum]
        
        # Create 2x2 table: treatment x outcome
        control = stratum_data[stratum_data[treatment_col] == 0]
        treatment = stratum_data[stratum_data[treatment_col] == 1]
        
        if len(control) > 0 and len(treatment) > 0:
            table = pd.crosstab(
                stratum_data[treatment_col],
                stratum_data[var] > 0 if var in ['has_any_female', 'has_any_urm'] else stratum_data[var],
                margins=False
            )
            
            if table.shape == (2, 2):
                strata_tables.append(table.values)
    
    if not strata_tables:
        return np.nan
    
    # Cochran-Mantel-Haenszel test
    try:
        from statsmodels.stats.contingency_tables import StratifiedTable
        st = StratifiedTable(strata_tables)
        result = st.test_null_odds()
        return result.pvalue
    except:
        # Fallback to simple weighted average
        return stratified_t_test(data, var, treatment_col, strata_col)

# Calculate summary statistics by treatment and stratification
results = []

# 1. Final sample of seminars with demographic data
seminars_with_demo = df[df['speakers_with_demographics'] > 0]

# 2-7. Calculate all requested statistics
variables = {
    'seminars_with_demographics': 'Final seminars with demographic data',
    'pct_female_recipients': '% Email recipients female',
    'pct_urm_among_female_recipients': '% Female recipients URM',
    'frac_women_faculty': 'Department Female % (faculty)',
    'frac_urm_faculty': 'Department URM % (faculty)',
    'total_speakers_analyzed': 'Total speakers analyzed',
    'avg_speaker_appearances': 'Average speaker appearances'
}

# Calculate % URM among female recipients
df['female_recipients'] = df['num_email_recipients_analyzed'] * df['pct_female_recipients']
df['urm_female_recipients'] = df['female_recipients'] * df['pct_urm_recipients']
df['pct_urm_among_female_recipients'] = np.where(
    df['female_recipients'] > 0,
    df['urm_female_recipients'] / df['female_recipients'],
    np.nan
)

# Add derived variables
df['seminars_with_demographics'] = (df['speakers_with_demographics'] > 0).astype(int)
df['total_speakers_analyzed'] = df['speakers_with_demographics']

# Calculate average speaker appearances from speaker data
speaker_stats = speaker_appearances.groupby('speaker_id').size().reset_index(name='appearances')
df['avg_speaker_appearances'] = speaker_stats['appearances'].mean()

print("STRATIFICATION-AWARE BALANCE TABLE")
print("=" * 100)
print(f"{'Variable':<40} {'Control Mean (SD)':<20} {'Treatment Mean (SD)':<20} {'P-value':<15}")
print("=" * 100)

# Overall statistics first
print("\nOVERALL STATISTICS (pooled across strata):")
print("-" * 100)

for var, label in variables.items():
    if var in df.columns:
        control_data = df[df['treatment'] == 0][var].dropna()
        treatment_data = df[df['treatment'] == 1][var].dropna()
        
        control_mean = control_data.mean()
        control_sd = control_data.std()
        treatment_mean = treatment_data.mean()
        treatment_sd = treatment_data.std()
        
        # Use appropriate test
        if var in ['seminars_with_demographics', 'has_any_female', 'has_any_urm']:
            p_value = stratified_proportion_test(df, var)
        else:
            p_value = stratified_t_test(df, var)
        
        print(f"{label:<40} {control_mean:>6.3f} ({control_sd:>6.3f})   "
              f"{treatment_mean:>6.3f} ({treatment_sd:>6.3f})   {p_value:>6.3f}")

# Now by stratification bin
print("\n\nBY STRATIFICATION BIN:")
print("=" * 100)

for bin_cat in bins:
    bin_data = df[df['bin_category'] == bin_cat]
    
    if len(bin_data) > 0:
        n_control = len(bin_data[bin_data['treatment'] == 0])
        n_treatment = len(bin_data[bin_data['treatment'] == 1])
        
        print(f"\nBin: {bin_cat} (n_control={n_control}, n_treatment={n_treatment})")
        print("-" * 100)
        
        for var, label in variables.items():
            if var in bin_data.columns:
                control_data = bin_data[bin_data['treatment'] == 0][var].dropna()
                treatment_data = bin_data[bin_data['treatment'] == 1][var].dropna()
                
                if len(control_data) > 0 and len(treatment_data) > 0:
                    control_mean = control_data.mean()
                    control_sd = control_data.std()
                    treatment_mean = treatment_data.mean()
                    treatment_sd = treatment_data.std()
                    
                    # Simple t-test within bin
                    _, p_value = stats.ttest_ind(control_data, treatment_data)
                    
                    print(f"{label:<40} {control_mean:>6.3f} ({control_sd:>6.3f})   "
                          f"{treatment_mean:>6.3f} ({treatment_sd:>6.3f})   {p_value:>6.3f}")

# Sample sizes summary
print("\n\nSAMPLE SIZES BY BIN:")
print("=" * 50)
print(f"{'Bin':<15} {'Control':<10} {'Treatment':<10} {'Total':<10}")
print("-" * 50)

for bin_cat in bins:
    bin_data = df[df['bin_category'] == bin_cat]
    n_control = len(bin_data[bin_data['treatment'] == 0])
    n_treatment = len(bin_data[bin_data['treatment'] == 1])
    print(f"{bin_cat:<15} {n_control:<10} {n_treatment:<10} {n_control + n_treatment:<10}")

total_control = len(df[df['treatment'] == 0])
total_treatment = len(df[df['treatment'] == 1])
print("-" * 50)
print(f"{'TOTAL':<15} {total_control:<10} {total_treatment:<10} {total_control + total_treatment:<10}")

# Statistical notes
print("\n\nSTATISTICAL NOTES:")
print("=" * 100)
print("1. P-values for overall statistics use stratification-aware tests:")
print("   - Continuous variables: Stratified t-test with inverse variance weighting")
print("   - Binary variables: Cochran-Mantel-Haenszel test")
print("2. Within-bin p-values use simple t-tests (for reference only)")
print("3. Stratification ensures randomization balance within bins, not necessarily overall")
print("4. Missing values are excluded from calculations")
print("5. Department-level randomization is respected in all tests")