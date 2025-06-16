import pandas as pd

# Load the data
df = pd.read_csv('/mnt/c/Users/jcerv/Jose/search-costs/05_statistical_analysis/outputs/master_analysis_dataset_final.csv')

# Show sample with key columns
key_cols = ['department', 'condition', 'dept_ranking', 'general_ranking', 'bin_category', 
            'num_black', 'pct_black', 'num_junior_speakers', 'num_senior_speakers',
            'num_black_junior', 'num_black_senior']

print("=== SAMPLE DATA (first 10 rows) ===")
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 40)
print(df[key_cols].head(10))

print("\n=== BIN CATEGORY DISTRIBUTION ===")
print(df['bin_category'].value_counts().sort_index())

print("\n=== TREATMENT/CONTROL DISTRIBUTION ===")
print(df['condition'].value_counts())

print("\n=== DEPARTMENT RANKING SUMMARY STATS ===")
print(df['dept_ranking'].describe())

print("\n=== BLACK SPEAKERS BY SENIORITY ===")
print(f"Total seminars: {len(df)}")
print(f"Seminars with any Black junior speakers: {df['has_any_black_junior'].sum()} ({df['has_any_black_junior'].mean()*100:.1f}%)")
print(f"Seminars with any Black senior speakers: {df['has_any_black_senior'].sum()} ({df['has_any_black_senior'].mean()*100:.1f}%)")
print(f"Seminars with any Black speakers: {df['has_any_black'].sum()} ({df['has_any_black'].mean()*100:.1f}%)")

print("\n=== DISCIPLINE DISTRIBUTION ===")
print(df['discipline'].value_counts())