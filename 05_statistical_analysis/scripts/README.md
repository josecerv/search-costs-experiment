# Statistical Analysis Scripts

This directory contains scripts for analyzing the impact of URM databases on seminar speaker selection in the Search Costs RCT.

## Overview

The main analysis examines whether departments selected speakers from the URM databases provided in the treatment condition, properly accounting for the peer university algorithm used in the experiment.

## Main Script

### `analyze_database_impact.py`
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
cd /mnt/c/Users/jcerv/Jose/search-costs/05_statistical_analysis
poetry run python scripts/analyze_database_impact.py
```

## Key Findings (as of June 5, 2025)

### Direct Database Usage
- **Female speakers**: Treatment 0.48% vs Control 0.00% (p=0.067)
- **URM speakers**: Treatment 3.12% vs Control 2.03% (53.8% increase, p=0.374)
- **Black speakers**: Treatment 2.51% vs Control 0.74% (240.1% increase, p=0.100)
- **Hispanic speakers**: No matches in either condition

### Key Insights
1. Direct database usage was minimal (~2-3% of relevant speakers)
2. Treatment departments showed higher usage for Black speakers (240% increase)
3. The main treatment effect likely worked through indirect mechanisms (awareness, signaling)

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