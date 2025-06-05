# Peer-Specific Database Matching Analysis: Final Summary

## Algorithm Clarification
The Qualtrics algorithm shows each department:
1. **At least 40 peer universities** (±20 ranks, expanded if needed)
2. **All URM faculty from those universities** (typically 20-65 faculty, average ~30)
3. Further expansion only if <20 URM faculty found

## Key Findings

### Database Exposure
- **Treatment departments** saw an average of 29.2 URM faculty (13.5 Black)
- **Control departments** saw an average of 30.6 URM faculty (14.0 Black)
- Range: 0-65 faculty (0 for departments without rankings)

### Question 1: % of speakers from shown database
- **Treatment**: 0.12% of all speakers came from shown databases
- **Control**: 0.10% of all speakers came from shown databases
- No significant difference

### Question 2: Binary - ANY speaker from shown database
- **Treatment**: 17/282 departments (6.0%) selected ≥1 speaker
- **Control**: 14/286 departments (4.9%) selected ≥1 speaker  
- p = 0.682 (not significant)

### Critical Finding: Black Speaker Selection
Despite similar overall database usage:
- **Treatment**: 10 Black speakers from shown databases
- **Control**: 3 Black speakers from shown databases
- **3.3x more Black speakers** selected by treatment departments

## Interpretation

1. **The database email did NOT increase overall database usage** - treatment and control departments were equally likely to select from their peer databases

2. **But it DID change WHO was selected** - treatment departments selected 3.3x more Black speakers when they did use the database

3. **The main effect worked indirectly** - the 37.7% increase in Black speaker representation came mostly (92%) from speakers NOT in the database

4. **Mechanism appears to be priming/awareness** - receiving the database changed search behavior even when not directly using it

## Technical Note
The peer contingency is properly accounted for. Each department saw only faculty from their ~40 peer universities, not the full database of 550 faculty. This makes the lack of difference in usage rates even more striking.