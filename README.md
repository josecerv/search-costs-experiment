# Search Costs Research Project

## Directory Structure

```
search-costs/
│
├── 01_experiment_design/        # Experimental design and randomization
│   ├── bins.py                  # Stratification logic
│   ├── pre-registration.txt     # Study pre-registration
│   └── randomized_data.csv      # Randomized treatment assignments
│
├── 02_intervention_materials/   # Study materials and databases
│   ├── databases/               # Discipline-specific faculty databases
│   └── email_campaigns/         # Campaign materials and tracking
│
├── 03_data_collection/          # Data processing pipeline
│   ├── config/                  # Configuration settings
│   ├── core/                    # Core processing modules
│   ├── processed/               # Clean, processed datasets
│   ├── raw/                     # Original data files
│   └── scripts/                 # Data processing scripts
│
├── 04_demographic_analysis/     # Demographic analysis tools
│   ├── core/                    # Analysis modules
│   ├── outputs/                 # Analysis results
│   ├── scripts/                 # Analysis execution scripts
│   └── speaker_photos/          # Speaker photo database
│
├── 05_statistical_analysis/     # Statistical analysis
│   ├── outputs/                 # Statistical results
│   └── scripts/                 # R and Python analysis scripts
│
├── 06_archive/                  # Archived analyses and backups
│
└── pipeline/                    # Master pipeline orchestration
    ├── run_complete_analysis.sh # Full pipeline execution
    ├── run_demographic_analysis.sh
    └── run_statistical_analysis.sh
```