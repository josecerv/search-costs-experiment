#!/usr/bin/env python3
"""
Create Final Dataset for Search Costs RCT
Single pipeline that merges, cleans, and standardizes data
Output: ONE clean file (master-data-final.csv)
"""

import sys
import asyncio
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import logging
from dotenv import load_dotenv
import os

# Load environment variables
env_path = Path(__file__).parent.parent.parent / '.env'
if env_path.exists():
    load_dotenv(env_path)

# Add paths
sys.path.append(str(Path(__file__).parent / ".."))
sys.path.append(str(Path(__file__).parent / "../.."))
from core.unified_data_processor import UnifiedDataProcessor
from config.settings import config
from core.normalization import generate_speaker_id

# Import standardizers
sys.path.append(str(Path(__file__).parent))
from standardize_academic_ranks import RankStandardizer
from standardize_universities import UniversityStandardizer

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


async def standardize_data(df):
    """Apply rank and university standardization to the dataframe"""
    
    logger.info("=== Starting Standardization ===")
    
    # Initialize standardizers
    rank_standardizer = RankStandardizer()
    university_standardizer = UniversityStandardizer()
    
    # 1. Standardize academic ranks
    logger.info("Standardizing academic ranks...")
    rank_columns = [col for col in df.columns if col.startswith('rank_') and col.endswith(('_1', '_2', '_3', '_4', '_5', '_6', '_7', '_8', '_9', '_10'))]
    rank_columns.extend([col for col in df.columns if col.startswith('rank_') and col.split('_')[-1].isdigit()])
    
    all_ranks = []
    for col in rank_columns:
        ranks = df[col].dropna().astype(str).unique()
        all_ranks.extend(ranks)
    
    unique_ranks = list(set(all_ranks))
    logger.info(f"Found {len(unique_ranks)} unique ranks to standardize")
    
    # Get standardized mappings
    rank_mapping = await rank_standardizer.standardize_ranks_batch(unique_ranks)
    
    # Apply rank standardization
    for col in rank_columns:
        standardized_col = f'{col}_standardized'
        df[standardized_col] = df[col].astype(str).map(rank_mapping).fillna('non-academic')
    
    # 2. Standardize universities
    logger.info("\nStandardizing universities...")
    university_columns = [col for col in df.columns if col.startswith('university_') and col.endswith(('_1', '_2', '_3', '_4', '_5', '_6', '_7', '_8', '_9', '_10'))]
    university_columns.extend([col for col in df.columns if col.startswith('university_') and col.split('_')[-1].isdigit()])
    
    # Add the host university column
    if 'university' in df.columns and 'university' not in university_columns:
        university_columns.insert(0, 'university')
    
    all_universities = []
    for col in university_columns:
        universities = df[col].dropna().astype(str).unique()
        all_universities.extend(universities)
    
    unique_universities = list(set(all_universities))
    logger.info(f"Found {len(unique_universities)} unique universities to standardize")
    
    # Get standardized mappings
    university_mapping = await university_standardizer.standardize_universities_batch(unique_universities)
    
    # Apply university standardization
    for col in university_columns:
        standardized_col = f'{col}_standardized'
        df[standardized_col] = df[col].astype(str).map(university_mapping).fillna(df[col])
    
    return df


