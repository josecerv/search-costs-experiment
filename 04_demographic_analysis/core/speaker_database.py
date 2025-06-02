"""
Speaker Database Management for Search Costs RCT
Handles speaker identity matching, deduplication, and caching to avoid expensive API calls
"""

import pandas as pd
import numpy as np
import hashlib
import unicodedata
import re
from pathlib import Path
import sys
import os

# Add config and core to path
sys.path.append(str(Path(__file__).parent.parent.parent / "03_data_collection"))
sys.path.append(str(Path(__file__).parent.parent.parent))
from config.settings import config
from core.normalization import normalize_text, generate_speaker_id as shared_generate_speaker_id

class SpeakerDatabase:
    """
    Manages a persistent database of speakers to avoid duplicate processing
    Key insight: Match speakers by normalized name + discipline + university
    """
    
    def __init__(self, fresh_start=False):
        self.database_path = config.SPEAKER_DATABASE
        self.photo_metadata_path = config.PHOTO_METADATA
        self.face_cache_path = config.FACE_ANALYSIS_CACHE
        self.name_cache_path = config.NAME_ANALYSIS_CACHE
        
        # Load existing databases or start fresh
        if fresh_start:
            print("Starting with fresh speaker database")
            self.speakers_db = self._create_empty_speakers_database()
            self.photo_metadata = self._create_empty_photo_metadata()
            self.face_cache = self._create_empty_face_cache()
            self.name_cache = self._create_empty_name_cache()
        else:
            self.speakers_db = self._load_speakers_database()
            self.photo_metadata = self._load_photo_metadata()
            self.face_cache = self._load_face_cache()
            self.name_cache = self._load_name_cache()
    
    def clear_all_data(self):
        """Clear all data and start fresh"""
        print("🔄 Clearing all speaker database data...")
        self.speakers_db = self._create_empty_speakers_database()
        self.photo_metadata = self._create_empty_photo_metadata()
        self.face_cache = self._create_empty_face_cache()
        self.name_cache = self._create_empty_name_cache()
        # Save empty databases to disk
        self.save_all()
        print("✅ Speaker database cleared")
    
    def clear_speakers_only(self):
        """Clear only the speaker database while preserving expensive caches"""
        print("🔄 Clearing speaker database (preserving caches)...")
        
        # Count existing caches before clearing
        photo_count = len(self.photo_metadata) if hasattr(self, 'photo_metadata') else 0
        face_count = len(self.face_cache) if hasattr(self, 'face_cache') else 0
        name_count = len(self.name_cache) if hasattr(self, 'name_cache') else 0
        
        print(f"   Preserving {photo_count} photo records")
        print(f"   Preserving {face_count} face analysis results") 
        print(f"   Preserving {name_count} name analysis results")
        
        # Only clear the speakers database
        self.speakers_db = self._create_empty_speakers_database()
        
        # Save only the speakers database (not the caches)
        self.speakers_db.to_csv(self.database_path, index=False, encoding='utf-8-sig')
        
        print("✅ Speaker database cleared (caches preserved)")
        print("   New speakers from master dataset will link to existing caches")
    
    def _normalize_string(self, s):
        """Normalizes strings for robust matching - uses shared normalization"""
        result = normalize_text(s)
        return result if result else None
    
    def _generate_speaker_id(self, name_norm, discipline_norm, university_norm):
        """Generate unique speaker ID using shared function
        
        Uses name + discipline + university to handle common names like "Yang Yang"
        The seminar's discipline is used as a proxy for speaker's field
        """
        # Use shared function for consistent ID generation
        return shared_generate_speaker_id(name_norm, discipline_norm, university_norm)
    
    def _load_speakers_database(self):
        """Load existing speakers database"""
        if self.database_path.exists():
            try:
                df = pd.read_csv(self.database_path, encoding='utf-8-sig')
                print(f"Loaded {len(df)} speakers from database")
                return df
            except Exception as e:
                print(f"Error loading speakers database: {e}")
                return self._create_empty_speakers_database()
        else:
            print("Creating new speakers database")
            return self._create_empty_speakers_database()
    
    def _create_empty_speakers_database(self):
        """Create empty speakers database with proper schema"""
        return pd.DataFrame(columns=[
            'speaker_id',           # Unique identifier
            'name',                 # Original name
            'name_norm',           # Normalized name
            'discipline',          # Original discipline
            'discipline_norm',     # Normalized discipline  
            'university',          # Original university/affiliation
            'university_norm',     # Normalized university
            'first_seen',          # First time this speaker was encountered
            'last_seen',           # Last time this speaker was seen
            'appearance_count',    # Number of times speaker appeared
            'photo_downloaded',    # Boolean: has photo been downloaded
            'face_analyzed',       # Boolean: has face analysis been completed
            'name_analyzed',       # Boolean: has name analysis been completed
            'notes'                # Any additional notes
        ])
    
    def _load_photo_metadata(self):
        """Load photo download metadata"""
        if self.photo_metadata_path.exists():
            try:
                df = pd.read_csv(self.photo_metadata_path, encoding='utf-8-sig')
                return df
            except Exception as e:
                print(f"Error loading photo metadata: {e}")
                return self._create_empty_photo_metadata()
        else:
            return self._create_empty_photo_metadata()
    
    def _create_empty_photo_metadata(self):
        """Create empty photo metadata with proper schema"""
        return pd.DataFrame(columns=[
            'speaker_id',
            'photo_filename',
            'photo_url',
            'download_timestamp',
            'download_success',
            'file_size',
            'image_width',
            'image_height',
            'search_query_used'
        ])
    
    def _load_face_cache(self):
        """Load face analysis cache"""
        if self.face_cache_path.exists():
            try:
                df = pd.read_csv(self.face_cache_path, encoding='utf-8-sig')
                return df
            except Exception as e:
                print(f"Error loading face cache: {e}")
                return self._create_empty_face_cache()
        else:
            return self._create_empty_face_cache()
    
    def _create_empty_face_cache(self):
        """Create empty face analysis cache"""
        return pd.DataFrame(columns=[
            'speaker_id',
            'face_gender',
            'face_gender_confidence',
            'face_race',
            'face_race_confidence',
            'face_analysis_success',
            'analysis_timestamp',
            'deepface_version'
        ])
    
    def _load_name_cache(self):
        """Load name analysis cache"""
        if self.name_cache_path.exists():
            try:
                df = pd.read_csv(self.name_cache_path, encoding='utf-8-sig')
                return df
            except Exception as e:
                print(f"Error loading name cache: {e}")
                return self._create_empty_name_cache()
        else:
            return self._create_empty_name_cache()
    
    def _create_empty_name_cache(self):
        """Create empty name analysis cache"""
        return pd.DataFrame(columns=[
            'speaker_id',
            'name_gender',
            'name_gender_confidence',
            'name_race',
            'name_race_confidence',
            'name_analysis_success',
            'analysis_timestamp',
            'gpt_model_used'
        ])
    
    def add_or_update_speaker(self, name, discipline, university, additional_info=None):
        """
        Add new speaker or update existing one
        Returns speaker_id and whether it's a new speaker
        """
        # Normalize identifiers
        name_norm = self._normalize_string(name)
        discipline_norm = self._normalize_string(discipline)
        university_norm = self._normalize_string(university)
        
        if not name_norm:
            # Skip speakers with empty or invalid names
            return None, False
        
        # Generate speaker ID
        speaker_id = self._generate_speaker_id(name_norm, discipline_norm, university_norm)
        
        # Check if speaker already exists
        existing = self.speakers_db[self.speakers_db['speaker_id'] == speaker_id]
        
        current_timestamp = pd.Timestamp.now().isoformat()
        
        if len(existing) > 0:
            # Update existing speaker
            idx = existing.index[0]
            self.speakers_db.loc[idx, 'last_seen'] = current_timestamp
            self.speakers_db.loc[idx, 'appearance_count'] += 1
            
            # Update with any new information
            if additional_info:
                for key, value in additional_info.items():
                    if key in self.speakers_db.columns and pd.isna(self.speakers_db.loc[idx, key]):
                        self.speakers_db.loc[idx, key] = value
            
            return speaker_id, False  # Not new
        else:
            # Add new speaker
            new_speaker = {
                'speaker_id': speaker_id,
                'name': name,
                'name_norm': name_norm,
                'discipline': discipline,
                'discipline_norm': discipline_norm,
                'university': additional_info.get('affiliation', university) if additional_info else university,  # Use raw affiliation
                'university_norm': university_norm,  # This is already normalized
                'first_seen': current_timestamp,
                'last_seen': current_timestamp,
                'appearance_count': 1,
                'photo_downloaded': False,
                'face_analyzed': False,
                'name_analyzed': False,
                'notes': ''
            }
            
            # Add any additional information
            if additional_info:
                new_speaker.update(additional_info)
            
            # Add to database
            self.speakers_db = pd.concat([
                self.speakers_db, 
                pd.DataFrame([new_speaker])
            ], ignore_index=True)
            
            return speaker_id, True  # New speaker
    
    def get_speakers_needing_photos(self):
        """Get speakers who need photo downloads"""
        return self.speakers_db[
            ~self.speakers_db['photo_downloaded'] |
            self.speakers_db['photo_downloaded'].isna()
        ].copy()
    
    def get_speakers_needing_face_analysis(self):
        """Get speakers who have photos but need face analysis"""
        return self.speakers_db[
            (self.speakers_db['photo_downloaded'] == True) &
            (~self.speakers_db['face_analyzed'] | 
             self.speakers_db['face_analyzed'].isna())
        ].copy()
    
    def get_speakers_needing_name_analysis(self):
        """Get speakers who need name analysis"""
        return self.speakers_db[
            ~self.speakers_db['name_analyzed'] |
            self.speakers_db['name_analyzed'].isna()
        ].copy()
    
    def mark_photo_downloaded(self, speaker_id, success=True):
        """Mark a speaker's photo as downloaded"""
        mask = self.speakers_db['speaker_id'] == speaker_id
        if mask.any():
            self.speakers_db.loc[mask, 'photo_downloaded'] = success
    
    def mark_face_analyzed(self, speaker_id, success=True):
        """Mark a speaker's face as analyzed"""
        mask = self.speakers_db['speaker_id'] == speaker_id
        if mask.any():
            self.speakers_db.loc[mask, 'face_analyzed'] = success
    
    def mark_name_analyzed(self, speaker_id, success=True):
        """Mark a speaker's name as analyzed"""
        mask = self.speakers_db['speaker_id'] == speaker_id
        if mask.any():
            self.speakers_db.loc[mask, 'name_analyzed'] = success
    
    def add_photo_metadata(self, photo_data):
        """Add photo download metadata"""
        self.photo_metadata = pd.concat([
            self.photo_metadata,
            pd.DataFrame([photo_data])
        ], ignore_index=True)
    
    def add_face_analysis(self, analysis_data):
        """Add face analysis results"""
        # Remove existing analysis for this speaker if any
        self.face_cache = self.face_cache[
            self.face_cache['speaker_id'] != analysis_data['speaker_id']
        ]
        
        # Add new analysis
        self.face_cache = pd.concat([
            self.face_cache,
            pd.DataFrame([analysis_data])
        ], ignore_index=True)
        
        # Mark as analyzed in main database
        self.mark_face_analyzed(analysis_data['speaker_id'], 
                               analysis_data.get('face_analysis_success', True))
    
    def add_name_analysis(self, analysis_data):
        """Add name analysis results"""
        # Remove existing analysis for this speaker if any
        self.name_cache = self.name_cache[
            self.name_cache['speaker_id'] != analysis_data['speaker_id']
        ]
        
        # Add new analysis
        self.name_cache = pd.concat([
            self.name_cache,
            pd.DataFrame([analysis_data])
        ], ignore_index=True)
        
        # Mark as analyzed in main database
        self.mark_name_analyzed(analysis_data['speaker_id'],
                               analysis_data.get('name_analysis_success', True))
    
    def get_face_analysis(self, speaker_id):
        """Get cached face analysis for a speaker"""
        result = self.face_cache[self.face_cache['speaker_id'] == speaker_id]
        return result.iloc[0].to_dict() if len(result) > 0 else None
    
    def get_name_analysis(self, speaker_id):
        """Get cached name analysis for a speaker"""
        result = self.name_cache[self.name_cache['speaker_id'] == speaker_id]
        return result.iloc[0].to_dict() if len(result) > 0 else None
    
    def save_all(self):
        """Save all databases to disk"""
        try:
            self.speakers_db.to_csv(self.database_path, index=False, encoding='utf-8-sig')
            self.photo_metadata.to_csv(self.photo_metadata_path, index=False, encoding='utf-8-sig')
            self.face_cache.to_csv(self.face_cache_path, index=False, encoding='utf-8-sig')
            self.name_cache.to_csv(self.name_cache_path, index=False, encoding='utf-8-sig')
            print("All databases saved successfully")
        except Exception as e:
            print(f"Error saving databases: {e}")
    
    def get_stats(self):
        """Get database statistics"""
        return {
            'total_speakers': len(self.speakers_db),
            'speakers_with_photos': self.speakers_db['photo_downloaded'].sum() if 'photo_downloaded' in self.speakers_db.columns else 0,
            'speakers_face_analyzed': self.speakers_db['face_analyzed'].sum() if 'face_analyzed' in self.speakers_db.columns else 0,
            'speakers_name_analyzed': self.speakers_db['name_analyzed'].sum() if 'name_analyzed' in self.speakers_db.columns else 0,
            'total_appearances': self.speakers_db['appearance_count'].sum() if 'appearance_count' in self.speakers_db.columns else 0,
            'cache_sizes': {
                'face_cache': len(self.face_cache),
                'name_cache': len(self.name_cache),
                'photo_metadata': len(self.photo_metadata)
            }
        }
    
    def process_speaker_appearances(self, appearances_df):
        """
        Process a DataFrame of speaker appearances and return speaker IDs
        This replaces the old person_id system with speaker_id system
        """
        print(f"Processing {len(appearances_df)} speaker appearances...")
        
        # Prepare results
        results = []
        new_speakers = 0
        
        for idx, row in appearances_df.iterrows():
            try:
                # Use seminar's discipline (which is standardized) 
                seminar_discipline = row.get('discipline', '')
                
                # Get speaker's affiliation (already standardized in data collection phase)
                speaker_affiliation = row.get('affiliation', '')
                speaker_affiliation_raw = row.get('affiliation_raw', '')
                
                speaker_id, is_new = self.add_or_update_speaker(
                    name=row.get('name', ''),
                    discipline=seminar_discipline,
                    university=speaker_affiliation,  # Use pre-standardized affiliation for ID
                    additional_info={
                        'first_name': row.get('first_name', ''),
                        'last_name': row.get('last_name', ''),
                        'affiliation': speaker_affiliation_raw,  # Keep raw for display
                        'affiliation_normalized': speaker_affiliation,  # Pre-standardized from data collection
                        'seminar_university': row.get('university', ''),  # Where they spoke
                        'seminar_discipline': seminar_discipline
                    }
                )
                
                # Skip if speaker was invalid (empty name)
                if speaker_id is None:
                    continue
                
                # Add speaker_id to the appearance record
                appearance_record = row.to_dict()
                appearance_record['speaker_id'] = speaker_id
                results.append(appearance_record)
                
                if is_new:
                    new_speakers += 1
                    
            except Exception as e:
                print(f"Error processing speaker {row.get('name', 'unknown')}: {e}")
                continue
        
        print(f"Processed {len(results)} appearances: {new_speakers} new speakers, "
              f"{len(results) - new_speakers} existing speakers")
        
        # Save the updated database
        self.save_all()
        
        return pd.DataFrame(results)

# Global database instance
speaker_db = SpeakerDatabase(fresh_start=False)