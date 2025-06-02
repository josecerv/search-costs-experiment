#!/bin/bash
# Spring Data Integration Script for Search Costs RCT
# Pulls Spring data from Google Sheets and integrates with existing pipeline

echo "========================================"
echo "Search Costs RCT - Spring Data Integration"
echo "========================================"
echo "Started at: $(date)"
echo ""

# Set error handling
set -e

# Check environment setup
echo "=== Environment Check ==="
if [ ! -f "../../.env" ]; then
    echo "⚠️  Environment not configured. Please run:"
    echo "cd ../.."
    echo "./setup_env.sh"
    exit 1
fi

# Load environment
export $(cat ../../.env | grep -v '^#' | xargs)

# Check Google Sheets API configuration
if [ -z "$GOOGLE_SHEETS_API_KEY" ] && [ -z "$GOOGLE_SERVICE_ACCOUNT_FILE" ]; then
    echo "❌ Google Sheets API not configured"
    echo "Please configure one of the following in .env:"
    echo "1. GOOGLE_SHEETS_API_KEY=your_api_key"
    echo "2. GOOGLE_SERVICE_ACCOUNT_FILE=path/to/service-account.json"
    echo ""
    echo "For setup instructions:"
    echo "https://developers.google.com/sheets/api/quickstart/python"
    exit 1
fi

echo "✅ Environment configured"
echo ""

# Step 1: Pull Spring Data from Google Sheets
echo "=== Step 1: Pulling Spring Data ==="

# Default Google Sheets URL (your Spring '25 Seminars sheet)
SPRING_SHEET_URL="https://docs.google.com/spreadsheets/d/1k6xDRMJkYGaX0cbXZ3cyJeEUMYJSs6fMIQEn-T--3QQ/edit?gid=1686776172#gid=1686776172"
SPRING_SHEET_NAME="Spring '25 Seminars"

echo "Pulling data from Google Sheets..."
echo "Sheet: $SPRING_SHEET_NAME"

python3 pull_spring_data.py \
    --url "$SPRING_SHEET_URL" \
    --sheet-name "$SPRING_SHEET_NAME"

if [ $? -ne 0 ]; then
    echo "❌ Failed to pull Spring data"
    exit 1
fi

echo "✅ Spring data pulled successfully"
echo ""

# Step 2: Merge Spring data with Fall data
echo "=== Step 2: Merging Fall and Spring Data ==="

cd ../core
python3 data_processor.py --mode merge-spring

if [ $? -ne 0 ]; then
    echo "❌ Failed to merge Spring data"
    exit 1
fi

echo "✅ Spring data merged successfully"
echo ""

# Step 3: Validate the combined dataset
echo "=== Step 3: Validating Combined Dataset ==="

python3 validator.py --file ../processed/master-data-full-year.csv

if [ $? -ne 0 ]; then
    echo "⚠️  Validation warnings found (check details above)"
else
    echo "✅ Validation passed"
fi

echo ""

# Step 4: Update demographic analysis with new speakers
echo "=== Step 4: Demographic Analysis Status ==="

cd ../../04_demographic_analysis/scripts
python3 demographic-analysis-optimized.py --mode status

echo ""
echo "Next steps to analyze Spring speakers:"
echo "1. Run demographic analysis on full year data:"
echo "   python3 demographic-analysis-optimized.py --data-file ../../03_data_collection/processed/master-data-full-year.csv"
echo ""
echo "2. Or run selective analysis:"
echo "   python3 demographic-analysis-optimized.py --mode photos"
echo "   python3 demographic-analysis-optimized.py --mode names"
echo ""

# Summary
echo ""
echo "========================================"
echo "SPRING INTEGRATION SUMMARY"
echo "========================================"

# Get file sizes and row counts
FALL_FILE="../../../03_data_collection/processed/master-data-fall-complete.csv"
SPRING_FILE="../../../03_data_collection/raw/master-data-spring.csv"
FULL_YEAR_FILE="../../../03_data_collection/processed/master-data-full-year.csv"

if [ -f "$FALL_FILE" ]; then
    FALL_ROWS=$(tail -n +2 "$FALL_FILE" | wc -l)
    echo "📊 Fall seminars: $FALL_ROWS"
fi

if [ -f "$SPRING_FILE" ]; then
    SPRING_ROWS=$(tail -n +2 "$SPRING_FILE" | wc -l)
    echo "📊 Spring seminars: $SPRING_ROWS"
fi

if [ -f "$FULL_YEAR_FILE" ]; then
    TOTAL_ROWS=$(tail -n +2 "$FULL_YEAR_FILE" | wc -l)
    echo "📊 Total seminars: $TOTAL_ROWS"
fi

echo ""
echo "🎉 Spring integration complete!"
echo ""
echo "Key files created:"
echo "✅ Raw Spring data: 03_data_collection/raw/master-data-spring.csv"
echo "✅ Combined dataset: 03_data_collection/processed/master-data-full-year.csv"
echo ""
echo "Benefits of the optimized pipeline:"
echo "⚡ Only NEW speakers will be analyzed (huge cost savings!)"
echo "🔄 Existing Fall speaker analysis results are preserved"
echo "📊 Smart deduplication prevents duplicate analysis"
echo ""
echo "Integration completed at: $(date)"