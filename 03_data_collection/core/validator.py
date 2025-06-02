"""
Data Validation for Search Costs RCT
Comprehensive validation of data quality and experimental integrity
"""

import pandas as pd
import numpy as np
import re
from pathlib import Path
import sys
from datetime import datetime

# Add config to path
sys.path.append(str(Path(__file__).parent / ".."))
from config.settings import config

class DataValidator:
    """
    Comprehensive data validation for the Search Costs RCT
    """
    
    def __init__(self):
        self.validation_results = {}
        
    def validate_column_structure(self, df):
        """Validate expected column structure"""
        print("=== Column Structure Validation ===")
        
        # Required base columns
        required_base = [
            'seminar_id', 'university', 'discipline', 'seminar_name',
            'condition', 'contact_type', 'Link', 'bin_category'
        ]
        
        missing_base = [col for col in required_base if col not in df.columns]
        if missing_base:
            print(f"❌ Missing required columns: {missing_base}")
            return False
        else:
            print(f"✅ All required base columns present")
        
        # Check speaker columns
        speaker_patterns = [
            r'First Name_\d+',
            r'Last Name_\d+', 
            r'rank_\d+',
            r'university_\d+',
            r'date_\d+'
        ]
        
        speaker_cols = []
        for pattern in speaker_patterns:
            matching_cols = [col for col in df.columns if re.match(pattern, col)]
            speaker_cols.extend(matching_cols)
        
        # Find max speaker number
        max_speaker_num = 0
        for col in speaker_cols:
            match = re.search(r'_(\d+)$', col)
            if match:
                num = int(match.group(1))
                max_speaker_num = max(max_speaker_num, num)
        
        print(f"✅ Speaker columns found up to speaker #{max_speaker_num}")
        
        self.validation_results['column_structure'] = {
            'required_columns_present': len(missing_base) == 0,
            'missing_columns': missing_base,
            'max_speaker_number': max_speaker_num,
            'total_speaker_columns': len(speaker_cols)
        }
        
        return len(missing_base) == 0
    
    def validate_data_types(self, df):
        """Validate data types and formats"""
        print("\n=== Data Type Validation ===")
        
        issues = []
        
        # Seminar ID should be numeric or string that can be converted
        if 'seminar_id' in df.columns:
            invalid_ids = df[df['seminar_id'].isna()]
            if len(invalid_ids) > 0:
                issues.append(f"Found {len(invalid_ids)} rows with missing seminar_id")
        
        # Condition should be 'control' or 'treatment'
        if 'condition' in df.columns:
            valid_conditions = {'control', 'treatment'}
            invalid_conditions = df[~df['condition'].isin(valid_conditions) & df['condition'].notna()]
            if len(invalid_conditions) > 0:
                unique_invalid = invalid_conditions['condition'].unique()
                issues.append(f"Found invalid conditions: {unique_invalid}")
        
        # University and discipline should be strings
        for col in ['university', 'discipline', 'seminar_name']:
            if col in df.columns:
                empty_values = df[df[col].isna() | (df[col] == '')]
                if len(empty_values) > 0:
                    issues.append(f"Found {len(empty_values)} empty values in {col}")
        
        if issues:
            print(f"❌ Data type issues found:")
            for issue in issues:
                print(f"   - {issue}")
        else:
            print(f"✅ No data type issues found")
        
        self.validation_results['data_types'] = {
            'issues_found': len(issues),
            'issues': issues
        }
        
        return len(issues) == 0
    
    def validate_experimental_integrity(self, df):
        """Validate experimental design integrity"""
        print("\n=== Experimental Integrity Validation ===")
        
        issues = []
        
        # Treatment balance
        if 'condition' in df.columns:
            condition_counts = df['condition'].value_counts()
            
            if 'control' not in condition_counts or 'treatment' not in condition_counts:
                issues.append("Missing control or treatment group")
            else:
                control_count = condition_counts['control']
                treatment_count = condition_counts['treatment']
                
                # Check if groups are reasonably balanced (within 20%)
                balance_ratio = min(control_count, treatment_count) / max(control_count, treatment_count)
                
                if balance_ratio < 0.8:
                    issues.append(f"Groups are imbalanced: control={control_count}, treatment={treatment_count}")
                
                print(f"Treatment balance: control={control_count}, treatment={treatment_count} (ratio: {balance_ratio:.3f})")
        
        # Stratification integrity
        if 'bin_category' in df.columns and 'condition' in df.columns:
            # Check if each bin has both treatment and control
            cross_tab = pd.crosstab(df['bin_category'], df['condition'], dropna=False)
            
            for bin_cat in cross_tab.index:
                control_in_bin = cross_tab.loc[bin_cat, 'control'] if 'control' in cross_tab.columns else 0
                treatment_in_bin = cross_tab.loc[bin_cat, 'treatment'] if 'treatment' in cross_tab.columns else 0
                
                if control_in_bin == 0 or treatment_in_bin == 0:
                    issues.append(f"Bin {bin_cat} is missing control or treatment assignments")
        
        # Check for duplicate seminar IDs
        if 'seminar_id' in df.columns:
            duplicates = df[df['seminar_id'].duplicated()]
            if len(duplicates) > 0:
                issues.append(f"Found {len(duplicates)} duplicate seminar IDs")
        
        if issues:
            print(f"❌ Experimental integrity issues:")
            for issue in issues:
                print(f"   - {issue}")
        else:
            print(f"✅ Experimental integrity validated")
        
        self.validation_results['experimental_integrity'] = {
            'issues_found': len(issues),
            'issues': issues
        }
        
        return len(issues) == 0
    
    def validate_speaker_data(self, df):
        """Validate speaker data quality"""
        print("\n=== Speaker Data Validation ===")
        
        # Count seminars with speakers
        seminars_with_speakers = 0
        total_speakers = 0
        speaker_name_issues = 0
        
        for idx, row in df.iterrows():
            seminar_has_speaker = False
            
            i = 1
            while f'First Name_{i}' in df.columns or f'Last Name_{i}' in df.columns:
                fn_col = f'First Name_{i}'
                ln_col = f'Last Name_{i}'
                
                fn = row.get(fn_col, '')
                ln = row.get(ln_col, '')
                
                # Check if speaker has at least first or last name
                has_first = pd.notna(fn) and str(fn).strip() != ''
                has_last = pd.notna(ln) and str(ln).strip() != ''
                
                if has_first or has_last:
                    total_speakers += 1
                    seminar_has_speaker = True
                    
                    # Check for name quality issues
                    full_name = f"{fn} {ln}".strip()
                    if len(full_name) < 3:
                        speaker_name_issues += 1
                
                i += 1
            
            if seminar_has_speaker:
                seminars_with_speakers += 1
        
        coverage_rate = seminars_with_speakers / len(df) if len(df) > 0 else 0
        avg_speakers_per_seminar = total_speakers / len(df) if len(df) > 0 else 0
        
        print(f"Speaker data summary:")
        print(f"  - Seminars with speakers: {seminars_with_speakers}/{len(df)} ({coverage_rate:.1%})")
        print(f"  - Total speakers found: {total_speakers}")
        print(f"  - Average speakers per seminar: {avg_speakers_per_seminar:.2f}")
        print(f"  - Speakers with name issues: {speaker_name_issues}")
        
        # Quality thresholds
        issues = []
        if coverage_rate < 0.5:
            issues.append(f"Low speaker coverage: only {coverage_rate:.1%} of seminars have speakers")
        
        if speaker_name_issues / total_speakers > 0.1 if total_speakers > 0 else False:
            issues.append(f"High rate of name quality issues: {speaker_name_issues}/{total_speakers}")
        
        if issues:
            print(f"❌ Speaker data issues:")
            for issue in issues:
                print(f"   - {issue}")
        else:
            print(f"✅ Speaker data quality acceptable")
        
        self.validation_results['speaker_data'] = {
            'seminars_with_speakers': seminars_with_speakers,
            'total_speakers': total_speakers,
            'coverage_rate': coverage_rate,
            'avg_speakers_per_seminar': avg_speakers_per_seminar,
            'name_issues': speaker_name_issues,
            'issues_found': len(issues),
            'issues': issues
        }
        
        return len(issues) == 0
    
    def validate_research_data(self, df_path=None):
        """Run comprehensive validation on research data"""
        print(f"=== Search Costs RCT Data Validation ===")
        print(f"Started at: {datetime.now()}")
        
        # Load data
        if df_path is None:
            df_path = config.MASTER_DATA_COMPLETE
        
        if not df_path.exists():
            print(f"❌ Data file not found: {df_path}")
            return False
        
        print(f"Loading data from: {df_path}")
        df = pd.read_csv(df_path, encoding='utf-8-sig', low_memory=False)
        print(f"Loaded {len(df)} rows, {len(df.columns)} columns")
        
        # Run all validations
        validations = [
            self.validate_column_structure(df),
            self.validate_data_types(df),
            self.validate_experimental_integrity(df), 
            self.validate_speaker_data(df)
        ]
        
        # Overall result
        all_passed = all(validations)
        
        print(f"\n=== Validation Summary ===")
        if all_passed:
            print(f"✅ All validations passed")
            print(f"Data is ready for demographic analysis")
        else:
            print(f"❌ Some validations failed")
            print(f"Please review and fix issues before proceeding")
        
        # Save validation report
        self.save_validation_report()
        
        return all_passed
    
    def save_validation_report(self):
        """Save detailed validation report"""
        report_path = config.PROCESSED_DATA_DIR / "validation_report.json"
        
        import json
        
        # Add timestamp and summary
        self.validation_results['timestamp'] = datetime.now().isoformat()
        self.validation_results['summary'] = {
            'total_validations': 4,
            'passed_validations': sum(1 for v in ['column_structure', 'data_types', 'experimental_integrity', 'speaker_data'] 
                                    if self.validation_results.get(v, {}).get('issues_found', 1) == 0)
        }
        
        with open(report_path, 'w') as f:
            json.dump(self.validation_results, f, indent=2, default=str)
        
        print(f"Validation report saved: {report_path}")

def main():
    """Command line interface for validation"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Validate Search Costs RCT data')
    parser.add_argument('--file', help='Data file to validate (default: complete dataset)')
    
    args = parser.parse_args()
    
    validator = DataValidator()
    
    if args.file:
        file_path = Path(args.file)
    else:
        file_path = None
    
    success = validator.validate_research_data(file_path)
    
    if success:
        print("\n🎉 Data validation successful!")
        exit(0)
    else:
        print("\n❌ Data validation failed!")
        exit(1)

if __name__ == "__main__":
    main()