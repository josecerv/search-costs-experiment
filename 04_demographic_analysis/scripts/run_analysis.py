"""
Demographic Analysis for Search Costs RCT
Analyzes speaker demographics according to CLAUDE.md specifications

Key features:
- Uses pre-standardized affiliations from data collection phase
- Downloads speaker photos (with rate limiting)
- Face analysis (DeepFace with subprocess isolation)
- Name analysis (GPT-4o with async processing)
- Outputs: people_combined_analysis.csv + speaker_appearances_analysis.csv
"""

# CRITICAL: Set threading before ANY imports to prevent memory corruption
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Load environment variables from .env file
from pathlib import Path
from dotenv import load_dotenv

# Load .env from project root
env_path = Path(__file__).parent.parent.parent / '.env'
if env_path.exists():
    load_dotenv(env_path)
    print(f"✅ Loaded environment from {env_path}")
else:
    print(f"⚠️  No .env file found at {env_path}")

import cv2
cv2.setNumThreads(0)  # CRITICAL: Must be before any cv2 operations

import pandas as pd
import numpy as np
import sys
from pathlib import Path
from datetime import datetime
import argparse
import asyncio

# Add paths for our new modules
sys.path.append(str(Path(__file__).parent.parent / "core"))
sys.path.append(str(Path(__file__).parent.parent.parent / "03_data_collection"))
sys.path.append(str(Path(__file__).parent.parent.parent / "03_data_collection" / "core"))

from config.settings import config
from speaker_database import speaker_db
from photo_manager import photo_manager
from face_analyzer import FaceAnalyzer
from name_analyzer import name_analyzer

# Initialize face analyzer
face_analyzer = FaceAnalyzer()
# Data should already be cleaned in 03_data_collection

