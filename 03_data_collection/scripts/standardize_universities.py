#!/usr/bin/env python3
"""
University standardization to extract parent institutions
Normalizes to superordinate university, removing departments/labs/centers
Uses LLM to handle complex affiliations and medical schools
"""

import pandas as pd
import numpy as np
import json
import asyncio
from pathlib import Path
import os
from typing import Dict, List, Optional, Set, Tuple
import re
from datetime import datetime
import logging
from openai import AsyncOpenAI
from dotenv import load_dotenv
import pickle

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
STANDARDIZATION_CACHE = CACHE_DIR / 'university_standardization_cache.pkl'
KNOWN_UNIVERSITIES = CACHE_DIR / 'known_universities.json'

class UniversityStandardizer:
    def __init__(self):
        self.cache = self._load_cache()
        self.known_mappings = self._load_known_mappings()
        self.api_key = os.getenv('OPENAI_API_KEY')
        if self.api_key:
            self.client = AsyncOpenAI(api_key=self.api_key)
        else:
            logger.warning("No OpenAI API key found - will use pattern matching only")
            self.client = None
    
    def _load_cache(self) -> Dict[str, str]:
        """Load existing standardization cache"""
        if STANDARDIZATION_CACHE.exists():
            with open(STANDARDIZATION_CACHE, 'rb') as f:
                return pickle.load(f)
        return {}
    
    def _save_cache(self):
        """Save cache to file"""
        with open(STANDARDIZATION_CACHE, 'wb') as f:
            pickle.dump(self.cache, f)
        logger.info(f"Saved {len(self.cache)} mappings to cache")
    
    def _load_known_mappings(self) -> Dict[str, str]:
        """Load comprehensive mapping of common variations"""
        # Common university abbreviations and variations
        mappings = {
            # Common US Universities
            'mit': 'Massachusetts Institute of Technology',
            'massachusetts institute of technology': 'Massachusetts Institute of Technology',
            'mass inst tech': 'Massachusetts Institute of Technology',
            'mass. inst. tech.': 'Massachusetts Institute of Technology',
            
            'harvard': 'Harvard University',
            'harvard u': 'Harvard University',
            'harvard univ': 'Harvard University',
            
            'stanford': 'Stanford University',
            'stanford u': 'Stanford University',
            'stanford univ': 'Stanford University',
            
            'berkeley': 'University of California, Berkeley',
            'uc berkeley': 'University of California, Berkeley',
            'ucb': 'University of California, Berkeley',
            'university of california berkeley': 'University of California, Berkeley',
            'univ of california berkeley': 'University of California, Berkeley',
            'u.c. berkeley': 'University of California, Berkeley',
            
            'ucla': 'University of California, Los Angeles',
            'uc los angeles': 'University of California, Los Angeles',
            'university of california los angeles': 'University of California, Los Angeles',
            
            'ucsd': 'University of California, San Diego',
            'uc san diego': 'University of California, San Diego',
            'university of california san diego': 'University of California, San Diego',
            
            'ucsb': 'University of California, Santa Barbara',
            'uc santa barbara': 'University of California, Santa Barbara',
            
            'nyu': 'New York University',
            'new york u': 'New York University',
            'new york univ': 'New York University',
            
            'columbia': 'Columbia University',
            'columbia u': 'Columbia University',
            'columbia univ': 'Columbia University',
            
            'princeton': 'Princeton University',
            'princeton u': 'Princeton University',
            'princeton univ': 'Princeton University',
            
            'yale': 'Yale University',
            'yale u': 'Yale University',
            'yale univ': 'Yale University',
            
            'cornell': 'Cornell University',
            'cornell u': 'Cornell University',
            'cornell univ': 'Cornell University',
            
            'upenn': 'University of Pennsylvania',
            'u penn': 'University of Pennsylvania',
            'penn': 'University of Pennsylvania',
            'univ of pennsylvania': 'University of Pennsylvania',
            
            'caltech': 'California Institute of Technology',
            'cal tech': 'California Institute of Technology',
            'california inst tech': 'California Institute of Technology',
            
            'cmu': 'Carnegie Mellon University',
            'carnegie mellon': 'Carnegie Mellon University',
            'carnegie mellon u': 'Carnegie Mellon University',
            
            # University of Hawaii variations (addressing your specific issue)
            'u hawaii': 'University of Hawaii',
            'u of hawaii': 'University of Hawaii',
            'univ hawaii': 'University of Hawaii',
            'univ of hawaii': 'University of Hawaii',
            'university of hawaii': 'University of Hawaii',
            'u hawaii manoa': 'University of Hawaii at Manoa',
            'uh manoa': 'University of Hawaii at Manoa',
            'university of hawaii manoa': 'University of Hawaii at Manoa',
            'university of hawaii at manoa': 'University of Hawaii at Manoa',
            'u hawaii hilo': 'University of Hawaii at Hilo',
            'uh hilo': 'University of Hawaii at Hilo',
            'university of hawaii hilo': 'University of Hawaii at Hilo',
            'university of hawaii at hilo': 'University of Hawaii at Hilo',
            
            # State universities
            'asu': 'Arizona State University',
            'arizona state': 'Arizona State University',
            'arizona state u': 'Arizona State University',
            
            'osu': 'Ohio State University',
            'ohio state': 'Ohio State University',
            'the ohio state university': 'Ohio State University',
            
            'msu': 'Michigan State University',
            'michigan state': 'Michigan State University',
            'michigan state u': 'Michigan State University',
            
            'psu': 'Pennsylvania State University',
            'penn state': 'Pennsylvania State University',
            'pennsylvania state': 'Pennsylvania State University',
            
            # International
            'oxford': 'University of Oxford',
            'oxford u': 'University of Oxford',
            'oxford university': 'University of Oxford',
            
            'cambridge': 'University of Cambridge',
            'cambridge u': 'University of Cambridge',
            'cambridge university': 'University of Cambridge',
            
            'eth': 'ETH Zurich',
            'eth zurich': 'ETH Zurich',
            
            # Medical schools and their parent universities
            'albert einstein college of medicine': 'Yeshiva University',
            'albert einstein': 'Yeshiva University',
            'weill cornell medicine': 'Cornell University',
            'weill cornell medical college': 'Cornell University',
            'harvard medical school': 'Harvard University',
            'yale school of medicine': 'Yale University',
            'stanford school of medicine': 'Stanford University',
            'johns hopkins school of medicine': 'Johns Hopkins University',
            'perelman school of medicine': 'University of Pennsylvania',
            'pritzker school of medicine': 'University of Chicago',
            'david geffen school of medicine': 'University of California, Los Angeles',
            'keck school of medicine': 'University of Southern California',
            'icahn school of medicine': 'Mount Sinai Health System',
            'nyu school of medicine': 'New York University',
            'nyu grossman school of medicine': 'New York University',
            'columbia vagelos college': 'Columbia University',
            'warren alpert medical school': 'Brown University',
            'geisel school of medicine': 'Dartmouth College',
            
            # Texas universities
            'texas a&m': 'Texas A&M University',
            'tamu': 'Texas A&M University',
            'ut austin': 'University of Texas at Austin',
            'ut dallas': 'University of Texas at Dallas',
            'rice': 'Rice University',
            
            # Other common variations
            'lehigh': 'Lehigh University',
            'lehigh u': 'Lehigh University',
            'cuny': 'City University of New York',
            
            # Labs/Centers that should map to universities
            'ipac': 'California Institute of Technology',  # IPAC is at Caltech
            'fermilab': 'ORG: Fermi National Accelerator Laboratory',
            'cern': 'ORG: CERN',
            'brookhaven': 'ORG: Brookhaven National Laboratory',
            
            # Satellite campuses (keep as separate)
            'nyu shanghai': 'New York University Shanghai',
            'nyu abu dhabi': 'New York University Abu Dhabi',
        }
        
        # Create case-insensitive version
        case_insensitive = {}
        for k, v in mappings.items():
            case_insensitive[k.lower()] = v
        
        return case_insensitive
    
    def _clean_name(self, name: str) -> str:
        """Clean and preprocess university name"""
        if pd.isna(name) or str(name).strip() == '':
            return ''
        
        name = str(name).strip()
        
        # Remove common noise
        name = re.sub(r'\d{1,2}/\d{1,2}/\d{2,4}', '', name)  # dates
        name = re.sub(r'\d{4}-\d{2}-\d{2}', '', name)  # ISO dates
        name = re.sub(r'\s+', ' ', name)  # multiple spaces
        # Keep alphanumeric, spaces, commas, dots, hyphens, AND ampersands
        name = re.sub(r'[^\w\s,.&-]', '', name)
        name = name.strip()
        
        # Skip if empty or just numbers
        if not name or re.match(r'^[\d\s\-/]+$', name):
            return ''
        
        return name
    
    def _extract_parent_university(self, name: str) -> Optional[str]:
        """Extract parent university from complex affiliations"""
        name_clean = name.strip()
        
        # First check if it's already in our known mappings
        if name_clean.lower() in self.known_mappings:
            return self.known_mappings[name_clean.lower()]
        
        # Patterns to extract parent university
        extraction_patterns = [
            # First check for "X Lab Group, University Name" pattern (like "Zhao Lab Group, University of California, Riverside")
            (r'^[^,]+\s+(?:lab|laboratory)\s+(?:group|team)?,\s*(.+)$', r'\1'),
            
            # Extract university from "University Name, Department of X" (must be more specific)
            (r'^(.+?)\s*,\s*department\s+of\s+.+$', r'\1'),
            
            # Extract university from "Department/Lab/Center, University Name"
            (r'^[^,]+(?:department|dept|lab|laboratory|center|centre|institute|school|college|division|program|group)[^,]*,\s*(.+)$', r'\1'),
            
            # Extract university from "University Name, Department/Lab/etc" (general)
            (r'^(.+?),\s*(?:department|dept|lab|laboratory|center|centre|institute|school|college|division|program|group|ipac).+$', r'\1'),
            
            # Handle "School/College of X" patterns
            (r'^(.+?)\s+(?:school|college)\s+of\s+(?:medicine|medical sciences?|engineering|business|law|education|nursing|public health),?\s*(.*)$', None),  # Special handling
            
            # Remove trailing lab/center/institute info
            (r'^(.+?)\s*[-–]\s*(?:department|dept|lab|laboratory|center|centre|institute|ipac|division).*$', r'\1'),
            (r'^(.+?)\s+(?:department|dept|lab|laboratory|center|centre|institute|ipac|division).*$', r'\1'),
            
            # Handle "X Industrial and Systems Engineering" type patterns (Lehigh example)
            (r'^(.+?)\s+(?:industrial|mechanical|electrical|chemical|civil|computer|biomedical)\s+(?:and\s+\w+\s+)?engineering.*$', r'\1'),
            
            # Remove parenthetical additions
            (r'^(.+?)\s*\([^)]+\)\s*$', r'\1'),
            
            # Special case for "X at Y" where Y is the university
            (r'^[^,]+\s+at\s+(.+)$', r'\1'),
        ]
        
        for pattern, replacement in extraction_patterns:
            match = re.search(pattern, name_clean, re.IGNORECASE)
            if match:
                if replacement is None:
                    # Special handling for medical schools
                    school_name = match.group(1)
                    parent_info = match.group(2) if match.lastindex >= 2 else ""
                    
                    # Check if parent university is mentioned after the comma
                    if parent_info:
                        return self._extract_parent_university(parent_info)
                    else:
                        # Try to map known schools to parent universities
                        school_map = {
                            # Medical schools
                            'albert einstein': 'Yeshiva University',
                            'icahn': 'Mount Sinai Health System',
                            'mount sinai': 'Mount Sinai Health System',
                            'weill cornell': 'Cornell University',
                            'pritzker': 'University of Chicago',
                            'perelman': 'University of Pennsylvania',
                            'keck': 'University of Southern California',
                            'david geffen': 'University of California, Los Angeles',
                            'stanford': 'Stanford University',
                            'harvard': 'Harvard University',
                            'yale': 'Yale University',
                            'johns hopkins': 'Johns Hopkins University',
                            'nyu grossman': 'New York University',
                            'nyu langone': 'New York University',
                            'columbia vagelos': 'Columbia University',
                            'warren alpert': 'Brown University',
                            'geisel': 'Dartmouth College',
                            'feinberg': 'Northwestern University',
                            'mayo clinic alix': 'Mayo Clinic',
                            
                            # Engineering schools
                            'tandon': 'New York University',
                            'viterbi': 'University of Southern California',
                            'mccormick': 'Northwestern University',
                            'whiting': 'Johns Hopkins University',
                            'jacobs': 'University of California, San Diego',
                        }
                        
                        school_lower = school_name.lower()
                        for key, parent in school_map.items():
                            if key in school_lower:
                                return parent
                        
                        # If no mapping found, extract base university name
                        if 'university' in school_lower:
                            return self._standardize_with_patterns(school_name)
                        else:
                            return school_name + " University"
                else:
                    result = re.sub(pattern, replacement, name_clean, flags=re.IGNORECASE)
                    # Recursively clean in case there are multiple levels
                    return self._extract_parent_university(result.strip())
        
        # Try basic standardization patterns
        return self._standardize_with_patterns(name_clean)
    
    def _standardize_with_patterns(self, name: str) -> Optional[str]:
        """Try to standardize university name format"""
        name_lower = name.lower().strip()
        
        # Check exact matches in known mappings
        if name_lower in self.known_mappings:
            return self.known_mappings[name_lower]
        
        # Basic standardization patterns
        patterns = [
            # University of X patterns
            (r'^u\.?\s+(?:of\s+)?(.+)$', r'University of \1'),
            (r'^univ\.?\s+(?:of\s+)?(.+)$', r'University of \1'),
            
            # X University patterns (but not if it's already "X University")
            (r'^(.+?)(?<!\suniversity)\s+u\.?$', r'\1 University'),
            (r'^(.+?)(?<!\suniversity)\s+univ\.?$', r'\1 University'),
            
            # UC System
            (r'^uc\s+(.+)$', r'University of California, \1'),
            (r'^u\.?c\.?\s+(.+)$', r'University of California, \1'),
            
            # State universities
            (r'^(.+?)\s+state\s*$', r'\1 State University'),
            
            # Institute patterns
            (r'^(.+?)\s+inst\.?\s*$', r'\1 Institute'),
            (r'^(.+?)\s+inst\.?\s+of\s+tech(?:nology)?\.?$', r'\1 Institute of Technology'),
        ]
        
        for pattern, replacement in patterns:
            match = re.match(pattern, name_lower)
            if match:
                result = re.sub(pattern, replacement, name_lower)
                # Proper case the result
                words = result.split()
                capitalized = []
                for word in words:
                    if word.lower() in ['of', 'at', 'the', 'and', 'for', 'in']:
                        capitalized.append(word.lower())
                    else:
                        capitalized.append(word.capitalize())
                # Always capitalize first word
                if capitalized:
                    capitalized[0] = capitalized[0].capitalize()
                return ' '.join(capitalized)
        
        return None
    
    async def standardize_universities_batch(self, universities: List[str]) -> Dict[str, str]:
        """Standardize a batch of university names efficiently"""
        results = {}
        need_llm = []
        
        # Process all universities
        for uni in universities:
            cleaned = self._clean_name(uni)
            
            if not cleaned:
                results[uni] = uni  # Return original if can't clean
                continue
            
            # Check cache first
            if cleaned in self.cache:
                results[uni] = self.cache[cleaned]
                continue
            
            # Check if it's in our known mappings (high confidence)
            if cleaned.lower() in self.known_mappings:
                standardized = self.known_mappings[cleaned.lower()]
                results[uni] = standardized
                self.cache[cleaned] = standardized
                continue
            
            # Everything else goes to LLM for accurate extraction
            need_llm.append((uni, cleaned))
        
        # Second pass: Use LLM for remaining
        if need_llm and self.client:
            logger.info(f"Using LLM for {len(need_llm)} universities...")
            
            # Process in batches of 50 for efficiency
            for i in range(0, len(need_llm), 50):
                batch = need_llm[i:i+50]
                batch_results = await self._standardize_batch_llm(batch)
                
                for (original, cleaned), standardized in zip(batch, batch_results):
                    results[original] = standardized
                    self.cache[cleaned] = standardized
        
        # Save cache after processing
        self._save_cache()
        
        return results
    
    async def _standardize_batch_llm(self, batch: List[Tuple[str, str]]) -> List[str]:
        """Standardize a batch of universities using LLM"""
        names_list = [cleaned for _, cleaned in batch]
        
        prompt = f"""Extract and standardize the PARENT UNIVERSITY from these affiliations. 

CRITICAL RULES:
1. Extract the main university, NOT departments/labs/centers/schools
2. Use full official names (e.g., "MIT" → "Massachusetts Institute of Technology")
3. Remove ALL department/lab/center/program info
4. ONLY preserve satellite campuses if they're separate institutions
5. If it's truly a company/non-academic org with NO university affiliation, prefix with "ORG: "
6. If invalid/unclear, return "INVALID"

EXAMPLES:
- "Yale School of Medicine" → "Yale University"
- "MIT Department of Physics" → "Massachusetts Institute of Technology"
- "Texas A&M University, Department of Mathematics" → "Texas A&M University"
- "Zhao Lab Group, University of California, Riverside" → "University of California, Riverside"
- "California Institute of Technology, IPAC" → "California Institute of Technology"
- "Albert Einstein College of Medicine" → "Yeshiva University"
- "Harvard Medical School" → "Harvard University"
- "Stanford School of Engineering" → "Stanford University"
- "Lehigh Industrial and Systems Engineering" → "Lehigh University"
- "Columbia University, Department of Computer Science" → "Columbia University"
- "NYU Shanghai" → "New York University Shanghai"
- "Google Research" → "ORG: Google"
- "IBM Research" → "ORG: IBM"

Affiliations to standardize:
{chr(10).join(f'{i+1}. "{name}"' for i, name in enumerate(names_list))}

Return ONLY a JSON array with the PARENT UNIVERSITIES in the same order."""

        try:
            response = await self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                response_format={"type": "json_object"}
            )
            
            content = response.choices[0].message.content
            # Try to extract array from JSON response
            import json
            data = json.loads(content)
            
            # Handle different response formats
            if isinstance(data, list):
                return data
            elif isinstance(data, dict):
                # Try to find a list in the response
                for key, value in data.items():
                    if isinstance(value, list) and len(value) == len(batch):
                        return value
                # If dict but no list found, try to extract values
                if len(data) == len(batch):
                    return list(data.values())
            
            # Fallback - return cleaned names
            return [cleaned for _, cleaned in batch]
                
        except Exception as e:
            logger.error(f"Error in LLM standardization: {e}")
            # Return cleaned versions as fallback
            return [cleaned for _, cleaned in batch]


# Convenience function for use in other scripts
async def standardize_universities(universities: List[str]) -> Dict[str, str]:
    """Standardize a list of university names"""
    standardizer = UniversityStandardizer()
    return await standardizer.standardize_universities_batch(universities)


if __name__ == "__main__":
    # Test the standardizer
    test_unis = [
        "MIT",
        "U Hawaii",
        "University of Hawaii",
        "UH Manoa",
        "UC Berkeley",
        "Stanford",
        "harvard",
        "ASU",
        "Ohio State",
        "Google Research",
        "12/31/2024",
        ""
    ]
    
    async def test():
        standardizer = UniversityStandardizer()
        results = await standardizer.standardize_universities_batch(test_unis)
        
        print("\nStandardization Results:")
        print("-" * 50)
        for original, standardized in results.items():
            if original != standardized:
                print(f"{original:<30} → {standardized}")
    
    asyncio.run(test())