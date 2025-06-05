#!/usr/bin/env python3
"""
COMPREHENSIVE LLM-based matching between URM database faculty and seminar speakers.

This version maintains discipline-specific matching but dramatically improves coverage by:
1. Checking the top 200 candidates (not just 20) using multiple matching strategies
2. Using fuzzy name matching to catch variations
3. Considering last name matches even with different first names
4. Batching efficiently to minimize API calls while ensuring thorough coverage

Key improvements over original:
- Checks 10x more candidates (200 vs 20)
- Uses multiple pre-filtering strategies (exact, fuzzy, last name, initials)
- Maintains discipline boundaries as intended by the experiment
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json
import asyncio
import aiohttp
from typing import Dict, List, Tuple, Optional, Set
import logging
from datetime import datetime
import os
import re
from unicodedata import normalize
from dotenv import load_dotenv
from fuzzywuzzy import fuzz
import hashlib

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

# Paths
BASE_DIR = Path("/mnt/c/Users/jcerv/Jose/search-costs")
DATABASES_DIR = BASE_DIR / "02_intervention_materials/databases"
OUTPUTS_DIR = BASE_DIR / "05_statistical_analysis/outputs"
CACHE_DIR = BASE_DIR / "05_statistical_analysis/cache"

# Create directories if they don't exist
OUTPUTS_DIR.mkdir(exist_ok=True)
CACHE_DIR.mkdir(exist_ok=True)

# Cache file for LLM results
LLM_CACHE_FILE = CACHE_DIR / "llm_matching_comprehensive_cache.json"

# Configuration
CANDIDATES_PERCENTAGE = 0.35  # Check top 35% of speakers in each discipline
SPEAKERS_PER_BATCH = 50   # Send 50 speakers per LLM call
MAX_CONCURRENT_REQUESTS = 5  # Concurrent API calls


def clean_name(name: str) -> str:
    """Clean and normalize a name by removing special characters and extra spaces."""
    if pd.isna(name) or not isinstance(name, str):
        return ""

    # Normalize unicode characters
    name = normalize("NFD", name).encode("ascii", "ignore").decode("utf-8")

    # Remove non-alphanumeric characters except spaces, hyphens, apostrophes
    name = re.sub(r"[^a-zA-Z\s\-\']", "", name)

    # Replace multiple spaces with single space
    name = re.sub(r"\s+", " ", name)

    # Strip leading/trailing whitespace
    name = name.strip()

    return name


def extract_name_components(name: str) -> Dict[str, str]:
    """Extract first name, last name, and initials from a full name."""
    parts = name.split()
    
    if len(parts) == 0:
        return {"first": "", "last": "", "middle": "", "initials": ""}
    elif len(parts) == 1:
        return {"first": "", "last": parts[0], "middle": "", "initials": parts[0][0].upper() if parts[0] else ""}
    else:
        first = parts[0]
        last = parts[-1]
        middle = " ".join(parts[1:-1]) if len(parts) > 2 else ""
        
        # Create initials (first + middle initials + last)
        initials = first[0].upper() if first else ""
        if middle:
            for m in middle.split():
                if m:
                    initials += m[0].upper()
        initials += last[0].upper() if last else ""
        
        return {"first": first, "last": last, "middle": middle, "initials": initials}


def calculate_name_similarity(name1: str, name2: str) -> float:
    """
    Calculate a comprehensive similarity score between two names.
    
    Uses multiple strategies:
    1. Exact match (score = 100)
    2. Fuzzy string matching
    3. Last name matching with first name variations
    4. Initial matching
    """
    if not name1 or not name2:
        return 0
    
    name1_clean = clean_name(name1).lower()
    name2_clean = clean_name(name2).lower()
    
    # Exact match
    if name1_clean == name2_clean:
        return 100
    
    # Get name components
    comp1 = extract_name_components(name1_clean)
    comp2 = extract_name_components(name2_clean)
    
    scores = []
    
    # Full name fuzzy match
    scores.append(fuzz.ratio(name1_clean, name2_clean))
    scores.append(fuzz.token_sort_ratio(name1_clean, name2_clean))
    
    # Last name match is critical
    if comp1["last"] and comp2["last"]:
        last_name_score = fuzz.ratio(comp1["last"], comp2["last"])
        
        # If last names match well, check first names
        if last_name_score > 85:
            # Check if one first name is nickname/short form of other
            if comp1["first"] and comp2["first"]:
                first_score = fuzz.ratio(comp1["first"], comp2["first"])
                # Boost score if last names match and first names are similar
                scores.append((last_name_score + first_score) / 2)
                
                # Check if one name contains the other (e.g., "Rob" in "Robert")
                if comp1["first"] in comp2["first"] or comp2["first"] in comp1["first"]:
                    scores.append(90)
            
            # Check initials match
            if comp1["initials"] and comp2["initials"]:
                if comp1["initials"] == comp2["initials"]:
                    scores.append(85)
                elif comp1["initials"][0] == comp2["initials"][0] and comp1["initials"][-1] == comp2["initials"][-1]:
                    scores.append(80)
    
    return max(scores) if scores else 0


def load_database_faculty() -> pd.DataFrame:
    """Load all URM faculty from the databases."""
    all_faculty = []

    # Map database filenames to disciplines
    discipline_map = {
        "chemistry.csv": "Chemistry",
        "computerScience.csv": "Computer Science",
        "mathematics.csv": "Mathematics",
        "mechanicalEngineering.csv": "Mechanical Engineering",
        "physics.csv": "Physics",
    }

    for filename, discipline in discipline_map.items():
        filepath = DATABASES_DIR / filename
        logger.info(f"Loading {discipline} database from {filepath}")

        df = pd.read_csv(filepath)
        df["discipline"] = discipline
        df["database_file"] = filename

        # Clean the name and extract components
        df["name_cleaned"] = df["Name"].apply(clean_name)
        
        name_components = df["name_cleaned"].apply(extract_name_components)
        df["first_name"] = name_components.apply(lambda x: x["first"])
        df["last_name"] = name_components.apply(lambda x: x["last"])
        df["middle_name"] = name_components.apply(lambda x: x["middle"])
        df["initials"] = name_components.apply(lambda x: x["initials"])
        
        # Create a unique ID for each database faculty
        df["database_id"] = df.apply(
            lambda row: hashlib.md5(f"{row['Name']}_{row['Schools']}_{discipline}".encode()).hexdigest()[:16],
            axis=1
        )

        all_faculty.append(df)

    combined = pd.concat(all_faculty, ignore_index=True)
    logger.info(f"Loaded {len(combined)} total URM faculty from databases")

    return combined


def load_unique_speakers() -> pd.DataFrame:
    """Load unique speakers from the speaker appearances analysis."""
    # Load speaker appearances
    speakers_file = BASE_DIR / "04_demographic_analysis/outputs/speaker_appearances_analysis.csv"
    logger.info(f"Loading speakers from {speakers_file}")

    speakers_df = pd.read_csv(speakers_file)

    # Get unique speakers with their info
    unique_speakers = (
        speakers_df.groupby("speaker_id")
        .agg(
            {
                "name": "first",
                "first_name": "first",
                "last_name": "first",
                "discipline": "first",
                "affiliation_standardized": "first",
                "combined_race": "first",
                "combined_gender": "first",
                "is_urm": "first",
            }
        )
        .reset_index()
    )

    # Clean the names and extract components
    unique_speakers["name_cleaned"] = unique_speakers["name"].apply(clean_name)
    
    name_components = unique_speakers["name_cleaned"].apply(extract_name_components)
    unique_speakers["first_name_cleaned"] = name_components.apply(lambda x: x["first"])
    unique_speakers["last_name_cleaned"] = name_components.apply(lambda x: x["last"])
    unique_speakers["middle_name_cleaned"] = name_components.apply(lambda x: x["middle"])
    unique_speakers["initials"] = name_components.apply(lambda x: x["initials"])

    logger.info(f"Loaded {len(unique_speakers)} unique speakers")

    return unique_speakers


def find_candidate_speakers(
    database_person: Dict,
    discipline_speakers: pd.DataFrame
) -> pd.DataFrame:
    """
    Find the top candidate speakers for a database faculty member.
    
    Uses multiple strategies to ensure we don't miss matches:
    1. Fuzzy name matching
    2. Last name matching
    3. Initial matching
    4. Partial name matching
    
    Checks top 35% of speakers in the discipline for thorough coverage.
    """
    if len(discipline_speakers) == 0:
        return pd.DataFrame()
    
    # Calculate how many candidates to check (35% of discipline speakers)
    top_n = max(1, int(len(discipline_speakers) * CANDIDATES_PERCENTAGE))
    
    # Calculate similarity scores for all speakers in discipline
    scores = []
    
    db_name = database_person["name_cleaned"]
    db_last = database_person.get("last_name", "").lower()
    db_first = database_person.get("first_name", "").lower()
    db_initials = database_person.get("initials", "")
    
    for idx, speaker in discipline_speakers.iterrows():
        speaker_name = speaker["name_cleaned"]
        
        # Calculate comprehensive similarity score based on NAME ONLY
        score = calculate_name_similarity(database_person["Name"], speaker["name"])
        
        scores.append({
            "speaker_id": speaker["speaker_id"],
            "score": score,
            "speaker_name": speaker["name"],
            "speaker_last": speaker.get("last_name_cleaned", ""),
            "match_type": "fuzzy"
        })
    
    # Convert to DataFrame and sort by score
    scores_df = pd.DataFrame(scores)
    scores_df = scores_df.sort_values("score", ascending=False)
    
    # Take top N candidates
    top_candidates_ids = scores_df.head(top_n)["speaker_id"].tolist()
    
    # Get the full speaker records for top candidates
    candidates = discipline_speakers[discipline_speakers["speaker_id"].isin(top_candidates_ids)].copy()
    
    # Add score information
    candidates = candidates.merge(
        scores_df[["speaker_id", "score", "match_type"]], 
        on="speaker_id", 
        how="left"
    )
    
    # Sort by score
    candidates = candidates.sort_values("score", ascending=False)
    
    logger.debug(f"Found {len(candidates)} candidates for {database_person['Name']}")
    logger.debug(f"Top 5 scores: {candidates['score'].head().tolist()}")
    
    return candidates


async def match_batch_with_llm(
    session: aiohttp.ClientSession,
    database_person: Dict,
    speaker_batch: List[Dict],
    cache: Dict,
) -> Optional[Dict]:
    """
    Use LLM to check if a database person matches any speakers in a batch.
    """
    # Create cache key
    batch_ids = "_".join(sorted([s["speaker_id"] for s in speaker_batch]))
    cache_key = f"{database_person['database_id']}_{hashlib.md5(batch_ids.encode()).hexdigest()[:8]}"
    
    # Check cache first
    if cache_key in cache:
        logger.debug(f"Using cached result for {cache_key}")
        return cache.get(cache_key)

    # Prepare the prompt
    prompt = f"""You are an expert at matching academic faculty names. I need you to determine if a faculty member from a URM database matches any speakers in seminar data.

