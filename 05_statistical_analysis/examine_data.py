import pandas as pd

# Load the data
df = pd.read_csv('/mnt/c/Users/jcerv/Jose/search-costs/05_statistical_analysis/outputs/master_analysis_dataset_final.csv')

print("Dataset shape:", df.shape)
print("\n=== DEPARTMENT RANK COLUMNS ===")
print("\ndept_ranking:")
print(f"  Type: {df['dept_ranking'].dtype}")
print(f"  Unique values: {df['dept_ranking'].nunique()}")
print(f"  Range: {df['dept_ranking'].min()} to {df['dept_ranking'].max()}")
print(f"  Missing values: {df['dept_ranking'].isna().sum()}")

print("\ngeneral_ranking:")
print(f"  Type: {df['general_ranking'].dtype}")
print(f"  Unique values: {df['general_ranking'].nunique()}")  
print(f"  Range: {df['general_ranking'].min()} to {df['general_ranking'].max()}")
print(f"  Missing values: {df['general_ranking'].isna().sum()}")

print("\nmissing_dept_rank:")
print(f"  Type: {df['missing_dept_rank'].dtype}")
print(f"  Unique values: {df['missing_dept_rank'].unique()}")

print("\nbin_category:")
print(f"  Type: {df['bin_category'].dtype}")
print(f"  Unique values: {df['bin_category'].unique()}")

print("\n=== BLACK SPEAKER VARIABLES ===")
black_cols = [col for col in df.columns if 'black' in col.lower()]
for col in black_cols:
    print(f"\n{col}:")
    print(f"  Type: {df[col].dtype}")
    if df[col].dtype in ['int64', 'float64']:
        print(f"  Range: {df[col].min()} to {df[col].max()}")
        print(f"  Mean: {df[col].mean():.3f}")

print("\n=== JUNIOR/SENIOR SPEAKER VARIABLES ===")
junior_senior_cols = [col for col in df.columns if 'junior' in col.lower() or 'senior' in col.lower()]
for col in junior_senior_cols:
    print(f"\n{col}:")
    print(f"  Type: {df[col].dtype}")
    if df[col].dtype in ['int64', 'float64']:
        print(f"  Range: {df[col].min()} to {df[col].max()}")
        print(f"  Mean: {df[col].mean():.3f}")

print("\n=== SAMPLE DATA (first 5 rows) ===")
# Show key columns
key_cols = ['department', 'condition', 'dept_ranking', 'general_ranking', 'bin_category', 
            'num_black', 'pct_black', 'num_junior_speakers', 'num_senior_speakers',
            'num_black_junior', 'num_black_senior', 'pct_black_junior', 'pct_black_senior']
print(df[key_cols].head())