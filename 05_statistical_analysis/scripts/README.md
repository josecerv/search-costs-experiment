# Statistical Analysis Scripts

This directory contains the core scripts for the search cost study statistical analysis.

## Main Scripts

### Core Analysis Scripts

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

### Database Matching Scripts

4. **llm_database_speaker_matching.py**
   - Uses GPT-4o to match URM database faculty to seminar speakers
   - Handles name variations, middle names, and university moves
   - Caches results for efficiency
   - Output: `llm_database_speaker_matches.csv` with all 550 faculty match results

5. **analyze_peer_denominators.py**
   - Analyzes database usage with correct denominators (peer university speakers)
   - Implements the Qualtrics peer selection algorithm (40+ universities, 20+ URM faculty)
   - Calculates treatment effects for database usage
   - Output: `peer_database_usage_correct_denominator.csv`

### Legacy Database Analysis Scripts

6. **analyze_database_treatment_effect.py**
   - Earlier analysis of database treatment effects
   - Uses simpler matching approach

7. **analyze_black_database_selection.py**
   - Analyzes Black speaker selection from databases
   - Pre-LLM matching approach

8. **create_database_speaker_match_report.py**
   - Creates detailed reports on database-speaker matches
   - Useful for validation and debugging

### Utility Scripts

9. **show_dataset_structure.py**
   - Utility script to display the structure of the master analysis dataset
   - Shows all variable names and categories
   - Useful for understanding the data structure

## Running the Analysis

### Standard Analysis Pipeline

```bash
# From the scripts directory
python create_seminar_batch_mapping.py
python create_analysis_dataset.py
python comprehensive_analysis.py
```

### Database Matching Analysis

```bash
# Run LLM-based matching (takes ~30 minutes)
python llm_database_speaker_matching.py

# Analyze results with peer denominators
python analyze_peer_denominators.py
```

## Output Files

All outputs are saved to `../outputs/`:

### Core Analysis Outputs
- `master_analysis_dataset.csv` - Complete dataset for analysis
- `primary_results_summary.csv` - Main regression results
- `regression_summary_final.csv` - Detailed regression tables
- `semester_analysis_summary_final.csv` - Results by semester
- `discipline_analysis_summary_final.csv` - Results by discipline
- `comprehensive_results_final.json` - Complete results in JSON format

### Database Matching Outputs
- `llm_database_speaker_matches.csv` - All 550 faculty with match results
- `llm_matching_analysis.json` - Summary statistics
- `peer_database_usage_correct_denominator.csv` - Department-level usage with peer denominators
- `peer_denominator_analysis_summary.json` - Treatment effect analysis
- `llm_race_mismatches.csv` - Cases where database and speaker demographics differ