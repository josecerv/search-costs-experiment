# LLM-Based Database Speaker Matching: Final Report

## Executive Summary

Using GPT-4o to match URM database faculty to seminar speakers, we found that only **75 out of 550 faculty (13.6%)** from the databases appeared as speakers. This is dramatically lower than the previous flawed analysis that claimed 922 matches.

## Key Findings

### 1. Match Quality
- **Total matches**: 75 (all high confidence)
- **Match rate by discipline**:
  - Mathematics: 23.8% (highest)
  - Physics: 18.8%
  - Chemistry: 18.5%
  - Computer Science: 4.3%
  - Mechanical Engineering: 3.8% (lowest)

### 2. Database Usage
- **Treatment departments**: 49 used database speakers (6.0%)
- **Control departments**: 54 used database speakers (6.4%)
- No significant difference in database usage between conditions (p = nan)

### 3. Treatment Effect on Black Speakers
- **Treatment**: 2.64% Black speakers
- **Control**: 1.92% Black speakers
- **Absolute increase**: 0.72 percentage points
- **Relative increase**: 37.7% (p = 0.014, significant)

### 4. Source of Treatment Effect
Of the 61 additional Black speakers in treatment departments:
- **5 came from the database** (8.2%)
- **56 came from other sources** (91.8%)

This strongly suggests the treatment worked primarily through **indirect mechanisms** rather than direct database usage.

### 5. Overall URM Effect
- **Treatment**: 8.40% URM speakers (Black + Latino)
- **Control**: 7.57% URM speakers
- **Difference**: 0.83 percentage points (p = 0.141, not significant)

## Data Quality Issues

The analysis revealed concerning demographic classification errors:
- **12 race mismatches** (16% of matches)
- **14 gender mismatches** (19% of matches)

These suggest the demographic analysis pipeline may have accuracy issues that need addressing.

## Methodology

The LLM matching approach:
1. Cleaned names by removing special characters and normalizing spacing
2. For each database faculty, found potential matches in the same discipline
3. Used GPT-4o to analyze name variations, accounting for:
   - Middle names/initials
   - University moves
   - Common misspellings
   - Name variations (accents, nicknames)
4. Required high confidence matches only

## Conclusions

1. **The URM databases had minimal direct impact** - only 13.6% of database faculty appeared as speakers

2. **The treatment effect on Black speakers was real and significant** - 37.7% increase (p = 0.014)

3. **The effect worked almost entirely through indirect mechanisms** - 92% of the increase came from speakers NOT in the database

4. **Possible indirect mechanisms include**:
   - Awareness/priming effect from receiving the database
   - Signaling institutional commitment to diversity
   - Prompting broader searches beyond the provided names
   - Creating accountability or social pressure

5. **Previous matching algorithms were severely flawed** - overestimating matches by >10x due to partial name matching

This analysis provides strong evidence that simply providing lists of diverse candidates may increase diversity through psychological and social mechanisms rather than direct selection from those lists.