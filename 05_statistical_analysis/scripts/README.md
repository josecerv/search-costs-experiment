# Statistical Analysis Scripts

This directory contains scripts for analyzing the impact of URM databases on seminar speaker selection in the Search Costs RCT.

## Overview

The main analysis examines whether departments selected speakers from the URM databases provided in the treatment condition, properly accounting for the peer university algorithm used in the experiment.

## Main Scripts

### `analyze_database_impact_final.py` (CURRENT)
**Clean analysis of database impact at the seminar level**

**What it does:**
For each seminar:
- **Denominator**: ALL speakers in the seminar (not just peer speakers)
- **Numerator**: Speakers who were in the tailored database shown to that department
  - This includes only URM faculty from the department's peer universities (±20 ranks, min 40)
  - The database was tailored - each department only saw faculty from their peer institutions

**Key metrics:**
- % of all seminar speakers who came from the database
- Count of speakers from the database by demographic (URM, Black, Hispanic, Female)
- Binary: whether the seminar had ANY speaker from the database

**Outputs:**
- `database_impact_final.csv` - Seminar-level results
- `database_impact_summary_final.csv` - Summary statistics with p-values
- `database_impact_final.json` - Complete report in JSON format

### `analyze_database_impact.py` (ORIGINAL)
Comprehensive analysis of database impact on speaker selection.

**What it does:**
- Implements the peer university selection algorithm (±20 ranks, expanding to 40 peers)
- Matches seminar speakers with database faculty using LLM results
- Calculates percentages, counts, and binary presence for each demographic group
- Compares treatment vs control conditions
- Generates detailed reports and summary statistics

**Key analyses:**
1. **% of speakers from database** - What percentage of female/URM/Black/Hispanic speakers from peer universities were from the database?
2. **Count of speakers from database** - Raw counts of matched speakers
3. **Binary presence** - Did the department select ANY speaker from the database?

**Outputs:**
- `database_impact_by_department.csv` - Department-level results
- `database_impact_summary.csv` - Summary statistics by condition and demographic
- `database_impact_treatment_effects.csv` - Treatment effect estimates and p-values
- `database_impact_analysis_report.md` - Comprehensive human-readable report
- `database_impact_analysis.json` - Machine-readable summary

## Running the Analysis

```bash
cd search-costs/05_statistical_analysis
poetry run python scripts/analyze_database_impact_final.py
```

## Key Findings (June 2025)

### Overall Statistics
- **Seminars analyzed**: 1,656 (811 treatment, 845 control)
- **Total speaker appearances**: 23,168
- **Total unique speakers**: 21,982

### Database Impact: % of ALL Speakers from Tailored Database

**All/URM Speakers:**
- Treatment: 0.131% ± 0.920%
- Control: 0.165% ± 1.947%
- No significant difference (p=0.659)

**Black Speakers:**
- Treatment: 0.076% ± 0.724%
- Control: 0.034% ± 0.571%
- 122% relative increase but not significant (p=0.193)

**Seminars with ANY Speaker from Database:**
- Treatment: 19/811 (2.3%)
- Control: 15/845 (1.8%)
- Not significant (p=0.489)

**Seminars with ANY Black Speaker from Database:**
- Treatment: 10/811 (1.2%)
- Control: 4/845 (0.5%)
- 2.6x higher but not quite significant (p=0.111)

### Key Insights
1. **Extremely low usage rates** - Only 0.13% of speakers came from the database
2. **Only 2.3% of seminars** had any speaker from the database
3. **Directional effect for Black speakers** - Treatment seminars 2.6x more likely to have a Black database speaker
4. **Total impact minimal** - Only 19 speakers out of 11,295 in treatment came from database

## Supporting Scripts

### `create_analysis_dataset.py`
Creates the master analysis dataset by merging all data sources. Run this if you need to refresh the master dataset.

### `llm_database_speaker_matching.py`
Uses GPT-4o to match database faculty with seminar speakers. Results are cached in `cache/llm_matching_cache.json`.

### `create_seminar_batch_mapping.py`
Maps seminars to email batches for treatment assignment tracking.

### `comprehensive_analysis.py`
Runs full regression analysis with clustered standard errors (for broader RCT analysis beyond database impact).

## Data Dependencies

The analysis requires:
1. **Speaker appearances data**: `04_demographic_analysis/outputs/speaker_appearances_analysis.csv`
2. **URM databases**: `02_intervention_materials/databases/*.csv`
3. **LLM matching results**: `outputs/llm_database_speaker_matches.csv`
4. **Faculty counts**: `06_archive/department faculty count.csv`

## Technical Notes

### Peer University Algorithm
The analysis replicates the exact algorithm used in the Qualtrics survey:
1. Start with universities ±20 ranks from the department
2. Expand symmetrically if needed to ensure at least 40 peer universities
3. Filter database and speakers to only those from peer universities

### Matching Methodology
- Uses LLM (GPT-4o) results that account for:
  - Name variations (nicknames, middle names, accents)
  - University moves between database creation and speaking
  - High-confidence matches only

### Statistical Tests
- Two-sample t-tests for treatment effects
- Department-level analysis (unit of randomization)
- Percentages calculated with appropriate denominators (peer university speakers only)