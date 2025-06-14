import pandas as pd
import numpy as np
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Load the data
master_data = pd.read_csv('/mnt/c/Users/jcerv/Jose/search-costs/05_statistical_analysis/outputs/master_analysis_dataset_final.csv')
speaker_appearances = pd.read_csv('/mnt/c/Users/jcerv/Jose/search-costs/04_demographic_analysis/outputs/speaker_appearances_analysis.csv')
email_demographics = pd.read_csv('/mnt/c/Users/jcerv/Jose/search-costs/05_statistical_analysis/outputs/email_recipient_demographics_by_dept.csv')

# Main dataframe
df = master_data.copy()

# Calculate % URM among female recipients properly
# This requires looking at the email demographics data
dept_female_urm = email_demographics.copy()

# Calculate the number of female recipients
dept_female_urm['num_female_recipients'] = dept_female_urm['num_email_recipients'] * dept_female_urm['pct_female_recipients']

# We need to calculate how many female recipients are URM
# Since we have total URM recipients and need to know what fraction are female
# We'll need to make an assumption or use available data

# If we don't have the exact breakdown, we can estimate based on the overall patterns
# For now, let's check what data we have
print("Email demographics columns:", dept_female_urm.columns.tolist())
print("\nSample of email demographics data:")
print(dept_female_urm[['department', 'num_email_recipients', 'num_female_recipients', 
                      'pct_female_recipients', 'num_urm_recipients', 'pct_urm_recipients']].head(10))

# For a proper calculation, we'd need the intersection of female AND URM
# Let's see if the master data has this information
print("\nMaster data columns related to recipients:")
recipient_cols = [col for col in df.columns if 'recipient' in col.lower()]
print(recipient_cols)

# Merge email demographics with main data
df = df.merge(dept_female_urm[['department', 'num_female_recipients']], 
              on='department', how='left')

# Calculate average speaker appearances per seminar
speaker_counts = speaker_appearances.groupby('speaker_id').size().reset_index(name='total_appearances')
seminar_avg = speaker_appearances.groupby('seminar_id').apply(
    lambda x: speaker_counts[speaker_counts['speaker_id'].isin(x['speaker_id'])]['total_appearances'].mean()
).reset_index(name='avg_speaker_appearances')

df = df.merge(seminar_avg, on='seminar_id', how='left')

print("\n" + "="*120)
print("CORRECTED SUMMARY STATISTICS WITH STRATIFICATION-AWARE P-VALUES")
print("="*120)
print()

# 1. Final sample of seminars with actual demographic data
seminars_control = len(df[(df['treatment'] == 0) & (df['speakers_with_demographics'] > 0)])
seminars_treatment = len(df[(df['treatment'] == 1) & (df['speakers_with_demographics'] > 0)])
print(f"1. Final sample of seminars with demographic data:")
print(f"   Control: {seminars_control}")
print(f"   Treatment: {seminars_treatment}")
print(f"   Total: {seminars_control + seminars_treatment}")
print()

# Create summary table
stats_data = []

# 2. % of Email recipients that were female
var = 'pct_female_recipients'
control = df[df['treatment'] == 0][var].dropna()
treatment = df[df['treatment'] == 1][var].dropna()
stats_data.append({
    'Statistic': '2. % Email recipients female',
    'Control Mean': f"{control.mean():.1%}",
    'Control SD': f"({control.std():.1%})",
    'Treatment Mean': f"{treatment.mean():.1%}",
    'Treatment SD': f"({treatment.std():.1%})",
    'Difference': f"{treatment.mean() - control.mean():.1%}",
    'P-value': ''
})

# 3. % of Female recipients that were URM
# This needs to be calculated as: (Female recipients who are URM) / (Total female recipients)
# We need to check if we have this data in the master dataset

# First, let's see what URM-related columns we have
urm_cols = [col for col in df.columns if 'urm' in col.lower()]
print("\nURM-related columns in master data:")
for col in urm_cols:
    print(f"  - {col}")

# The master data should have info about female URM recipients
# Let's calculate it properly based on what's available

# Check if we have the right columns
if 'pct_urm_recipients' in df.columns and 'pct_female_recipients' in df.columns:
    # We need to know what fraction of URMs are female
    # This might require additional data or assumptions
    
    # For now, let's note that we need this specific breakdown
    print("\nNOTE: To calculate '% of Female recipients that were URM', we need:")
    print("  - Number of female recipients who are URM")
    print("  - Total number of female recipients")
    print("  This requires intersection data (Female AND URM) which may need to be calculated from raw recipient data")

# Let's continue with available data
# 3. For now, we'll use overall URM % among recipients as a proxy
var = 'pct_urm_recipients'
control = df[df['treatment'] == 0][var].dropna()
treatment = df[df['treatment'] == 1][var].dropna()
stats_data.append({
    'Statistic': '3. % Recipients that were URM (overall)',
    'Control Mean': f"{control.mean():.1%}",
    'Control SD': f"({control.std():.1%})",
    'Treatment Mean': f"{treatment.mean():.1%}",
    'Treatment SD': f"({treatment.std():.1%})",
    'Difference': f"{treatment.mean() - control.mean():.1%}",
    'P-value': ''
})