class OptimizedDemographicAnalysis:
    """
    Main orchestrator for demographic analysis with intelligent caching
    """
    
    def __init__(self, fresh_start=False):
        self.config = config
        print(f"=== Optimized Demographic Analysis ===")
        print(f"Started at: {datetime.now()}")
        
        # Clear database if fresh start requested
        if fresh_start:
            speaker_db.clear_speakers_only()
        
        # Check API status
        api_status = config.get_api_status()
        print(f"API Status: {api_status}")
        
        self.skip_name_analysis = not api_status['openai']
        self.skip_photo_downloads = not (api_status['serpapi'] or api_status['google_search'])
        
        if self.skip_name_analysis:
            print("⚠️  OpenAI API not configured - name analysis will be skipped")
            print("   To enable: Add OPENAI_API_KEY to your .env file")
        
        if self.skip_photo_downloads:
            print("⚠️  No image search API configured - photo downloads will be skipped")
            print("   To enable: Add SERPAPI_KEY or GOOGLE_SEARCH_API_KEY to your .env file")
    
    def load_and_parse_data(self, file_path=None):
        """
        Load data and extract speaker appearances
        ALWAYS uses standardized data to prevent double counting
        """
        if file_path is None:
            # Use the FINAL clean, standardized dataset
            final_path = self.config.PROCESSED_DATA_DIR / "master-data-final.csv"
            
            if not final_path.exists():
                # Final data must exist - cannot proceed without it
                raise FileNotFoundError(
                    f"Final dataset not found: {final_path}\n"
                    f"Please run the data pipeline first:\n"
                    f"  cd /mnt/c/Users/jcerv/Jose/search-costs/03_data_collection/scripts\n"
                    f"  ./run_final_pipeline.sh"
                )
            
            file_path = final_path
            print("📊 Using final clean, standardized dataset")
        else:
            # Convert string path to Path object
            file_path = Path(file_path)
            # Verify it's the final dataset
            if 'final' not in str(file_path):
                print("⚠️  WARNING: Not using the final dataset may lead to inaccurate counts!")
                response = input("Continue anyway? (y/n): ")
                if response.lower() != 'y':
                    raise ValueError("Analysis cancelled - please use master-data-final.csv")
        
        print(f"\nLoading data from: {file_path}")
        
        if not file_path.exists():
            raise FileNotFoundError(f"Data file not found: {file_path}\n" + 
                                  "Please run: cd ../03_data_collection/scripts && ./prepare-complete-dataset.sh")
        
        # Load data - should already be cleaned and standardized
        df = pd.read_csv(file_path, encoding='utf-8-sig', low_memory=False)
        print(f"Loaded {len(df)} seminars from standardized dataset")
        
        # Extract speaker appearances
        appearances = self._extract_speaker_appearances(df)
        print(f"Note: Data should already be cleaned in 03_data_collection pipeline")
        
        # Process through speaker database
        print(f"\nProcessing speakers through database...")
        appearances_with_speaker_ids = speaker_db.process_speaker_appearances(appearances)
        
        # Store appearances for later use in appearance analysis
        self._appearances_with_ids = appearances_with_speaker_ids
        
        # Get unique speakers
        unique_speakers = speaker_db.speakers_db.copy()
        
        print(f"\n📊 Analysis Summary:")
        print(f"  Total speaker appearances: {len(appearances)}")
        print(f"  Unique speakers identified: {len(unique_speakers)}")
        print(f"  Average appearances per speaker: {len(appearances)/len(unique_speakers) if len(unique_speakers) > 0 else 0:.2f}")
        
        print(f"\nDatabase status:")
        stats = speaker_db.get_stats()
        print(f"  Speakers with photos: {stats['speakers_with_photos']}")
        print(f"  Speakers face analyzed: {stats['speakers_face_analyzed']}")
        print(f"  Speakers name analyzed: {stats['speakers_name_analyzed']}")
        
        # Always attempt to link existing cached data to speakers
        print("\n🔗 Checking for existing cached data to link...")
        linked_stats = self._link_existing_photos_to_speakers()
        if linked_stats['total_linked'] > 0:
            # Update stats
            stats = speaker_db.get_stats()
            print(f"  After linking - Speakers with photos: {stats['speakers_with_photos']}")
            print(f"  After linking - Speakers face analyzed: {stats['speakers_face_analyzed']}")
            print(f"  After linking - Speakers name analyzed: {stats['speakers_name_analyzed']}")
        
        return appearances_with_speaker_ids, unique_speakers
    
    def _link_existing_photos_to_speakers(self):
        """Link existing photos in directory to speakers in database"""
        # Get existing photo metadata
        photo_metadata = speaker_db.photo_metadata
        if len(photo_metadata) > 0 and 'download_success' in photo_metadata.columns:
            successful_photos = photo_metadata[photo_metadata['download_success'] == True]
        else:
            successful_photos = pd.DataFrame()
        
        linked_count = 0
        if len(successful_photos) > 0 and 'speaker_id' in successful_photos.columns:
            for speaker_id in successful_photos['speaker_id'].unique():
                # Check if speaker exists and needs linking
                speaker_mask = speaker_db.speakers_db['speaker_id'] == speaker_id
                if speaker_mask.any() and not speaker_db.speakers_db.loc[speaker_mask, 'photo_downloaded'].iloc[0]:
                    # Check if photo file actually exists
                    photo_record = successful_photos[successful_photos['speaker_id'] == speaker_id].iloc[0]
                    photo_path = config.SPEAKER_PHOTOS_DIR / photo_record['photo_filename']
                    if photo_path.exists():
                        speaker_db.speakers_db.loc[speaker_mask, 'photo_downloaded'] = True
                        linked_count += 1
        
        # Also link face and name analyses
        face_count = 0
        if len(speaker_db.face_cache) > 0 and 'face_analysis_success' in speaker_db.face_cache.columns:
            successful_face_analyses = speaker_db.face_cache[speaker_db.face_cache['face_analysis_success'] == True]
            for speaker_id in successful_face_analyses['speaker_id'].unique():
                speaker_mask = speaker_db.speakers_db['speaker_id'] == speaker_id
                if speaker_mask.any() and not speaker_db.speakers_db.loc[speaker_mask, 'face_analyzed'].iloc[0]:
                    speaker_db.speakers_db.loc[speaker_mask, 'face_analyzed'] = True
                    face_count += 1
        
        name_count = 0
        if len(speaker_db.name_cache) > 0 and 'name_analysis_success' in speaker_db.name_cache.columns:
            successful_name_analyses = speaker_db.name_cache[speaker_db.name_cache['name_analysis_success'] == True]
            for speaker_id in successful_name_analyses['speaker_id'].unique():
                speaker_mask = speaker_db.speakers_db['speaker_id'] == speaker_id  
                if speaker_mask.any() and not speaker_db.speakers_db.loc[speaker_mask, 'name_analyzed'].iloc[0]:
                    speaker_db.speakers_db.loc[speaker_mask, 'name_analyzed'] = True
                    name_count += 1
        
        # Save updates - CRITICAL: Must save before subprocess runs
        speaker_db.save_all()
        print(f"  Linked {linked_count} photos, {face_count} face analyses, {name_count} name analyses")
        print("  ✅ Force saved all databases to disk for subprocess access")
        
        return {
            'photos_linked': linked_count,
            'face_analyses_linked': face_count,
            'name_analyses_linked': name_count,
            'total_linked': linked_count + face_count + name_count
        }
    
    def _extract_speaker_appearances(self, df):
        """Extract all speaker appearances from the seminar data"""
        print("Extracting speaker appearances...")
        
        # Required seminar columns
        seminar_cols = ['seminar_id', 'university', 'discipline', 'seminar_name',
                       'condition', 'contact_type', 'Link', 'bin_category']
        
        # Check for missing columns
        missing_cols = [col for col in seminar_cols if col not in df.columns]
        if missing_cols:
            print(f"Warning: Missing columns {missing_cols}, using available columns")
            seminar_cols = [col for col in seminar_cols if col in df.columns]
        
        speakers_list = []
        max_speakers = 203  # Updated to include Spring speakers (129-203)
        
        for idx, row in df.iterrows():
            # Get seminar info
            seminar_info = {col: row.get(col) for col in seminar_cols}
            
            if pd.isna(seminar_info.get('seminar_id')):
                continue
            
            # Extract speakers for this seminar
            for i in range(1, max_speakers + 1):
                fn_col = f'First Name_{i}'
                ln_col = f'Last Name_{i}'
                rank_col = f'rank_{i}'
                uni_col = f'university_{i}'
                date_col = f'date_{i}'
                
                # Check if speaker columns exist
                if fn_col not in df.columns:
                    break
                
                first_name = row.get(fn_col, '')
                last_name = row.get(ln_col, '')
                
                # Check if speaker has any name information
                has_first = pd.notna(first_name) and str(first_name).strip() != ''
                has_last = pd.notna(last_name) and str(last_name).strip() != ''
                
                if not (has_first or has_last):
                    continue
                
                # Get standardized columns
                rank_std_col = f'rank_{i}_standardized'
                uni_std_col = f'university_{i}_standardized'
                
                # Check for PhD year column
                phd_year_col = f'phd_graduation_year_{i}'
                phd_year = row.get(phd_year_col) if phd_year_col in df.columns else None
                
                # Create speaker appearance record
                speaker_details = {
                    'speaker_num_in_seminar': i,
                    'name': f"{first_name or ''} {last_name or ''}".strip(),
                    'first_name': str(first_name).strip() if pd.notna(first_name) else '',
                    'last_name': str(last_name).strip() if pd.notna(last_name) else '',
                    'rank': row.get(rank_std_col, row.get(rank_col, '')) if rank_std_col in df.columns else row.get(rank_col, ''),
                    'affiliation_raw': row.get(uni_col, '') if uni_col in df.columns else '',
                    'affiliation_standardized': row.get(uni_std_col, '') if uni_std_col in df.columns else '',
                    'date': row.get(date_col, '') if date_col in df.columns else '',
                    'phd_graduation_year': phd_year if pd.notna(phd_year) else None
                }
                
                # Combine seminar and speaker info
                appearance = {**seminar_info, **speaker_details}
                
                # Use standardized affiliation if available, otherwise raw, otherwise seminar university
                if speaker_details['affiliation_standardized']:
                    appearance['affiliation'] = speaker_details['affiliation_standardized']
                elif speaker_details['affiliation_raw']:
                    appearance['affiliation'] = speaker_details['affiliation_raw']
                else:
                    appearance['affiliation'] = seminar_info.get('university_standardized', seminar_info.get('university', ''))
                
                speakers_list.append(appearance)
        
        appearances_df = pd.DataFrame(speakers_list)
        print(f"Extracted {len(appearances_df)} speaker appearances")
        
        return appearances_df
    
    def run_photo_downloads_only(self, force_redownload=False):
        """
        Run ONLY photo downloads (no face analysis)
        """
        print(f"\n=== Photo Download Phase ===")
        
        # Get speakers needing photos
        if force_redownload:
            speakers_needing_photos = speaker_db.speakers_db.copy()
            print(f"Force redownload: processing all {len(speakers_needing_photos)} speakers")
        else:
            speakers_needing_photos = speaker_db.get_speakers_needing_photos()
            print(f"Found {len(speakers_needing_photos)} speakers needing photo downloads")
        
        # Download photos
        if len(speakers_needing_photos) > 0:
            print("Starting photo downloads...")
            photo_results = photo_manager.download_photos_parallel(speakers_needing_photos)
            
            successful_downloads = sum(1 for r in photo_results if r['success'])
            print(f"Photo downloads complete: {successful_downloads} successful")
        else:
            print("All speakers already have photos downloaded")
    
    def run_photo_analysis(self, force_redownload=False):
        """
        Run photo download and face analysis with caching
        """
        print(f"\n=== Photo Analysis Phase ===")
        
        if self.skip_photo_downloads:
            print("⏭️  Skipping photo downloads (no API configured)")
            print("   Using existing photos only...")
        else:
            # Get speakers needing photos
            if force_redownload:
                speakers_needing_photos = speaker_db.speakers_db.copy()
                print(f"Force redownload: processing all {len(speakers_needing_photos)} speakers")
            else:
                speakers_needing_photos = speaker_db.get_speakers_needing_photos()
                print(f"Found {len(speakers_needing_photos)} speakers needing photo downloads")
            
            # Download photos
            if len(speakers_needing_photos) > 0:
                print("Starting photo downloads...")
                photo_results = photo_manager.download_photos_parallel(speakers_needing_photos)
                
                successful_downloads = sum(1 for r in photo_results if r['success'])
                print(f"Photo downloads complete: {successful_downloads} successful")
            else:
                print("All speakers already have photos downloaded")
        
        # Get speakers needing face analysis
        speakers_needing_face_analysis = speaker_db.get_speakers_needing_face_analysis()
        print(f"Found {len(speakers_needing_face_analysis)} speakers needing face analysis")
        
        # Run face analysis
        if len(speakers_needing_face_analysis) > 0:
            print("Starting face analysis...")
            # Get photo paths for speakers
            photo_paths = []
            speaker_ids = []
            
            # Handle both list and DataFrame returns
            if hasattr(speakers_needing_face_analysis, 'iterrows'):
                # It's a DataFrame
                for idx, speaker in speakers_needing_face_analysis.iterrows():
                    speaker_id = speaker.get('speaker_id', idx)
                    # Get photo path from photo manager
                    photo_path = photo_manager.get_photo_path(speaker_id)
                    if photo_path:
                        # Convert Path to string
                        photo_path_str = str(photo_path)
                        if os.path.exists(photo_path_str):
                            photo_paths.append(photo_path_str)
                            speaker_ids.append(speaker_id)
            else:
                # It's a list of speaker IDs
                for speaker_id in speakers_needing_face_analysis:
                    # Get photo path from photo manager
                    photo_path = photo_manager.get_photo_path(speaker_id)
                    if photo_path:
                        # Convert Path to string
                        photo_path_str = str(photo_path)
                        if os.path.exists(photo_path_str):
                            photo_paths.append(photo_path_str)
                            speaker_ids.append(speaker_id)
            
            if len(photo_paths) > 0:
                print(f"Found {len(photo_paths)} valid photos to analyze")
                
                # For stability, recommend using the isolated batch script
                print("\n⚠️  Note: For face analysis, it's recommended to use:")
                print("   ./run_face_analysis_safe.sh")
                print("   This uses subprocess isolation to prevent memory errors.")
                print("\nAttempting direct analysis (may encounter memory issues)...")
                
                # Analyze faces one by one with immediate saving
                try:
                    successful_analyses = 0
                    for i, (photo_path, speaker_id) in enumerate(zip(photo_paths, speaker_ids)):
                        result = face_analyzer.analyze_face(photo_path)
                        
                        if result['success']:
                            # Transform nested result to flat format expected by database
                            face_data = {
                                'speaker_id': speaker_id,
                                'face_gender': result['gender']['value'],
                                'face_gender_confidence': result['gender']['confidence'],
                                'face_race': result['race']['value'],
                                'face_race_confidence': result['race']['confidence'],
                                'face_analysis_success': True,
                                'analysis_timestamp': pd.Timestamp.now().isoformat(),
                                'deepface_version': result.get('deepface_version', 'unknown')
                            }
                            speaker_db.add_face_analysis(face_data)
                            successful_analyses += 1
                        else:
                            # Record failed analysis
                            face_data = {
                                'speaker_id': speaker_id,
                                'face_gender': 'unknown',
                                'face_gender_confidence': 0.0,
                                'face_race': 'unknown',
                                'face_race_confidence': 0.0,
                                'face_analysis_success': False,
                                'analysis_timestamp': pd.Timestamp.now().isoformat(),
                                'deepface_version': result.get('deepface_version', 'unknown')
                            }
                            speaker_db.add_face_analysis(face_data)
                        
                        # Save progress every 10 faces
                        if (i + 1) % 10 == 0:
                            speaker_db.save_all()
                            print(f"Analyzed {i + 1}/{len(photo_paths)} faces")
                    
                    # Final save
                    speaker_db.save_all()
                    print(f"Face analysis complete: {successful_analyses} successful")
                except Exception as e:
                    print(f"\n❌ Face analysis failed: {e}")
                    print("\nPlease use the subprocess isolation method instead:")
                    print("cd /mnt/c/Users/jcerv/Jose/search-costs/pipeline")
                    print("./run_face_analysis_safe.sh")
                    raise
            else:
                print("No valid photos found for face analysis")
        else:
            print("All speakers with photos already have face analysis")
    
    def run_name_analysis(self, force_reprocess=False):
        """
        Run FAST name analysis with async/await
        """
        print(f"\n=== Name Analysis Phase (Fast Async Mode) ===")
        
        if self.skip_name_analysis:
            print("⏭️  Skipping name analysis (OpenAI API not configured)")
            print("   Demographics will be based on face analysis only")
            return
        
        # Get speakers needing name analysis
        if force_reprocess:
            speakers_needing_name_analysis = speaker_db.speakers_db.copy()
            print(f"Force reprocess: analyzing all {len(speakers_needing_name_analysis)} speakers")
        else:
            speakers_needing_name_analysis = speaker_db.get_speakers_needing_name_analysis()
            print(f"Found {len(speakers_needing_name_analysis)} speakers needing name analysis")
        
        # Run FAST async name analysis
        if len(speakers_needing_name_analysis) > 0:
            print("Starting FAST async name analysis...")
            
            # Import and run the fast analyzer
            from fast_name_analysis import FastNameAnalyzer
            
            async def run_fast_analysis():
                analyzer = FastNameAnalyzer()
                results = await analyzer.analyze_all_async(
                    speakers_needing_name_analysis,
                    max_concurrent=150,  # Increased from 100 for faster processing
                    batch_size=300      # Increased from 200 for faster processing
                )
                return results
            
            # Run the async function
            name_results = asyncio.run(run_fast_analysis())
            
            successful_analyses = sum(1 for r in name_results if r['success'])
            print(f"\n✅ Name analysis complete: {successful_analyses} successful")
        else:
            print("All speakers already have name analysis")
    
    def combine_and_export_results(self):
        """
        Combine all analysis results and export in original format
        """
        print(f"\n=== Combining Results ===")
        
        # Get all speakers with their analyses
        speakers = speaker_db.speakers_db.copy()
        face_cache = speaker_db.face_cache.copy()
        name_cache = speaker_db.name_cache.copy()
        
        print(f"Combining results for {len(speakers)} speakers")
        
        # Fix column names in face_cache if needed
        if 'gender' in face_cache.columns and 'face_gender' not in face_cache.columns:
            print("Renaming face_cache columns to match expected format...")
            face_cache = face_cache.rename(columns={
                'gender': 'face_gender',
                'gender_confidence': 'face_gender_confidence',
                'race': 'face_race',
                'race_confidence': 'face_race_confidence',
                'success': 'face_analysis_success'
            })
        
        # Merge face analysis
        speakers = speakers.merge(
            face_cache[['speaker_id', 'face_gender', 'face_gender_confidence', 
                       'face_race', 'face_race_confidence', 'face_analysis_success']],
            on='speaker_id', how='left'
        )
        
        # Merge name analysis
        speakers = speakers.merge(
            name_cache[['speaker_id', 'name_gender', 'name_gender_confidence',
                       'name_race', 'name_race_confidence', 'name_analysis_success']],
            on='speaker_id', how='left'
        )
        
        # Debug: Check what we have
        print(f"\nDebug info:")
        print(f"  Face cache columns: {face_cache.columns.tolist()}")
        print(f"  Name cache columns: {name_cache.columns.tolist()}")
        print(f"  Face analyses: {face_cache['face_analysis_success'].sum() if 'face_analysis_success' in face_cache.columns else 0} successful")
        print(f"  Name analyses: {name_cache['name_analysis_success'].sum() if 'name_analysis_success' in name_cache.columns else 0} successful")
        
        # Fill missing values
        for col in ['face_gender', 'name_gender']:
            speakers[col] = speakers[col].fillna('unknown')
        
        for col in ['face_gender_confidence', 'face_gender_confidence',
                   'name_race_confidence', 'name_race_confidence']:
            speakers[col] = speakers[col].fillna(0.0)
        
        for col in ['face_analysis_success', 'name_analysis_success']:
            speakers[col] = speakers[col].fillna(False)
        
        # Standardize gender values to lowercase
        def standardize_gender(gender):
            if pd.isna(gender) or str(gender).lower() == 'unknown':
                return 'unknown'
            gender_map = {
                'male': 'man',
                'female': 'woman',
                'man': 'man',
                'woman': 'woman',
                'non-binary': 'non-binary',
                'nonbinary': 'non-binary'
            }
            return gender_map.get(str(gender).lower(), 'unknown')
        
        # Standardize race values to lowercase pre-registered categories
        def standardize_race(race):
            if pd.isna(race) or str(race).lower() == 'unknown':
                return 'unknown'
            race_map = {
                'white': 'white',
                'black': 'black',
                'asian': 'asian',
                'south asian': 'asian',
                'indian': 'asian',
                'hispanic': 'latino',
                'hispanic/latino': 'latino',
                'latino': 'latino',
                'latino hispanic': 'latino',
                'native american': 'native american',
                'middle eastern': 'white',
                'mixed': 'mixed/other',
                'other': 'mixed/other',
                'mixed/other': 'mixed/other'
            }
            return race_map.get(str(race).lower(), 'unknown')
        
        # Apply standardization to all gender and race columns
        speakers['face_gender'] = speakers['face_gender'].apply(standardize_gender)
        speakers['name_gender'] = speakers['name_gender'].apply(standardize_gender)
        speakers['face_race'] = speakers['face_race'].apply(standardize_race)
        speakers['name_race'] = speakers['name_race'].apply(standardize_race)
        
        # Combine gender (prioritize face if confidence > 90% AND valid category, otherwise use name)
        def combine_gender(row):
            valid_genders = ['man', 'woman']  # Only binary genders allowed
            
            # Get the standardized values from the row
            face_gender = standardize_gender(row.get('face_gender', 'unknown'))
            name_gender = standardize_gender(row.get('name_gender', 'unknown'))
            
            # First try face analysis if high confidence AND valid category
            if (row.get('face_analysis_success', False) and 
                row.get('face_gender_confidence', 0) > 90 and 
                face_gender in valid_genders):
                return face_gender
            # Otherwise use name analysis if available
            elif name_gender in valid_genders:
                return name_gender
            else:
                return 'unknown'
        
        speakers['combined_gender'] = speakers.apply(combine_gender, axis=1)
        
        # Combine race (same logic - only valid categories)
        def combine_race(row):
            valid_races = ['white', 'black', 'latino', 'asian', 'native american']  # Only these 5 allowed
            
            # Get the standardized values from the row
            face_race = standardize_race(row.get('face_race', 'unknown'))
            name_race = standardize_race(row.get('name_race', 'unknown'))
            
            # First try face analysis if high confidence AND valid category
            if (row.get('face_analysis_success', False) and 
                row.get('face_race_confidence', 0) > 90 and 
                face_race in valid_races):
                return face_race
            # Otherwise use name analysis if available
            elif name_race in valid_races:
                return name_race
            else:
                return 'unknown'
        
        speakers['combined_race'] = speakers.apply(combine_race, axis=1)
        
        # Log warning if any speakers still have unknown or invalid demographics
        invalid_genders = ~speakers['combined_gender'].isin(['man', 'woman'])
        invalid_races = ~speakers['combined_race'].isin(['white', 'black', 'latino', 'asian', 'native american'])
        
        if invalid_genders.any() or invalid_races.any():
            print(f"\n⚠️  Warning: Found speakers with invalid demographics:")
            print(f"   Invalid gender: {invalid_genders.sum()} speakers")
            print(f"   Invalid race: {invalid_races.sum()} speakers")
            print(f"   These speakers may not have successful name analysis")
            
            # Log examples of invalid values
            if invalid_genders.any():
                invalid_gender_values = speakers[invalid_genders]['combined_gender'].value_counts()
                print(f"   Invalid gender values: {invalid_gender_values.to_dict()}")
            if invalid_races.any():
                invalid_race_values = speakers[invalid_races]['combined_race'].value_counts()
                print(f"   Invalid race values: {invalid_race_values.to_dict()}")
        
        # Calculate URM status using standardized race values
        urm_categories = config.URM_CATEGORIES  # ['black', 'latino', 'native american']
        speakers['is_urm'] = speakers['combined_race'].isin(urm_categories)
        
        # Ensure we have all necessary columns for statistical analysis
        # The speakers dataframe should already have discipline_norm from speaker_db
        if 'discipline_norm' not in speakers.columns:
            print("⚠️  Warning: discipline_norm not found in speakers dataframe")
            # Try to get it from speaker_db if missing
            if 'discipline_norm' in speaker_db.speakers_db.columns:
                speakers = speakers.merge(
                    speaker_db.speakers_db[['speaker_id', 'discipline_norm', 'first_name', 'last_name']],
                    on='speaker_id',
                    how='left',
                    suffixes=('', '_db')
                )
        
        # Export combined people analysis (equivalent to people_combined_analysis.csv)
        people_output_path = config.DEMOGRAPHIC_OUTPUTS_DIR / "people_combined_analysis.csv"
        speakers.to_csv(people_output_path, index=False, encoding='utf-8-sig')
        print(f"People analysis saved: {people_output_path}")
        
        # Create appearance-level data for seminar analysis
        self._create_appearance_analysis(speakers)
        
        return speakers
    
    def _create_appearance_analysis(self, speakers_df):
        """
        Create appearance-level analysis by merging demographics with all appearances
        """
        print("Creating appearance-level analysis...")
        
        # Get the appearances with speaker IDs that we stored earlier
        if hasattr(self, '_appearances_with_ids'):
            appearances = self._appearances_with_ids
        else:
            # Fallback: reload and reprocess
            print("  Reloading appearance data...")
            df = pd.read_csv(config.PROCESSED_DATA_DIR / "master-data-final.csv", 
                           encoding='utf-8-sig', low_memory=False)
            appearances = self._extract_speaker_appearances(df)
            appearances = speaker_db.process_speaker_appearances(appearances)
        
        print(f"  Merging {len(appearances)} appearances with {len(speakers_df)} speaker demographics...")
        
        # Merge appearances with speaker demographics
        # Note: phd_graduation_year comes from appearances, not speakers_df
        appearances_with_demographics = appearances.merge(
            speakers_df[['speaker_id', 'combined_gender', 'combined_race', 'is_urm',
                        'face_gender', 'face_gender_confidence', 'face_race', 'face_race_confidence',
                        'name_gender', 'name_gender_confidence', 'name_race', 'name_race_confidence',
                        'face_analysis_success', 'name_analysis_success']],
            on='speaker_id',
            how='left'
        )
        
        # Add a flag for whether demographics were found
        appearances_with_demographics['has_demographics'] = appearances_with_demographics['speaker_id'].notna()
        
        # Save the full appearance-level analysis
        appearance_output_path = config.DEMOGRAPHIC_OUTPUTS_DIR / "speaker_appearances_analysis.csv"
        appearances_with_demographics.to_csv(appearance_output_path, index=False, encoding='utf-8-sig')
        
        print(f"Appearance analysis saved: {appearance_output_path}")
        print(f"  Total appearances: {len(appearances_with_demographics)}")
        print(f"  Appearances with demographics: {appearances_with_demographics['has_demographics'].sum()}")
        print(f"  Match rate: {appearances_with_demographics['has_demographics'].mean():.1%}")
    
    def run_full_analysis(self, data_file=None, force_reprocess=False):
        """
        Run the complete demographic analysis pipeline
        """
        print(f"=== Starting Full Demographic Analysis Pipeline ===")
        
        try:
            # Phase 1: Load and process data
            appearances, speakers = self.load_and_parse_data(data_file)
            
            # Phase 2: Photo analysis
            self.run_photo_analysis(force_redownload=force_reprocess)
            
            # Phase 3: Name analysis
            self.run_name_analysis(force_reprocess=force_reprocess)
            
            # Phase 4: Combine and export
            final_results = self.combine_and_export_results()
            
            # Summary
            print(f"\n=== Analysis Complete ===")
            total_speakers = len(final_results)
            analyzed_speakers = len(final_results[
                (final_results['face_analysis_success'] == True) | 
                (final_results['name_analysis_success'] == True)
            ])
            
            print(f"Total unique speakers: {total_speakers}")
            print(f"Successfully analyzed: {analyzed_speakers}")
            print(f"Analysis rate: {analyzed_speakers/total_speakers*100:.1f}%")
            
            # Gender distribution
            gender_dist = final_results['combined_gender'].value_counts()
            print(f"\nGender distribution:")
            for gender, count in gender_dist.items():
                print(f"  {gender}: {count}")
            
            # Race distribution  
            race_dist = final_results['combined_race'].value_counts()
            print(f"\nRace distribution:")
            for race, count in race_dist.items():
                print(f"  {race}: {count}")
            
            # URM statistics
            urm_count = final_results['is_urm'].sum()
            urm_rate = urm_count / total_speakers
            print(f"\nURM speakers: {urm_count}/{total_speakers} ({urm_rate:.1%})")
            
            return True
            
        except Exception as e:
            print(f"❌ Analysis failed: {e}")
            import traceback
            traceback.print_exc()
            return False
    
    def get_analysis_status(self):
        """Get current analysis status"""
        print(f"=== Analysis Status ===")
        
        stats = speaker_db.get_stats()
        
        print(f"Speaker Database:")
        print(f"  Total speakers: {stats['total_speakers']}")
        print(f"  With photos: {stats['speakers_with_photos']}")
        print(f"  Face analyzed: {stats['speakers_face_analyzed']}")
        print(f"  Name analyzed: {stats['speakers_name_analyzed']}")
        print(f"  Total appearances: {stats['total_appearances']}")
        
        # Check output files
        output_files = [
            config.DEMOGRAPHIC_OUTPUTS_DIR / "people_combined_analysis.csv",
            config.DEMOGRAPHIC_OUTPUTS_DIR / "speaker_appearances_analysis.csv"
        ]
        
        print(f"\nOutput Files:")
        for file_path in output_files:
            exists = "✅" if file_path.exists() else "❌"
            print(f"  {exists} {file_path.name}")
        
        return stats

