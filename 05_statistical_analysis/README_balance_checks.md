# Balance Checks and Summary Statistics

This directory contains the final consolidated scripts for balance checks and summary statistics for the Search Costs RCT.

## Main Scripts

### 1. `balance_checks_final.py`
**Purpose**: Comprehensive balance checks with stratification-aware p-values

**Features**:
- Coverage analysis (% of seminars with demographic data)
- Stratification-aware balance tests using regression with fixed effects
- Cohen's d effect sizes for practical significance
- Joint balance tests (Hotelling's T-squared)
- Within-bin balance checks
- Multiple testing corrections

**Usage**:
```bash
python3 balance_checks_final.py
```

**Output**: 
- Console report with all balance statistics
- `outputs/balance_checks_results.xlsx` with detailed results

### 2. `comprehensive_summary_statistics.py`
**Purpose**: Additional helpful summary statistics beyond balance checks

**Features**:
- Discipline distribution across treatment arms
- Temporal distribution (Fall vs Spring seminars)
- Speaker diversity metrics (including Gini coefficients)
- Department characteristics summary
- LaTeX table generation for papers

**Usage**:
```bash
python3 comprehensive_summary_statistics.py
```

**Output**:
- Console report with all statistics
- `outputs/comprehensive_summary_statistics.xlsx` with detailed results
- `outputs/latex_tables/` directory with formatted tables

## Key Findings

### Coverage Rates
- Control: 846/949 seminars (89.1%)
- Treatment: 809/932 seminars (86.8%)
- No significant difference in coverage (p = 0.118)

### Balance Assessment
- Most variables show small standardized differences (<0.3 SD)
- Stratification successfully balanced randomization within bins
- No individual variable shows significant imbalance after accounting for stratification

### Additional Statistics
- **Discipline Distribution**: Well-balanced across all 5 disciplines
- **Temporal Coverage**: Similar Fall/Spring distribution between arms
- **Speaker Diversity**: 
  - ~76% of seminars have at least one female speaker
  - ~54% of seminars have at least one URM speaker
  - Gini coefficients suggest moderate concentration of diversity

## Archived Scripts
Previous iterations of balance check scripts have been moved to `archive_balance_checks/` for reference.

## Dependencies
- pandas, numpy, scipy
- statsmodels (for regression-based tests)
- openpyxl (for Excel output)

All dependencies are managed via Poetry in the project's `pyproject.toml`.