# 4. Department Female % (faculty)
var = 'frac_women_faculty'
control = df[df['treatment'] == 0][var].dropna()
treatment = df[df['treatment'] == 1][var].dropna()
stats_data.append({
    'Statistic': '4. Department Female % (faculty)',
    'Control Mean': f"{control.mean():.1%}",
    'Control SD': f"({control.std():.1%})",
    'Treatment Mean': f"{treatment.mean():.1%}",
    'Treatment SD': f"({treatment.std():.1%})",
    'Difference': f"{treatment.mean() - control.mean():.1%}",
    'P-value': ''
})

# 5. Department URM % (faculty)
var = 'frac_urm_faculty'
control = df[df['treatment'] == 0][var].dropna()
treatment = df[df['treatment'] == 1][var].dropna()
stats_data.append({
    'Statistic': '5. Department URM % (faculty)',
    'Control Mean': f"{control.mean():.1%}",
    'Control SD': f"({control.std():.1%})",
    'Treatment Mean': f"{treatment.mean():.1%}",
    'Treatment SD': f"({treatment.std():.1%})",
    'Difference': f"{treatment.mean() - control.mean():.1%}",
    'P-value': ''
})

# 6. Total Speakers analyzed
var = 'speakers_with_demographics'
control = df[df['treatment'] == 0][var].dropna()
treatment = df[df['treatment'] == 1][var].dropna()
stats_data.append({
    'Statistic': '6. Total speakers analyzed',
    'Control Mean': f"{control.sum():.0f}",
    'Control SD': f"(mean/sem: {control.mean():.1f}/{control.std()/np.sqrt(len(control)):.1f})",
    'Treatment Mean': f"{treatment.sum():.0f}",
    'Treatment SD': f"(mean/sem: {treatment.mean():.1f}/{treatment.std()/np.sqrt(len(treatment)):.1f})",
    'Difference': f"{treatment.sum() - control.sum():.0f}",
    'P-value': ''
})

# 7. Average speaker appearances
var = 'avg_speaker_appearances'
control = df[df['treatment'] == 0][var].dropna()
treatment = df[df['treatment'] == 1][var].dropna()
stats_data.append({
    'Statistic': '7. Average speaker appearances',
    'Control Mean': f"{control.mean():.2f}",
    'Control SD': f"({control.std():.2f})",
    'Treatment Mean': f"{treatment.mean():.2f}",
    'Treatment SD': f"({treatment.std():.2f})",
    'Difference': f"{treatment.mean() - control.mean():.3f}",
    'P-value': ''
})

# Print summary table
stats_df = pd.DataFrame(stats_data)
print("\nSUMMARY TABLE:")
print("-" * 120)
for _, row in stats_df.iterrows():
    print(f"{row['Statistic']:<40} {row['Control Mean']:>12} {row['Control SD']:>12} {row['Treatment Mean']:>12} {row['Treatment SD']:>12} {row['Difference']:>10}")

# Calculate stratified p-values
print("\n\nSTRATIFIED P-VALUES (accounting for randomization within bins):")
print("-" * 80)

key_vars = {
    'pct_female_recipients': '% Email recipients female',
    'pct_urm_recipients': '% Recipients that were URM',
    'frac_women_faculty': 'Department Female % (faculty)',
    'frac_urm_faculty': 'Department URM % (faculty)',
    'speakers_with_demographics': 'Total speakers per seminar',
    'avg_speaker_appearances': 'Average speaker appearances'
}

for var, label in key_vars.items():
    if var in df.columns:
        # Remove missing values
        clean_df = df[[var, 'treatment', 'bin_category']].dropna()
        if len(clean_df) > 10:
            # Use simple t-test within strata approach
            strata_ps = []
            strata_weights = []
            
            for bin_cat in clean_df['bin_category'].unique():
                bin_data = clean_df[clean_df['bin_category'] == bin_cat]
                if len(bin_data) > 5:
                    control = bin_data[bin_data['treatment'] == 0][var]
                    treatment = bin_data[bin_data['treatment'] == 1][var]
                    if len(control) > 1 and len(treatment) > 1:
                        _, p = stats.ttest_ind(control, treatment)
                        strata_ps.append(p)
                        strata_weights.append(len(bin_data))
            
            # Weighted average p-value
            if strata_ps:
                weights = np.array(strata_weights) / sum(strata_weights)
                combined_p = np.average(strata_ps, weights=weights)
                print(f"{label:<40} p = {combined_p:.4f}")

print("\n\nIMPORTANT NOTE:")
print("-" * 80)
print("The statistic '% of Female recipients that were URM' requires data on the intersection")
print("of female AND URM status among email recipients. This would need to be calculated from")
print("the raw recipient-level data, not just department-level aggregates.")
print("\nCurrently showing overall URM % among all recipients as available metric.")