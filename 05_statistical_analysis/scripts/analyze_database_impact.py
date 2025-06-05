#!/usr/bin/env python3
"""
Analyze Database Impact on Seminar Speakers

This script analyzes whether departments selected speakers from the URM databases
provided in the treatment condition, accounting for the peer university algorithm.

Key analyses:
1. % of female/URM/Black/Hispanic speakers from database in eligible peer departments
2. Count of these speakers  
3. Binary presence (any speaker from database)
4. Comparison between treatment and control conditions
"""

import json
import logging
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, List, Set, Tuple
import sys

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent.parent))

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class DatabaseImpactAnalyzer:
    """Analyze the impact of URM databases on seminar speaker selection"""

    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.outputs_dir = self.base_dir / "outputs"
        self.cache_dir = self.base_dir / "cache"
        
        # University rankings by discipline
        self.rankings = self._load_university_rankings()
        
    def _load_university_rankings(self) -> Dict[str, List[str]]:
        """Load university rankings for each discipline"""
        
        # Rankings from the Qualtrics algorithm
        rankings = {
            "Physics": [
                "Massachusetts Institute of Technology", "Stanford University", "California Institute of Technology",
                "Harvard University", "Princeton University", "University of California, Berkeley", "Cornell University",
                "University of Chicago", "Columbia University", "University of California, Santa Barbara",
                "University of Illinois Urbana-Champaign", "Yale University", "Johns Hopkins University",
                "University of Michigan", "University of Pennsylvania", "University of Texas at Austin",
                "University of California, Los Angeles", "University of Colorado Boulder",
                "University of Maryland, College Park", "University of Washington", "Georgia Institute of Technology",
                "Northwestern University", "Pennsylvania State University", "Rice University",
                "Stony Brook University", "University of California, San Diego", "University of Wisconsin-Madison",
                "Carnegie Mellon University", "Duke University", "New York University", "Ohio State University",
                "Rutgers University-New Brunswick", "Brown University", "University of North Carolina at Chapel Hill",
                "Michigan State University", "University of Arizona", "University of California, Irvine",
                "Boston University", "Purdue University", "University of California, Davis", "University of Florida",
                "University of Minnesota", "University of Pittsburgh", "University of Virginia", "Vanderbilt University",
                "Washington University in St. Louis", "Texas A&M University", "University of California, Santa Cruz",
                "University of Notre Dame", "Arizona State University", "Florida State University",
                "Indiana University Bloomington", "University of Rochester", "Virginia Tech",
                "Case Western Reserve University", "Graduate Center, CUNY", "Dartmouth College", "Emory University",
                "Iowa State University", "Northeastern University", "Rensselaer Polytechnic Institute",
                "Syracuse University", "University of California, Riverside", "University of Massachusetts Amherst",
                "University of Southern California", "University of Tennessee", "Brandeis University",
                "Clemson University", "North Carolina State University", "University of Iowa", "University of Oregon",
                "University of Utah", "Boston College", "Louisiana State University", "University of Delaware",
                "University of Illinois Chicago", "University of New Mexico", "Colorado School of Mines",
                "Colorado State University", "Georgetown University", "Tufts University", "University of Connecticut",
                "University of Kansas", "University of Nebraska-Lincoln", "University of Oklahoma",
                "Washington State University", "Kansas State University", "University at Buffalo", "University of Georgia",
                "University of Houston", "University of Kentucky", "University of Texas at Dallas", "Baylor University",
                "Drexel University", "Ohio University", "Temple University", "Tulane University",
                "University of Central Florida", "University of Cincinnati", "University of Maryland, Baltimore County",
                "University of Wisconsin-Milwaukee", "West Virginia University", "Auburn University",
                "Oregon State University", "University of Hawaii at Manoa", "University of Missouri",
                "University of Texas at Arlington", "George Mason University", "George Washington University",
                "Montana State University", "Oklahoma State University-Stillwater", "University of Alabama",
                "University of Miami", "University of New Hampshire", "University of South Carolina",
                "Georgia State University", "New Jersey Institute of Technology", "University of Alabama in Huntsville",
                "University of Nevada, Las Vegas", "Wayne State University", "Binghamton University", "Kent State University",
                "Texas Tech University", "University of Arkansas", "University of Denver", "University of South Florida",
                "Mississippi State University", "University at Albany, SUNY", "University of Mississippi",
                "University of Colorado Denver", "Old Dominion University", "University of Alabama at Birmingham",
                "University of Louisville", "University of Maine", "University of Nevada, Reno", "University of Memphis",
                "University of North Texas", "Virginia Commonwealth University", "Utah State University",
                "Florida International University", "University of Texas at San Antonio", "University of Texas at El Paso",
                "North Dakota State University", "University of Louisiana at Lafayette", "University of Southern Mississippi",
                "University of Montana"
            ],
            # Add other disciplines' rankings here (Chemistry, CS, Math, MechE)
            # For now, using Physics ranking as placeholder for all
            "Chemistry": None,  # Will use Physics as default
            "Computer Science": None,
            "Mathematics": None,
            "Mechanical Engineering": None
        }
        
        # Use Physics ranking as default for other disciplines for now
        for discipline in ["Chemistry", "Computer Science", "Mathematics", "Mechanical Engineering"]:
            if rankings[discipline] is None:
                rankings[discipline] = rankings["Physics"]
                
        return rankings
        
    def get_peer_universities(self, university: str, discipline: str, min_faculty: int = 20) -> List[str]:
        """
        Get peer universities using the algorithm from the Qualtrics survey.
        
        Args:
            university: Name of the university
            discipline: Academic discipline
            min_faculty: Minimum number of URM faculty to ensure (default 20)
            
        Returns:
            List of peer university names
        """
        ranking = self.rankings.get(discipline, self.rankings["Physics"])
        
        try:
            index = ranking.index(university)
        except ValueError:
            logger.warning(f"University {university} not found in {discipline} ranking")
            return []
            
        # Initial peer selection: +/- 20 ranks
        min_rank = max(0, index - 20)
        max_rank = min(len(ranking) - 1, index + 20)
        peers = ranking[min_rank:max_rank + 1]
        peers = [p for p in peers if p != university]
        
        # Ensure at least 40 peers (expanding symmetrically if needed)
        rank_inc = 1
        while len(peers) < 40 and len(peers) < len(ranking) - 1:
            new_min = max(0, index - 20 - rank_inc)
            new_max = min(len(ranking) - 1, index + 20 + rank_inc)
            
            if new_min < min_rank and ranking[new_min] not in peers:
                peers.insert(0, ranking[new_min])
                min_rank = new_min
                
            if new_max > max_rank and ranking[new_max] not in peers:
                peers.append(ranking[new_max])
                max_rank = new_max
                
            rank_inc += 1
            
        return peers
        
    def load_data(self) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """Load all necessary data files"""
        
        logger.info("Loading data files...")
        
        # Load speaker appearances data (individual speaker level)
        speaker_data_path = Path(__file__).parent.parent.parent / "04_demographic_analysis" / "outputs" / "speaker_appearances_analysis.csv"
        speaker_data = pd.read_csv(speaker_data_path)
        
        # Load LLM matching results
        llm_matches = pd.read_csv(self.outputs_dir / "llm_database_speaker_matches.csv")
        
        # Load faculty count data
        faculty_counts_path = Path(__file__).parent.parent.parent / "06_archive" / "department faculty count.csv"
        faculty_counts = pd.read_csv(faculty_counts_path)
        
        # Load URM database files
        database_dir = Path(__file__).parent.parent.parent / "02_intervention_materials" / "databases"
        urm_databases = {}
        for discipline in ['chemistry', 'computerScience', 'mathematics', 'mechanicalEngineering', 'physics']:
            db_path = database_dir / f"{discipline}.csv"
            if db_path.exists():
                urm_databases[discipline] = pd.read_csv(db_path)
                
        return speaker_data, llm_matches, faculty_counts, urm_databases
        
    def analyze_database_impact(self):
        """Main analysis function"""
        
        # Load data
        speaker_data, llm_matches, faculty_counts, urm_databases = self.load_data()
        
        # Get unique departments with treatment assignment
        dept_info = speaker_data.groupby(['university', 'discipline']).agg({
            'condition': 'first'
        }).reset_index()
        
        # Map discipline names to database names
        discipline_map = {
            'Chemistry': 'chemistry',
            'Physics': 'physics',
            'Mathematics': 'mathematics',
            'Computer Science': 'computerScience',
            'Mechanical Engineering': 'mechanicalEngineering'
        }
        
        results = []
        
        for _, dept in dept_info.iterrows():
            university = dept['university']
            discipline = dept['discipline']
            condition = dept['condition']
            
            # Get peer universities for this department
            peers = self.get_peer_universities(university, discipline)
            
            # Get speakers from this department's seminars
            dept_speakers = speaker_data[
                (speaker_data['university'] == university) & 
                (speaker_data['discipline'] == discipline)
            ]
            
            # Filter to speakers from peer universities only
            peer_speakers = dept_speakers[dept_speakers['affiliation_standardized'].isin(peers)]
            
            # Get matched database speakers for this discipline
            db_matches = llm_matches[
                (llm_matches['database_discipline'] == discipline) & 
                (llm_matches['matched'] == True)
            ]
            
            # Filter to database faculty from peer universities
            peer_db_matches = db_matches[db_matches['database_university'].isin(peers)]
            
            # Get the full URM database for this discipline to count available faculty
            db_key = discipline_map.get(discipline)
            if db_key and db_key in urm_databases:
                full_db = urm_databases[db_key]
                # Filter to peer universities
                peer_db_full = full_db[full_db['Schools'].isin(peers)]
            else:
                peer_db_full = pd.DataFrame()
            
            # Calculate metrics for each demographic group
            for demo_group in ['female', 'URM', 'Black', 'Hispanic']:
                # Get speakers from peer universities with this demographic
                if demo_group == 'female':
                    peer_speakers_demo = peer_speakers[peer_speakers['combined_gender'] == 'woman']
                elif demo_group == 'URM':
                    peer_speakers_demo = peer_speakers[peer_speakers['is_urm'] == True]
                elif demo_group == 'Black':
                    peer_speakers_demo = peer_speakers[peer_speakers['combined_race'] == 'black']
                elif demo_group == 'Hispanic':
                    peer_speakers_demo = peer_speakers[peer_speakers['combined_race'] == 'latino']
                
                # Count how many database faculty of this demographic were available
                if demo_group == 'female' and not peer_db_full.empty:
                    db_demo_count = len(peer_db_full[peer_db_full['Gender'] == 'Female'])
                elif demo_group in ['URM', 'Black', 'Hispanic'] and not peer_db_full.empty:
                    if demo_group == 'URM':
                        db_demo_count = len(peer_db_full[peer_db_full['Race'].isin(['Black', 'Hispanic'])])
                    else:
                        db_demo_count = len(peer_db_full[peer_db_full['Race'] == demo_group])
                else:
                    db_demo_count = 0
                
                # Get matched speakers for this demographic
                if demo_group == 'female':
                    matched_speakers = peer_speakers_demo[
                        peer_speakers_demo['name'].isin(peer_db_matches['speaker_name'].values)
                    ]
                else:
                    # For race-based demographics, need to check both speaker and database demographics
                    if demo_group == 'URM':
                        relevant_db_matches = peer_db_matches[
                            peer_db_matches['database_race'].isin(['Black', 'Hispanic'])
                        ]
                    elif demo_group == 'Black':
                        relevant_db_matches = peer_db_matches[
                            peer_db_matches['database_race'] == 'Black'
                        ]
                    elif demo_group == 'Hispanic':
                        relevant_db_matches = peer_db_matches[
                            peer_db_matches['database_race'] == 'Hispanic'
                        ]
                    
                    matched_speakers = peer_speakers_demo[
                        peer_speakers_demo['name'].isin(relevant_db_matches['speaker_name'].values)
                    ]
                
                # Calculate metrics
                total_peer_speakers = len(peer_speakers)
                total_demo_speakers = len(peer_speakers_demo)
                matched_count = len(matched_speakers.drop_duplicates(subset=['name', 'affiliation_standardized']))
                
                # Percentage of demographic speakers from database
                pct_from_db = (matched_count / total_demo_speakers * 100) if total_demo_speakers > 0 else 0
                
                # Binary: any speaker from database
                any_from_db = 1 if matched_count > 0 else 0
                
                results.append({
                    'university': university,
                    'discipline': discipline,
                    'condition': condition,
                    'demographic': demo_group,
                    'total_peer_speakers': total_peer_speakers,
                    'total_demo_speakers': total_demo_speakers,
                    'matched_speakers_count': matched_count,
                    'pct_demo_from_database': pct_from_db,
                    'any_speaker_from_database': any_from_db,
                    'num_peer_universities': len(peers),
                    'num_demo_in_database': db_demo_count
                })
        
        # Convert to DataFrame
        results_df = pd.DataFrame(results)
        
        # Calculate summary statistics by condition
        summary_stats = []
        
        for demo in ['female', 'URM', 'Black', 'Hispanic']:
            demo_results = results_df[results_df['demographic'] == demo]
            
            for condition in ['treatment', 'control']:
                cond_data = demo_results[demo_results['condition'] == condition]
                
                summary_stats.append({
                    'demographic': demo,
                    'condition': condition,
                    'n_departments': len(cond_data),
                    'mean_pct_from_database': cond_data['pct_demo_from_database'].mean(),
                    'std_pct_from_database': cond_data['pct_demo_from_database'].std(),
                    'total_matched_speakers': cond_data['matched_speakers_count'].sum(),
                    'total_demo_speakers': cond_data['total_demo_speakers'].sum(),
                    'pct_depts_with_any_match': cond_data['any_speaker_from_database'].mean() * 100,
                    'mean_demo_in_database': cond_data['num_demo_in_database'].mean()
                })
                
        summary_df = pd.DataFrame(summary_stats)
        
        # Calculate treatment effects
        treatment_effects = []
        
        for demo in ['female', 'URM', 'Black', 'Hispanic']:
            demo_results = results_df[results_df['demographic'] == demo]
            
            treatment_data = demo_results[demo_results['condition'] == 'treatment']
            control_data = demo_results[demo_results['condition'] == 'control']
            
            # T-test for percentage from database
            from scipy import stats
            t_stat, p_value = stats.ttest_ind(
                treatment_data['pct_demo_from_database'].dropna(),
                control_data['pct_demo_from_database'].dropna()
            )
            
            # Calculate effect sizes
            treatment_mean = treatment_data['pct_demo_from_database'].mean()
            control_mean = control_data['pct_demo_from_database'].mean()
            effect_size = treatment_mean - control_mean
            
            treatment_effects.append({
                'demographic': demo,
                'treatment_mean_pct': treatment_mean,
                'control_mean_pct': control_mean,
                'effect_size_pct': effect_size,
                'relative_increase_pct': (effect_size / control_mean * 100) if control_mean > 0 else np.nan,
                't_statistic': t_stat,
                'p_value': p_value,
                'significant': p_value < 0.05
            })
            
        effects_df = pd.DataFrame(treatment_effects)
        
        # Create comprehensive output
        comprehensive_results = []
        
        for demo in ['female', 'URM', 'Black', 'Hispanic']:
            # Get data for each condition
            for condition in ['treatment', 'control']:
                cond_summary = summary_df[
                    (summary_df['demographic'] == demo) & 
                    (summary_df['condition'] == condition)
                ].iloc[0]
                
                comprehensive_results.append({
                    'demographic': demo,
                    'condition': condition,
                    'pct_speakers_from_database': float(cond_summary['mean_pct_from_database']),
                    'count_speakers_from_database': int(cond_summary['total_matched_speakers']),
                    'total_speakers_in_demographic': int(cond_summary['total_demo_speakers']),
                    'any_speaker_from_database_pct': float(cond_summary['pct_depts_with_any_match']),
                    'n_departments': int(cond_summary['n_departments']),
                    'mean_available_in_database': float(cond_summary['mean_demo_in_database'])
                })
            
            # Add treatment effect row
            effect = effects_df[effects_df['demographic'] == demo].iloc[0]
            comprehensive_results.append({
                'demographic': demo,
                'condition': 'treatment_effect',
                'pct_speakers_from_database': float(effect['effect_size_pct']),
                'count_speakers_from_database': None,
                'total_speakers_in_demographic': None,
                'any_speaker_from_database_pct': None,
                'n_departments': None,
                'mean_available_in_database': None,
                'p_value': float(effect['p_value']),
                'relative_increase_pct': float(effect['relative_increase_pct']) if pd.notna(effect['relative_increase_pct']) else None
            })
        
        # Save single comprehensive CSV
        comprehensive_df = pd.DataFrame(comprehensive_results)
        comprehensive_df.to_csv(self.outputs_dir / "database_impact_analysis.csv", index=False)
        
        # Also save JSON for easy parsing
        with open(self.outputs_dir / "database_impact_analysis.json", "w") as f:
            json.dump({
                "analysis_date": str(pd.Timestamp.now()),
                "results": comprehensive_results,
                "summary": {
                    "female": {
                        "treatment_pct": float(summary_df[(summary_df['demographic'] == 'female') & (summary_df['condition'] == 'treatment')]['mean_pct_from_database'].values[0]),
                        "control_pct": float(summary_df[(summary_df['demographic'] == 'female') & (summary_df['condition'] == 'control')]['mean_pct_from_database'].values[0]),
                        "treatment_count": int(summary_df[(summary_df['demographic'] == 'female') & (summary_df['condition'] == 'treatment')]['total_matched_speakers'].values[0]),
                        "control_count": int(summary_df[(summary_df['demographic'] == 'female') & (summary_df['condition'] == 'control')]['total_matched_speakers'].values[0]),
                        "treatment_any_pct": float(summary_df[(summary_df['demographic'] == 'female') & (summary_df['condition'] == 'treatment')]['pct_depts_with_any_match'].values[0]),
                        "control_any_pct": float(summary_df[(summary_df['demographic'] == 'female') & (summary_df['condition'] == 'control')]['pct_depts_with_any_match'].values[0])
                    },
                    "URM": {
                        "treatment_pct": float(summary_df[(summary_df['demographic'] == 'URM') & (summary_df['condition'] == 'treatment')]['mean_pct_from_database'].values[0]),
                        "control_pct": float(summary_df[(summary_df['demographic'] == 'URM') & (summary_df['condition'] == 'control')]['mean_pct_from_database'].values[0]),
                        "treatment_count": int(summary_df[(summary_df['demographic'] == 'URM') & (summary_df['condition'] == 'treatment')]['total_matched_speakers'].values[0]),
                        "control_count": int(summary_df[(summary_df['demographic'] == 'URM') & (summary_df['condition'] == 'control')]['total_matched_speakers'].values[0]),
                        "treatment_any_pct": float(summary_df[(summary_df['demographic'] == 'URM') & (summary_df['condition'] == 'treatment')]['pct_depts_with_any_match'].values[0]),
                        "control_any_pct": float(summary_df[(summary_df['demographic'] == 'URM') & (summary_df['condition'] == 'control')]['pct_depts_with_any_match'].values[0])
                    },
                    "Black": {
                        "treatment_pct": float(summary_df[(summary_df['demographic'] == 'Black') & (summary_df['condition'] == 'treatment')]['mean_pct_from_database'].values[0]),
                        "control_pct": float(summary_df[(summary_df['demographic'] == 'Black') & (summary_df['condition'] == 'control')]['mean_pct_from_database'].values[0]),
                        "treatment_count": int(summary_df[(summary_df['demographic'] == 'Black') & (summary_df['condition'] == 'treatment')]['total_matched_speakers'].values[0]),
                        "control_count": int(summary_df[(summary_df['demographic'] == 'Black') & (summary_df['condition'] == 'control')]['total_matched_speakers'].values[0]),
                        "treatment_any_pct": float(summary_df[(summary_df['demographic'] == 'Black') & (summary_df['condition'] == 'treatment')]['pct_depts_with_any_match'].values[0]),
                        "control_any_pct": float(summary_df[(summary_df['demographic'] == 'Black') & (summary_df['condition'] == 'control')]['pct_depts_with_any_match'].values[0])
                    },
                    "Hispanic": {
                        "treatment_pct": float(summary_df[(summary_df['demographic'] == 'Hispanic') & (summary_df['condition'] == 'treatment')]['mean_pct_from_database'].values[0]),
                        "control_pct": float(summary_df[(summary_df['demographic'] == 'Hispanic') & (summary_df['condition'] == 'control')]['mean_pct_from_database'].values[0]),
                        "treatment_count": int(summary_df[(summary_df['demographic'] == 'Hispanic') & (summary_df['condition'] == 'treatment')]['total_matched_speakers'].values[0]),
                        "control_count": int(summary_df[(summary_df['demographic'] == 'Hispanic') & (summary_df['condition'] == 'control')]['total_matched_speakers'].values[0]),
                        "treatment_any_pct": float(summary_df[(summary_df['demographic'] == 'Hispanic') & (summary_df['condition'] == 'treatment')]['pct_depts_with_any_match'].values[0]),
                        "control_any_pct": float(summary_df[(summary_df['demographic'] == 'Hispanic') & (summary_df['condition'] == 'control')]['pct_depts_with_any_match'].values[0])
                    }
                }
            }, f, indent=2)
        
        logger.info("Analysis complete! Saved to database_impact_analysis.csv")
        


def main():
    """Main entry point"""
    analyzer = DatabaseImpactAnalyzer()
    analyzer.analyze_database_impact()


if __name__ == "__main__":
    main()