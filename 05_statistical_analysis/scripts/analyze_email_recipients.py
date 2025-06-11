"""
Analyze demographics of email recipients to create moderator variables.

This script:
1. Loads email recipient data from the campaign files
2. Extracts unique recipients per department
3. Runs demographic analysis using existing name analysis pipeline
4. Calculates department-level percentages for moderation analysis
"""
import pandas as pd
import numpy as np
import json
import asyncio
import logging
import sys
from pathlib import Path
from typing import Dict, List, Tuple
import re
import os
from dotenv import load_dotenv

# Add parent directories to path
sys.path.append(str(Path(__file__).parent.parent.parent))
from core.normalization import normalize_text

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('email_recipient_analysis.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# We'll use OpenAI directly for name analysis
import openai
from openai import AsyncOpenAI

def extract_title(contact_name: str) -> tuple[str, str]:
    """Extract title and clean name from contact_name field."""
    if pd.isna(contact_name):
        return None, None
    
    # Common academic titles
    titles = [
        'Professor', 'Prof.', 'Prof', 'Dr.', 'Dr', 
        'Assistant Professor', 'Associate Professor',
        'Asst. Professor', 'Assoc. Professor'
    ]
    
    name = contact_name.strip()
    extracted_title = None
    
    # Check for titles at the beginning
    for title in titles:
        if name.lower().startswith(title.lower()):
            extracted_title = title
            name = name[len(title):].strip()
            break
    
    # Clean any remaining punctuation
    name = re.sub(r'^[,\s]+', '', name)
    
    return extracted_title, name

def load_existing_results(cache_file: str) -> Dict:
    """Load existing results from cache file."""
    if Path(cache_file).exists():
        with open(cache_file, 'r') as f:
            return json.load(f)
    return {}

def save_results(results: Dict, cache_file: str):
    """Save results to cache file."""
    # Create directory if it doesn't exist
    Path(cache_file).parent.mkdir(parents=True, exist_ok=True)
    with open(cache_file, 'w') as f:
        json.dump(results, f, indent=2)

async def analyze_name_batch(names: List[Tuple[str, str]], client: AsyncOpenAI) -> Dict:
    """Analyze a batch of names for demographics."""
    # Create prompt for batch analysis
    names_text = "\n".join([f"{i+1}. {name[0]}" for i, name in enumerate(names)])
    
    prompt = f"""Analyze the following names and infer likely gender and race/ethnicity based on the name alone.
For each name, provide your best guess for:
- Gender: Male, Female, or Unknown
- Race: White, Black, Hispanic, Asian, Native American, or Unknown

Format your response as a JSON array with objects containing: number, gender, race

Names:
{names_text}
"""

    try:
        response = await client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert at demographic inference from names. Provide your best assessment based on name patterns."},
                {"role": "user", "content": prompt}
            ],
            temperature=0,
            response_format={ "type": "json_object" }
        )
        
        # Parse response
        content = response.choices[0].message.content
        data = json.loads(content)
        
        # Handle both array and object responses
        if isinstance(data, dict) and 'results' in data:
            results_array = data['results']
        elif isinstance(data, list):
            results_array = data
        else:
            # Try to extract array from the response
            results_array = list(data.values())[0] if data else []
        
        # Map results back to names
        results = {}
        for i, (display_name, normalized_name) in enumerate(names):
            if i < len(results_array):
                result = results_array[i]
                results[normalized_name] = {
                    'gender': result.get('gender', 'Unknown'),
                    'race': result.get('race', 'Unknown'),
                    'display_name': display_name
                }
            else:
                results[normalized_name] = {
                    'gender': 'Unknown',
                    'race': 'Unknown',
                    'display_name': display_name
                }
        
        return results
        
    except Exception as e:
        logger.error(f"Error analyzing batch: {str(e)}")
        # Return unknown for all names in case of error
        return {
            name[1]: {
                'gender': 'Unknown',
                'race': 'Unknown', 
                'display_name': name[0]
            } for name in names
        }

def classify_academic_rank(title: str) -> str:
    """Classify academic rank from title."""
    if pd.isna(title) or not title:
        return 'Unknown'
    
    title_lower = title.lower()
    
    if 'assistant' in title_lower:
        return 'Assistant Professor'
    elif 'associate' in title_lower:
        return 'Associate Professor'
    elif 'professor' in title_lower or 'prof' in title_lower:
        return 'Full Professor'
    elif 'dr' in title_lower:
        return 'PhD/Researcher'
    else:
        return 'Unknown'

