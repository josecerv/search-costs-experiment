import pandas as pd
import numpy as np
from scipy import stats

# Original seminar counts (from seminar_batch_mapping.csv)
original_control = 949
original_treatment = 932
original_total = 1881

# Seminars with demographic data (from master_analysis_dataset_final.csv)
demo_control = 846
demo_treatment = 809
demo_total = 1655

# Calculate coverage rates
coverage_control = demo_control / original_control
coverage_treatment = demo_treatment / original_treatment
coverage_overall = demo_total / original_total

print("DEMOGRAPHIC DATA COVERAGE ANALYSIS")
print("="*80)
print("\nOriginal seminar counts (before demographic analysis):")
print(f"  Control: {original_control}")
print(f"  Treatment: {original_treatment}")
print(f"  Total: {original_total}")

print("\nSeminars with demographic data:")
print(f"  Control: {demo_control}")
print(f"  Treatment: {demo_treatment}")
print(f"  Total: {demo_total}")

print("\nCOVERAGE RATES:")
print("-"*80)
print(f"Control:   {demo_control}/{original_control} = {coverage_control:.1%}")
print(f"Treatment: {demo_treatment}/{original_treatment} = {coverage_treatment:.1%}")
print(f"Overall:   {demo_total}/{original_total} = {coverage_overall:.1%}")

print(f"\nDifference in coverage rates: {(coverage_treatment - coverage_control)*100:.1f} percentage points")

# Test for difference in coverage rates using chi-square test
# Create contingency table
has_demo = [demo_control, demo_treatment]
no_demo = [original_control - demo_control, original_treatment - demo_treatment]
contingency_table = np.array([has_demo, no_demo])

# Chi-square test
chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table.T)

print(f"\nChi-square test for difference in coverage rates:")
print(f"  Chi-square statistic: {chi2:.3f}")
print(f"  P-value: {p_value:.4f}")

# Also calculate using proportions test
from statsmodels.stats.proportion import proportions_ztest

count = np.array([demo_control, demo_treatment])
nobs = np.array([original_control, original_treatment])

z_stat, p_value_z = proportions_ztest(count, nobs)
print(f"\nTwo-proportion z-test:")
print(f"  Z-statistic: {z_stat:.3f}")
print(f"  P-value: {p_value_z:.4f}")

# Calculate 95% confidence intervals for coverage rates
from statsmodels.stats.proportion import proportion_confint

ci_control = proportion_confint(demo_control, original_control, method='wilson')
ci_treatment = proportion_confint(demo_treatment, original_treatment, method='wilson')

print(f"\n95% Confidence Intervals for coverage rates:")
print(f"  Control:   {coverage_control:.1%} ({ci_control[0]:.1%}, {ci_control[1]:.1%})")
print(f"  Treatment: {coverage_treatment:.1%} ({ci_treatment[0]:.1%}, {ci_treatment[1]:.1%})")

print("\n" + "="*80)
print("INTERPRETATION:")
print("-"*80)
print(f"• {coverage_overall:.1%} of all seminars had speaker demographic data")
print(f"• Coverage rates are very similar between conditions ({coverage_control:.1%} vs {coverage_treatment:.1%})")
print(f"• The {abs(coverage_treatment - coverage_control)*100:.1f}pp difference is not statistically significant (p={p_value:.3f})")
print("• No evidence of differential data availability between treatment arms")
print("• High coverage rate (>85%) ensures results are representative")