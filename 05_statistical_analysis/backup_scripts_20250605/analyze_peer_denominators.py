#!/usr/bin/env python3
"""
Calculate database usage rates with the correct denominator:
speakers from eligible peer universities (not all speakers).
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json
import logging
from scipy import stats

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Paths
BASE_DIR = Path("/mnt/c/Users/jcerv/Jose/search-costs")
OUTPUTS_DIR = BASE_DIR / "05_statistical_analysis/outputs"


def get_discipline_rankings():
    """Get rankings for each discipline."""
    master_file = BASE_DIR / "05_statistical_analysis/outputs/master_analysis_dataset.csv"
    df = pd.read_csv(master_file)
    rankings = {}

    for discipline in df["discipline"].unique():
        disc_data = df[df["discipline"] == discipline]
        uni_ranks = disc_data[["university", "dept_ranking"]].drop_duplicates()
        uni_ranks = uni_ranks[uni_ranks["dept_ranking"].notna()]
        uni_ranks = uni_ranks.sort_values("dept_ranking")
        rankings[discipline] = uni_ranks["university"].tolist()

    return rankings


def get_peer_universities(university, ranking_list):
    """Get peer universities (40 minimum, ±20 ranks)."""
    if university not in ranking_list:
        return []

    index = ranking_list.index(university)
    min_rank = max(0, index - 20)
    max_rank = min(len(ranking_list) - 1, index + 20)

    peers = ranking_list[min_rank : max_rank + 1]
    peers = [p for p in peers if p != university]

    # Ensure at least 40
    if len(peers) < 40:
        if min_rank == 0:
            max_rank = min(len(ranking_list) - 1, 40)
            peers = ranking_list[min_rank : max_rank + 1]
        elif max_rank == len(ranking_list) - 1:
            min_rank = max(0, len(ranking_list) - 41)
            peers = ranking_list[min_rank : max_rank + 1]
        peers = [p for p in peers if p != university]

    if len(peers) > 40:
        peers = peers[:40]

    return peers


def main():
    logger.info("Calculating database usage with correct denominators")

    # Load data
    seminars_df = pd.read_csv(BASE_DIR / "03_data_collection/processed/master-data-final.csv")
    appearances_df = pd.read_csv(
        BASE_DIR / "04_demographic_analysis/outputs/speaker_appearances_analysis.csv"
    )

    # Load database faculty
    database_files = {
        "Chemistry": "chemistry.csv",
        "Computer Science": "computerScience.csv",
        "Mathematics": "mathematics.csv",
        "Mechanical Engineering": "mechanicalEngineering.csv",
        "Physics": "physics.csv",
    }

    all_database_faculty = []
    for discipline, filename in database_files.items():
        df = pd.read_csv(BASE_DIR / f"02_intervention_materials/databases/{filename}")
        df["discipline"] = discipline
        all_database_faculty.append(df)

    database_df = pd.concat(all_database_faculty, ignore_index=True)

    # Load LLM matches
    matches_df = pd.read_csv(OUTPUTS_DIR / "llm_database_speaker_matches.csv")
    matched_database = matches_df[matches_df["matched"] == True]

    # Create mapping
    database_to_speaker = {}
    for _, row in matched_database.iterrows():
        key = (row["database_name"], row["database_university"], row["database_discipline"])
        database_to_speaker[key] = row["speaker_id"]

    # Get rankings
    discipline_rankings = get_discipline_rankings()

    # Get unique departments
    departments = seminars_df[["university", "discipline", "condition"]].drop_duplicates()

    results = []

    for _, dept in departments.iterrows():
        university = dept["university"]
        discipline = dept["discipline"]
        condition = dept["condition"]

        if discipline not in database_files or discipline not in discipline_rankings:
            continue

        ranking_list = discipline_rankings[discipline]

        # Get peer universities
        peer_unis = get_peer_universities(university, ranking_list)

        # Get database faculty from peers
        disc_database = database_df[database_df["discipline"] == discipline]
        shown_faculty = disc_database[disc_database["Schools"].isin(peer_unis)]

        # Get speaker IDs for shown faculty
        shown_speaker_ids = []
        for _, fac in shown_faculty.iterrows():
            key = (fac["Name"], fac["Schools"], discipline)
            if key in database_to_speaker:
                shown_speaker_ids.append(database_to_speaker[key])

        # Get all speakers for this department
        dept_seminars = seminars_df[
            (seminars_df["university"] == university) & (seminars_df["discipline"] == discipline)
        ]["seminar_id"].unique()

        dept_speakers = appearances_df[appearances_df["seminar_id"].isin(dept_seminars)]

        # KEY CALCULATION: Speakers from peer universities
        speakers_from_peer_unis = dept_speakers[
            dept_speakers["affiliation_standardized"].isin(peer_unis)
        ]

        # Calculate with correct denominator
        total_speakers = len(dept_speakers)
        speakers_from_peers = len(speakers_from_peer_unis)
        speakers_from_shown_db = len(
            dept_speakers[dept_speakers["speaker_id"].isin(shown_speaker_ids)]
        )

        # Percentages
        if speakers_from_peers > 0:
            percent_db_of_peers = speakers_from_shown_db / speakers_from_peers
        else:
            percent_db_of_peers = 0

        # For Black speakers
        black_from_peers = len(
            speakers_from_peer_unis[speakers_from_peer_unis["combined_race"] == "black"]
        )
        black_from_shown_db = len(
            dept_speakers[
                (dept_speakers["speaker_id"].isin(shown_speaker_ids))
                & (dept_speakers["combined_race"] == "black")
            ]
        )

        results.append(
            {
                "university": university,
                "discipline": discipline,
                "condition": condition,
                "peer_universities": len(peer_unis),
                "shown_database_size": len(shown_faculty),
                "shown_black_faculty": len(shown_faculty[shown_faculty["Race"] == "Black"]),
                "total_speakers": total_speakers,
                "speakers_from_peer_unis": speakers_from_peers,
                "speakers_from_shown_db": speakers_from_shown_db,
                "percent_of_all_speakers": speakers_from_shown_db / total_speakers
                if total_speakers > 0
                else 0,
                "percent_of_peer_speakers": percent_db_of_peers,
                "used_shown_db": speakers_from_shown_db > 0,
                "black_speakers_total": len(
                    dept_speakers[dept_speakers["combined_race"] == "black"]
                ),
                "black_from_peers": black_from_peers,
                "black_from_shown_db": black_from_shown_db,
            }
        )

    # Convert to DataFrame
    results_df = pd.DataFrame(results)

    # Analyze by condition
    treatment = results_df[results_df["condition"] == "treatment"]
    control = results_df[results_df["condition"] == "control"]

    print("\n" + "=" * 60)
    print("DATABASE USAGE WITH CORRECT DENOMINATORS")
    print("=" * 60)

    print(f"\nSpeakers from peer universities:")
    print(
        f"Treatment: {treatment['speakers_from_peer_unis'].sum()} / {treatment['total_speakers'].sum()} ({treatment['speakers_from_peer_unis'].sum() / treatment['total_speakers'].sum():.1%} of all speakers)"
    )
    print(
        f"Control: {control['speakers_from_peer_unis'].sum()} / {control['total_speakers'].sum()} ({control['speakers_from_peer_unis'].sum() / control['total_speakers'].sum():.1%} of all speakers)"
    )

    print(f"\nDatabase speakers as % of ALL speakers:")
    print(f"Treatment: {treatment['percent_of_all_speakers'].mean():.2%}")
    print(f"Control: {control['percent_of_all_speakers'].mean():.2%}")

    print(f"\nDatabase speakers as % of PEER university speakers:")
    print(f"Treatment: {treatment['percent_of_peer_speakers'].mean():.2%}")
    print(f"Control: {control['percent_of_peer_speakers'].mean():.2%}")

    # T-test for difference
    t_stat, p_value = stats.ttest_ind(
        treatment["percent_of_peer_speakers"].dropna(), control["percent_of_peer_speakers"].dropna()
    )
    print(f"Difference: p = {p_value:.3f}")

    print(f"\nBinary outcome - ANY speaker from shown database:")
    print(
        f"Treatment: {treatment['used_shown_db'].sum()} / {len(treatment)} ({treatment['used_shown_db'].mean():.1%})"
    )
    print(
        f"Control: {control['used_shown_db'].sum()} / {len(control)} ({control['used_shown_db'].mean():.1%})"
    )

    # Department-level aggregates
    print(f"\nDepartment-level averages:")
    print(f"Average % of peer speakers from database:")
    print(f"  Treatment: {treatment['percent_of_peer_speakers'].mean():.2%}")
    print(f"  Control: {control['percent_of_peer_speakers'].mean():.2%}")

    # Save results
    results_df.to_csv(OUTPUTS_DIR / "peer_database_usage_correct_denominator.csv", index=False)

    summary = {
        "speakers_from_peers": {
            "treatment_total": int(treatment["speakers_from_peer_unis"].sum()),
            "control_total": int(control["speakers_from_peer_unis"].sum()),
            "treatment_percent_of_all": float(
                treatment["speakers_from_peer_unis"].sum() / treatment["total_speakers"].sum()
            ),
            "control_percent_of_all": float(
                control["speakers_from_peer_unis"].sum() / control["total_speakers"].sum()
            ),
        },
        "database_usage_rates": {
            "percent_of_all_speakers": {
                "treatment": float(treatment["percent_of_all_speakers"].mean()),
                "control": float(control["percent_of_all_speakers"].mean()),
            },
            "percent_of_peer_speakers": {
                "treatment": float(treatment["percent_of_peer_speakers"].mean()),
                "control": float(control["percent_of_peer_speakers"].mean()),
                "p_value": float(p_value),
            },
        },
        "binary_used_database": {
            "treatment": float(treatment["used_shown_db"].mean()),
            "control": float(control["used_shown_db"].mean()),
        },
        "black_speakers": {
            "from_peers_treatment": int(treatment["black_from_peers"].sum()),
            "from_peers_control": int(control["black_from_peers"].sum()),
            "from_database_treatment": int(treatment["black_from_shown_db"].sum()),
            "from_database_control": int(control["black_from_shown_db"].sum()),
        },
    }

    with open(OUTPUTS_DIR / "peer_denominator_analysis_summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\nResults saved to:")
    print(f"  - {OUTPUTS_DIR / 'peer_database_usage_correct_denominator.csv'}")
    print(f"  - {OUTPUTS_DIR / 'peer_denominator_analysis_summary.json'}")


if __name__ == "__main__":
    main()