def main():
    """Command line interface"""
    parser = argparse.ArgumentParser(description='Optimized Demographic Analysis for Search Costs RCT')
    parser.add_argument('--data-file', help='Input data file (default: complete dataset)')
    parser.add_argument('--mode', choices=['full', 'photos', 'photos-only', 'names', 'combine', 'status'], 
                       default='full', help='Analysis mode')
    parser.add_argument('--force-reprocess', action='store_true', 
                       help='Force reprocessing even if cached results exist')
    parser.add_argument('--fresh-start', action='store_true',
                       help='Clear all cached data and start fresh')
    
    args = parser.parse_args()
    
    # Only start fresh if explicitly requested
    fresh_start = args.fresh_start
    
    analyzer = OptimizedDemographicAnalysis(fresh_start=fresh_start)
    
    if args.mode == 'status':
        analyzer.get_analysis_status()
    elif args.mode == 'photos':
        appearances, speakers = analyzer.load_and_parse_data(args.data_file)
        analyzer.run_photo_analysis(force_redownload=args.force_reprocess)
        # Always combine results after photo analysis
        analyzer.combine_and_export_results()
    elif args.mode == 'photos-only':
        appearances, speakers = analyzer.load_and_parse_data(args.data_file)
        analyzer.run_photo_downloads_only(force_redownload=args.force_reprocess)
    elif args.mode == 'names':
        appearances, speakers = analyzer.load_and_parse_data(args.data_file)
        analyzer.run_name_analysis(force_reprocess=args.force_reprocess)
        # Always combine results after name analysis
        analyzer.combine_and_export_results()
    elif args.mode == 'combine':
        # Need to load data first to have appearances available
        appearances, speakers = analyzer.load_and_parse_data(args.data_file)
        analyzer.combine_and_export_results()
    elif args.mode == 'full':
        success = analyzer.run_full_analysis(args.data_file, args.force_reprocess)
        if not success:
            exit(1)
    
    print("\n🎉 Optimized demographic analysis complete!")

if __name__ == "__main__":
    # Required for multiprocessing on Windows/macOS
    import multiprocessing
    multiprocessing.freeze_support()
    main()