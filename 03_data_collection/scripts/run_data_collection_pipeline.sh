#!/bin/bash
#
# SEARCH COSTS RCT - DATA COLLECTION PIPELINE
# Creates master-data-final.csv with all standardizations applied
#

set -e  # Exit on any error

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}======================================${NC}"
echo -e "${BLUE}SEARCH COSTS RCT - DATA COLLECTION${NC}"
echo -e "${BLUE}======================================${NC}"
echo "Started at: $(date)"
echo ""

# Check if we should update Spring data
UPDATE_SPRING=false
if [[ "$1" == "--update-spring" ]]; then
    UPDATE_SPRING=true
    echo -e "${GREEN}✓ Will update Spring data from Google Sheets${NC}"
fi

# Get the directory of this script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Step 1: Update Spring data if requested
if [ "$UPDATE_SPRING" = true ]; then
    echo -e "\n${BLUE}Step 1: Updating Spring data from Google Sheets...${NC}"
    poetry run python pull_spring_data.py
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ Spring data updated successfully${NC}"
    else
        echo -e "${RED}✗ Failed to update Spring data${NC}"
        exit 1
    fi
else
    echo -e "\n${BLUE}Step 1: Using existing Spring data (use --update-spring to refresh)${NC}"
fi

# Step 2: Run the main data processing pipeline
echo -e "\n${BLUE}Step 2: Processing and standardizing data...${NC}"
echo -e "${YELLOW}Note: Speaker enrichment is now enabled by default. Use --skip-enrichment to disable.${NC}"
poetry run python create_final_dataset.py

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Data processing completed successfully${NC}"
else
    echo -e "${RED}✗ Data processing failed${NC}"
    exit 1
fi

# Step 3: Validate the output
echo -e "\n${BLUE}Step 3: Validating final dataset...${NC}"
if [ -f "../processed/master-data-final.csv" ]; then
    # Get basic stats
    LINES=$(wc -l < ../processed/master-data-final.csv)
    SIZE=$(ls -lh ../processed/master-data-final.csv | awk '{print $5}')
    echo -e "${GREEN}✓ Output file created successfully${NC}"
    echo "  - File: ../processed/master-data-final.csv"
    echo "  - Size: $SIZE"
    echo "  - Rows: $LINES"
    
    # Check if summary exists
    if [ -f "../processed/final_dataset_summary.json" ]; then
        echo -e "\n${GREEN}✓ Summary statistics:${NC}"
        cat ../processed/final_dataset_summary.json | poetry run python -m json.tool
    fi
else
    echo -e "${RED}✗ Output file not found!${NC}"
    exit 1
fi

echo -e "\n${BLUE}======================================${NC}"
echo -e "${GREEN}✅ Pipeline completed successfully!${NC}"
echo -e "${BLUE}======================================${NC}"
echo "Completed at: $(date)"
echo ""
echo "Next steps:"
echo "1. Run demographic analysis: cd ../../pipeline && ./run_demographic_analysis.sh"
echo "2. Run statistical analysis: cd ../../pipeline && ./run_statistical_analysis.sh"