DATABASE FACULTY:
Name: {database_person['Name']} (cleaned: {database_person['name_cleaned']})
Components: First="{database_person.get('first_name', '')}", Last="{database_person.get('last_name', '')}", Middle="{database_person.get('middle_name', '')}"
University: {database_person['Schools']}
Discipline: {database_person['discipline']}
Title: {database_person.get('Title', 'Unknown')}
Race: {database_person.get('Race', 'Unknown')}
Gender: {database_person.get('Gender', 'Unknown')}

POTENTIAL SPEAKER MATCHES (all from {database_person['discipline']}):
"""

    for i, speaker in enumerate(speaker_batch):
        prompt += f"""
{i+1}. {speaker['name']} | {speaker['affiliation_standardized']} | Score: {speaker.get('score', 0):.1f} | ID: {speaker['speaker_id']}"""

    prompt += """

MATCHING CRITERIA:
1. Same person despite name variations (Bob/Robert, Kate/Katherine, etc.)
2. Middle names/initials may be included or omitted
3. Women may have changed last names due to marriage
4. Common misspellings or transcription errors (e.g., "John" vs "Jon")
5. People may have moved between universities
6. Nicknames and shortened versions count as matches

Return ONLY a JSON response listing ALL matches found:
{
    "match_found": true/false,
    "matches": [
        {
            "speaker_id": "speaker_id",
            "speaker_name": "full name as it appears",
            "confidence": "high/medium/low",
            "reasoning": "brief explanation"
        }
    ]
}