def generate_summary_statistics(df):
    """Generate comprehensive summary statistics"""
    
    logger.info("\n=== Generating Summary Statistics ===")
    
    # Count speakers
    total_speakers = 0
    speakers_with_rank = 0
    speakers_with_standardized_rank = 0
    
    for idx, row in df.iterrows():
        for i in range(1, 129):
            fn_col = f'First Name_{i}'
            if fn_col not in df.columns:
                break
                
            first_name = row.get(fn_col)
            if pd.notna(first_name) and str(first_name).strip():
                total_speakers += 1
                
                # Check rank
                rank_col = f'rank_{i}'
                if rank_col in df.columns and pd.notna(row.get(rank_col)):
                    speakers_with_rank += 1
                
                # Check standardized rank
                rank_std_col = f'rank_{i}_standardized'
                if rank_std_col in df.columns and pd.notna(row.get(rank_std_col)):
                    speakers_with_standardized_rank += 1
    
    # Seminar statistics
    seminars_with_speakers = 0
    for idx, row in df.iterrows():
        has_speaker = False
        for i in range(1, 129):
            fn_col = f'First Name_{i}'
            if fn_col in df.columns and pd.notna(row.get(fn_col)):
                has_speaker = True
                break
        if has_speaker:
            seminars_with_speakers += 1
    
    # Count UNIQUE SPEAKERS by name + discipline + affiliation ONLY
    unique_speaker_ids = set()
    
    for idx, row in df.iterrows():
        seminar_discipline = row.get('discipline', '')
        
        for i in range(1, 129):
            fn_col = f'First Name_{i}'
            ln_col = f'Last Name_{i}'
            uni_col = f'university_{i}'
            uni_std_col = f'university_{i}_standardized'
            
            if fn_col in df.columns and ln_col in df.columns:
                first_name = row.get(fn_col)
                last_name = row.get(ln_col)
                
                if pd.notna(first_name) or pd.notna(last_name):
                    full_name = f"{first_name or ''} {last_name or ''}".strip()
                    
                    # Get standardized affiliation if available
                    if uni_std_col in df.columns and pd.notna(row.get(uni_std_col)):
                        affiliation = row.get(uni_std_col)
                    elif uni_col in df.columns and pd.notna(row.get(uni_col)):
                        affiliation = row.get(uni_col)
                    else:
                        affiliation = row.get('university', '')
                    
                    # Generate speaker ID using shared function
                    speaker_id = generate_speaker_id(full_name, seminar_discipline, affiliation)
                    if speaker_id:
                        unique_speaker_ids.add(speaker_id)
    
    stats = {
        'total_seminars': len(df),
        'seminars_with_speakers': seminars_with_speakers,
        'total_speaker_appearances': total_speakers,
        'unique_speakers_by_name_discipline_affiliation': len(unique_speaker_ids),
        'speakers_with_rank': speakers_with_rank,
        'speakers_with_standardized_rank': speakers_with_standardized_rank,
        'timestamp': datetime.now().isoformat()
    }
    
    # Print summary
    print("\n" + "="*60)
    print("FINAL DATASET SUMMARY")
    print("="*60)
    print(f"Total seminars: {stats['total_seminars']:,}")
    print(f"Seminars with speakers: {stats['seminars_with_speakers']:,}")
    print(f"Total speaker appearances: {stats['total_speaker_appearances']:,}")
    print(f"UNIQUE SPEAKERS (name + discipline + affiliation): {stats['unique_speakers_by_name_discipline_affiliation']:,}")
    print(f"Speakers with rank data: {stats['speakers_with_rank']:,} ({stats['speakers_with_rank']/stats['total_speaker_appearances']*100:.1f}%)")
    print(f"Speakers with standardized rank: {stats['speakers_with_standardized_rank']:,} ({stats['speakers_with_standardized_rank']/stats['total_speaker_appearances']*100:.1f}%)")
    
    return stats


async def main():
    """Main pipeline function"""
    
    print("\n" + "="*60)
    print("SEARCH COSTS RCT - CREATE FINAL DATASET")
    print("="*60)
    print(f"Started at: {datetime.now()}")
    
    # Check for API key
    if not os.getenv('OPENAI_API_KEY'):
        logger.error("OPENAI_API_KEY not set. Please set it in your .env file")
        return 1
    
    # Step 1: Run the unified data processor
    logger.info("Step 1: Running unified data processor (merge + clean)")
    processor = UnifiedDataProcessor()
    df_cleaned = await processor.run_full_pipeline()
    
    if df_cleaned is None:
        logger.error("Data processing failed")
        return 1
    
    # Step 2: Apply standardization
    logger.info("\nStep 2: Applying standardization")
    df_standardized = await standardize_data(df_cleaned)
    
    # Step 3: Final cleanup - clean any remaining problematic names after standardization
    logger.info("\nStep 3: Final name cleaning")
    initial_speakers = sum(1 for idx, row in df_standardized.iterrows() 
                          for i in range(1, 129) 
                          if f'First Name_{i}' in df_standardized.columns 
                          and pd.notna(row.get(f'First Name_{i}')))
    
    # Re-apply name cleaning with standardized data
    processor_final = UnifiedDataProcessor()
    df_final = await processor_final.clean_speaker_names(df_standardized)
    
    final_speakers = sum(1 for idx, row in df_final.iterrows() 
                        for i in range(1, 129) 
                        if f'First Name_{i}' in df_final.columns 
                        and pd.notna(row.get(f'First Name_{i}')))
    
    if initial_speakers != final_speakers:
        logger.info(f"Removed {initial_speakers - final_speakers} additional problematic names after standardization")
    
    # Step 4: Save final dataset
    output_file = config.PROCESSED_DATA_DIR / 'master-data-final.csv'
    df_final.to_csv(output_file, index=False, encoding='utf-8-sig')
    logger.info(f"\n✅ Final dataset saved to: {output_file}")
    
    # Step 5: Generate summary statistics
    stats = generate_summary_statistics(df_final)
    
    # Save summary
    summary_file = config.PROCESSED_DATA_DIR / 'final_dataset_summary.json'
    import json
    with open(summary_file, 'w') as f:
        json.dump(stats, f, indent=2)
    
    print(f"\n✅ Summary saved to: {summary_file}")
    print(f"\nCompleted at: {datetime.now()}")
    print("="*60)
    
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))