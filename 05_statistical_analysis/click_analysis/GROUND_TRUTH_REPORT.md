# Ground Truth Click Analysis Report

## Summary

The previous analysis scripts contained errors in matching seminars to email recipients, resulting in severe undercounting of engagement, particularly for faculty and seminar-specific contacts.

## Key Findings

### Overall Engagement
- **55.3%** of seminars (915/1654) had their database link clicked at least once
- Total clicks: 1,894 across all seminars
- Average clicks per seminar: 1.15

### By Treatment Condition
**Treatment Group:**
- Click rate: 55.2% (446/808 seminars)
- Total clicks: 1,009
- Average clicks per seminar: 1.25

**Control Group:**
- Click rate: 55.4% (469/846 seminars)  
- Total clicks: 885
- Average clicks per seminar: 1.05

### Click Sources
Seminars reached by contact type:
- Department chairs: 725 seminars (1,286 clicks)
- Faculty: 200 seminars (348 clicks)
- Seminar contacts: 160 seminars (260 clicks)
- Seminars with multiple click sources: 170

## Errors in Previous Analysis

The old scripts reported:
- Only 38 faculty clicked (vs. actual 200)
- Only 69 seminar contacts clicked (vs. actual 160)
- Overall click rate of 47.5% (vs. actual 55.3%)

The main issue was incorrect matching logic between the master seminar dataset and email campaign data. The old scripts failed to properly:
1. Use the seminar name mapping from speaker_appearances_analysis.csv
2. Match seminars with flexible name comparison
3. Account for all variations in how seminars were referenced

## Conclusions

1. **Engagement was strong**: Over half of all seminars had someone click on their database link
2. **Treatment effect on intensity**: While click rates were similar between groups (55.2% vs 55.4%), the treatment group had higher engagement intensity (1.25 vs 1.05 clicks per seminar)
3. **Department chairs were key**: They accounted for the majority of engagement, reaching 725 seminars
4. **Faculty and seminar organizers also engaged**: Combined, they reached 360 seminars, much higher than previously reported

## Data Files
- Analysis script: `/05_statistical_analysis/click_analysis/analyze_seminar_clicks.py`
- Results: `/05_statistical_analysis/click_analysis/ground_truth_results.json`
- Detailed data: `/05_statistical_analysis/click_analysis/seminar_click_details.csv`