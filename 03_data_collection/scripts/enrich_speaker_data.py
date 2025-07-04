#!/usr/bin/env python3
"""
Enrich Speaker Data with Affiliations and PhD Years
Uses Perplexity API to retrieve missing affiliations and PhD graduation years
Designed to integrate into the data collection pipeline
"""

import asyncio
import json
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import re

import pandas as pd
from dotenv import load_dotenv
from openai import AsyncOpenAI
import hashlib

# Load environment variables
env_path = Path(__file__).parent.parent.parent / '.env'
if env_path.exists():
    load_dotenv(env_path)

# Add paths
sys.path.append(str(Path(__file__).parent / ".."))
sys.path.append(str(Path(__file__).parent / "../.."))
from config.settings import config
from core.normalization import generate_speaker_id, normalize_text

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class SpeakerDataEnricher:
    """Enriches speaker data with affiliations and PhD years using Perplexity API"""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize enricher with API key and cache"""
        self.api_key = api_key or os.getenv('PERPLEXITY_API_KEY')
        if not self.api_key:
            raise ValueError("PERPLEXITY_API_KEY not set. Please set it in your .env file")
        
        self.client = AsyncOpenAI(
            api_key=self.api_key,
            base_url="https://api.perplexity.ai"
        )
        
        # Setup cache directory in data collection area
        self.cache_dir = Path(__file__).parent.parent / 'cache' / 'speaker_enrichment'
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
        # Load existing cache
        self.cache_file = self.cache_dir / 'enrichment_cache.json'
        self.cache = self._load_cache()
        
        # Rate limiting
        self.semaphore = asyncio.Semaphore(10)  # Max 10 concurrent requests
        self.request_count = 0
        self.max_requests_per_batch = 100
        
    def _load_cache(self) -> Dict:
        """Load existing cache from disk"""
        if self.cache_file.exists():
            try:
                with open(self.cache_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Failed to load cache: {e}")
        return {}
    
    def _save_cache(self):
        """Save cache to disk"""
        try:
            with open(self.cache_file, 'w') as f:
                json.dump(self.cache, f, indent=2)
            logger.debug(f"Cache saved to {self.cache_file} ({len(self.cache)} entries)")
        except Exception as e:
            logger.error(f"Failed to save cache to {self.cache_file}: {e}")
    
    def _generate_cache_key(self, first_name: str, last_name: str, discipline: str, affiliation: str = "") -> str:
        """Generate cache key for speaker"""
        key_string = f"{first_name}|{last_name}|{discipline}|{affiliation}".lower()
        return hashlib.md5(key_string.encode()).hexdigest()
    
    async def _query_affiliation(self, first_name: str, last_name: str, discipline: str) -> Optional[str]:
        """Query Perplexity for current affiliation"""
        async with self.semaphore:
            try:
                messages = [
                    {
                        "role": "system",
                        "content": (
                            "You are a precise research assistant. When asked about someone's affiliation, "
                            "return ONLY the institution or organization name. Do not include job titles, "
                            "departments, citations, or any other text."
                        )
                    },
                    {
                        "role": "user",
                        "content": (
                            f"What is the current primary institutional affiliation of {first_name} {last_name} "
                            f"who works in the field of {discipline}? "
                            "Return ONLY the institution name (e.g., 'Stanford University', 'Google', 'MIT'). "
                            "If the person is not found or affiliation is unknown, return 'UNKNOWN'."
                        )
                    }
                ]
                
                response = await self.client.chat.completions.create(
                    model="sonar-pro",
                    messages=messages,
                    temperature=0.1,
                    max_tokens=50
                )
                
                affiliation = response.choices[0].message.content.strip()
                
                # Validate response
                if self._validate_affiliation(affiliation):
                    return affiliation
                return None
                
            except Exception as e:
                logger.error(f"Error querying affiliation for {first_name} {last_name}: {e}")
                return None
    
    async def _query_phd_year(self, first_name: str, last_name: str, discipline: str, affiliation: str, rank: str = "") -> Optional[str]:
        """Query Perplexity for PhD graduation year with improved prompt and validation"""
        async with self.semaphore:
            try:
                # Add rank context to improve accuracy
                rank_context = ""
                if rank:
                    rank_context = f"Their current academic rank is {rank}. "
                
                messages = [
                    {
                        "role": "system",
                        "content": (
                            "You are a precise research assistant. When asked about PhD graduation years:\n"
                            "- Return ONLY a 4-digit year for PAST PhD graduations (e.g., 2015)\n"
                            "- Return '0' ONLY for current PhD students (not postdocs or faculty)\n"
                            "- Return 'NA' for those without a PhD\n"
                            "- NEVER return future years or expected graduation dates\n"
                            "- Professors CANNOT be current students - they have already graduated"
                        )
                    },
                    {
                        "role": "user",
                        "content": (
                            f"{first_name} {last_name} works in {discipline} "
                            f"{'at ' + affiliation if affiliation and affiliation != 'UNKNOWN' else ''}. "
                            f"{rank_context}"
                            "What year did they complete/graduate with their PhD? "
                            "Remember: Return ONLY the past graduation year (not future), "
                            "'0' for current PhD students only, or 'NA' if no PhD."
                        )
                    }
                ]
                
                response = await self.client.chat.completions.create(
                    model="sonar-pro",
                    messages=messages,
                    temperature=0.1,
                    max_tokens=10
                )
                
                phd_year = response.choices[0].message.content.strip()
                
                # Validate response with rank context
                validated_year = self._validate_phd_year(phd_year, rank)
                return validated_year
                
            except Exception as e:
                logger.error(f"Error querying PhD year for {first_name} {last_name}: {e}")
                return None
    
    def _validate_affiliation(self, affiliation: str) -> bool:
        """Validate affiliation response"""
        if not affiliation or affiliation == "UNKNOWN":
            return False
        
        # Check for overly long responses (likely contains extra text)
        if len(affiliation.split()) > 10:
            return False
        
        # Check for common invalid patterns
        invalid_patterns = [
            r"currently works at",
            r"is affiliated with",
            r"professor at",
            r"researcher at",
            r"based at",
            r"citation",
            r"\[.*\]",  # Citations
            r"\(.*\)",  # Parenthetical info
        ]
        
        for pattern in invalid_patterns:
            if re.search(pattern, affiliation, re.IGNORECASE):
                return False
        
        return True
    
    def _validate_phd_year(self, phd_year: str, rank: str = "") -> Optional[str]:
        """Validate and normalize PhD year response with rank-based validation"""
        if not phd_year:
            return None
        
        # Clean the response
        phd_year = phd_year.strip().upper()
        
        # Check for NA
        if phd_year == "NA" or "NOT" in phd_year or "NO PHD" in phd_year:
            return "NA"
        
        # Check for current student
        if phd_year == "0" or "CURRENT" in phd_year or "STUDENT" in phd_year:
            # Validate against rank - professors cannot be current students
            if rank:
                professor_ranks = ['professor', 'associate professor', 'assistant professor',
                                 'full professor', 'prof', 'prof.', 'emeritus', 'adjunct']
                if any(prof_rank in rank.lower() for prof_rank in professor_ranks):
                    # This is likely an error - professors are not current students
                    logger.warning(f"Rank '{rank}' marked as current student - likely an error")
                    return None
            return "0"
        
        # Extract year if present
        year_match = re.search(r'(\d{4})', phd_year)
        if year_match:
            year = int(year_match.group(1))
            # Validate reasonable range (no future years)
            current_year = datetime.now().year
            if 1900 <= year <= current_year:
                return str(year)
            elif year > current_year:
                logger.warning(f"Future PhD year {year} detected - ignoring")
                return None
        
        return None
    
    async def enrich_speaker(self, row: Dict, skip_existing_phd: bool = True) -> Tuple[Optional[str], Optional[str], bool]:
        """
        Enrich a single speaker with affiliation and PhD year.
        
        Args:
            row: Speaker data including first_name, last_name, discipline, affiliation, rank
            skip_existing_phd: If True, skip speakers who already have PhD data
            
        Returns:
            Tuple of (affiliation, phd_year, is_cache_hit)
        """
        first_name = str(row.get('first_name', '')).strip()
        last_name = str(row.get('last_name', '')).strip()
        discipline = str(row.get('discipline', '')).strip()
        current_affiliation = str(row.get('affiliation', '')).strip()
        rank = str(row.get('rank', '')).strip()
        existing_phd = row.get('phd_graduation_year')
        
        # Skip if no name
        if not first_name or not last_name:
            return None, None, False
        
        # Skip if already has PhD data and skip_existing_phd is True
        # Check if existing_phd is actually a valid value (not None, NaN, or empty string)
        if skip_existing_phd and pd.notna(existing_phd) and str(existing_phd).strip().lower() not in ['', 'nan', 'none']:
            logger.debug(f"Skipping {first_name} {last_name} - already has PhD year: {existing_phd}")
            return current_affiliation, existing_phd, True  # Return existing data
        
        # Check cache first
        cache_key = self._generate_cache_key(first_name, last_name, discipline, current_affiliation)
        if cache_key in self.cache:
            cached = self.cache[cache_key]
            return cached.get('affiliation'), cached.get('phd_year'), True  # True = cache hit
        
        # Query for missing affiliation
        retrieved_affiliation = current_affiliation
        if not current_affiliation or current_affiliation.lower() in ['nan', 'none', '']:
            retrieved_affiliation = await self._query_affiliation(first_name, last_name, discipline)
            if not retrieved_affiliation:
                retrieved_affiliation = current_affiliation
            await asyncio.sleep(0.5)  # Rate limit
        
        # Query for PhD year with rank context
        phd_year = await self._query_phd_year(first_name, last_name, discipline, retrieved_affiliation, rank)
        await asyncio.sleep(0.5)  # Rate limit
        
        # Cache results
        self.cache[cache_key] = {
            'affiliation': retrieved_affiliation,
            'phd_year': phd_year,
            'timestamp': datetime.now().isoformat()
        }
        
        self.request_count += 2
        
        # Save cache periodically
        if self.request_count % 10 == 0:
            self._save_cache()
        
        return retrieved_affiliation, phd_year, False  # False = API call made
    
    async def enrich_dataframe(self, df: pd.DataFrame, sample_size: Optional[int] = None, skip_existing_phd: bool = True) -> pd.DataFrame:
        """
        Enrich entire dataframe with affiliations and PhD years.
        
        Args:
            df: DataFrame with speaker data
            sample_size: Optional sample size for testing
            skip_existing_phd: If True, skip speakers who already have PhD data
        
        Returns:
            Enriched DataFrame
        """
        logger.info(f"Starting enrichment for {len(df)} speakers")
        logger.info(f"Cache contains {len(self.cache)} existing entries")
        
        # Create copy to avoid modifying original
        df_enriched = df.copy()
        
        # Add new columns if they don't exist
        if 'retrieved_affiliation' not in df_enriched.columns:
            df_enriched['retrieved_affiliation'] = None
        if 'phd_graduation_year' not in df_enriched.columns:
            df_enriched['phd_graduation_year'] = None
        
        # Count existing PhD data
        existing_phd_count = df_enriched['phd_graduation_year'].notna().sum()
        logger.info(f"Speakers with existing PhD data: {existing_phd_count}")
        
        # Sample if requested
        if sample_size and sample_size < len(df_enriched):
            df_sample = df_enriched.sample(n=sample_size, random_state=42)
            sample_indices = df_sample.index
        else:
            sample_indices = df_enriched.index
        
        # Process in batches
        batch_size = 50
        total_processed = 0
        cache_hits = 0
        api_calls = 0
        skipped_existing = 0
        
        for i in range(0, len(sample_indices), batch_size):
            batch_indices = sample_indices[i:i + batch_size]
            batch_tasks = []
            
            for idx in batch_indices:
                row = df_enriched.loc[idx]
                task = self.enrich_speaker(row.to_dict(), skip_existing_phd=skip_existing_phd)
                batch_tasks.append((idx, task))
            
            # Process batch
            results = await asyncio.gather(*[task for _, task in batch_tasks])
            
            # Update dataframe and track statistics
            for (idx, _), (affiliation, phd_year, is_cache_hit) in zip(batch_tasks, results):
                # Get original data
                original_phd = df_enriched.at[idx, 'phd_graduation_year']
                
                # Check if this speaker was skipped due to existing PhD data
                was_skipped = skip_existing_phd and pd.notna(original_phd) and str(original_phd).strip().lower() not in ['', 'nan', 'none']
                
                if was_skipped:
                    skipped_existing += 1
                    # Even if skipped, count cache hit status
                    if is_cache_hit:
                        cache_hits += 1
                else:
                    # Update the dataframe with new data
                    if affiliation:
                        df_enriched.at[idx, 'retrieved_affiliation'] = affiliation
                    if phd_year:
                        df_enriched.at[idx, 'phd_graduation_year'] = phd_year
                    
                    if is_cache_hit:
                        cache_hits += 1
                    else:
                        api_calls += 1
            
            total_processed += len(batch_indices)
            logger.info(f"Processed {total_processed}/{len(sample_indices)} speakers (skipped {skipped_existing} with existing PhD data)")
            
            # Rate limit between batches
            if self.request_count >= self.max_requests_per_batch:
                logger.info("Rate limit reached, pausing for 60 seconds...")
                await asyncio.sleep(60)
                self.request_count = 0
        
        # Final cache save
        self._save_cache()
        
        # Log summary statistics
        enriched_affiliations = df_enriched['retrieved_affiliation'].notna().sum()
        enriched_phd_years = df_enriched['phd_graduation_year'].notna().sum()
        new_phd_years = enriched_phd_years - existing_phd_count
        
        logger.info(f"\nEnrichment Summary:")
        logger.info(f"  - Total speakers: {len(df_enriched)}")
        logger.info(f"  - Skipped (already had PhD data in input): {skipped_existing}")
        logger.info(f"  - Retrieved from cache: {cache_hits}")
        logger.info(f"  - New API calls made: {api_calls}")
        logger.info(f"  - Total processed: {cache_hits + api_calls}")
        if (cache_hits + api_calls) > 0:
            logger.info(f"  - Cache hit rate: {cache_hits/(cache_hits+api_calls)*100:.1f}%")
        logger.info(f"  - Affiliations enriched: {enriched_affiliations}")
        logger.info(f"  - PhD years total: {enriched_phd_years}")
        logger.info(f"  - PhD years newly added: {new_phd_years}")
        logger.info(f"  - Cache now contains: {len(self.cache)} entries")
        
        return df_enriched


async def enrich_speaker_data_from_file(input_file: Path, output_file: Path, sample_size: Optional[int] = None):
    """Convenience function to enrich speaker data from a CSV file"""
    logger.info(f"Loading data from {input_file}")
    df = pd.read_csv(input_file, encoding='utf-8-sig')
    
    enricher = SpeakerDataEnricher()
    df_enriched = await enricher.enrich_dataframe(df, sample_size=sample_size)
    
    logger.info(f"Saving enriched data to {output_file}")
    df_enriched.to_csv(output_file, index=False, encoding='utf-8-sig')
    
    return df_enriched


async def main():
    """Main function for testing"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Enrich speaker data with affiliations and PhD years')
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
        
        await enrich_speaker_data_from_file(input_file, output_file, args.sample)
    else:
        # Default test with people_combined_analysis.csv
        test_file = Path("/mnt/c/Users/jcerv/Jose/search-costs/04_demographic_analysis/outputs/people_combined_analysis.csv")
        if test_file.exists():
            output_file = Path("/mnt/c/Users/jcerv/Jose/search-costs/03_data_collection/processed/test_enriched_speakers.csv")
            await enrich_speaker_data_from_file(test_file, output_file, sample_size=10)
            logger.info(f"Test completed. Check {output_file}")
        else:
            logger.error("No input file specified and test file not found")
            return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))