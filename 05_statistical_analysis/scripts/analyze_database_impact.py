#!/usr/bin/env python3
"""
Simple Database Impact Analysis at Seminar Level

For each seminar:
- Denominator: ALL speakers in the seminar
- Numerator: Speakers who were in the tailored database shown to that department
  (i.e., URM faculty from peer universities)
"""

import json
import logging
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, List, Tuple
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


class SimpleDatabaseAnalyzer:
    """Simple analysis of database impact"""
    
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.outputs_dir = self.base_dir / "outputs"
        self.data_dir = Path(__file__).parent.parent.parent
        
        # Load rankings
        self._load_rankings()
        
    def _load_rankings(self) -> None:
        """Load university rankings by discipline"""
        logger.info("Loading university rankings...")
        
        master_df = pd.read_csv(self.outputs_dir / "master_analysis_dataset.csv")
        self.rankings = {}
        
        for discipline in master_df["discipline"].unique():
            disc_data = master_df[master_df["discipline"] == discipline]
            uni_ranks = disc_data[["university", "dept_ranking"]].drop_duplicates()
            uni_ranks = uni_ranks[uni_ranks["dept_ranking"].notna()]
            uni_ranks = uni_ranks.sort_values("dept_ranking")
            self.rankings[discipline] = uni_ranks["university"].tolist()
            
    def get_peer_universities(self, university: str, discipline: str) -> List[str]:
        """Get peer universities (±20 ranks, min 40)"""
        ranking = self.rankings.get(discipline, [])
        
        if university not in ranking:
            return []
            
        index = ranking.index(university)
        
        # ±20 ranks
        min_rank = max(0, index - 20)
        max_rank = min(len(ranking) - 1, index + 20)
        peers = ranking[min_rank:max_rank + 1]
        peers = [p for p in peers if p != university]
        
        # Expand to 40
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
        
    def run_analysis(self) -> None:
        """Run the simple analysis"""
        
        logger.info("Loading data...")
        
        # Load speaker data
        speaker_data = pd.read_csv(
            self.data_dir / "04_demographic_analysis/outputs/speaker_appearances_analysis.csv"
        )
        
        # Load LLM matches to get database faculty
        llm_matches = pd.read_csv(self.outputs_dir / "llm_database_speaker_matches.csv")
        matched_db = llm_matches[llm_matches['matched'] == True]
        
        # Create mapping of speaker_id to database info
        db_speaker_map = {}
        for _, row in matched_db.iterrows():
            db_speaker_map[row['speaker_id']] = {
                'database_university': row['database_university'],
                'database_discipline': row['database_discipline'],
                'database_race': row['database_race'],
                'database_gender': row['database_gender']
            }
        
        # Get unique seminars
        seminars = speaker_data.groupby(['seminar_id', 'university', 'discipline', 'condition']).size().reset_index()
        
        logger.info(f"Analyzing {len(seminars)} seminars...")
        
        results = []
        
        for _, seminar in seminars.iterrows():
            seminar_id = seminar['seminar_id']
            university = seminar['university']
            discipline = seminar['discipline']
            condition = seminar['condition']
            
            # Get peer universities for this department
            peers = self.get_peer_universities(university, discipline)
            if not peers:
                continue
            
            # Get all speakers for this seminar
            sem_speakers = speaker_data[speaker_data['seminar_id'] == seminar_id]
            total_speakers = len(sem_speakers)
            unique_speakers = sem_speakers['speaker_id'].nunique()
            
            # Count speakers who:
            # 1. Are in the database (matched)
            # 2. Are from peer universities
            # 3. Are in the correct discipline
            
            speakers_from_db = 0
            urm_from_db = 0
            black_from_db = 0
            hispanic_from_db = 0
            female_from_db = 0
            
            for _, speaker in sem_speakers.iterrows():
                speaker_id = speaker['speaker_id']
                
                # Check if speaker is in database
                if speaker_id in db_speaker_map:
                    db_info = db_speaker_map[speaker_id]
                    
                    # Check if from peer university and correct discipline
                    if (db_info['database_university'] in peers and 
                        db_info['database_discipline'] == discipline):
                        
                        speakers_from_db += 1
                        
                        # Check demographics from SPEAKER data, not database
                        speaker_race = speaker.get('combined_race', '')
                        speaker_gender = speaker.get('combined_gender', '')
                        
                        if speaker_race in ['black', 'latino', 'hispanic']:
                            urm_from_db += 1
                        if speaker_race == 'black':
                            black_from_db += 1
                        if speaker_race in ['latino', 'hispanic']:
                            hispanic_from_db += 1
                        if speaker_gender == 'woman':
                            female_from_db += 1
            
            # Calculate percentages
            result = {
                'seminar_id': seminar_id,
                'university': university,
                'discipline': discipline,
                'condition': condition,
                'total_speakers': total_speakers,
                'unique_speakers': unique_speakers,
                'speakers_from_db': speakers_from_db,
                'urm_from_db': urm_from_db,
                'black_from_db': black_from_db,
                'hispanic_from_db': hispanic_from_db,
                'female_from_db': female_from_db,
                'pct_from_db': (speakers_from_db / total_speakers * 100) if total_speakers > 0 else 0,
                'pct_urm_from_db': (urm_from_db / total_speakers * 100) if total_speakers > 0 else 0,
                'pct_black_from_db': (black_from_db / total_speakers * 100) if total_speakers > 0 else 0,
                'pct_hispanic_from_db': (hispanic_from_db / total_speakers * 100) if total_speakers > 0 else 0,
                'pct_female_from_db': (female_from_db / total_speakers * 100) if total_speakers > 0 else 0,
                'any_from_db': 1 if speakers_from_db > 0 else 0,
                'any_urm_from_db': 1 if urm_from_db > 0 else 0,
                'any_black_from_db': 1 if black_from_db > 0 else 0,
                'any_hispanic_from_db': 1 if hispanic_from_db > 0 else 0,
                'any_female_from_db': 1 if female_from_db > 0 else 0
            }
            
            results.append(result)
        
        # Convert to DataFrame
        df = pd.DataFrame(results)
        
        # Generate summary
        self.generate_summary(df)
        
    def generate_summary(self, df: pd.DataFrame) -> None:
        """Generate summary statistics"""
        
        logger.info("Generating summary...")
        
        treatment = df[df['condition'] == 'treatment']
        control = df[df['condition'] == 'control']
        
        print("\n" + "="*80)
        print("DATABASE IMPACT ANALYSIS - SIMPLE VERSION")
        print("="*80)
        
        print(f"\nOVERALL:")
        print(f"  Seminars analyzed: {len(df)}")
        print(f"  Treatment: {len(treatment)}")
        print(f"  Control: {len(control)}")
        print(f"  Total speaker appearances: {df['total_speakers'].sum():,}")
        print(f"  Total unique speakers: {df['unique_speakers'].sum():,}")
        
        # Summary statistics
        summary_data = []
        
        print(f"\nPERCENTAGE OF SPEAKERS FROM DATABASE (MEAN ± SD):")
        
        for metric, label in [
            ('pct_from_db', 'All speakers'),
            ('pct_urm_from_db', 'URM speakers'),
            ('pct_black_from_db', 'Black speakers'),
            ('pct_hispanic_from_db', 'Hispanic speakers'),
            ('pct_female_from_db', 'Female speakers')
        ]:
            treat_mean = treatment[metric].mean()
            treat_std = treatment[metric].std()
            control_mean = control[metric].mean()
            control_std = control[metric].std()
            
            # T-test
            t_stat, p_value = stats.ttest_ind(treatment[metric], control[metric])
            
            print(f"\n{label}:")
            print(f"  Treatment: {treat_mean:.3f}% ± {treat_std:.3f}%")
            print(f"  Control: {control_mean:.3f}% ± {control_std:.3f}%")
            print(f"  Difference: {treat_mean - control_mean:.3f} pp")
            print(f"  Relative: {((treat_mean - control_mean) / control_mean * 100):.1f}%" if control_mean > 0 else "  Relative: N/A")
            print(f"  P-value: {p_value:.3f}")
            
            summary_data.append({
                'metric': label,
                'treatment_mean': treat_mean,
                'treatment_std': treat_std,
                'control_mean': control_mean,
                'control_std': control_std,
                'difference_pp': treat_mean - control_mean,
                'relative_pct': ((treat_mean - control_mean) / control_mean * 100) if control_mean > 0 else None,
                'p_value': p_value
            })
        
        print(f"\nSEMINARS WITH ANY SPEAKER FROM DATABASE:")
        
        for metric, label in [
            ('any_from_db', 'Any speaker'),
            ('any_urm_from_db', 'Any URM'),
            ('any_black_from_db', 'Any Black'),
            ('any_hispanic_from_db', 'Any Hispanic'),
            ('any_female_from_db', 'Any Female')
        ]:
            treat_pct = treatment[metric].mean() * 100
            control_pct = control[metric].mean() * 100
            
            # Fisher's exact test
            from scipy.stats import fisher_exact
            contingency = [
                [treatment[metric].sum(), len(treatment) - treatment[metric].sum()],
                [control[metric].sum(), len(control) - control[metric].sum()]
            ]
            _, p_value = fisher_exact(contingency)
            
            print(f"\n{label}:")
            print(f"  Treatment: {treatment[metric].sum()}/{len(treatment)} ({treat_pct:.1f}%)")
            print(f"  Control: {control[metric].sum()}/{len(control)} ({control_pct:.1f}%)")
            print(f"  P-value: {p_value:.3f}")
        
        # Total counts
        print(f"\nTOTAL SPEAKER COUNTS:")
        print(f"  From database - Treatment: {treatment['speakers_from_db'].sum()}, Control: {control['speakers_from_db'].sum()}")
        print(f"  URM from database - Treatment: {treatment['urm_from_db'].sum()}, Control: {control['urm_from_db'].sum()}")
        print(f"  Black from database - Treatment: {treatment['black_from_db'].sum()}, Control: {control['black_from_db'].sum()}")
        print(f"  Hispanic from database - Treatment: {treatment['hispanic_from_db'].sum()}, Control: {control['hispanic_from_db'].sum()}")
        
        # Save outputs
        df.to_csv(self.outputs_dir / "database_impact_final.csv", index=False)
        
        summary_df = pd.DataFrame(summary_data)
        summary_df.to_csv(self.outputs_dir / "database_impact_summary_final.csv", index=False)
        
        # Create final JSON report
        output = {
            'analysis_date': str(pd.Timestamp.now()),
            'methodology': 'Percentage of all seminar speakers who were from the tailored database',
            'overall': {
                'seminars_analyzed': len(df),
                'treatment_seminars': len(treatment),
                'control_seminars': len(control),
                'total_speakers': int(df['total_speakers'].sum()),
                'unique_speakers': int(df['unique_speakers'].sum())
            },
            'key_results': summary_df.to_dict('records'),
            'interpretation': 'Treatment shows what % of speakers came from the URM database shown to that department'
        }
        
        with open(self.outputs_dir / "database_impact_final.json", "w") as f:
            json.dump(output, f, indent=2)
            
        print(f"\nFINAL OUTPUTS:")
        print(f"  - database_impact_final.csv")
        print(f"  - database_impact_summary_final.csv")
        print(f"  - database_impact_final.json")


def main():
    """Run the analysis"""
    analyzer = SimpleDatabaseAnalyzer()
    analyzer.run_analysis()


if __name__ == "__main__":
    main()