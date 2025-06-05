#!/usr/bin/env python3
"""
Focused Analysis: Black Speaker Selection from URM Databases

This script specifically analyzes whether treatment departments were more likely
to select Black speakers FROM THE URM DATABASES compared to control departments.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json
from scipy import stats
from typing import Dict, List, Tuple

# Paths
data_dir = Path("/mnt/c/Users/jcerv/Jose/search-costs")
output_dir = Path("/mnt/c/Users/jcerv/Jose/search-costs/05_statistical_analysis/outputs")

print("="*80)
print("BLACK SPEAKER SELECTION FROM URM DATABASES - FOCUSED ANALYSIS")
print("="*80)

# 1. Load the department stats from our comprehensive analysis
dept_stats = pd.read_csv(output_dir / "database_effect_dept_stats.csv")
print(f"\nLoaded {len(dept_stats)} departments")

# 2. Load the detailed matches to understand Black speakers from database
all_matches = pd.read_csv(output_dir / "database_matches_all.csv")
black_matches = all_matches[all_matches['speaker_race'] == 'black']
print(f"Found {len(black_matches)} Black speaker matches from database")

# 3. Calculate focused statistics
treatment = dept_stats[dept_stats['treatment'] == 1]
control = dept_stats[dept_stats['treatment'] == 0]

print("\n" + "="*60)
print("MAIN QUESTION: Did treatment select more Black speakers")
print("specifically FROM THE URM DATABASE?")
print("="*60)

# A. Among ALL departments
print("\n1. BLACK SPEAKERS FROM DATABASE (All Departments)")
print("-"*60)

# Raw numbers
treat_black_from_db = treatment['black_from_db'].sum()
ctrl_black_from_db = control['black_from_db'].sum()
treat_total_speakers = treatment['total_speakers'].sum()
ctrl_total_speakers = control['total_speakers'].sum()

print(f"\nAbsolute numbers:")
print(f"  Treatment: {treat_black_from_db} Black speakers from database")
print(f"             (out of {treat_total_speakers} total speakers)")
print(f"  Control:   {ctrl_black_from_db} Black speakers from database")
print(f"             (out of {ctrl_total_speakers} total speakers)")

# As percentage of all speakers
treat_pct = treat_black_from_db / treat_total_speakers * 100
ctrl_pct = ctrl_black_from_db / ctrl_total_speakers * 100

print(f"\nAs % of all speakers:")
print(f"  Treatment: {treat_pct:.3f}%")
print(f"  Control:   {ctrl_pct:.3f}%")
print(f"  Difference: {treat_pct - ctrl_pct:.3f} percentage points")
print(f"  Relative increase: {(treat_pct - ctrl_pct) / ctrl_pct * 100:.1f}%")

# Statistical test
# Create binary indicator for each department
treatment['has_black_from_db'] = (treatment['black_from_db'] > 0).astype(int)
control['has_black_from_db'] = (control['black_from_db'] > 0).astype(int)

# Binary test
_, p_binary = stats.ttest_ind(treatment['has_black_from_db'], control['has_black_from_db'])
print(f"\nProbability of selecting ANY Black speaker from database:")
print(f"  Treatment: {treatment['has_black_from_db'].mean()*100:.1f}%")
print(f"  Control:   {control['has_black_from_db'].mean()*100:.1f}%")
print(f"  p-value: {p_binary:.4f}")

# B. Among departments with Black speakers
print("\n2. AMONG DEPARTMENTS WITH BLACK SPEAKERS")
print("-"*60)

treat_with_black = treatment[treatment['black_speakers'] > 0]
ctrl_with_black = control[control['black_speakers'] > 0]

print(f"\nDepartments with any Black speakers:")
print(f"  Treatment: {len(treat_with_black)} departments")
print(f"  Control:   {len(ctrl_with_black)} departments")

# What % of Black speakers came from database?
treat_black_total = treat_with_black['black_speakers'].sum()
ctrl_black_total = ctrl_with_black['black_speakers'].sum()
treat_black_db = treat_with_black['black_from_db'].sum()
ctrl_black_db = ctrl_with_black['black_from_db'].sum()

print(f"\nOf all Black speakers, % from database:")
print(f"  Treatment: {treat_black_db}/{treat_black_total} = {treat_black_db/treat_black_total*100:.1f}%")
print(f"  Control:   {ctrl_black_db}/{ctrl_black_total} = {ctrl_black_db/ctrl_black_total*100:.1f}%")

# C. By discipline
print("\n3. BLACK DATABASE SELECTION BY DISCIPLINE")
print("-"*60)

disciplines = dept_stats['discipline'].unique()
disc_results = []

for disc in disciplines:
    disc_treat = dept_stats[(dept_stats['discipline'] == disc) & (dept_stats['treatment'] == 1)]
    disc_ctrl = dept_stats[(dept_stats['discipline'] == disc) & (dept_stats['treatment'] == 0)]
    
    if len(disc_treat) > 5 and len(disc_ctrl) > 5:  # Need enough departments
        # Black from database
        treat_black_db_disc = disc_treat['black_from_db'].sum()
        ctrl_black_db_disc = disc_ctrl['black_from_db'].sum()
        
        # Total speakers
        treat_total_disc = disc_treat['total_speakers'].sum()
        ctrl_total_disc = disc_ctrl['total_speakers'].sum()
        
        # Binary: any department selecting Black from database
        treat_any = (disc_treat['black_from_db'] > 0).mean()
        ctrl_any = (disc_ctrl['black_from_db'] > 0).mean()
        
        # T-test on binary
        _, p_val = stats.ttest_ind(
            (disc_treat['black_from_db'] > 0).astype(int),
            (disc_ctrl['black_from_db'] > 0).astype(int)
        )
        
        disc_results.append({
            'discipline': disc,
            'treat_black_from_db': treat_black_db_disc,
            'ctrl_black_from_db': ctrl_black_db_disc,
            'treat_pct': treat_black_db_disc / treat_total_disc * 100 if treat_total_disc > 0 else 0,
            'ctrl_pct': ctrl_black_db_disc / ctrl_total_disc * 100 if ctrl_total_disc > 0 else 0,
            'treat_any_pct': treat_any * 100,
            'ctrl_any_pct': ctrl_any * 100,
            'p_value': p_val
        })

print("\nBlack speakers from database as % of all speakers:")
print("Discipline       | Treatment | Control | Diff (pp) | p-value")
print("-"*60)

for res in disc_results:
    diff = res['treat_pct'] - res['ctrl_pct']
    sig = "***" if res['p_value'] < 0.01 else "**" if res['p_value'] < 0.05 else "*" if res['p_value'] < 0.1 else ""
    print(f"{res['discipline']:16s} | {res['treat_pct']:8.3f}% | {res['ctrl_pct']:7.3f}% | "
          f"{diff:+9.3f} | {res['p_value']:.4f} {sig}")

print("\nProbability of ANY Black speaker from database:")
print("Discipline       | Treatment | Control | Diff (pp) | p-value")
print("-"*60)

for res in disc_results:
    diff = res['treat_any_pct'] - res['ctrl_any_pct']
    sig = "***" if res['p_value'] < 0.01 else "**" if res['p_value'] < 0.05 else "*" if res['p_value'] < 0.1 else ""
    print(f"{res['discipline']:16s} | {res['treat_any_pct']:8.1f}% | {res['ctrl_any_pct']:7.1f}% | "
          f"{diff:+9.1f} | {res['p_value']:.4f} {sig}")

# D. Semester analysis
print("\n4. BLACK DATABASE SELECTION BY SEMESTER")
print("-"*60)

# We need to go back to the original data for this
master_data = pd.read_csv(data_dir / "03_data_collection/processed/master-data-final.csv", low_memory=False)

# Count Black database matches by semester
fall_treat_black_db = 0
fall_ctrl_black_db = 0
spring_treat_black_db = 0
spring_ctrl_black_db = 0

for _, match in black_matches.iterrows():
    # Determine semester from date
    date_str = str(match['date'])
    is_fall = any(date_str.startswith(month) for month in ['8/', '9/', '10/', '11/', '12/'])
    
    if match['condition'] == 'treatment':
        if is_fall:
            fall_treat_black_db += 1
        else:
            spring_treat_black_db += 1
    else:
        if is_fall:
            fall_ctrl_black_db += 1
        else:
            spring_ctrl_black_db += 1

print(f"\nFall semester:")
print(f"  Treatment: {fall_treat_black_db} Black speakers from database")
print(f"  Control:   {fall_ctrl_black_db} Black speakers from database")

print(f"\nSpring semester:")
print(f"  Treatment: {spring_treat_black_db} Black speakers from database")
print(f"  Control:   {spring_ctrl_black_db} Black speakers from database")

# E. Which specific Black faculty were selected?
print("\n5. TOP BLACK FACULTY SELECTED FROM DATABASE")
print("-"*60)

# Count by faculty member
black_faculty_counts = black_matches.groupby(['urm_name', 'urm_university', 'condition']).size().reset_index(name='count')
black_faculty_counts = black_faculty_counts.sort_values('count', ascending=False)

print("\nMost frequently selected Black faculty from database:")
print("Name | University | Condition | Times Selected")
print("-"*60)

for _, fac in black_faculty_counts.head(10).iterrows():
    print(f"{fac['urm_name'][:30]:30s} | {fac['urm_university'][:25]:25s} | "
          f"{fac['condition']:9s} | {fac['count']}")

print("\n" + "="*60)
print("KEY FINDING:")
print("="*60)
print(f"""
The treatment did NOT significantly increase selection of Black speakers 
from the URM database:

