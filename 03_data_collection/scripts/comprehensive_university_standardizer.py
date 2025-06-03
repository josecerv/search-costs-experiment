#!/usr/bin/env python3
"""
Comprehensive university standardization using LLM as primary method
This replaces the previous approach with a much more thorough system
"""

import pandas as pd
import numpy as np
import json
import asyncio
from pathlib import Path
import os
from typing import Dict, List, Set, Tuple
import re
from datetime import datetime
import logging
from openai import AsyncOpenAI
from dotenv import load_dotenv
import pickle
from collections import Counter

# Load environment variables
env_path = Path(__file__).parent.parent.parent / '.env'
if env_path.exists():
    load_dotenv(env_path)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Cache files
CACHE_DIR = Path(__file__).parent.parent / 'cache'
CACHE_DIR.mkdir(exist_ok=True)
COMPREHENSIVE_CACHE = CACHE_DIR / 'comprehensive_university_cache.pkl'


class ComprehensiveUniversityStandardizer:
    def __init__(self):
        self.cache = self._load_cache()
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OpenAI API key is required for comprehensive standardization")
        self.client = AsyncOpenAI(api_key=self.api_key)
        
    def _load_cache(self) -> Dict[str, str]:
        """Load existing comprehensive cache"""
        if COMPREHENSIVE_CACHE.exists():
            with open(COMPREHENSIVE_CACHE, 'rb') as f:
                return pickle.load(f)
        return {}
    
    def _save_cache(self):
        """Save cache to file"""
        with open(COMPREHENSIVE_CACHE, 'wb') as f:
            pickle.dump(self.cache, f)
        logger.info(f"Saved {len(self.cache)} mappings to comprehensive cache")
    
    async def analyze_all_universities(self, df: pd.DataFrame) -> Dict[str, int]:
        """Extract and count all unique university mentions from the dataset"""
        logger.info("Extracting all university mentions from dataset...")
        
        # Get all university columns
        university_cols = []
        for col in df.columns:
            if 'university' in col.lower() and 'standardized' not in col:
                university_cols.append(col)
        
        logger.info(f"Found {len(university_cols)} university columns")
        
        # Collect all university names
        all_universities = []
        for col in university_cols:
            universities = df[col].dropna().astype(str).str.strip()
            universities = universities[universities != '']
            all_universities.extend(universities.tolist())
        
        # Count occurrences
        university_counts = Counter(all_universities)
        
        logger.info(f"Found {len(all_universities)} total university mentions")
        logger.info(f"Found {len(university_counts)} unique university names")
        
        return dict(university_counts)
    
    async def standardize_batch_comprehensive(self, universities: List[Tuple[str, int]]) -> Dict[str, str]:
        """Standardize a batch of universities using comprehensive LLM approach"""
        
        # Create the batch for LLM processing
        names_list = [name for name, _ in universities]
        
        prompt = f"""You are an expert at standardizing university names. Your task is to standardize these university/institution names to their OFFICIAL, FULL names.

CRITICAL RULES:
1. Use your knowledge to expand ALL abbreviations to full official names:
   - "MIT" → "Massachusetts Institute of Technology"
   - "UCLA" → "University of California, Los Angeles"
   - "CU Boulder" → "University of Colorado Boulder"
   - "UIUC" → "University of Illinois Urbana-Champaign"
   - "NYU" → "New York University"
   - "CMU" → "Carnegie Mellon University"
   - "GT" or "Georgia Tech" → "Georgia Institute of Technology"

2. Standardize all format variations to the official name:
   - "U of Chicago" → "University of Chicago"
   - "UC Berkeley" → "University of California, Berkeley"
   - "Penn State" → "Pennsylvania State University"
   - "Cal Tech" → "California Institute of Technology"

3. Fix ALL typos and misspellings:
   - "Univeristy of San Francisco" → "University of San Francisco"
   - "Standford" → "Stanford University"

4. Remove ALL department/school/lab/center information:
   - "MIT Department of Physics" → "Massachusetts Institute of Technology"
   - "Stanford School of Medicine" → "Stanford University"
   - "University of Texas at Austin, Department of Chemistry" → "University of Texas at Austin"

5. For multi-campus systems, standardize campus names:
   - "UCSD" → "University of California, San Diego"
   - "UT Dallas" → "University of Texas at Dallas"
   - "SUNY Buffalo" → "University at Buffalo"

6. For international universities, use the standard English name:
   - "Universität München" → "Ludwig Maximilian University of Munich"
   - "EPFL" → "École Polytechnique Fédérale de Lausanne"

7. Handle special cases:
   - National labs: Prefix with "ORG: " (e.g., "ORG: Fermi National Accelerator Laboratory")
   - Companies: Prefix with "ORG: " (e.g., "ORG: Google")
   - If truly ambiguous or invalid: Return "INVALID"

8. Always return the MOST OFFICIAL, COMPLETE name you know.

Universities to standardize:
{chr(10).join(f'{i+1}. "{name}"' for i, name in enumerate(names_list))}

Return ONLY a JSON array with the standardized names in the SAME ORDER. Use your full knowledge to get the official names right."""

        try:
            response = await self.client.chat.completions.create(
                model="gpt-4o",  # Using GPT-4o for better accuracy
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                response_format={"type": "json_object"}
            )
            
            content = response.choices[0].message.content
            data = json.loads(content)
            
            # Extract the results
            if isinstance(data, list):
                results = data
            elif isinstance(data, dict):
                # Try to find a list in the response
                for key, value in data.items():
                    if isinstance(value, list) and len(value) == len(universities):
                        results = value
                        break
                else:
                    # If no list found, try values
                    if len(data) == len(universities):
                        results = list(data.values())
                    else:
                        logger.error(f"Unexpected response format: {data}")
                        results = names_list
            else:
                logger.error(f"Unexpected response type: {type(data)}")
                results = names_list
            
            # Create mapping
            mapping = {}
            for (original, count), standardized in zip(universities, results):
                mapping[original] = standardized
                self.cache[original] = standardized
            
            return mapping
            
        except Exception as e:
            logger.error(f"Error in comprehensive LLM standardization: {e}")
            # Return original names as fallback
            return {name: name for name, _ in universities}
    
    async def standardize_all_universities(self, university_counts: Dict[str, int]) -> Dict[str, str]:
        """Standardize all universities in the dataset"""
        logger.info("Starting comprehensive standardization...")
        
        # Filter out already cached entries
        need_standardization = []
        results = {}
        
        for uni, count in university_counts.items():
            if uni in self.cache:
                results[uni] = self.cache[uni]
            else:
                need_standardization.append((uni, count))
        
        logger.info(f"Already cached: {len(results)}")
        logger.info(f"Need standardization: {len(need_standardization)}")
        
        # Sort by count (descending) to prioritize common universities
        need_standardization.sort(key=lambda x: x[1], reverse=True)
        
        # Process in batches of 25 for better LLM performance
        batch_size = 25
        for i in range(0, len(need_standardization), batch_size):
            batch = need_standardization[i:i+batch_size]
            logger.info(f"Processing batch {i//batch_size + 1}/{(len(need_standardization) + batch_size - 1)//batch_size}")
            
            batch_results = await self.standardize_batch_comprehensive(batch)
            results.update(batch_results)
            
            # Save cache periodically
            if (i + batch_size) % 100 == 0:
                self._save_cache()
        
        # Final cache save
        self._save_cache()
        
        return results
    
    def generate_report(self, original_counts: Dict[str, int], standardized_mapping: Dict[str, str]) -> str:
        """Generate a detailed report of the standardization"""
        # Count standardized universities
        standardized_counts = Counter()
        for original, standardized in standardized_mapping.items():
            count = original_counts.get(original, 0)
            standardized_counts[standardized] += count
        
        report = []
        report.append("="*80)
        report.append("COMPREHENSIVE UNIVERSITY STANDARDIZATION REPORT")
        report.append("="*80)
        report.append(f"\nOriginal unique universities: {len(original_counts)}")
        report.append(f"Standardized unique universities: {len(standardized_counts)}")
        report.append(f"Reduction: {len(original_counts) - len(standardized_counts)} ({(1 - len(standardized_counts)/len(original_counts))*100:.1f}%)")
        
        # Find biggest consolidations
        consolidations = {}
        for original, standardized in standardized_mapping.items():
            if original != standardized:
                if standardized not in consolidations:
                    consolidations[standardized] = []
                consolidations[standardized].append((original, original_counts.get(original, 0)))
        
        # Sort by number of variations consolidated
        sorted_consolidations = sorted(consolidations.items(), 
                                     key=lambda x: sum(count for _, count in x[1]), 
                                     reverse=True)
        
        report.append("\n" + "="*80)
        report.append("TOP CONSOLIDATIONS (by total occurrences)")
        report.append("="*80)
        
        for i, (standardized, originals) in enumerate(sorted_consolidations[:20]):
            if len(originals) > 1:  # Only show actual consolidations
                total = sum(count for _, count in originals)
                report.append(f"\n{i+1}. {standardized} ({total} total occurrences)")
                sorted_originals = sorted(originals, key=lambda x: x[1], reverse=True)
                for orig, count in sorted_originals[:5]:  # Show top 5 variations
                    if orig != standardized:
                        report.append(f"   ← {orig} ({count})")
                if len(originals) > 5:
                    report.append(f"   ... and {len(originals)-5} more variations")
        
        return "\n".join(report)