async def analyze_recipients():
    """Main function to analyze email recipients."""
    logger.info("Starting email recipient analysis...")
    
    # Load email campaign data
    email_file = Path(__file__).parent.parent.parent / "02_intervention_materials" / "email_campaigns" / "email-launch.csv"
    logger.info(f"Loading email data from {email_file}")
    
    email_df = pd.read_csv(email_file)
    logger.info(f"Loaded {len(email_df)} email records")
    
    # Extract unique recipients with their departments
    recipients_df = email_df[['contact_name', 'department', 'contact_type']].copy()
    
    # Extract titles and clean names
    recipients_df[['title', 'clean_name']] = recipients_df['contact_name'].apply(
        lambda x: pd.Series(extract_title(x))
    )
    
    # Classify academic ranks
    recipients_df['academic_rank'] = recipients_df['title'].apply(classify_academic_rank)
    
    # Normalize names for demographic analysis
    recipients_df['normalized_name'] = recipients_df['clean_name'].apply(
        lambda x: normalize_text(x) if pd.notna(x) else None
    )
    
    # Remove duplicates and invalid entries
    valid_recipients = recipients_df[recipients_df['normalized_name'].notna()].copy()
    unique_recipients = valid_recipients.drop_duplicates(subset=['normalized_name', 'department'])
    
    logger.info(f"Found {len(unique_recipients)} unique recipients across departments")
    
    # Prepare for demographic analysis
    names_for_analysis = unique_recipients[['normalized_name', 'clean_name']].drop_duplicates()
    logger.info(f"Analyzing {len(names_for_analysis)} unique names")
    
    # Run demographic analysis
    cache_file = Path(__file__).parent.parent / "outputs" / "email_recipient_demographics_cache.json"
    existing_results = load_existing_results(str(cache_file))
    
    # Filter out names we've already analyzed
    new_names = names_for_analysis[
        ~names_for_analysis['normalized_name'].isin(existing_results.keys())
    ]
    
    if len(new_names) > 0:
        logger.info(f"Analyzing {len(new_names)} new names...")
        
        # Initialize OpenAI client
        client = AsyncOpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        
        # Prepare batches for analysis
        names_list = new_names[['clean_name', 'normalized_name']].values.tolist()
        batch_size = 25  # Smaller batches for better accuracy
        batches = [names_list[i:i+batch_size] for i in range(0, len(names_list), batch_size)]
        
        # Run async analysis
        all_results = existing_results.copy()
        
        for i, batch in enumerate(batches):
            logger.info(f"Processing batch {i+1}/{len(batches)}")
            try:
                batch_results = await analyze_name_batch(batch, client)
                all_results.update(batch_results)
                
                # Save progress
                if (i + 1) % 5 == 0:
                    save_results(all_results, str(cache_file))
                    logger.info(f"Saved progress after batch {i+1}")
                    
                # Small delay to avoid rate limits
                await asyncio.sleep(0.5)
                
            except Exception as e:
                logger.error(f"Error in batch {i+1}: {str(e)}")
                continue
        
        # Save final results
        save_results(all_results, str(cache_file))
    else:
        logger.info("All names already analyzed, using cached results")
        all_results = existing_results
    
    # Merge results back to recipients
    demographics_data = []
    for name in unique_recipients['normalized_name']:
        if name in all_results:
            demo = all_results[name]
            demographics_data.append({
                'normalized_name': name,
                'gender_name': demo.get('gender'),
                'race_name': demo.get('race'),
                'is_female': 1 if demo.get('gender') == 'Female' else 0,
                'is_urm': 1 if demo.get('race') in ['Black', 'Hispanic', 'Native American'] else 0,
                'is_black': 1 if demo.get('race') == 'Black' else 0,
                'is_hispanic': 1 if demo.get('race') == 'Hispanic' else 0
            })
    
    demographics_df = pd.DataFrame(demographics_data)
    unique_recipients = unique_recipients.merge(demographics_df, on='normalized_name', how='left')
    
    # Calculate department-level statistics
    dept_stats = unique_recipients.groupby('department').agg({
        'normalized_name': 'count',  # Total recipients
        'is_female': ['sum', 'mean'],
        'is_urm': ['sum', 'mean'],
        'is_black': ['sum', 'mean'],
        'is_hispanic': ['sum', 'mean'],
        'academic_rank': lambda x: (x == 'Assistant Professor').sum()
    }).round(4)
    
    dept_stats.columns = [
        'num_email_recipients',
        'num_female_recipients',
        'pct_female_recipients',
        'num_urm_recipients',
        'pct_urm_recipients',
        'num_black_recipients',
        'pct_black_recipients',
        'num_hispanic_recipients',
        'pct_hispanic_recipients',
        'num_assistant_prof_recipients'
    ]
    
    # Add percentage of assistant professors
    dept_stats['pct_assistant_prof_recipients'] = (
        dept_stats['num_assistant_prof_recipients'] / dept_stats['num_email_recipients']
    ).round(4)
    
    # Clean department names to match master dataset format
    dept_stats['department_clean'] = dept_stats.index.str.replace(r'^(.+?)-(.+)$', r'\2-\1', regex=True)
    
    # Save department-level results
    output_file = Path(__file__).parent.parent / "outputs" / "email_recipient_demographics_by_dept.csv"
    dept_stats.to_csv(output_file)
    logger.info(f"Saved department-level statistics to {output_file}")
    
    # Also save detailed recipient data
    detailed_file = Path(__file__).parent.parent / "outputs" / "email_recipient_demographics_detailed.csv"
    unique_recipients.to_csv(detailed_file, index=False)
    logger.info(f"Saved detailed recipient data to {detailed_file}")
    
    # Print summary statistics
    logger.info("\n=== Summary Statistics ===")
    logger.info(f"Total unique recipients: {len(unique_recipients)}")
    logger.info(f"Total departments: {len(dept_stats)}")
    logger.info(f"Overall % female: {unique_recipients['is_female'].mean()*100:.1f}%")
    logger.info(f"Overall % URM: {unique_recipients['is_urm'].mean()*100:.1f}%")
    logger.info(f"Overall % assistant professors: {(unique_recipients['academic_rank'] == 'Assistant Professor').mean()*100:.1f}%")
    
    return dept_stats

if __name__ == "__main__":
    # Run the analysis
    asyncio.run(analyze_recipients())