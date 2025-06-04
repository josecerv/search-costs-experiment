#!/usr/bin/env python3
"""
Create a comprehensive CSV showing:
1. All URM faculty in our databases
2. Which ones matched to seminar speakers
3. The demographic information of those matches
"""

import pandas as pd
from pathlib import Path

# Paths
data_dir = Path("/mnt/c/Users/jcerv/Jose/search-costs")
output_dir = Path("/mnt/c/Users/jcerv/Jose/search-costs/05_statistical_analysis/outputs")

print("Creating comprehensive database-speaker match report...")

# 1. Load all URM databases
all_urm_faculty = []
db_dir = data_dir / "02_intervention_materials/databases"

discipline_map = {
    'chemistry': 'Chemistry',
    'physics': 'Physics', 
    'mathematics': 'Mathematics',
    'computerScience': 'Computer Science',
    'mechanicalEngineering': 'Mechanical Engineering'
}

for file_name, discipline in discipline_map.items():
    df = pd.read_csv(db_dir / f"{file_name}.csv")
    df['discipline'] = discipline
    df['database_file'] = file_name
    all_urm_faculty.append(df)

urm_faculty_df = pd.concat(all_urm_faculty, ignore_index=True)
print(f"Total URM faculty in databases: {len(urm_faculty_df)}")
print(f"  Black: {len(urm_faculty_df[urm_faculty_df['Race'] == 'Black'])}")
print(f"  Hispanic: {len(urm_faculty_df[urm_faculty_df['Race'] == 'Hispanic'])}")
print(f"  Native American: {len(urm_faculty_df[urm_faculty_df['Race'] == 'Native American'])}")

# 2. Load the matches we found
matches_df = pd.read_csv(output_dir / "database_matches_all.csv")
print(f"\nTotal matches found: {len(matches_df)}")

# 3. Create a comprehensive report
# For each URM faculty member, find all their matches
report_rows = []

for _, faculty in urm_faculty_df.iterrows():
    # Base information about the faculty member
    base_info = {
        'database_name': faculty['Name'],
        'database_university': faculty['Schools'],
        'database_race': faculty['Race'],
        'database_gender': faculty['Gender'],
        'database_title': faculty['Title'],
        'database_discipline': faculty['discipline'],
        'database_research': faculty.get('Research.Area', ''),
    }
    
    # Find matches for this faculty member
    faculty_matches = matches_df[
        (matches_df['urm_name'] == faculty['Name']) &
        (matches_df['urm_university'] == faculty['Schools'])
    ]
    
    if len(faculty_matches) == 0:
        # No matches - still include in report
        row = base_info.copy()
        row.update({
            'matched': 'No',
            'num_matches': 0,
            'speaker_name': '',
            'speaker_university': '',
            'speaker_race_identified': '',
            'seminar_university': '',
            'seminar_discipline': '',
            'seminar_condition': '',
            'seminar_date': '',
            'semester': ''
        })
        report_rows.append(row)
    else:
        # Has matches - create a row for each match
        row = base_info.copy()
        row.update({
            'matched': 'Yes',
            'num_matches': len(faculty_matches),
            'speaker_name': '',
            'speaker_university': '',
            'speaker_race_identified': '',
            'seminar_university': '',
            'seminar_discipline': '',
            'seminar_condition': '',
            'seminar_date': '',
            'semester': ''
        })
        report_rows.append(row)
        
        # Add individual match details
        for _, match in faculty_matches.iterrows():
            match_row = base_info.copy()
            match_row.update({
                'matched': 'Match Detail',
                'num_matches': '',
                'speaker_name': match['speaker_name'],
                'speaker_university': match['speaker_university'],
                'speaker_race_identified': match['speaker_race'],
                'seminar_university': match['seminar_university'],
                'seminar_discipline': match['discipline'],
                'seminar_condition': match['condition'],
                'seminar_date': match['date'],
                'semester': match['semester']
            })
            report_rows.append(match_row)

