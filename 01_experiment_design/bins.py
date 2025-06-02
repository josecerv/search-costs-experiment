import pandas as pd
import os

# --- Configuration ---
MASTER_DATA_INPUT = 'master-data-fall.csv'
RANDOMIZATION_DATA_INPUT = 'randomized_data.csv'
MASTER_DATA_OUTPUT = 'master-data-fall_with_bins.csv'
# --- End Configuration ---

print(f"--- Starting Script 1: Add Bin Categories to Master Data ---")

# --- Load Data ---
print(f"Loading master data: {MASTER_DATA_INPUT}")
try:
    # Use latin1 encoding based on previous experience with this file
    master_df = pd.read_csv(MASTER_DATA_INPUT, encoding='latin1')
    print(f"Loaded {len(master_df)} rows from master data.")
except FileNotFoundError:
    print(f"Error: Master data file not found at {MASTER_DATA_INPUT}")
    exit()
except Exception as e:
    print(f"Error loading master data: {e}")
    exit()

print(f"Loading randomization data: {RANDOMIZATION_DATA_INPUT}")
try:
    random_df = pd.read_csv(RANDOMIZATION_DATA_INPUT)
    # Select only necessary columns to avoid duplicating 'condition' etc.
    random_df = random_df[['department', 'bin_category']].copy()
    print(f"Loaded {len(random_df)} rows from randomization data.")
except FileNotFoundError:
    print(f"Error: Randomization data file not found at {RANDOMIZATION_DATA_INPUT}")
    exit()
except Exception as e:
    print(f"Error loading randomization data: {e}")
    exit()

# --- Prepare for Merge ---
# Create the 'department' key in the master data (University-Discipline)
if 'university' in master_df.columns and 'discipline' in master_df.columns:
    print("Creating 'department' key in master data (University-Discipline)...")
    master_df['department'] = master_df['university'] + '-' + master_df['discipline']
else:
    print("Error: Master data is missing 'university' or 'discipline' columns. Cannot create merge key.")
    exit()

# --- Perform Merge ---
print("Merging bin_category from randomization data into master data...")
initial_rows = len(master_df)
# Use left merge to keep all rows from master_df
merged_df = pd.merge(master_df, random_df, on='department', how='left')

if len(merged_df) != initial_rows:
    print("Warning: Number of rows changed during merge. Check merge keys.")

# --- Check Merge Results ---
missing_bins = merged_df['bin_category'].isnull().sum()
if missing_bins > 0:
    print(f"Warning: {missing_bins} rows in the master data did not have a matching 'department' in the randomization data.")
    print("These rows will have NaN for 'bin_category'. Example departments not matched:")
    print(merged_df[merged_df['bin_category'].isnull()]['department'].value_counts().head())
else:
    print("Merge successful. All master data rows seem to have a corresponding bin category.")

# Drop the temporary department key from the master data if desired (optional)
# merged_df = merged_df.drop(columns=['department'])

# --- Save Output ---
print(f"Saving updated master data to: {MASTER_DATA_OUTPUT}")
try:
    # Save using utf-8-sig for better Excel compatibility if needed, or just utf-8
    merged_df.to_csv(MASTER_DATA_OUTPUT, index=False, encoding='utf-8-sig')
    print("Successfully saved updated master data.")
except Exception as e:
    print(f"Error saving updated master data: {e}")

print(f"--- Script 1 Finished ---")

