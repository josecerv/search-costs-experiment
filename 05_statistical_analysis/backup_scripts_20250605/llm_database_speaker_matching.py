#!/usr/bin/env python3
"""
LLM-based matching between URM database faculty and seminar speakers.

This script uses GPT-4 to accurately match faculty from the URM databases
to speakers in the seminar data, considering name variations, middle names,
and potential misspellings while ensuring discipline matching.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json
import asyncio
import aiohttp
from typing import Dict, List, Tuple, Optional
import logging
from datetime import datetime
import os
import re
from unicodedata import normalize
from dotenv import load_dotenv

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
LLM_CACHE_FILE = CACHE_DIR / "llm_matching_cache.json"


def clean_name(name: str) -> str:
    """
    Clean and normalize a name by removing special characters and extra spaces.

    Args:
        name: Raw name string

    Returns:
        Cleaned name string
    """
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

        # Clean the name
        df["name_cleaned"] = df["Name"].apply(clean_name)

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

    # Clean the names
    unique_speakers["name_cleaned"] = unique_speakers["name"].apply(clean_name)

    logger.info(f"Loaded {len(unique_speakers)} unique speakers")

    return unique_speakers


async def match_with_llm(
    session: aiohttp.ClientSession,
    database_person: Dict,
    potential_matches: List[Dict],
    cache: Dict,
) -> Optional[Dict]:
    """
    Use LLM to match a database person with potential speaker matches.

    Args:
        session: aiohttp session for API calls
        database_person: Dictionary with database faculty info
        potential_matches: List of potential speaker matches
        cache: Dictionary to cache results

    Returns:
        Best match dictionary or None if no match found
    """
    # Create cache key
    cache_key = f"{database_person['name_cleaned']}_{database_person['discipline']}"

    # Check cache first
    if cache_key in cache:
        logger.debug(f"Using cached result for {cache_key}")
        return cache.get(cache_key)

    # Prepare the prompt
    prompt = f"""You are an expert at matching academic faculty names. I need you to determine if a faculty member from a URM database matches any speakers in seminar data.

DATABASE FACULTY:
Name: {database_person['Name']} (cleaned: {database_person['name_cleaned']})
University: {database_person['Schools']}
Discipline: {database_person['discipline']}
Title: {database_person.get('Title', 'Unknown')}

POTENTIAL SPEAKER MATCHES (same discipline):
"""

    for i, speaker in enumerate(
        potential_matches[:20]
    ):  # Limit to top 20 to keep prompt reasonable
        prompt += f"""
{i+1}. Name: {speaker['name']} (cleaned: {speaker['name_cleaned']})
   University: {speaker['affiliation_standardized']}
   Speaker ID: {speaker['speaker_id']}
"""

    prompt += """
Please analyze if the DATABASE FACULTY matches any of the POTENTIAL SPEAKERS.

Consider:
1. Full name matches (accounting for middle names/initials)
2. Name variations (e.g., nicknames, shortened versions)
3. University affiliations (people can move between institutions)
4. Common misspellings or transcription errors

