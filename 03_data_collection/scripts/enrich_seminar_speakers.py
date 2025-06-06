#!/usr/bin/env python3
"""
Enrich Seminar Speaker Data with Affiliations and PhD Years
Works with the seminar-level data structure (master-data-final.csv)
Extracts unique speakers, enriches them, and maps back to seminars
"""

import asyncio
import logging
import sys
from pathlib import Path
from typing import Dict, Set, Tuple
import pandas as pd
import numpy as np
from datetime import datetime

# Add paths
sys.path.append(str(Path(__file__).parent / ".."))
sys.path.append(str(Path(__file__).parent / "../.."))
from config.settings import config
from core.normalization import generate_speaker_id, normalize_text

# Import the enricher
from enrich_speaker_data import SpeakerDataEnricher

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SeminarSpeakerEnricher:
    """Enriches speakers in seminar-level data structure"""
    
    def __init__(self):
        self.enricher = SpeakerDataEnricher()
        
    def extract_unique_speakers(self, df: pd.DataFrame) -> pd.DataFrame:
        """Extract unique speakers from seminar data into a flat structure"""
        logger.info("Extracting unique speakers from seminar data...")
        
        speakers_list = []
        speaker_ids_seen = set()
        
        for idx, row in df.iterrows():
            seminar_discipline = row.get('discipline', '')
            
            # Process each speaker column (up to 128)
            for i in range(1, 129):
                fn_col = f'First Name_{i}'
                ln_col = f'Last Name_{i}'
                uni_col = f'university_{i}'
                uni_std_col = f'university_{i}_standardized'
                rank_col = f'rank_{i}'
                rank_std_col = f'rank_{i}_standardized'
                
                if fn_col not in df.columns or ln_col not in df.columns:
                    break
                
                first_name = row.get(fn_col)
                last_name = row.get(ln_col)
                
                # Skip if no name
                if pd.isna(first_name) or pd.isna(last_name):
                    continue
                
                first_name = str(first_name).strip()
                last_name = str(last_name).strip()
                
                if not first_name or not last_name:
                    continue
                
                # Get affiliation (prefer standardized)
                if uni_std_col in df.columns and pd.notna(row.get(uni_std_col)):
                    affiliation = str(row.get(uni_std_col))
                elif uni_col in df.columns and pd.notna(row.get(uni_col)):
                    affiliation = str(row.get(uni_col))
                else:
                    affiliation = ""
                
                # Get rank (prefer standardized)
                if rank_std_col in df.columns and pd.notna(row.get(rank_std_col)):
                    rank = str(row.get(rank_std_col))
                elif rank_col in df.columns and pd.notna(row.get(rank_col)):
                    rank = str(row.get(rank_col))
                else:
                    rank = ""
                
                # Generate speaker ID
                full_name = f"{first_name} {last_name}"
                speaker_id = generate_speaker_id(full_name, seminar_discipline, affiliation)
                
                # Skip if we've seen this speaker before
                if speaker_id in speaker_ids_seen:
                    continue
                
                speaker_ids_seen.add(speaker_id)
                
                # Check for existing PhD year
                phd_year_col = f'phd_graduation_year_{i}'
                existing_phd_year = row.get(phd_year_col) if phd_year_col in df.columns else None
                
                # Add to list
                speakers_list.append({
                    'speaker_id': speaker_id,
                    'first_name': first_name,
                    'last_name': last_name,
                    'discipline': seminar_discipline,
                    'affiliation': affiliation,
                    'rank': rank,
                    'full_name': full_name,
                    'phd_graduation_year': existing_phd_year  # Include existing PhD year
                })
        
        speakers_df = pd.DataFrame(speakers_list)
        logger.info(f"Extracted {len(speakers_df)} unique speakers")
        
        return speakers_df
    
    async def enrich_seminar_data(self, df: pd.DataFrame, sample_size: int = None) -> pd.DataFrame:
        """Main enrichment function for seminar data"""
        logger.info("Starting seminar speaker enrichment...")
        
        # Step 1: Extract unique speakers
        unique_speakers = self.extract_unique_speakers(df)
        
        if len(unique_speakers) == 0:
            logger.warning("No speakers found to enrich")
            return df
        
        # Step 2: Enrich unique speakers
        logger.info(f"Enriching {len(unique_speakers)} unique speakers...")
        enriched_speakers = await self.enricher.enrich_dataframe(unique_speakers, sample_size, skip_existing_phd=True)
        
        # Step 3: Create lookup dictionaries
        affiliation_lookup = {}
        phd_year_lookup = {}
        
        for _, speaker in enriched_speakers.iterrows():
            speaker_id = speaker['speaker_id']
            
            # Track retrieved affiliations for filling missing values
            if pd.notna(speaker.get('retrieved_affiliation')) and speaker['retrieved_affiliation']:
                # Only use retrieved affiliation if original was missing
                if pd.isna(speaker.get('affiliation')) or speaker.get('affiliation', '').strip() == '':
                    affiliation_lookup[speaker_id] = speaker['retrieved_affiliation']
            
            # Add PhD year if available
            if pd.notna(speaker.get('phd_graduation_year')) and speaker['phd_graduation_year']:
                phd_year_lookup[speaker_id] = speaker['phd_graduation_year']
        
        # Step 4: Map enrichments back to seminar data
        logger.info("Mapping enrichments back to seminar data...")
        df_enriched = df.copy()
        
        # Add PhD year columns for each speaker position
        for i in range(1, 129):
            fn_col = f'First Name_{i}'
            if fn_col not in df_enriched.columns:
                break
            
            # Add PhD year column for this speaker position
            df_enriched[f'phd_graduation_year_{i}'] = None
        
        # Map enrichments
        enriched_count = 0
        for idx, row in df_enriched.iterrows():
            seminar_discipline = row.get('discipline', '')
            
            for i in range(1, 129):
                fn_col = f'First Name_{i}'
                ln_col = f'Last Name_{i}'
                uni_col = f'university_{i}'
                uni_std_col = f'university_{i}_standardized'
                
                if fn_col not in df_enriched.columns or ln_col not in df_enriched.columns:
                    break
                
                first_name = row.get(fn_col)
                last_name = row.get(ln_col)
                
                if pd.isna(first_name) or pd.isna(last_name):
                    continue
                
                first_name = str(first_name).strip()
                last_name = str(last_name).strip()
                
                if not first_name or not last_name:
                    continue
                
                # Get current affiliation
                if uni_std_col in df_enriched.columns and pd.notna(row.get(uni_std_col)):
                    affiliation = str(row.get(uni_std_col))
                elif uni_col in df_enriched.columns and pd.notna(row.get(uni_col)):
                    affiliation = str(row.get(uni_col))
                else:
                    affiliation = ""
                
                # Generate speaker ID
                full_name = f"{first_name} {last_name}"
                speaker_id = generate_speaker_id(full_name, seminar_discipline, affiliation)
                
                # Map enrichments
                # Fill missing affiliations with retrieved values
                if speaker_id in affiliation_lookup:
                    # Only fill if the original affiliation is missing
                    if pd.isna(affiliation) or affiliation.strip() == '':
                        df_enriched.at[idx, uni_col] = affiliation_lookup[speaker_id]
                        enriched_count += 1
                
                # Add PhD year
                if speaker_id in phd_year_lookup:
                    df_enriched.at[idx, f'phd_graduation_year_{i}'] = phd_year_lookup[speaker_id]
        
        logger.info(f"Filled {enriched_count} missing affiliations")
        
        # Log summary statistics
        total_speakers = sum(1 for idx, row in df_enriched.iterrows() 
                           for i in range(1, 129) 
                           if f'First Name_{i}' in df_enriched.columns 
                           and pd.notna(row.get(f'First Name_{i}')))
        
        enriched_phd_years = sum(1 for idx, row in df_enriched.iterrows() 
                               for i in range(1, 129) 
                               if f'phd_graduation_year_{i}' in df_enriched.columns 
                               and pd.notna(row.get(f'phd_graduation_year_{i}')))
        
        logger.info(f"\nEnrichment Summary:")
        logger.info(f"  - Total speaker appearances: {total_speakers}")
        logger.info(f"  - Unique speakers processed: {len(unique_speakers)}")
        logger.info(f"  - Missing affiliations filled: {enriched_count}")
        logger.info(f"  - PhD years added: {enriched_phd_years}")
        
        return df_enriched


