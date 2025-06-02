#!/usr/bin/env python3
"""
Spring Data Puller for Search Costs RCT
Pulls Spring semester data from Google Sheets and integrates with pipeline
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime

# Add paths
sys.path.append(str(Path(__file__).parent / ".."))
from core.google_sheets_client import google_sheets_client
from config.settings import config

def pull_spring_data(sheet_url, sheet_name="Spring '25 Seminars", validate_only=False):
    """Pull Spring data from Google Sheets"""
    
    print(f"=== Spring Data Puller ===")
    print(f"Started at: {datetime.now()}")
    print("")
    
    # Validate connection first
    print("Step 1: Validating Google Sheets connection...")
    connection_ok = google_sheets_client.validate_connection(sheet_url)
    
    if not connection_ok:
        print("❌ Connection validation failed")
        print("Please check your Google Sheets API configuration:")
        print("1. Ensure GOOGLE_SHEETS_API_KEY is set in .env, OR")
        print("2. Ensure GOOGLE_SERVICE_ACCOUNT_FILE points to valid JSON file")
        return False
    
    if validate_only:
        print("✅ Connection validation successful")
        return True
    
    # Get available sheets
    print("\nStep 2: Checking available sheets...")
    available_sheets = google_sheets_client.get_available_sheets(sheet_url)
    
    if available_sheets:
        print("Available sheets:")
        for sheet in available_sheets:
            marker = "⭐" if sheet['title'] == sheet_name else "  "
            print(f"{marker} {sheet['title']} ({sheet['rows']} rows, {sheet['cols']} cols)")
        print("")
    
    # Fetch the data
    print(f"Step 3: Fetching data from '{sheet_name}'...")
    try:
        spring_df = google_sheets_client.fetch_spring_data(sheet_url, sheet_name)
        
        if spring_df is None or len(spring_df) == 0:
            print("❌ No data retrieved")
            return False
        
        print(f"✅ Successfully retrieved {len(spring_df)} rows")
        
        # Display summary
        print(f"\nSpring Data Summary:")
        print(f"  Rows: {len(spring_df)}")
        print(f"  Columns: {len(spring_df.columns)}")
        print(f"  File saved: {config.MASTER_DATA_SPRING}")
        
        # Show first few rows (for verification)
        print(f"\nFirst 3 rows preview:")
        print(spring_df.head(3).to_string())
        
        return True
        
    except Exception as e:
        print(f"❌ Failed to fetch Spring data: {e}")
        return False

def main():
    """Command line interface"""
    parser = argparse.ArgumentParser(description='Pull Spring data from Google Sheets')
    parser.add_argument('--url', 
                       default='https://docs.google.com/spreadsheets/d/1k6xDRMJkYGaX0cbXZ3cyJeEUMYJSs6fMIQEn-T--3QQ/edit?gid=1686776172#gid=1686776172',
                       help='Google Sheets URL (default: your Spring 25 sheet)')
    parser.add_argument('--sheet-name', 
                       default="Spring '25 Seminars",
                       help="Name of the sheet/tab to fetch")
    parser.add_argument('--validate-only', action='store_true',
                       help='Only validate connection, do not fetch data')
    
    args = parser.parse_args()
    
    # Check if environment is configured
    api_status = config.get_api_status()
    if not api_status.get('google_sheets', False):
        print("❌ Google Sheets API not configured")
        print("Please run: ./setup_env.sh and configure Google Sheets credentials")
        sys.exit(1)
    
    # Pull the data
    success = pull_spring_data(
        sheet_url=args.url,
        sheet_name=args.sheet_name,
        validate_only=args.validate_only
    )
    
    if success:
        if not args.validate_only:
            print("\n🎉 Spring data pull successful!")
            print("\nNext steps:")
            print("1. Run unified data processor: python3 ../core/data_processor.py --mode merge-spring")
            print("2. Or run full analysis: ./run-full-analysis-optimized.sh")
        sys.exit(0)
    else:
        print("\n❌ Spring data pull failed")
        sys.exit(1)

if __name__ == "__main__":
    main()