Return your response as JSON:
{
    "match_found": true/false,
    "matched_speaker_id": "speaker_id if match found, null otherwise",
    "matched_speaker_name": "full name if match found, null otherwise",
    "confidence": "high/medium/low",
    "reasoning": "brief explanation"
}
"""

    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"}

    data = {
        "model": "gpt-4o",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.1,
        "response_format": {"type": "json_object"},
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
                elif response.status in [500, 502, 503, 504]:
                    # Server errors - retry with backoff
                    if attempt < max_retries - 1:
                        delay = base_delay * (2**attempt)
                        logger.warning(f"Server error {response.status}, retrying in {delay}s...")
                        await asyncio.sleep(delay)
                        continue
                    else:
                        logger.error(
                            f"API error {response.status} after {max_retries} attempts: {await response.text()}"
                        )
                        return None
                else:
                    logger.error(f"API error {response.status}: {await response.text()}")
                    return None

        except Exception as e:
            if attempt < max_retries - 1:
                delay = base_delay * (2**attempt)
                logger.warning(
                    f"Error matching {database_person['Name']}: {e}, retrying in {delay}s..."
                )
                await asyncio.sleep(delay)
                continue
            else:
                logger.error(
                    f"Error matching {database_person['Name']} after {max_retries} attempts: {e}"
                )
                return None


async def process_database_faculty(
    database_faculty: pd.DataFrame, speakers: pd.DataFrame, max_concurrent: int = 10
) -> List[Dict]:
    """
    Process all database faculty through LLM matching.

    Args:
        database_faculty: DataFrame of URM database faculty
        speakers: DataFrame of unique speakers
        max_concurrent: Maximum concurrent API requests

    Returns:
        List of match results
    """
    # Load cache if exists
    cache = {}
    if LLM_CACHE_FILE.exists():
        with open(LLM_CACHE_FILE, "r") as f:
            cache = json.load(f)
        logger.info(f"Loaded {len(cache)} cached matches")

    results = []

    # Create a semaphore for rate limiting
    semaphore = asyncio.Semaphore(max_concurrent)

    async def process_one(session, person_row):
        async with semaphore:
            person_dict = person_row.to_dict()

            # Find potential matches in the same discipline
            discipline_speakers = speakers[speakers["discipline"] == person_dict["discipline"]]

            # Convert to list of dicts for the LLM
            potential_matches = discipline_speakers.to_dict("records")

            # Sort by name similarity (simple approach - could be improved)
            potential_matches.sort(
                key=lambda x: (
                    person_dict["name_cleaned"].lower() in x["name_cleaned"].lower()
                    or x["name_cleaned"].lower() in person_dict["name_cleaned"].lower()
                ),
                reverse=True,
            )

            match_result = await match_with_llm(session, person_dict, potential_matches, cache)

            if match_result and match_result.get("match_found"):
                # Find the matched speaker details
                matched_speaker = (
                    speakers[speakers["speaker_id"] == match_result["matched_speaker_id"]].iloc[0]
                    if match_result.get("matched_speaker_id")
                    else None
                )

                result = {
                    "database_name": person_dict["Name"],
                    "database_name_cleaned": person_dict["name_cleaned"],
                    "database_university": person_dict["Schools"],
                    "database_discipline": person_dict["discipline"],
                    "database_race": person_dict.get("Race", ""),
                    "database_gender": person_dict.get("Gender", ""),
                    "matched": True,
                    "speaker_id": match_result.get("matched_speaker_id"),
                    "speaker_name": match_result.get("matched_speaker_name"),
                    "speaker_university": matched_speaker["affiliation_standardized"]
                    if matched_speaker is not None
                    else None,
                    "speaker_race": matched_speaker["combined_race"]
                    if matched_speaker is not None
                    else None,
                    "speaker_gender": matched_speaker["combined_gender"]
                    if matched_speaker is not None
                    else None,
                    "confidence": match_result.get("confidence"),
                    "reasoning": match_result.get("reasoning"),
                }
            else:
                result = {
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
                    "reasoning": "No match found",
                }

            return result

    # Process in batches
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _, person_row in database_faculty.iterrows():
            task = process_one(session, person_row)
            tasks.append(task)

        # Process with progress reporting
        total = len(tasks)
        completed = 0

        for i in range(0, len(tasks), max_concurrent):
            batch = tasks[i : i + max_concurrent]
            batch_results = await asyncio.gather(*batch, return_exceptions=True)

            for result in batch_results:
                if isinstance(result, Exception):
                    logger.error(f"Error in batch: {result}")
                else:
                    results.append(result)
                    completed += 1

            # Save cache periodically
            with open(LLM_CACHE_FILE, "w") as f:
                json.dump(cache, f, indent=2)

            logger.info(f"Progress: {completed}/{total} ({completed/total*100:.1f}%)")

    # Final cache save
    with open(LLM_CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)

    return results


def analyze_matches(matches_df: pd.DataFrame) -> Dict:
    """Analyze the matching results."""
    analysis = {
        "total_database_faculty": len(matches_df),
        "total_matched": len(matches_df[matches_df["matched"]]),
        "match_rate": len(matches_df[matches_df["matched"]]) / len(matches_df),
        "by_discipline": {},
        "by_race": {},
        "by_confidence": {},
        "unique_speakers_matched": matches_df[matches_df["matched"]]["speaker_id"].nunique(),
    }

    # By discipline
    for discipline in matches_df["database_discipline"].unique():
        disc_df = matches_df[matches_df["database_discipline"] == discipline]
        analysis["by_discipline"][discipline] = {
            "total": len(disc_df),
            "matched": len(disc_df[disc_df["matched"]]),
            "match_rate": len(disc_df[disc_df["matched"]]) / len(disc_df)
            if len(disc_df) > 0
            else 0,
        }

    # By race
    for race in matches_df["database_race"].unique():
        race_df = matches_df[matches_df["database_race"] == race]
        analysis["by_race"][race] = {
            "total": len(race_df),
            "matched": len(race_df[race_df["matched"]]),
            "match_rate": len(race_df[race_df["matched"]]) / len(race_df)
            if len(race_df) > 0
            else 0,
        }

    # By confidence
    matched_df = matches_df[matches_df["matched"]]
    for conf in ["high", "medium", "low"]:
        conf_count = len(matched_df[matched_df["confidence"] == conf])
        analysis["by_confidence"][conf] = conf_count

    return analysis


async def main():
    """Main execution function."""
    logger.info("Starting LLM-based database speaker matching")

    # Load data
    logger.info("Loading database faculty...")
    database_faculty = load_database_faculty()

    logger.info("Loading unique speakers...")
    speakers = load_unique_speakers()

    # Run matching
    logger.info("Starting LLM matching process...")
    matches = await process_database_faculty(database_faculty, speakers, max_concurrent=5)

    # Convert to DataFrame
    matches_df = pd.DataFrame(matches)

    # Save detailed results
    output_file = OUTPUTS_DIR / "llm_database_speaker_matches.csv"
    matches_df.to_csv(output_file, index=False)
    logger.info(f"Saved detailed matches to {output_file}")

    # Analyze results
    analysis = analyze_matches(matches_df)

    # Save analysis
    analysis_file = OUTPUTS_DIR / "llm_matching_analysis.json"
    with open(analysis_file, "w") as f:
        json.dump(analysis, f, indent=2)

    # Print summary
    print("\n" + "=" * 60)
    print("LLM MATCHING RESULTS SUMMARY")
    print("=" * 60)
    print(f"Total database faculty: {analysis['total_database_faculty']}")
    print(f"Total matched: {analysis['total_matched']}")
    print(f"Match rate: {analysis['match_rate']:.1%}")
    print(f"Unique speakers matched: {analysis['unique_speakers_matched']}")

    print("\nBy Discipline:")
    for disc, stats in analysis["by_discipline"].items():
        print(f"  {disc}: {stats['matched']}/{stats['total']} ({stats['match_rate']:.1%})")

    print("\nBy Race:")
    for race, stats in analysis["by_race"].items():
        print(f"  {race}: {stats['matched']}/{stats['total']} ({stats['match_rate']:.1%})")

    print("\nBy Confidence:")
    for conf, count in analysis["by_confidence"].items():
        print(f"  {conf}: {count}")

    # Check for race/gender mismatches
    matched_df = matches_df[matches_df["matched"]]
    race_mismatches = matched_df[
        (matched_df["database_race"] != matched_df["speaker_race"])
        & (matched_df["speaker_race"].notna())
    ]

    if len(race_mismatches) > 0:
        print(
            f"\nWARNING: Found {len(race_mismatches)} race mismatches between database and speaker demographics"
        )
        mismatch_file = OUTPUTS_DIR / "llm_race_mismatches.csv"
        race_mismatches.to_csv(mismatch_file, index=False)
        print(f"Race mismatches saved to {mismatch_file}")


if __name__ == "__main__":
    asyncio.run(main())
