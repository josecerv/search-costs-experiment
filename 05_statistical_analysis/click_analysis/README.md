# Click Analysis Documentation

## Overview
This directory contains the corrected click analysis for the seminar database intervention experiment. The analysis tracks which seminars had their database links clicked by recipients of our email campaign.

## Key Files

### Primary Analysis Script
- `analyze_seminar_clicks.py` - Main analysis script that:
  - Loads seminar data from multiple sources
  - Matches email recipients to seminars
  - Calculates click rates avoiding double-counting
  - Generates detailed statistics by treatment condition

### Output Files
- `corrected_results.json` - Summary statistics including:
  - Overall click rate: 55.3% (915/1654 seminars)
  - Treatment vs control comparison
  - Click source breakdown
- `seminar_click_details_corrected.csv` - Seminar-level data with click status
- `ground_truth_results.json` - Previous version (kept for reference)
- `seminar_click_details.csv` - Previous version details

### Documentation
- `GROUND_TRUTH_REPORT.md` - Initial analysis findings
- `REVIEWER_SCRUTINY_REPORT.md` - Validation checks and corrections

## Data Sources

1. **Master Seminar Dataset**: `/05_statistical_analysis/outputs/master_analysis_dataset.csv`
   - Contains all 1,654 seminars with treatment assignments
   - Key fields: seminar_id, university, discipline, treatment

2. **Seminar Names Mapping**: `/04_demographic_analysis/outputs/speaker_appearances_analysis.csv`
   - Maps seminar_id to actual seminar names
   - Critical for matching email references to seminars

3. **Email Campaign Data**: `/02_intervention_materials/email_campaigns/email-launch.csv`
   - 1,599 emails sent to faculty, seminar organizers, and department chairs
   - Contains bit.ly links and recipient information

4. **Click Data**: `/01_experiment_design/bitly_cache.json`
   - Raw click counts for each bit.ly link
   - Total: 892 clicks across 531 links

## Analysis Methodology

### 1. Seminar-Email Matching
The analysis matches seminars to email recipients through:

- **Department Chairs**: When a department chair clicks, ALL seminars in their department are marked as clicked
  - Example: Chair of "MIT-Physics" clicks → all MIT Physics seminars marked as clicked
  
- **Faculty/Seminar Organizers**: Match specific seminars listed in their email
  - Uses flexible name matching to handle variations
  - Example: "Topology Seminar" matches "topology seminar series"

### 2. Click Attribution (Avoiding Double-Counting)
**Critical**: Each click is counted only once in totals, but properly attributed to all relevant seminars.

- If a department chair's link got 5 clicks, those 5 clicks count toward the total
- But all 10 seminars in that department are marked as "clicked" (binary yes/no)
- This gives us both accurate click counts AND seminar coverage

### 3. Treatment vs Control
Emails and seminars were randomized into treatment/control:
- Treatment: Links to database with scholar profiles
- Control: Links to database with department listings

## Key Results

### Overall Engagement
- **55.3%** of seminars (915/1654) had at least one click
- **892** total clicks across all links
- **531** links clicked out of 1,599 sent (33.2%)

### By Treatment Condition
- **Treatment**: 55.2% click rate (446/808 seminars), 476 total clicks
- **Control**: 55.4% click rate (469/846 seminars), 416 total clicks

### By Contact Type
Seminars reached by:
- Department chairs: 725 seminars
- Faculty: 200 seminars  
- Seminar contacts: 160 seminars
- Multiple sources: 170 seminars

## Common Pitfalls to Avoid

1. **Double-Counting Clicks**: Previous scripts summed clicks across seminars, inflating totals
2. **Poor Matching Logic**: Must use seminar names from speaker_appearances_analysis.csv
3. **Missing Department Chairs**: They cover multiple seminars - don't attribute to just one
4. **Overly Strict Name Matching**: Use flexible comparison for seminar names

## Running the Analysis

```bash
cd /Users/josecervantez/Documents/Jose-CODE/search-costs
python 05_statistical_analysis/click_analysis/analyze_seminar_clicks.py
```

The script will:
1. Load and merge all data sources
2. Process 1,599 email records
3. Output results to JSON and CSV files
4. Print summary statistics to console

## For Future Analysis

When updating or re-running:
1. Ensure all source data files are present and up-to-date
2. Check that seminar IDs are consistent across datasets
3. Verify bit.ly data matches the email campaign period
4. Use the corrected methodology to avoid double-counting

The analysis shows strong engagement with over half of seminars having someone explore the database tools we provided.