async def main():
    """Run comprehensive standardization on the dataset"""
    # Load the current dataset
    data_file = Path(__file__).parent.parent / 'processed' / 'master-data-final.csv'
    
    if not data_file.exists():
        logger.error(f"Dataset not found at {data_file}")
        logger.info("Running data pipeline first...")
        os.system("cd .. && ./run_final_pipeline.sh")
    
    logger.info(f"Loading dataset from {data_file}")
    df = pd.read_csv(data_file, low_memory=False)
    
    # Initialize standardizer
    standardizer = ComprehensiveUniversityStandardizer()
    
    # Extract all universities
    university_counts = await standardizer.analyze_all_universities(df)
    
    # Standardize all universities
    standardized_mapping = await standardizer.standardize_all_universities(university_counts)
    
    # Generate report
    report = standardizer.generate_report(university_counts, standardized_mapping)
    print(report)
    
    # Save report
    report_file = Path(__file__).parent / 'comprehensive_standardization_report.txt'
    with open(report_file, 'w') as f:
        f.write(report)
    logger.info(f"Report saved to {report_file}")
    
    # Apply standardizations to dataset
    logger.info("Applying standardizations to dataset...")
    
    # Apply to all university columns
    for col in df.columns:
        if 'university' in col.lower() and 'standardized' not in col:
            standardized_col = col + '_standardized'
            df[standardized_col] = df[col].map(standardized_mapping).fillna(df[col])
    
    # Save updated dataset
    logger.info("Saving updated dataset...")
    df.to_csv(data_file, index=False)
    
    # Update summary
    summary = {
        'total_seminars': len(df),
        'seminars_with_speakers': len(df[df['speaker_1_name'].notna()]),
        'total_speaker_appearances': sum(df[f'speaker_{i}_name'].notna().sum() for i in range(1, 129)),
        'unique_speakers_by_name_discipline_affiliation': len(df[['speaker_1_name', 'speaker_1_discipline', 'speaker_1_university_standardized']].drop_duplicates()),
        'speakers_with_rank': sum(df[f'speaker_{i}_rank'].notna().sum() for i in range(1, 129)),
        'speakers_with_standardized_rank': sum(df[f'speaker_{i}_rank_standardized'].notna().sum() for i in range(1, 129)),
        'timestamp': datetime.now().isoformat()
    }
    
    summary_file = Path(__file__).parent.parent / 'processed' / 'final_dataset_summary.json'
    with open(summary_file, 'w') as f:
        json.dump(summary, f, indent=2)
    
    logger.info("Comprehensive standardization complete!")


if __name__ == "__main__":
    asyncio.run(main())