If no matches, return {"match_found": false, "matches": []}
"""

    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"}

    data = {
        "model": "gpt-4o",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1,
        "response_format": {"type": "json_object"},
        "max_tokens": 1000
    }

    # Retry logic with exponential backoff
    max_retries = 3
    base_delay = 1

    for attempt in range(max_retries):
        try:
            async with session.post(
                "https://api.openai.com/v1/chat/completions", headers=headers, json=data
            ) as response:
                if response.status == 200:
                    result = await response.json()
                    match_info = json.loads(result["choices"][0]["message"]["content"])
                    
                    # Cache the result
                    cache[cache_key] = match_info
                    
                    return match_info
                    
                elif response.status == 429:  # Rate limit
                    retry_after = int(response.headers.get("Retry-After", base_delay * (2**attempt)))
                    logger.warning(f"Rate limited, waiting {retry_after}s...")
                    await asyncio.sleep(retry_after)
                    continue
                    
                else:
                    logger.error(f"API error {response.status}: {await response.text()}")
                    if attempt < max_retries - 1:
                        delay = base_delay * (2**attempt)
                        await asyncio.sleep(delay)
                        continue
                    return None

        except Exception as e:
            if attempt < max_retries - 1:
                delay = base_delay * (2**attempt)
                logger.warning(f"Error: {e}, retrying in {delay}s...")
                await asyncio.sleep(delay)
                continue
            else:
                logger.error(f"Error after {max_retries} attempts: {e}")
                return None


async def process_database_faculty(
    database_faculty: pd.DataFrame,
    speakers: pd.DataFrame,
    max_concurrent: int = MAX_CONCURRENT_REQUESTS
) -> List[Dict]:
    """
    Process all database faculty through comprehensive LLM matching.
    """
    # Load cache if exists
    cache = {}
    if LLM_CACHE_FILE.exists():
        with open(LLM_CACHE_FILE, "r") as f:
            cache = json.load(f)
        logger.info(f"Loaded {len(cache)} cached matches")

    results = []
    semaphore = asyncio.Semaphore(max_concurrent)

    async def process_one(session, person_row):
        async with semaphore:
            person_dict = person_row.to_dict()
            
            # Find speakers in the same discipline
            discipline_speakers = speakers[speakers["discipline"] == person_dict["discipline"]]
            
            logger.info(f"Processing {person_dict['Name']} ({person_dict['discipline']}) - "
                       f"{len(discipline_speakers)} speakers in discipline")
            
            # Find top candidates using comprehensive matching (35% of discipline)
            candidates = find_candidate_speakers(person_dict, discipline_speakers)
            
            if len(candidates) == 0:
                # No speakers in this discipline
                return [{
                    "database_id": person_dict["database_id"],
                    "database_name": person_dict["Name"],
                    "database_name_cleaned": person_dict["name_cleaned"],
                    "database_university": person_dict["Schools"],
                    "database_discipline": person_dict["discipline"],
                    "database_race": person_dict.get("Race", ""),
                    "database_gender": person_dict.get("Gender", ""),
                    "matched": False,
                    "speaker_id": None,
                    "speaker_name": None,
                    "speaker_university": None,
                    "speaker_race": None,
                    "speaker_gender": None,
                    "confidence": None,
                    "reasoning": "No speakers found in discipline",
                    "candidates_checked": 0,
                    "top_candidate_score": 0
                }]
            
            # Convert candidates to list of dicts
            candidate_list = candidates.to_dict('records')
            
            # Process in batches
            all_matches = []
            candidates_checked = 0
            
            for i in range(0, len(candidate_list), SPEAKERS_PER_BATCH):
                batch = candidate_list[i:i + SPEAKERS_PER_BATCH]
                candidates_checked += len(batch)
                
                batch_result = await match_batch_with_llm(session, person_dict, batch, cache)
                
                if batch_result and batch_result.get("match_found"):
                    all_matches.extend(batch_result.get("matches", []))
                    # If we found high-confidence matches, we can stop checking more batches
                    if any(m.get("confidence") == "high" for m in batch_result.get("matches", [])):
                        logger.info(f"Found high-confidence match for {person_dict['Name']}, stopping search")
                        break
            
            # Save the top score for analysis
            top_score = candidates.iloc[0]["score"] if len(candidates) > 0 else 0
            
            # Process results
            if all_matches:
                # Create a result for each match
                match_results = []
                for match in all_matches:
                    matched_speaker = speakers[speakers["speaker_id"] == match["speaker_id"]].iloc[0]
                    
                    result = {
                        "database_id": person_dict["database_id"],
                        "database_name": person_dict["Name"],
                        "database_name_cleaned": person_dict["name_cleaned"],
                        "database_university": person_dict["Schools"],
                        "database_discipline": person_dict["discipline"],
                        "database_race": person_dict.get("Race", ""),
                        "database_gender": person_dict.get("Gender", ""),
                        "matched": True,
                        "speaker_id": match["speaker_id"],
                        "speaker_name": match["speaker_name"],
                        "speaker_university": matched_speaker["affiliation_standardized"],
                        "speaker_race": matched_speaker["combined_race"],
                        "speaker_gender": matched_speaker["combined_gender"],
                        "confidence": match["confidence"],
                        "reasoning": match["reasoning"],
                        "candidates_checked": candidates_checked,
                        "top_candidate_score": top_score
                    }
                    match_results.append(result)
                
                return match_results
            else:
                # No match found
                return [{
                    "database_id": person_dict["database_id"],
                    "database_name": person_dict["Name"],
                    "database_name_cleaned": person_dict["name_cleaned"],
                    "database_university": person_dict["Schools"],
                    "database_discipline": person_dict["discipline"],
                    "database_race": person_dict.get("Race", ""),
                    "database_gender": person_dict.get("Gender", ""),
                    "matched": False,
                    "speaker_id": None,
                    "speaker_name": None,
                    "speaker_university": None,
                    "speaker_race": None,
                    "speaker_gender": None,
                    "confidence": None,
                    "reasoning": f"No match found among {candidates_checked} candidates checked",
                    "candidates_checked": candidates_checked,
                    "top_candidate_score": top_score
                }]

    # Process in batches
    async with aiohttp.ClientSession() as session:
        # Process faculty members
        for idx, person_row in database_faculty.iterrows():
            faculty_results = await process_one(session, person_row)
            results.extend(faculty_results)
            
            # Save cache periodically
            if (idx + 1) % 20 == 0:
                with open(LLM_CACHE_FILE, "w") as f:
                    json.dump(cache, f, indent=2)
                logger.info(f"Progress: {idx + 1}/{len(database_faculty)} faculty processed")

    # Final cache save
    with open(LLM_CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)

    return results


def analyze_comprehensive_matches(matches_df: pd.DataFrame) -> Dict:
    """Analyze the comprehensive matching results."""
    # Get unique matches
    unique_database_matched = matches_df[matches_df["matched"]]["database_id"].nunique()
    total_database = matches_df["database_id"].nunique()
    
    analysis = {
        "total_database_faculty": total_database,
        "unique_database_matched": unique_database_matched,
        "match_rate": unique_database_matched / total_database,
        "total_match_records": len(matches_df[matches_df["matched"]]),
        "avg_candidates_checked": matches_df["candidates_checked"].mean(),
        "avg_top_score": matches_df["top_candidate_score"].mean(),
        "by_discipline": {},
        "by_race": {},
        "by_confidence": {},
        "unique_speakers_matched": matches_df[matches_df["matched"]]["speaker_id"].nunique(),
    }
    
    # By discipline
    for discipline in matches_df["database_discipline"].unique():
        disc_df = matches_df[matches_df["database_discipline"] == discipline]
        unique_matched = disc_df[disc_df["matched"]]["database_id"].nunique()
        total = disc_df["database_id"].nunique()
        
        analysis["by_discipline"][discipline] = {
            "total": total,
            "matched": unique_matched,
            "match_rate": unique_matched / total if total > 0 else 0,
            "avg_candidates_checked": disc_df["candidates_checked"].mean(),
            "avg_top_score": disc_df["top_candidate_score"].mean()
        }
    
    # By race
    for race in matches_df["database_race"].unique():
        if race:  # Skip empty values
            race_df = matches_df[matches_df["database_race"] == race]
            unique_matched = race_df[race_df["matched"]]["database_id"].nunique()
            total = race_df["database_id"].nunique()
            
            analysis["by_race"][race] = {
                "total": total,
                "matched": unique_matched,
                "match_rate": unique_matched / total if total > 0 else 0
            }
    
    # By confidence
    matched_df = matches_df[matches_df["matched"]]
    for conf in ["high", "medium", "low"]:
        conf_count = len(matched_df[matched_df["confidence"] == conf])
        analysis["by_confidence"][conf] = conf_count
    
    # Score distribution for non-matches
    non_matches = matches_df[~matches_df["matched"]]
    analysis["non_match_score_distribution"] = {
        "mean": non_matches["top_candidate_score"].mean(),
        "median": non_matches["top_candidate_score"].median(),
        "max": non_matches["top_candidate_score"].max(),
        "min": non_matches["top_candidate_score"].min()
    }
    
    return analysis


async def main():
    """Main execution function."""
    logger.info("Starting COMPREHENSIVE LLM-based database speaker matching")
    logger.info(f"Will check top {CANDIDATES_PERCENTAGE*100:.0f}% of speakers in each discipline")
    logger.info(f"Batch size: {SPEAKERS_PER_BATCH} speakers per LLM call")
    
    # Load data
    logger.info("Loading database faculty...")
    database_faculty = load_database_faculty()
    
    logger.info("Loading speakers...")
    speakers = load_unique_speakers()
    
    # Show scale of matching for each discipline
    logger.info("\nMatching scale by discipline (35% of speakers):")
    for discipline in ['Chemistry', 'Physics', 'Mathematics', 'Computer Science', 'Mechanical Engineering']:
        disc_speakers = speakers[speakers['discipline'] == discipline]
        num_to_check = max(1, int(len(disc_speakers) * CANDIDATES_PERCENTAGE))
        logger.info(f"  {discipline}: {len(disc_speakers)} speakers → checking top {num_to_check}")
    
    # Run matching
    logger.info("Starting comprehensive matching process...")
    matches = await process_database_faculty(database_faculty, speakers)
    
    # Convert to DataFrame
    matches_df = pd.DataFrame(matches)
    
    # Save detailed results
    output_file = OUTPUTS_DIR / "llm_database_speaker_matches_comprehensive.csv"
    matches_df.to_csv(output_file, index=False)
    logger.info(f"Saved detailed matches to {output_file}")
    
    # Analyze results
    analysis = analyze_comprehensive_matches(matches_df)
    
    # Save analysis
    analysis_file = OUTPUTS_DIR / "llm_matching_comprehensive_analysis.json"
    with open(analysis_file, "w") as f:
        json.dump(analysis, f, indent=2)
    
    # Create and save summary report
    report = []
    report.append("\n" + "=" * 80)
    report.append("COMPREHENSIVE LLM MATCHING RESULTS SUMMARY")
    report.append("=" * 80)
    report.append(f"Matching Strategy: Top {CANDIDATES_PERCENTAGE*100:.0f}% of speakers in each discipline")
    report.append(f"Average candidates checked per faculty: {analysis['avg_candidates_checked']:.1f}")
    report.append(f"Average top candidate score: {analysis['avg_top_score']:.1f}")
    
    report.append(f"\nUnique database faculty matched: {analysis['unique_database_matched']}/{analysis['total_database_faculty']} ({analysis['match_rate']:.1%})")
    report.append(f"Total match records: {analysis['total_match_records']}")
    report.append(f"Unique speakers matched: {analysis['unique_speakers_matched']}")
    
    report.append("\n\nBy Discipline:")
    for disc, stats in analysis["by_discipline"].items():
        report.append(f"  {disc}: {stats['matched']}/{stats['total']} ({stats['match_rate']:.1%})")
        report.append(f"    - Avg candidates checked: {stats['avg_candidates_checked']:.1f}")
        report.append(f"    - Avg top score: {stats['avg_top_score']:.1f}")
    
    report.append("\n\nBy Race:")
    for race, stats in analysis["by_race"].items():
        report.append(f"  {race}: {stats['matched']}/{stats['total']} ({stats['match_rate']:.1%})")
    
    report.append("\n\nBy Confidence:")
    total_conf = sum(analysis["by_confidence"].values())
    for conf, count in analysis["by_confidence"].items():
        pct = (count / total_conf * 100) if total_conf > 0 else 0
        report.append(f"  {conf}: {count} ({pct:.1f}%)")
    
    report.append("\n\nNon-Match Score Analysis:")
    report.append(f"  Mean top score for non-matches: {analysis['non_match_score_distribution']['mean']:.1f}")
    report.append(f"  Median: {analysis['non_match_score_distribution']['median']:.1f}")
    report.append(f"  Max: {analysis['non_match_score_distribution']['max']:.1f}")
    report.append("  (Low scores suggest these are true non-matches)")
    
    # Compare with original if it exists
    original_file = OUTPUTS_DIR / "llm_database_speaker_matches.csv"
    if original_file.exists():
        original_df = pd.read_csv(original_file)
        original_matched = len(original_df[original_df["matched"]])
        comprehensive_matched = analysis['unique_database_matched']
        
        improvement = comprehensive_matched - original_matched
        improvement_pct = (improvement / original_matched * 100) if original_matched > 0 else 0
        
        report.append(f"\n\nCOMPARISON WITH ORIGINAL (TOP 20) MATCHING:")
        report.append(f"Original matches: {original_matched}")
        report.append(f"Comprehensive matches: {comprehensive_matched}")
        report.append(f"Additional matches found: {improvement} ({improvement_pct:+.1f}%)")
    
    # Print and save report
    report_text = "\n".join(report)
    print(report_text)
    
    report_file = OUTPUTS_DIR / "llm_matching_comprehensive_report.txt"
    with open(report_file, "w") as f:
        f.write(report_text)
    
    logger.info(f"\nReport saved to {report_file}")


if __name__ == "__main__":
    # Install required package if not available
    try:
        from fuzzywuzzy import fuzz
    except ImportError:
        import subprocess
        logger.info("Installing fuzzywuzzy for fuzzy string matching...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "fuzzywuzzy", "python-Levenshtein"])
        from fuzzywuzzy import fuzz
    
    asyncio.run(main())