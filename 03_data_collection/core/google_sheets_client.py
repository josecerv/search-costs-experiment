"""
Google Sheets Client for Search Costs RCT
Handles pulling Spring data from Google Sheets with robust error handling
"""

import pandas as pd
import numpy as np
import os
import requests
import json
import sys
from pathlib import Path
from datetime import datetime
import re
from dotenv import load_dotenv

# Load environment variables
env_path = Path(__file__).parent.parent.parent / '.env'
if env_path.exists():
    load_dotenv(env_path)
else:
    # Fallback to absolute path
    env_path = Path('/mnt/c/Users/jcerv/Jose/search-costs/.env')
    if env_path.exists():
        load_dotenv(env_path)

# Add config to path
sys.path.append(str(Path(__file__).parent / ".."))
from config.settings import config

class GoogleSheetsClient:
    """
    Client for accessing Google Sheets data with multiple authentication methods
    """
    
    def __init__(self):
        self.config = config
        self.api_key = self.config.GOOGLE_SHEETS_API_KEY
        self.service_account_file = self.config.GOOGLE_SERVICE_ACCOUNT_FILE
        
        # Try to initialize Google Sheets access
        self.client = None
        self.use_api_key = False
        self.use_service_account = False
        
        self._initialize_client()
    
    def _initialize_client(self):
        """Initialize the Google Sheets client with available authentication"""
        
        # Method 1: Service Account (most secure for automation)
        if self.service_account_file and os.path.exists(self.service_account_file):
            try:
                import gspread
                from google.oauth2.service_account import Credentials
                
                # Set up service account authentication
                scopes = [
                    'https://www.googleapis.com/auth/spreadsheets.readonly',
                    'https://www.googleapis.com/auth/drive.readonly'
                ]
                
                credentials = Credentials.from_service_account_file(
                    self.service_account_file, scopes=scopes
                )
                
                self.client = gspread.authorize(credentials)
                self.use_service_account = True
                print("✅ Google Sheets initialized with Service Account")
                return
                
            except ImportError:
                print("⚠️  gspread package not installed. Install with: pip install gspread google-auth")
            except Exception as e:
                print(f"⚠️  Service account authentication failed: {e}")
        
        # Method 2: API Key (simpler but requires public sheets)
        if self.api_key:
            self.use_api_key = True
            print("✅ Google Sheets initialized with API Key")
            return
        
        print("❌ No Google Sheets authentication available")
        print("Please configure either:")
        print("1. GOOGLE_SHEETS_API_KEY in .env file, OR")
        print("2. GOOGLE_SERVICE_ACCOUNT_FILE path to service account JSON")
    
    def extract_sheet_id_and_gid(self, url):
        """Extract sheet ID and gid from Google Sheets URL"""
        # Extract the spreadsheet ID
        sheet_id_match = re.search(r'/spreadsheets/d/([a-zA-Z0-9-_]+)', url)
        if not sheet_id_match:
            raise ValueError("Could not extract spreadsheet ID from URL")
        
        sheet_id = sheet_id_match.group(1)
        
        # Extract the gid (sheet/tab ID) 
        gid_match = re.search(r'[#&]gid=([0-9]+)', url)
        gid = gid_match.group(1) if gid_match else '0'
        
        return sheet_id, gid
    
    def fetch_sheet_data_api_key(self, sheet_url, sheet_name=None):
        """Fetch data using Google Sheets API with API key"""
        if not self.api_key:
            raise ValueError("Google Sheets API key not configured")
        
        sheet_id, gid = self.extract_sheet_id_and_gid(sheet_url)
        
        # If sheet name is provided, try to get the specific sheet
        if sheet_name:
            # Use the values API with sheet name
            range_name = f"'{sheet_name}'"
            api_url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/{range_name}"
        else:
            # Use the gid from URL or default sheet
            api_url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/A:ZZ"
        
        params = {
            'key': self.api_key,
            'valueRenderOption': 'UNFORMATTED_VALUE',
            'dateTimeRenderOption': 'FORMATTED_STRING'
        }
        
        try:
            print(f"Fetching data from Google Sheets API...")
            response = requests.get(api_url, params=params, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            
            if 'values' not in data:
                raise ValueError("No data found in the specified sheet")
            
            values = data['values']
            
            # Convert to DataFrame
            if len(values) == 0:
                return pd.DataFrame()
            
            # Use first row as headers
            headers = values[0] if values else []
            data_rows = values[1:] if len(values) > 1 else []
            
            # Pad rows to match header length
            max_cols = len(headers)
            padded_rows = []
            for row in data_rows:
                padded_row = row + [''] * (max_cols - len(row))
                padded_rows.append(padded_row[:max_cols])
            
            df = pd.DataFrame(padded_rows, columns=headers)
            
            print(f"✅ Successfully fetched {len(df)} rows, {len(df.columns)} columns")
            return df
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {e}")
        except json.JSONDecodeError as e:
            raise Exception(f"Failed to parse API response: {e}")
    
    def fetch_sheet_data_service_account(self, sheet_url, sheet_name=None):
        """Fetch data using gspread with service account"""
        if not self.use_service_account or not self.client:
            raise ValueError("Service account authentication not available")
        
        try:
            sheet_id, gid = self.extract_sheet_id_and_gid(sheet_url)
            
            # Open the spreadsheet
            spreadsheet = self.client.open_by_key(sheet_id)
            
            # Get the specific worksheet
            if sheet_name:
                worksheet = spreadsheet.worksheet(sheet_name)
            else:
                # Try to find worksheet by gid or use first sheet
                try:
                    worksheet = spreadsheet.get_worksheet_by_id(int(gid))
                except:
                    worksheet = spreadsheet.sheet1
            
            print(f"Fetching data from worksheet: {worksheet.title}")
            
            # Get all records as list of dictionaries
            records = worksheet.get_all_records()
            
            if not records:
                # If no records, try to get raw values
                values = worksheet.get_all_values()
                if values:
                    headers = values[0]
                    data_rows = values[1:]
                    df = pd.DataFrame(data_rows, columns=headers)
                else:
                    df = pd.DataFrame()
            else:
                df = pd.DataFrame(records)
            
            print(f"✅ Successfully fetched {len(df)} rows, {len(df.columns)} columns")
            return df
            
        except Exception as e:
            raise Exception(f"Service account fetch failed: {e}")
    
    def fetch_spring_data(self, sheet_url, sheet_name="Spring '25 Seminars"):
        """
        Main method to fetch Spring semester data
        Tries multiple authentication methods
        """
        print(f"=== Fetching Spring Data from Google Sheets ===")
        print(f"Sheet: {sheet_name}")
        print(f"URL: {sheet_url}")
        
        df = None
        errors = []
        
        # Try service account first (more reliable)
        if self.use_service_account:
            try:
                df = self.fetch_sheet_data_service_account(sheet_url, sheet_name)
                if df is not None and len(df) > 0:
                    print("✅ Data fetched using Service Account")
                    return self._process_spring_data(df)
            except Exception as e:
                errors.append(f"Service Account: {e}")
                print(f"⚠️  Service Account failed: {e}")
        
        # Try API key method
        if self.use_api_key:
            try:
                df = self.fetch_sheet_data_api_key(sheet_url, sheet_name)
                if df is not None and len(df) > 0:
                    print("✅ Data fetched using API Key")
                    return self._process_spring_data(df)
            except Exception as e:
                errors.append(f"API Key: {e}")
                print(f"⚠️  API Key failed: {e}")
        
        # If all methods failed
        if df is None or len(df) == 0:
            error_msg = "Failed to fetch data with all available methods:\n" + "\n".join(errors)
            raise Exception(error_msg)
        
        return self._process_spring_data(df)
    
    def _process_spring_data(self, df):
        """Process and validate the Spring data"""
        print(f"\n=== Processing Spring Data ===")
        print(f"Raw data shape: {df.shape}")
        
        # Ensure we have a valid DataFrame
        if not isinstance(df, pd.DataFrame):
            raise Exception(f"Expected DataFrame, got {type(df)}")
        
        if len(df) == 0:
            raise Exception("Empty DataFrame received")
        
        # Basic data cleaning
        # Remove completely empty rows
        df = df.dropna(how='all')
        
        # Strip whitespace from string columns
        try:
            string_cols = df.select_dtypes(include=['object']).columns
            for col in string_cols:
                if col in df.columns:
                    df[col] = df[col].astype(str).str.strip()
                    # Replace 'nan' strings with actual NaN
                    df[col] = df[col].replace('nan', np.nan)
        except Exception as e:
            print(f"Warning: Error cleaning string columns: {e}")
            # Continue anyway
        
        # Log column information
        print(f"Columns found: {list(df.columns)}")
        print(f"Processed data shape: {df.shape}")
        
        # Check for required columns (flexible matching)
        expected_patterns = [
            r'.*university.*|.*institution.*',
            r'.*department.*|.*discipline.*',
            r'.*seminar.*|.*title.*',
            r'.*speaker.*|.*name.*'
        ]
        
        found_columns = []
        for pattern in expected_patterns:
            matching_cols = [col for col in df.columns if re.search(pattern, col, re.IGNORECASE)]
            if matching_cols:
                found_columns.extend(matching_cols)
        
        print(f"Relevant columns identified: {found_columns}")
        
        # Save raw Spring data
        output_path = self.config.MASTER_DATA_SPRING
        df.to_csv(output_path, index=False, encoding='utf-8-sig')
        print(f"✅ Spring data saved to: {output_path}")
        
        return df
    
    def get_available_sheets(self, sheet_url):
        """Get list of available sheets/tabs in the spreadsheet"""
        if self.use_service_account and self.client:
            try:
                sheet_id, _ = self.extract_sheet_id_and_gid(sheet_url)
                spreadsheet = self.client.open_by_key(sheet_id)
                
                sheets = []
                for worksheet in spreadsheet.worksheets():
                    sheets.append({
                        'title': worksheet.title,
                        'id': worksheet.id,
                        'rows': worksheet.row_count,
                        'cols': worksheet.col_count
                    })
                
                return sheets
                
            except Exception as e:
                print(f"Could not get sheet list: {e}")
                return []
        
        return []
    
    def validate_connection(self, sheet_url):
        """Test the connection to Google Sheets"""
        print("=== Testing Google Sheets Connection ===")
        
        try:
            # Try to get basic spreadsheet info
            sheet_id, gid = self.extract_sheet_id_and_gid(sheet_url)
            print(f"Extracted Sheet ID: {sheet_id}")
            print(f"Extracted GID: {gid}")
            
            # Test connection
            if self.use_service_account:
                print("Testing service account connection...")
                sheets = self.get_available_sheets(sheet_url)
                if sheets:
                    print(f"✅ Service account working. Found {len(sheets)} sheets:")
                    for sheet in sheets:
                        print(f"  - {sheet['title']} ({sheet['rows']} rows)")
                    return True
            
            if self.use_api_key:
                print("Testing API key connection...")
                # Try a simple API call
                api_url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}"
                params = {'key': self.api_key}
                response = requests.get(api_url, params=params, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    print(f"✅ API key working. Spreadsheet: {data.get('properties', {}).get('title', 'Unknown')}")
                    return True
                else:
                    print(f"❌ API key failed: {response.status_code}")
            
            return False
            
        except Exception as e:
            print(f"❌ Connection test failed: {e}")
            return False

# Global Google Sheets client
google_sheets_client = GoogleSheetsClient()