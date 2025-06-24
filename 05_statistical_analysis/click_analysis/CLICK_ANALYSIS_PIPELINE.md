# Click Analysis Pipeline Documentation

## Overview

This directory contains the corrected click analysis pipeline that properly handles seminar names with commas and provides accurate click rates at the seminar level.

## Key Issue Resolved

Previous analyses incorrectly split seminar names at commas, creating ~1,600 phantom seminar references. For example, "Atomic, Molecular and Optical Seminar" was counted as 3 separate seminars. This has been fixed by using `email-list.csv` as the ground truth.

## Pipeline Steps

### 1. Generate Comprehensive Email-Seminar Mapping

The mapping file already exists at `comprehensive_email_seminar_mapping.csv` but can be regenerated if needed:

```bash
# From project root directory
python3 /path/to/comprehensive_correct_mapping.py
```

This script:
- Uses `/02_intervention_materials/email_campaigns/launch-prep/email-list.csv` as ground truth
- Properly preserves seminar names with commas
- Maps emails to seminars in the master dataset
- Handles department chair click propagation

### 2. Create Department-Level Click Statistics

To update the department-level data used by R analyses:

```bash
cd /05_statistical_analysis/scripts
python3 create_department_click_stats_corrected.py
```

This updates `email_clicks_from_bitly_cache.csv` with accurate department-level statistics.

### 3. Run Seminar-Level Click Analysis

```bash
cd /05_statistical_analysis/click_analysis
python3 analyze_seminar_clicks_corrected.py
```

This generates:
- `results.json` - Summary statistics
- `seminar_click_details.csv` - Individual seminar click data

## Key Files

### Input Files
- `/01_experiment_design/bitly_cache.json` - Raw click data from Bit.ly
- `/02_intervention_materials/email_campaigns/launch-prep/email-list.csv` - Ground truth seminar names
- `/02_intervention_materials/email_campaigns/email-launch.csv` - Email campaign data
- `/05_statistical_analysis/outputs/master_analysis_dataset.csv` - Master seminar dataset

### Output Files
- `comprehensive_email_seminar_mapping.csv` - Definitive email-to-seminar mapping
- `results.json` - Seminar-level click statistics
- `seminar_click_details.csv` - Individual seminar click status
- `click_statistics_by_condition.json` - Average clicks per email by condition

## Important Metrics

### Seminar-Level Click Rates (Correct)
- **Overall**: 54.4% (899/1,654 seminars)
- **Control**: 55.7% (471/846 seminars)
- **Treatment**: 53.0% (428/808 seminars)

### Department-Level Engagement (Different Metric)
- **Overall**: 57.3% of departments had any click
- **Control**: 56.5% of departments
- **Treatment**: 58.2% of departments

### Average Clicks per Email
- **Treatment**: 0.60 clicks/email
- **Control**: 0.52 clicks/email
- Difference not statistically significant (p=0.18)

## Common Pitfalls

1. **Don't split by commas** - Many seminar names contain commas
2. **Seminar vs Department rates** - These are different metrics
3. **Department chair propagation** - One click affects all seminars in department

## For R Analysis

The `speaker_counts_analysis.Rmd` file now correctly:
- Loads seminar-level click data from `click_analysis/seminar_click_details.csv`
- Reports actual seminar click rates (54.4%)
- Shows department-level rates as context

## Updating the Analysis

If you need to rerun the entire pipeline:

1. Ensure all input files are current
2. Run the comprehensive mapping script
3. Update department-level statistics
4. Run seminar-level analysis
5. Verify results in R Markdown output