- Treatment: {treat_black_from_db} Black speakers from database ({treat_pct:.3f}% of all speakers)
- Control:   {ctrl_black_from_db} Black speakers from database ({ctrl_pct:.3f}% of all speakers)
- Difference: {treat_black_from_db - ctrl_black_from_db} more speakers ({(treat_pct - ctrl_pct):.3f} pp)

This represents only {(treat_black_from_db - ctrl_black_from_db) / (treatment['black_speakers'].sum() - control['black_speakers'].sum()) * 100:.1f}% 
of the total Black speaker increase.

The main treatment effect worked through INDIRECT mechanisms, not direct 
selection from the provided database.
""")

# Save focused results
results = {
    'black_from_db_treatment': int(treat_black_from_db),
    'black_from_db_control': int(ctrl_black_from_db),
    'pct_speakers_black_from_db_treatment': float(treat_pct),
    'pct_speakers_black_from_db_control': float(ctrl_pct),
    'difference_pp': float(treat_pct - ctrl_pct),
    'p_value_binary': float(p_binary),
    'database_contribution_to_black_increase': float((treat_black_from_db - ctrl_black_from_db) / 
                                                    (treatment['black_speakers'].sum() - control['black_speakers'].sum()) * 100)
}

with open(output_dir / "black_database_selection_focused.json", 'w') as f:
    json.dump(results, f, indent=2)

print(f"\nResults saved to: {output_dir / 'black_database_selection_focused.json'}")