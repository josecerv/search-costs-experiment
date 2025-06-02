#!/usr/bin/env python3
"""
Comprehensive Statistical Analysis for Search Costs RCT
Generates summary statistics and runs OLS analysis with bin fixed effects
Tests the four main research questions with p-values overall and by semester
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.iolib.summary2 import summary_col
import sys
from pathlib import Path
from datetime import datetime
import warnings

warnings.filterwarnings('ignore')

# Add config path
sys.path.append(str(Path(__file__).parent.parent.parent / "03_data_collection"))
from config.settings import config

class ComprehensiveAnalysis:
    """
    Comprehensive analysis for the Search Costs RCT
    """
    
    def __init__(self):
        self.config = config
        self.results = {}
        print(f"=== Comprehensive Search Costs RCT Analysis ===")
        print(f"Started at: {datetime.now()}")
    
    def load_analysis_data(self):
        """Load the processed demographic analysis data"""
        print("\n=== Loading Analysis Data ===")
        
        # Look for the most recent combined analysis file
        combined_file = self.config.DEMOGRAPHIC_OUTPUTS_DIR / "people_combined_analysis.csv"
        appearance_file = self.config.DEMOGRAPHIC_OUTPUTS_DIR / "speaker_appearances_analysis.csv"
        
        # Try full year data first
        full_year_demo = self.config.PROJECT_ROOT / "04_demographic_analysis" / "outputs" / "people_combined_analysis_full_year.csv"
        
        if full_year_demo.exists():
            print(f"Loading full year demographic data: {full_year_demo}")
            speakers_df = pd.read_csv(full_year_demo, encoding='utf-8-sig')
        elif combined_file.exists():
            print(f"Loading demographic data: {combined_file}")
            speakers_df = pd.read_csv(combined_file, encoding='utf-8-sig')
        else:
            raise FileNotFoundError("No demographic analysis results found. Run demographic analysis first.")
        
        # Load the complete dataset for seminar-level information
        if self.config.MASTER_DATA_FULL_YEAR.exists():
            print(f"Loading full year seminar data: {self.config.MASTER_DATA_FULL_YEAR}")
            seminars_df = pd.read_csv(self.config.MASTER_DATA_FULL_YEAR, encoding='utf-8-sig', low_memory=False)
        elif self.config.MASTER_DATA_COMPLETE.exists():
            print(f"Loading fall seminar data: {self.config.MASTER_DATA_COMPLETE}")
            seminars_df = pd.read_csv(self.config.MASTER_DATA_COMPLETE, encoding='utf-8-sig', low_memory=False)
        else:
            raise FileNotFoundError("No processed seminar data found. Run data processing first.")
        
        print(f"Loaded {len(speakers_df)} speakers and {len(seminars_df)} seminars")
        
        return speakers_df, seminars_df
    
    def create_analysis_dataset(self, speakers_df, seminars_df):
        """Create the analysis dataset by combining speakers and seminars"""
        print("\n=== Creating Analysis Dataset ===")
        
        # Extract speaker appearances from seminar data
        appearances = []
        
        for idx, seminar_row in seminars_df.iterrows():
            seminar_info = {
                'seminar_id': seminar_row.get('seminar_id'),
                'university': seminar_row.get('university', ''),
                'discipline': seminar_row.get('discipline', ''),
                'seminar_name': seminar_row.get('seminar_name', ''),
                'condition': seminar_row.get('condition', ''),
                'bin_category': seminar_row.get('bin_category', ''),
                'contact_type': seminar_row.get('contact_type', ''),
                'Link': seminar_row.get('Link', '')
            }
            
            # Extract speakers for this seminar
            seminar_speakers = []
            for i in range(1, 204):  # Check up to 203 speakers (includes Spring)
                fn_col = f'First Name_{i}'
                ln_col = f'Last Name_{i}'
                
                if fn_col not in seminars_df.columns:
                    break
                
                first_name = seminar_row.get(fn_col, '')
                last_name = seminar_row.get(ln_col, '')
                
                # Check if speaker has any name information
                has_first = pd.notna(first_name) and str(first_name).strip() != ''
                has_last = pd.notna(last_name) and str(last_name).strip() != ''
                
                if has_first or has_last:
                    speaker_name = f"{first_name or ''} {last_name or ''}".strip()
                    speaker_info = {
                        **seminar_info,
                        'speaker_position': i,
                        'speaker_name': speaker_name,
                        'first_name': str(first_name).strip() if pd.notna(first_name) else '',
                        'last_name': str(last_name).strip() if pd.notna(last_name) else '',
                        'speaker_university': seminar_row.get(f'university_{i}', ''),
                        'speaker_rank': seminar_row.get(f'rank_{i}', ''),
                        'speaker_date': seminar_row.get(f'date_{i}', '')
                    }
                    seminar_speakers.append(speaker_info)
            
            # Add appearances for this seminar
            appearances.extend(seminar_speakers)
        
        appearances_df = pd.DataFrame(appearances)
        print(f"Extracted {len(appearances_df)} speaker appearances")
        
        # Merge with demographic data
        # We'll need to match speakers by name and affiliation
        # This is a simplified approach - in practice you'd use the speaker_id from the optimized system
        
        def find_demographic_match(speaker_row):
            """Find matching demographic data for a speaker"""
            speaker_name = speaker_row['speaker_name'].lower().strip()
            
            # Try to find exact name match first
            name_matches = speakers_df[speakers_df['name'].str.lower().str.strip() == speaker_name]
            
            # Define which columns to return
            demo_columns = ['combined_gender', 'combined_race', 'is_urm', 
                          'face_analysis_success', 'name_analysis_success', 
                          'speaker_id', 'photo_count']
            
            if len(name_matches) == 1:
                match = name_matches.iloc[0]
                return pd.Series({col: match.get(col, '') for col in demo_columns})
            elif len(name_matches) > 1:
                # Multiple matches, try to disambiguate by university
                speaker_uni = str(speaker_row.get('speaker_university', '')).lower().strip()
                seminar_uni = str(speaker_row.get('university', '')).lower().strip()
                
                for uni_key in [speaker_uni, seminar_uni]:
                    if uni_key:
                        uni_matches = name_matches[name_matches['university'].str.lower().str.contains(uni_key, na=False, regex=False)]
                        if len(uni_matches) >= 1:
                            match = uni_matches.iloc[0]
                            return pd.Series({col: match.get(col, '') for col in demo_columns})
                
                # If still multiple, return first
                match = name_matches.iloc[0]
                return pd.Series({col: match.get(col, '') for col in demo_columns})
            
            # No exact match, return default values
            return pd.Series({
                'combined_gender': 'unknown',
                'combined_race': 'unknown', 
                'is_urm': False,
                'face_analysis_success': False,
                'name_analysis_success': False,
                'speaker_id': '',
                'photo_count': 0
            })
        
        # Add demographic information
        print("Matching speakers with demographic data...")
        demo_data = appearances_df.apply(find_demographic_match, axis=1)
        
        # Combine with appearance data
        analysis_df = pd.concat([appearances_df, demo_data], axis=1)
        
        # Determine semester based on speaker date
        def determine_semester(date_str):
            """Determine if a date falls in Fall 2024 or Spring 2025"""
            if pd.isna(date_str) or str(date_str).strip() == '':
                return 'Fall 2024'  # Default to Fall if no date
            
            date_str = str(date_str).strip()
            
            # Try to parse the date
            try:
                # Handle various date formats
                if '/' in date_str:
                    # Format like 1/15/2025 or 01/15/2025
                    parts = date_str.split('/')
                    if len(parts) == 3:
                        month = int(parts[0])
                        year = int(parts[2]) if len(parts[2]) == 4 else 2000 + int(parts[2])
                elif '-' in date_str:
                    # Format like 2025-01-15
                    parts = date_str.split('-')
                    if len(parts) == 3:
                        year = int(parts[0])
                        month = int(parts[1])
                else:
                    return 'Fall 2024'  # Can't parse, default to Fall
                
                # Determine semester based on month and year
                # Fall 2024: August 2024 - December 2024
                # Spring 2025: January 2025 - May 2025
                if year == 2024 and month >= 8:
                    return 'Fall 2024'
                elif year == 2025 and month <= 5:
                    return 'Spring 2025'
                else:
                    return 'Fall 2024'  # Default for unclear cases
                    
            except:
                return 'Fall 2024'  # Default if parsing fails
        
        # Apply semester determination to each speaker
        analysis_df['semester'] = analysis_df['speaker_date'].apply(determine_semester)
        
        # Clean up and add derived variables
        analysis_df['is_treatment'] = (analysis_df['condition'] == 'treatment').astype(int)
        analysis_df['is_control'] = (analysis_df['condition'] == 'control').astype(int)
        analysis_df['is_male'] = (analysis_df['combined_gender'] == 'Male').astype(int)
        analysis_df['is_female'] = (analysis_df['combined_gender'] == 'Female').astype(int)
        analysis_df['is_urm'] = analysis_df['is_urm'].astype(int)
        
        # Add department identifier
        analysis_df['department'] = analysis_df['university'].astype(str) + ' - ' + analysis_df['discipline'].astype(str)
        
        print(f"Final analysis dataset: {len(analysis_df)} speaker appearances")
        
        return analysis_df
    
    def generate_summary_statistics(self, analysis_df):
        """Generate comprehensive summary statistics"""
        print("\n=== Generating Summary Statistics ===")
        
        summaries = {}
        
        # 1. Number of seminars by condition and semester
        seminar_summary = analysis_df.groupby(['semester', 'condition'])['seminar_id'].nunique().reset_index()
        seminar_summary.columns = ['semester', 'condition', 'n_seminars']
        seminar_pivot = seminar_summary.pivot(index='semester', columns='condition', values='n_seminars').fillna(0)
        
        print("📊 Seminars by Condition and Semester:")
        print(seminar_pivot)
        summaries['seminars_by_condition_semester'] = seminar_pivot
        
        # 2. Number of speakers by condition and semester
        speaker_summary = analysis_df.groupby(['semester', 'condition']).size().reset_index()
        speaker_summary.columns = ['semester', 'condition', 'n_speakers']
        speaker_pivot = speaker_summary.pivot(index='semester', columns='condition', values='n_speakers').fillna(0)
        
        print("\n📊 Speakers by Condition and Semester:")
        print(speaker_pivot)
        summaries['speakers_by_condition_semester'] = speaker_pivot
        
        # 3. Average speakers per seminar by department
        dept_avg = analysis_df.groupby(['department', 'condition']).agg({
            'seminar_id': 'nunique',
            'speaker_name': 'count'
        }).reset_index()
        dept_avg['avg_speakers_per_seminar'] = dept_avg['speaker_name'] / dept_avg['seminar_id']
        dept_avg = dept_avg.pivot(index='department', columns='condition', values='avg_speakers_per_seminar').fillna(0)
        
        print(f"\n📊 Average Speakers per Seminar by Department:")
        print(dept_avg.round(2))
        summaries['avg_speakers_per_seminar_by_dept'] = dept_avg
        
        # 4. Gender distribution
        gender_summary = analysis_df.groupby(['semester', 'condition', 'combined_gender']).size().unstack(fill_value=0)
        print(f"\n📊 Gender Distribution:")
        print(gender_summary)
        summaries['gender_distribution'] = gender_summary
        
        # 5. URM distribution
        urm_summary = analysis_df.groupby(['semester', 'condition'])['is_urm'].agg(['count', 'sum', 'mean']).round(3)
        urm_summary.columns = ['total_speakers', 'urm_speakers', 'urm_percentage']
        print(f"\n📊 URM Distribution:")
        print(urm_summary)
        summaries['urm_distribution'] = urm_summary
        
        # Overall summary
        print(f"\n📊 Overall Summary:")
        print(f"Total Seminars: {analysis_df['seminar_id'].nunique()}")
        print(f"Total Speakers: {len(analysis_df)}")
        print(f"Unique Speakers: {analysis_df['speaker_name'].nunique()}")
        print(f"Treatment Seminars: {analysis_df[analysis_df['condition'] == 'treatment']['seminar_id'].nunique()}")
        print(f"Control Seminars: {analysis_df[analysis_df['condition'] == 'control']['seminar_id'].nunique()}")
        
        self.results['summary_statistics'] = summaries
        return summaries
    
    def create_seminar_level_dataset(self, analysis_df):
        """Create seminar-level dataset for regression analysis"""
        print("\n=== Creating Seminar-Level Dataset ===")
        
        # Aggregate to seminar-semester level (seminars can have different speakers in different semesters)
        seminar_level = analysis_df.groupby(['seminar_id', 'semester']).agg({
            'university': 'first',
            'discipline': 'first',
            'seminar_name': 'first',
            'condition': 'first',
            'bin_category': 'first',
            'department': 'first',
            'is_treatment': 'first',
            'speaker_name': 'count',  # Total speakers
            'is_urm': ['sum', 'mean'],  # URM count and percentage
            'is_male': ['sum', 'mean'],  # Male count and percentage
            'is_female': ['sum', 'mean']  # Female count and percentage
        }).reset_index()
        
        # Flatten column names
        seminar_level.columns = [
            'seminar_id', 'semester', 'university', 'discipline', 'seminar_name', 'condition',
            'bin_category', 'department', 'is_treatment',
            'total_speakers', 'urm_count', 'urm_percentage',
            'male_count', 'male_percentage', 'female_count', 'female_percentage'
        ]
        
        # Add non-URM count
        seminar_level['non_urm_count'] = seminar_level['total_speakers'] - seminar_level['urm_count']
        
        # Only keep seminars that actually had speakers in that semester
        seminar_level = seminar_level[seminar_level['total_speakers'] > 0]
        
        print(f"Seminar-level dataset: {len(seminar_level)} seminar-semester combinations")
        print(f"  - Fall 2024: {len(seminar_level[seminar_level['semester'] == 'Fall 2024'])} seminars")
        print(f"  - Spring 2025: {len(seminar_level[seminar_level['semester'] == 'Spring 2025'])} seminars")
        
        return seminar_level
    
    def run_ols_analysis(self, seminar_df):
        """Run OLS analysis with bin fixed effects for the four research questions"""
        print("\n=== Running OLS Analysis with Bin Fixed Effects ===")
        
        # Ensure bin_category is treated as categorical
        seminar_df['bin_category'] = seminar_df['bin_category'].astype(str)
        
        # Research Question 1: Effect on URM percentage
        print("\n📊 Research Question 1: Effect on % URM Speakers")
        
        # Overall analysis
        model1_overall = smf.ols('urm_percentage ~ is_treatment + C(bin_category)', data=seminar_df).fit(cov_type='cluster', cov_kwds={'groups': seminar_df['department']})
        
        # By semester analysis
        fall_data = seminar_df[seminar_df['semester'].str.contains('Fall', na=False, regex=False)]
        spring_data = seminar_df[seminar_df['semester'].str.contains('Spring', na=False, regex=False)]
        
        models = {'Overall': model1_overall}
        
        if len(fall_data) > 0:
            model1_fall = smf.ols('urm_percentage ~ is_treatment + C(bin_category)', data=fall_data).fit(cov_type='cluster', cov_kwds={'groups': fall_data['department']})
            models['Fall'] = model1_fall
        
        if len(spring_data) > 0:
            model1_spring = smf.ols('urm_percentage ~ is_treatment + C(bin_category)', data=spring_data).fit(cov_type='cluster', cov_kwds={'groups': spring_data['department']})
            models['Spring'] = model1_spring
        
        # Extract results
        q1_results = {}
        for period, model in models.items():
            treatment_coef = model.params.get('is_treatment', np.nan)
            treatment_pvalue = model.pvalues.get('is_treatment', np.nan)
            treatment_se = model.bse.get('is_treatment', np.nan)
            
            q1_results[period] = {
                'coefficient': treatment_coef,
                'std_error': treatment_se,
                'p_value': treatment_pvalue,
                'n_obs': model.nobs,
                'r_squared': model.rsquared
            }
            
            print(f"{period}: β={treatment_coef:.4f}, SE={treatment_se:.4f}, p={treatment_pvalue:.4f}, N={model.nobs}")
        
        # Research Question 2a: Effect on total speakers
        print("\n📊 Research Question 2a: Effect on Total Speakers")
        
        model2a_overall = smf.ols('total_speakers ~ is_treatment + C(bin_category)', data=seminar_df).fit(cov_type='cluster', cov_kwds={'groups': seminar_df['department']})
        
        models_2a = {'Overall': model2a_overall}
        
        if len(fall_data) > 0:
            model2a_fall = smf.ols('total_speakers ~ is_treatment + C(bin_category)', data=fall_data).fit(cov_type='cluster', cov_kwds={'groups': fall_data['department']})
            models_2a['Fall'] = model2a_fall
        
        if len(spring_data) > 0:
            model2a_spring = smf.ols('total_speakers ~ is_treatment + C(bin_category)', data=spring_data).fit(cov_type='cluster', cov_kwds={'groups': spring_data['department']})
            models_2a['Spring'] = model2a_spring
        
        q2a_results = {}
        for period, model in models_2a.items():
            treatment_coef = model.params.get('is_treatment', np.nan)
            treatment_pvalue = model.pvalues.get('is_treatment', np.nan)
            treatment_se = model.bse.get('is_treatment', np.nan)
            
            q2a_results[period] = {
                'coefficient': treatment_coef,
                'std_error': treatment_se,
                'p_value': treatment_pvalue,
                'n_obs': model.nobs,
                'r_squared': model.rsquared
            }
            
            print(f"{period}: β={treatment_coef:.4f}, SE={treatment_se:.4f}, p={treatment_pvalue:.4f}, N={model.nobs}")
        
        # Research Question 2b: Effect on URM count
        print("\n📊 Research Question 2b: Effect on URM Count")
        
        model2b_overall = smf.ols('urm_count ~ is_treatment + C(bin_category)', data=seminar_df).fit(cov_type='cluster', cov_kwds={'groups': seminar_df['department']})
        
        models_2b = {'Overall': model2b_overall}
        
        if len(fall_data) > 0:
            model2b_fall = smf.ols('urm_count ~ is_treatment + C(bin_category)', data=fall_data).fit(cov_type='cluster', cov_kwds={'groups': fall_data['department']})
            models_2b['Fall'] = model2b_fall
        
        if len(spring_data) > 0:
            model2b_spring = smf.ols('urm_count ~ is_treatment + C(bin_category)', data=spring_data).fit(cov_type='cluster', cov_kwds={'groups': spring_data['department']})
            models_2b['Spring'] = model2b_spring
        
        q2b_results = {}
        for period, model in models_2b.items():
            treatment_coef = model.params.get('is_treatment', np.nan)
            treatment_pvalue = model.pvalues.get('is_treatment', np.nan)
            treatment_se = model.bse.get('is_treatment', np.nan)
            
            q2b_results[period] = {
                'coefficient': treatment_coef,
                'std_error': treatment_se,
                'p_value': treatment_pvalue,
                'n_obs': model.nobs,
                'r_squared': model.rsquared
            }
            
            print(f"{period}: β={treatment_coef:.4f}, SE={treatment_se:.4f}, p={treatment_pvalue:.4f}, N={model.nobs}")
        
        # Research Question 2c: Effect on non-URM count
        print("\n📊 Research Question 2c: Effect on Non-URM Count")
        
        model2c_overall = smf.ols('non_urm_count ~ is_treatment + C(bin_category)', data=seminar_df).fit(cov_type='cluster', cov_kwds={'groups': seminar_df['department']})
        
        models_2c = {'Overall': model2c_overall}
        
        if len(fall_data) > 0:
            model2c_fall = smf.ols('non_urm_count ~ is_treatment + C(bin_category)', data=fall_data).fit(cov_type='cluster', cov_kwds={'groups': fall_data['department']})
            models_2c['Fall'] = model2c_fall
        
        if len(spring_data) > 0:
            model2c_spring = smf.ols('non_urm_count ~ is_treatment + C(bin_category)', data=spring_data).fit(cov_type='cluster', cov_kwds={'groups': spring_data['department']})
            models_2c['Spring'] = model2c_spring
        
        q2c_results = {}
        for period, model in models_2c.items():
            treatment_coef = model.params.get('is_treatment', np.nan)
            treatment_pvalue = model.pvalues.get('is_treatment', np.nan)
            treatment_se = model.bse.get('is_treatment', np.nan)
            
            q2c_results[period] = {
                'coefficient': treatment_coef,
                'std_error': treatment_se,
                'p_value': treatment_pvalue,
                'n_obs': model.nobs,
                'r_squared': model.rsquared
            }
            
            print(f"{period}: β={treatment_coef:.4f}, SE={treatment_se:.4f}, p={treatment_pvalue:.4f}, N={model.nobs}")
        
        # Store all results
        ols_results = {
            'q1_urm_percentage': q1_results,
            'q2a_total_speakers': q2a_results, 
            'q2b_urm_count': q2b_results,
            'q2c_non_urm_count': q2c_results
        }
        
        self.results['ols_analysis'] = ols_results
        
        # Create summary table
        self._create_results_table(ols_results)
        
        return ols_results
    
    def _create_results_table(self, ols_results):
        """Create a summary table of all results"""
        print("\n=== 📊 COMPREHENSIVE RESULTS TABLE ===")
        
        # Create results dataframe
        results_data = []
        
        for question, periods in ols_results.items():
            for period, results in periods.items():
                results_data.append({
                    'Research_Question': question,
                    'Period': period,
                    'Coefficient': results['coefficient'],
                    'Std_Error': results['std_error'],
                    'P_Value': results['p_value'],
                    'Significant': '***' if results['p_value'] < 0.01 else '**' if results['p_value'] < 0.05 else '*' if results['p_value'] < 0.10 else '',
                    'N_Observations': results['n_obs'],
                    'R_Squared': results['r_squared']
                })
        
        results_df = pd.DataFrame(results_data)
        
        # Format and display
        print(results_df.round(4).to_string(index=False))
        
        # Save results
        output_path = self.config.STATISTICAL_ANALYSIS_DIR / "outputs" / "comprehensive_results.csv"
        results_df.to_csv(output_path, index=False)
        print(f"\n✅ Results saved to: {output_path}")
        
        # Key findings summary
        print("\n=== 🎯 KEY FINDINGS SUMMARY ===")
        
        overall_results = results_df[results_df['Period'] == 'Overall']
        
        for _, row in overall_results.iterrows():
            significance = row['Significant']
            direction = "increases" if row['Coefficient'] > 0 else "decreases"
            
            print(f"{row['Research_Question']}: Treatment {direction} outcome by {abs(row['Coefficient']):.4f} {significance}")
            print(f"  p-value: {row['P_Value']:.4f}, N: {int(row['N_Observations'])}")
    
    def run_comprehensive_analysis(self):
        """Run the complete analysis pipeline"""
        try:
            # Load data
            speakers_df, seminars_df = self.load_analysis_data()
            
            # Create analysis dataset
            analysis_df = self.create_analysis_dataset(speakers_df, seminars_df)
            
            # Generate summary statistics
            summary_stats = self.generate_summary_statistics(analysis_df)
            
            # Create seminar-level dataset
            seminar_df = self.create_seminar_level_dataset(analysis_df)
            
            # Run OLS analysis
            ols_results = self.run_ols_analysis(seminar_df)
            
            print(f"\n🎉 Comprehensive analysis complete!")
            print(f"Results saved to: {self.config.STATISTICAL_ANALYSIS_DIR}/outputs/")
            
            return True
            
        except Exception as e:
            print(f"❌ Analysis failed: {e}")
            import traceback
            traceback.print_exc()
            return False

def main():
    """Main function"""
    analyzer = ComprehensiveAnalysis()
    success = analyzer.run_comprehensive_analysis()
    
    if success:
        print("\n✅ Analysis completed successfully!")
    else:
        print("\n❌ Analysis failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()