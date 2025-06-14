import pandas as pd
import numpy as np

# Load the detailed recipient data
recipients = pd.read_csv('/mnt/c/Users/jcerv/Jose/search-costs/05_statistical_analysis/outputs/email_recipient_demographics_detailed.csv')

# Load the master data to get treatment assignments
master_data = pd.read_csv('/mnt/c/Users/jcerv/Jose/search-costs/05_statistical_analysis/outputs/master_analysis_dataset_final.csv')

print("Calculating % of Female Recipients that were URM")
print("="*80)

# First, let's understand the data structure
print(f"\nTotal email recipients analyzed: {len(recipients)}")
print(f"Female recipients: {recipients['is_female'].sum()}")
print(f"URM recipients: {recipients['is_urm'].sum()}")
print(f"Female AND URM recipients: {((recipients['is_female'] == 1) & (recipients['is_urm'] == 1)).sum()}")

# Calculate by department
dept_stats = recipients.groupby('department').agg({
    'is_female': ['sum', 'count'],
    'is_urm': 'sum'
}).reset_index()

dept_stats.columns = ['department', 'num_female', 'total_recipients', 'num_urm']

# Calculate female URM recipients by department
female_urm_by_dept = recipients[recipients['is_female'] == 1].groupby('department')['is_urm'].agg(['sum', 'count']).reset_index()
female_urm_by_dept.columns = ['department', 'num_female_urm', 'num_female_total']
female_urm_by_dept['pct_urm_among_female'] = female_urm_by_dept['num_female_urm'] / female_urm_by_dept['num_female_total']

# Merge with treatment assignment
dept_treatment = master_data[['department', 'treatment', 'bin_category']].drop_duplicates()
female_urm_stats = female_urm_by_dept.merge(dept_treatment, on='department', how='left')

# Calculate overall statistics
print("\n\nOVERALL STATISTICS:")
print("-"*80)

# Control departments
control_depts = female_urm_stats[female_urm_stats['treatment'] == 0]
control_female_total = control_depts['num_female_total'].sum()
control_female_urm = control_depts['num_female_urm'].sum()
control_pct = control_female_urm / control_female_total if control_female_total > 0 else 0

print(f"Control departments:")
print(f"  Total female recipients: {control_female_total}")
print(f"  Female URM recipients: {control_female_urm}")
print(f"  % of female recipients that are URM: {control_pct:.1%}")

# Treatment departments
treatment_depts = female_urm_stats[female_urm_stats['treatment'] == 1]
treatment_female_total = treatment_depts['num_female_total'].sum()
treatment_female_urm = treatment_depts['num_female_urm'].sum()
treatment_pct = treatment_female_urm / treatment_female_total if treatment_female_total > 0 else 0

print(f"\nTreatment departments:")
print(f"  Total female recipients: {treatment_female_total}")
print(f"  Female URM recipients: {treatment_female_urm}")
print(f"  % of female recipients that are URM: {treatment_pct:.1%}")

print(f"\nDifference (Treatment - Control): {(treatment_pct - control_pct):.1%}")

# Calculate department-level means (for comparison with simple average)
print("\n\nDEPARTMENT-LEVEL MEANS:")
print("-"*80)

# Only include departments with at least one female recipient
depts_with_female = female_urm_stats[female_urm_stats['num_female_total'] > 0]

control_dept_mean = depts_with_female[depts_with_female['treatment'] == 0]['pct_urm_among_female'].mean()
control_dept_sd = depts_with_female[depts_with_female['treatment'] == 0]['pct_urm_among_female'].std()

treatment_dept_mean = depts_with_female[depts_with_female['treatment'] == 1]['pct_urm_among_female'].mean()
treatment_dept_sd = depts_with_female[depts_with_female['treatment'] == 1]['pct_urm_among_female'].std()

print(f"Control: {control_dept_mean:.1%} (SD: {control_dept_sd:.1%})")
print(f"Treatment: {treatment_dept_mean:.1%} (SD: {treatment_dept_sd:.1%})")

# Save the department-level statistics
female_urm_stats.to_csv('/mnt/c/Users/jcerv/Jose/search-costs/05_statistical_analysis/outputs/female_urm_recipient_stats.csv', index=False)

print(f"\nSaved department-level statistics to: female_urm_recipient_stats.csv")

# Show some examples
print("\n\nEXAMPLES OF DEPARTMENTS WITH HIGH % FEMALE URM:")
print("-"*80)
high_female_urm = female_urm_stats[female_urm_stats['pct_urm_among_female'] > 0.3].sort_values('pct_urm_among_female', ascending=False)
for _, row in high_female_urm.head(10).iterrows():
    print(f"{row['department']:<60} {row['num_female_urm']:>3}/{row['num_female_total']:>3} = {row['pct_urm_among_female']:>5.1%} ({'treatment' if row['treatment'] == 1 else 'control'})")