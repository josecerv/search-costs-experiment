#!/bin/bash
# Run the final unified pipeline for Search Costs RCT

set -e  # Exit on error

echo "======================================"
echo "SEARCH COSTS RCT - FINAL DATA PIPELINE"
echo "Academic Year: July 2024 - June 2025"
echo "======================================"
echo "Started at: $(date)"
echo ""

# Ensure we're in the right directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Step 1: Run unified data processor with date filtering
echo "Step 1: Running data processor with date filtering..."
if ! command -v poetry &> /dev/null; then
    python3 ../core/unified_data_processor.py
else
    poetry run python ../core/unified_data_processor.py
fi

if [ $? -ne 0 ]; then
    echo "❌ Data processing failed!"
    exit 1
fi

# Step 2: Apply standardization
echo ""
echo "Step 2: Applying rank and university standardization..."
if ! command -v poetry &> /dev/null; then
    python3 create_final_dataset.py
else
    poetry run python create_final_dataset.py
fi

echo ""
echo "Pipeline complete!"
echo ""
echo "Output file: ../processed/master-data-final.csv"
echo "Summary: ../processed/final_dataset_summary.json"
echo ""
echo "Completed at: $(date)"