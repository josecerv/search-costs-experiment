#!/usr/bin/env python3
"""
Standardize academic ranks using GPT-4o
Categorizes ranks into: professor, associate professor, assistant professor, 
graduate student, post-doc, non-academic
"""

import pandas as pd
import numpy as np
import json
import asyncio
import aiohttp
from pathlib import Path
import os
from typing import Dict, List, Optional
import re
from datetime import datetime
import logging
from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(__file__).parent.parent.parent / '.env'
if env_path.exists():
    load_dotenv(env_path)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Define allowed categories
ALLOWED_RANKS = [
    "professor",
    "associate professor", 
    "assistant professor",
    "graduate student",
    "post-doc",
    "non-academic"
]

# Load OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set")

# Cache file for storing standardized mappings
CACHE_FILE = Path(__file__).parent.parent / 'cache' / 'rank_standardization_cache.csv'
CACHE_FILE.parent.mkdir(exist_ok=True)

class RankStandardizer:
    def __init__(self):
        self.cache = self._load_cache()
        self.session = None
        
    def _load_cache(self) -> Dict[str, str]:
        """Load existing standardization cache"""
        if CACHE_FILE.exists():
            df = pd.read_csv(CACHE_FILE)
            return dict(zip(df['original_rank'], df['standardized_rank']))
        return {}
    
    def _save_cache(self):
        """Save cache to file"""
        if self.cache:
            df = pd.DataFrame([
                {'original_rank': k, 'standardized_rank': v} 
                for k, v in self.cache.items()
            ])
            df.to_csv(CACHE_FILE, index=False)
            logger.info(f"Saved {len(df)} mappings to cache")
    
    async def _get_session(self):
        """Get or create aiohttp session"""
        if self.session is None:
            self.session = aiohttp.ClientSession()
        return self.session
    
    async def _standardize_rank_gpt(self, rank: str) -> str:
        """Use GPT-4o to standardize a single rank"""
        session = await self._get_session()
        
        prompt = f"""You are standardizing academic ranks for a research study. 
        
Categorize the following rank/title into EXACTLY ONE of these categories:
- professor (includes Full Professor, Professor, Distinguished Professor, Endowed Professor, etc.)
- associate professor (includes Associate Professor)
- assistant professor (includes Assistant Professor) 
- graduate student (includes PhD student, Masters student, any year graduate student)
- post-doc (includes Postdoctoral Fellow, Postdoc, Research Fellow, etc.)
- non-academic (includes industry positions, government, non-profit, emeritus, retired, or unknown)

Rank to categorize: "{rank}"

Rules:
1. If someone has multiple roles, choose the primary academic one
2. Research Scientists/Associates without professor title → post-doc
3. Lecturers/Instructors without professor rank → non-academic
4. Staff Scientists → non-academic
5. If unclear or missing → non-academic
6. Dates or non-rank text → non-academic

Respond with ONLY the category name, nothing else."""

        headers = {
            'Authorization': f'Bearer {OPENAI_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        data = {
            'model': 'gpt-4o',
            'messages': [{'role': 'user', 'content': prompt}],
            'temperature': 0,
            'max_tokens': 50
        }
        
        try:
            async with session.post(
                'https://api.openai.com/v1/chat/completions',
                headers=headers,
                json=data
            ) as response:
                if response.status == 200:
                    result = await response.json()
                    standardized = result['choices'][0]['message']['content'].strip().lower()
                    
                    # Validate response
                    if standardized not in ALLOWED_RANKS:
                        logger.warning(f"Invalid response '{standardized}' for rank '{rank}', defaulting to non-academic")
                        return "non-academic"
                    
                    return standardized
                else:
                    logger.error(f"API error {response.status} for rank '{rank}'")
                    return "non-academic"
                    
        except Exception as e:
            logger.error(f"Error standardizing rank '{rank}': {e}")
            return "non-academic"
    
    async def standardize_ranks_batch(self, ranks: List[str], batch_size: int = 50) -> Dict[str, str]:
        """Standardize multiple ranks with batching"""
        # Filter out already cached ranks
        uncached_ranks = [r for r in ranks if r not in self.cache]
        
        if not uncached_ranks:
            logger.info("All ranks already in cache")
            return {r: self.cache.get(r, "non-academic") for r in ranks}
        
        logger.info(f"Standardizing {len(uncached_ranks)} uncached ranks")
        
        # Process in batches
        results = {}
        for i in range(0, len(uncached_ranks), batch_size):
            batch = uncached_ranks[i:i+batch_size]
            
            # Create tasks for batch
            tasks = [self._standardize_rank_gpt(rank) for rank in batch]
            standardized = await asyncio.gather(*tasks)
            
            # Update results and cache
            for rank, std_rank in zip(batch, standardized):
                results[rank] = std_rank
                self.cache[rank] = std_rank
            
            logger.info(f"Processed batch {i//batch_size + 1}/{(len(uncached_ranks) + batch_size - 1)//batch_size}")
            
            # Save cache periodically
            if (i + batch_size) % 200 == 0:
                self._save_cache()
        
        # Final cache save
        self._save_cache()
        
        # Return all results including cached
        return {r: self.cache.get(r, "non-academic") for r in ranks}
    
    async def close(self):
        """Close aiohttp session"""
        if self.session:
            await self.session.close()

async def standardize_dataset(input_file: str, output_file: str):
    """Standardize ranks in the full dataset"""
    logger.info(f"Loading data from {input_file}")
    df = pd.read_csv(input_file, low_memory=False)
    
    # Extract all unique ranks
    all_ranks = []
    rank_columns = [col for col in df.columns if col.startswith('rank_')]
    
    for col in rank_columns:
        ranks = df[col].dropna().astype(str).unique()
        all_ranks.extend(ranks)
    
    unique_ranks = list(set(all_ranks))
    logger.info(f"Found {len(unique_ranks)} unique ranks across {len(rank_columns)} columns")
    
    # Standardize ranks
    standardizer = RankStandardizer()
    try:
        rank_mapping = await standardizer.standardize_ranks_batch(unique_ranks)
        
        # Apply standardization to dataframe
        logger.info("Applying standardization to dataset")
        for col in rank_columns:
            df[f'{col}_standardized'] = df[col].astype(str).map(rank_mapping).fillna('non-academic')
        
        # Save results
        logger.info(f"Saving standardized data to {output_file}")
        df.to_csv(output_file, index=False)
        
        # Generate summary report
        summary = {}
        for col in rank_columns:
            if f'{col}_standardized' in df:
                summary[col] = df[f'{col}_standardized'].value_counts().to_dict()
        
        report_file = Path(output_file).parent / 'rank_standardization_report.json'
        with open(report_file, 'w') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'total_ranks_processed': len(unique_ranks),
                'column_summaries': summary
            }, f, indent=2)
        
        logger.info(f"Standardization complete. Report saved to {report_file}")
        
    finally:
        await standardizer.close()

def main():
    """Main entry point"""
    import argparse
    parser = argparse.ArgumentParser(description='Standardize academic ranks using GPT-4o')
    parser.add_argument('--input', '-i', 
                       default='03_data_collection/processed/master-data-full-year.csv',
                       help='Input CSV file')
    parser.add_argument('--output', '-o',
                       default='03_data_collection/processed/master-data-standardized-ranks.csv',
                       help='Output CSV file')
    
    args = parser.parse_args()
    
    # Run async function
    asyncio.run(standardize_dataset(args.input, args.output))

if __name__ == '__main__':
    main()