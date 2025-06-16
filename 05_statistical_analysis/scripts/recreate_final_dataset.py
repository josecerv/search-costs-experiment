#!/usr/bin/env python3
"""
Pipeline script to recreate master_analysis_dataset_final.csv from master_analysis_dataset.csv
This script runs the necessary steps in sequence to add all required columns.
"""

import os
import sys
import subprocess
import pandas as pd

def run_script(script_name, description):
    """Run a Python script and handle errors"""
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"Script: {script_name}")
    print('='*60)
    
    script_path = os.path.join(os.path.dirname(__file__), script_name)
    
    try:
        result = subprocess.run([sys.executable, script_path], 
                              capture_output=True, 
                              text=True, 
                              check=True)
        print("✓ Success!")
        if result.stdout:
            print("Output:", result.stdout[:500])  # First 500 chars
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error running {script_name}")
        print("Error output:", e.stderr)
        return False

def main():
    """Run the complete pipeline to create master_analysis_dataset_final.csv"""
    
    # Check if master_analysis_dataset.csv exists
    outputs_dir = os.path.join(os.path.dirname(__file__), "../outputs")
    master_csv = os.path.join(outputs_dir, "master_analysis_dataset.csv")
    
    if not os.path.exists(master_csv):
        print(f"Error: {master_csv} not found!")
        print("Please run create_analysis_dataset.py first to create the base dataset.")
        sys.exit(1)
    
    print(f"Found master_analysis_dataset.csv")
    df = pd.read_csv(master_csv)
    print(f"Base dataset shape: {df.shape}")
    
    # Pipeline steps
    steps = [
        # Step 1: Check if email recipient demographics exist, if not create them
        {
            "check_file": "email_recipient_demographics_by_dept.csv",
            "script": "analyze_email_recipients.py",
            "description": "Analyze email recipients and create demographics file",
            "required": True
        },
        # Step 2: Add email recipient variables
        {
            "script": "add_email_recipient_vars.py",
            "description": "Add email recipient demographic variables",
            "required": True
        },
        # Step 3: Add seniority subgroups
        {
            "script": "add_seniority_subgroups.py",
            "description": "Add junior/senior speaker subgroup variables",
            "required": True
        }
    ]
    
    # Run each step
    for step in steps:
        # Check if we need to run this step
        if "check_file" in step:
            check_path = os.path.join(outputs_dir, step["check_file"])
            if os.path.exists(check_path):
                print(f"\n✓ {step['check_file']} already exists, skipping {step['script']}")
                continue
        
        # Run the script
        success = run_script(step["script"], step["description"])
        
        if not success and step.get("required", False):
            print(f"\nError: Failed to run required step: {step['description']}")
            sys.exit(1)
    
    # Verify final output
    final_csv = os.path.join(outputs_dir, "master_analysis_dataset_final.csv")
    if os.path.exists(final_csv):
        df_final = pd.read_csv(final_csv)
        print(f"\n{'='*60}")
        print("✓ SUCCESS! master_analysis_dataset_final.csv created")
        print(f"Final dataset shape: {df_final.shape}")
        print(f"Added {len(df_final.columns) - len(df.columns)} columns")
        
        # Show some of the new columns
        new_cols = set(df_final.columns) - set(df.columns)
        print(f"\nNew columns added ({len(new_cols)} total):")
        for col in sorted(list(new_cols))[:10]:
            print(f"  - {col}")
        if len(new_cols) > 10:
            print(f"  ... and {len(new_cols) - 10} more")
    else:
        print("\nError: master_analysis_dataset_final.csv was not created!")
        sys.exit(1)

if __name__ == "__main__":
    main()