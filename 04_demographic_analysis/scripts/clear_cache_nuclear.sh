#!/bin/bash

# Script to create timestamped backup and clear cache/outputs directories
# This forces a fresh analysis by removing all cached CSV files

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ANALYSIS_DIR="$(dirname "$SCRIPT_DIR")"

# Create timestamp for backup directory
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_DIR="${ANALYSIS_DIR}/backups/backup_${TIMESTAMP}"

# Create backup directory
echo "Creating backup directory: ${BACKUP_DIR}"
mkdir -p "${BACKUP_DIR}"
mkdir -p "${BACKUP_DIR}/cache"
mkdir -p "${BACKUP_DIR}/outputs"

# Backup cache CSV files
echo ""
echo "Backing up cache files..."
CACHE_COUNT=0
if [ -d "${ANALYSIS_DIR}/cache" ]; then
    for file in "${ANALYSIS_DIR}/cache"/*.csv; do
        if [ -f "$file" ]; then
            echo "  - Backing up: $(basename "$file")"
            mv "$file" "${BACKUP_DIR}/cache/"
            ((CACHE_COUNT++))
        fi
    done
fi

if [ $CACHE_COUNT -eq 0 ]; then
    echo "  No cache CSV files found to backup"
else
    echo "  Backed up $CACHE_COUNT cache files"
fi

# Backup outputs CSV files
echo ""
echo "Backing up output files..."
OUTPUT_COUNT=0
if [ -d "${ANALYSIS_DIR}/outputs" ]; then
    for file in "${ANALYSIS_DIR}/outputs"/*.csv; do
        if [ -f "$file" ]; then
            echo "  - Backing up: $(basename "$file")"
            mv "$file" "${BACKUP_DIR}/outputs/"
            ((OUTPUT_COUNT++))
        fi
    done
fi

if [ $OUTPUT_COUNT -eq 0 ]; then
    echo "  No output CSV files found to backup"
else
    echo "  Backed up $OUTPUT_COUNT output files"
fi

# Summary
echo ""
echo "========================================="
echo "CACHE CLEAR COMPLETE"
echo "========================================="
echo "Backup location: ${BACKUP_DIR}"
echo "Files backed up:"
echo "  - Cache files: $CACHE_COUNT"
echo "  - Output files: $OUTPUT_COUNT"
echo "  - Total files: $((CACHE_COUNT + OUTPUT_COUNT))"
echo ""
echo "Cache and outputs directories are now clear."
echo "Next analysis run will start fresh."
echo "========================================="

# Remove empty backup directories if nothing was backed up
if [ $CACHE_COUNT -eq 0 ] && [ $OUTPUT_COUNT -eq 0 ]; then
    echo ""
    echo "No files were backed up. Removing empty backup directory..."
    rm -rf "${BACKUP_DIR}"
fi