# 4. Create DataFrame and add summary statistics
report_df = pd.DataFrame(report_rows)

# 5. Add summary statistics
print("\n=== SUMMARY STATISTICS ===")
print(f"Total URM faculty in databases: {len(urm_faculty_df)}")
print(f"Faculty with at least one match: {len(report_df[(report_df['matched'] == 'Yes')])}")
print(f"Match rate: {len(report_df[(report_df['matched'] == 'Yes')]) / len(urm_faculty_df) * 100:.1f}%")

# By race
for race in ['Black', 'Hispanic', 'Native American']:
    race_faculty = urm_faculty_df[urm_faculty_df['Race'] == race]
    race_matched = report_df[(report_df['database_race'] == race) & (report_df['matched'] == 'Yes')]
    if len(race_faculty) > 0:
        print(f"\n{race} faculty:")
        print(f"  Total: {len(race_faculty)}")
        print(f"  Matched: {len(race_matched)}")
        print(f"  Match rate: {len(race_matched) / len(race_faculty) * 100:.1f}%")

# 6. Create a summary report
summary_df = urm_faculty_df.copy()
summary_df['matched'] = 'No'
summary_df['num_appearances'] = 0
summary_df['appeared_in_treatment'] = 0
summary_df['appeared_in_control'] = 0

for _, faculty in urm_faculty_df.iterrows():
    faculty_matches = matches_df[
        (matches_df['urm_name'] == faculty['Name']) &
        (matches_df['urm_university'] == faculty['Schools'])
    ]
    
    if len(faculty_matches) > 0:
        idx = summary_df[
            (summary_df['Name'] == faculty['Name']) &
            (summary_df['Schools'] == faculty['Schools'])
        ].index[0]
        
        summary_df.loc[idx, 'matched'] = 'Yes'
        summary_df.loc[idx, 'num_appearances'] = len(faculty_matches)
        summary_df.loc[idx, 'appeared_in_treatment'] = len(faculty_matches[faculty_matches['condition'] == 'treatment'])
        summary_df.loc[idx, 'appeared_in_control'] = len(faculty_matches[faculty_matches['condition'] == 'control'])

# 7. Save both reports
# Detailed report with all matches
report_df.to_csv(output_dir / "database_speaker_matches_detailed.csv", index=False)
print(f"\nDetailed report saved to: {output_dir / 'database_speaker_matches_detailed.csv'}")

# Summary report (one row per faculty)
summary_df = summary_df.sort_values(['matched', 'num_appearances'], ascending=[False, False])
summary_df.to_csv(output_dir / "database_faculty_match_summary.csv", index=False)
print(f"Summary report saved to: {output_dir / 'database_faculty_match_summary.csv'}")

# 8. Create a focused report on mismatches
print("\n=== DEMOGRAPHIC MISMATCHES ===")
mismatches = matches_df[matches_df['urm_race'] != matches_df['speaker_race']]
print(f"Found {len(mismatches)} cases where database race doesn't match identified race")

if len(mismatches) > 0:
    print("\nBreakdown of mismatches:")
    print("Database Race -> Identified Race:")
    mismatch_counts = mismatches.groupby(['urm_race', 'speaker_race']).size()
    for (db_race, speaker_race), count in mismatch_counts.items():
        print(f"  {db_race} -> {speaker_race}: {count}")
    
    mismatches.to_csv(output_dir / "database_demographic_mismatches.csv", index=False)
    print(f"\nMismatches saved to: {output_dir / 'database_demographic_mismatches.csv'}")

print("\n=== COMPLETE ===")
print(f"Created three files:")
print(f"1. database_speaker_matches_detailed.csv - All matches with details")
print(f"2. database_faculty_match_summary.csv - One row per faculty member")
print(f"3. database_demographic_mismatches.csv - Cases where race identification differed")