async def enrich_seminar_file(input_file: Path, output_file: Path, sample_size: int = None):
    """Convenience function to enrich seminar data from file"""
    logger.info(f"Loading seminar data from {input_file}")
    df = pd.read_csv(input_file, encoding='utf-8-sig', low_memory=False)
    
    enricher = SeminarSpeakerEnricher()
    df_enriched = await enricher.enrich_seminar_data(df, sample_size)
    
    logger.info(f"Saving enriched data to {output_file}")
    df_enriched.to_csv(output_file, index=False, encoding='utf-8-sig')
    
    return df_enriched


async def main():
    """Main function for testing"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Enrich seminar speaker data')
    parser.add_argument('--input', type=str, help='Input CSV file path')
    parser.add_argument('--output', type=str, help='Output CSV file path')
    parser.add_argument('--sample', type=int, help='Sample size for testing')
    
    args = parser.parse_args()
    
    if args.input and args.output:
        input_file = Path(args.input)
        output_file = Path(args.output)
        
        if not input_file.exists():
            logger.error(f"Input file not found: {input_file}")
            return 1
        
        await enrich_seminar_file(input_file, output_file, args.sample)
    else:
        # Default test with master-data-final.csv
        test_file = config.PROCESSED_DATA_DIR / 'master-data-final.csv'
        if test_file.exists():
            output_file = config.PROCESSED_DATA_DIR / 'test_enriched_seminars.csv'
            # Test with just 10 unique speakers
            await enrich_seminar_file(test_file, output_file, sample_size=10)
            logger.info(f"Test completed. Check {output_file}")
        else:
            logger.error("No input file specified and test file not found")
            return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))