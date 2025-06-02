#!/bin/bash
# Optimized Data Preparation Script for Search Costs RCT
# Uses the new unified data processor with validation

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# Get the project root (two levels up from scripts directory)
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"

echo "=== Search Costs RCT - Optimized Data Preparation ==="
echo "Started at: $(date)"

# Check if environment is set up
if [ ! -f "${PROJECT_ROOT}/.env" ]; then
    echo "⚠️  Environment not configured. Running setup..."
    "${PROJECT_ROOT}/setup_env.sh"
fi

# Load environment
if [ -f "${PROJECT_ROOT}/.env" ]; then
    echo "Loading environment variables..."
    export $(cat "${PROJECT_ROOT}/.env" | grep -v '^#' | xargs)
fi

echo ""
echo "=== Step 1: Unified Data Processing ==="
cd "${PROJECT_ROOT}"  # Go to project root

# First merge Fall datasets
python3 03_data_collection/core/data_processor.py --mode merge
if [ $? -ne 0 ]; then
    echo "❌ Fall data processing failed"
    exit 1
fi

# Then merge Spring data to create full year dataset
echo ""
echo "=== Merging Spring Data ==="
python3 03_data_collection/core/data_processor.py --mode merge-spring
if [ $? -ne 0 ]; then
    echo "❌ Spring data merge failed"
    exit 1
fi

echo ""
echo "=== Step 2: Data Validation ==="
# First validate Fall data
echo "Validating Fall data..."
python3 03_data_collection/core/validator.py

# Then validate full year data
echo ""
echo "Validating Full Year data..."
python3 -c "
import sys
sys.path.append('03_data_collection')
from core.validator import DataValidator
from config.settings import Config
config = Config()
validator = DataValidator()
validator.validate_research_data(config.MASTER_DATA_FULL_YEAR)
"

if [ $? -ne 0 ]; then
    echo "❌ Data validation failed"
    exit 1
fi

echo ""
echo "=== Step 3: Check Database Status ==="
python3 04_demographic_analysis/scripts/demographic-analysis-optimized.py --mode status

echo ""
echo "=== Data Preparation Complete ==="
echo "Next steps:"
echo "1. Run demographic analysis: python3 demographic-analysis-optimized.py"
echo "2. Or run photos only: python3 demographic-analysis-optimized.py --mode photos"
echo "3. Or run names only: python3 demographic-analysis-optimized.py --mode names"
echo ""
echo "To force reprocessing of cached data:"
echo "python3 demographic-analysis-optimized.py --force-reprocess"

echo ""
echo "Preparation completed at: $(date)"