# Click Analysis Documentation

## Overview

This directory contains the **corrected** click analysis for the academic seminar diversity intervention experiment. The analysis properly tracks which seminars had their database links clicked, using `email-list.csv` as the ground truth to avoid comma-splitting errors.

## Key Correction

Previous analyses incorrectly split seminar names containing commas (e.g., "Atomic, Molecular and Optical Seminar" was treated as 3 separate seminars). This created ~1,600 phantom seminar references and severely distorted the results. The corrected analysis preserves seminar names intact.

## Files

### Analysis Script
- `analyze_seminar_clicks_corrected.py` - Corrected analysis that:
  - Uses the comprehensive mapping from `email-list.csv`
  - Properly handles comma-containing seminar names
  - Avoids double-counting clicks
  - Propagates department chair clicks to all department seminars

### Output Files
- `results.json` - Summary statistics:
  - Overall click rate: **54.4%** (899/1,654 seminars)
  - Treatment: **53.0%** clicked
  - Control: **55.7%** clicked (control outperformed treatment)
  - Total Bit.ly clicks: 892

- `seminar_click_details.csv` - Seminar-level data with:
  - Seminar ID, university, discipline
  - Treatment assignment (0/1)
  - Click status (0/1)
  - Number of click sources

## Key Findings

1. **Control group performed better** - 55.7% vs 53.0% for treatment (2.7 percentage point difference)

2. **Department chairs drove engagement** - 80.3% of clicked seminars were reached through department chair emails

3. **High coverage achieved** - 99.9% of seminars successfully mapped to emails

4. **Click statistics by condition**:
   - Treatment: 0.60 average clicks per email (1.75 among clickers)
   - Control: 0.52 average clicks per email (1.61 among clickers)
   - Difference not statistically significant (p=0.18)

## Data Sources

The analysis relies on:
- `/comprehensive_email_seminar_mapping.csv` - Definitive email-to-seminar mapping
- `/02_intervention_materials/email_campaigns/launch-prep/email-list.csv` - Ground truth for seminar names
- `/01_experiment_design/bitly_cache.json` - Raw click data from Bit.ly
- `/05_statistical_analysis/outputs/master_analysis_dataset.csv` - Master seminar dataset

## Running the Analysis

```bash
python3 analyze_seminar_clicks_corrected.py
```

This will regenerate `results.json` and `seminar_click_details.csv` with the latest data.