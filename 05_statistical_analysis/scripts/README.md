# Statistical Analysis Scripts

This directory contains the core scripts for the search cost study statistical analysis.

## Main Scripts

1. **comprehensive_analysis.py**
   - Main analysis script that runs all pre-registered analyses
   - Uses the pre-created master analysis dataset
   - Generates regression tables and summary statistics
   - Handles primary outcomes, semester analysis, discipline breakdowns, and additional demographics

2. **create_analysis_dataset.py**
   - Creates the master analysis dataset used by comprehensive_analysis.py
   - Merges data from multiple sources (seminars, demographics, controls)
   - Calculates outcome variables and prepares all control variables
   - Generates both full-year and semester-specific outcomes

3. **create_seminar_batch_mapping.py**
   - Creates the mapping between seminars and email campaign batches
   - Essential for batch fixed effects in regression models
   - Must be run before create_analysis_dataset.py

4. **show_dataset_structure.py**
   - Utility script to display the structure of the master analysis dataset
   - Shows all variable names and categories
   - Useful for understanding the data structure

## Running the Analysis

To run the complete analysis pipeline:

```bash
# From the scripts directory
python create_seminar_batch_mapping.py
python create_analysis_dataset.py
python comprehensive_analysis.py
```

## Output Files

All outputs are saved to `../outputs/`:
- `master_analysis_dataset.csv` - Complete dataset for analysis
- `primary_results_summary.csv` - Main regression results
- `regression_summary_final.csv` - Detailed regression tables
- `semester_analysis_summary_final.csv` - Results by semester
- `discipline_analysis_summary_final.csv` - Results by discipline
- `comprehensive_results_final.json` - Complete results in JSON format