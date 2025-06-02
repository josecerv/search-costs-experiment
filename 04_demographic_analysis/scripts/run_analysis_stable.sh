#!/bin/bash
# Run demographic analysis using the stable deepface environment

# Ensure we're in the right directory
cd /mnt/c/Users/jcerv/Jose/search-costs

# Activate the stable environment
source deepface_stable/bin/activate

# Set environment variables to ensure stability
export TF_CPP_MIN_LOG_LEVEL=3
export TF_ENABLE_ONEDNN_OPTS=0
export CUDA_VISIBLE_DEVICES=-1

# Navigate to the analysis directory
cd 04_demographic_analysis/scripts

# Run the analysis
echo "Starting demographic analysis with stable DeepFace environment..."
python3 run_analysis.py "$@"
