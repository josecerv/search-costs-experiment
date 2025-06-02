"""
Configuration management for Search Costs RCT
Handles API keys, file paths, and processing settings securely
"""

import os
from pathlib import Path

class Config:
    """Centralized configuration for the Search Costs RCT pipeline"""
    
    # Project root directory - resolve to absolute path
    PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
    
    # Data directories
    DATA_COLLECTION_DIR = PROJECT_ROOT / "03_data_collection"
    DEMOGRAPHIC_ANALYSIS_DIR = PROJECT_ROOT / "04_demographic_analysis"
    STATISTICAL_ANALYSIS_DIR = PROJECT_ROOT / "05_statistical_analysis"
    
    # Raw data paths
    RAW_DATA_DIR = DATA_COLLECTION_DIR / "raw"
    PROCESSED_DATA_DIR = DATA_COLLECTION_DIR / "processed"
    
    # Demographic analysis paths
    SPEAKER_PHOTOS_DIR = DEMOGRAPHIC_ANALYSIS_DIR / "speaker_photos"
    CACHE_DIR = DEMOGRAPHIC_ANALYSIS_DIR / "cache"
    DEMOGRAPHIC_OUTPUTS_DIR = DEMOGRAPHIC_ANALYSIS_DIR / "outputs"
    
    # File names
    MASTER_DATA_FALL = RAW_DATA_DIR / "master-data-fall.csv"
    MASTER_DATA_LAILANIE = RAW_DATA_DIR / "master-data-fall-lailanie.csv"
    MASTER_DATA_SPRING = RAW_DATA_DIR / "master-data-spring.csv"
    
    # Allow environment variable override for data source
    _data_source = os.getenv('DEMOGRAPHIC_DATA_SOURCE', '')
    if _data_source and Path(_data_source).exists():
        MASTER_DATA_COMPLETE = Path(_data_source)
        MASTER_DATA_FULL_YEAR = Path(_data_source)
        MASTER_DATA_FINAL = Path(_data_source)
    else:
        # Legacy files (for backward compatibility)
        MASTER_DATA_COMPLETE = PROCESSED_DATA_DIR / "master-data-full-year.csv"  # Use full year data!
        MASTER_DATA_FULL_YEAR = PROCESSED_DATA_DIR / "master-data-full-year.csv"
        # NEW consolidated file
        MASTER_DATA_FINAL = PROCESSED_DATA_DIR / "master-data-final.csv"
    
    # Cache file names
    SPEAKER_DATABASE = CACHE_DIR / "speakers_database.csv"
    PHOTO_METADATA = CACHE_DIR / "photo_metadata.csv"
    FACE_ANALYSIS_CACHE = CACHE_DIR / "face_analysis_cache.csv"
    NAME_ANALYSIS_CACHE = CACHE_DIR / "name_analysis_cache.csv"
    
    # API Configuration (from environment variables)
    @property
    def OPENAI_API_KEY(self):
        key = os.getenv('OPENAI_API_KEY')
        if not key:
            raise ValueError("OPENAI_API_KEY environment variable not set")
        return key
    
    @property
    def SERPAPI_KEY(self):
        key = os.getenv('SERPAPI_KEY')
        if not key:
            raise ValueError("SERPAPI_KEY environment variable not set")
        return key
    
    @property
    def GOOGLE_SEARCH_API_KEY(self):
        key = os.getenv('GOOGLE_SEARCH_API_KEY')
        if not key:
            raise ValueError("GOOGLE_SEARCH_API_KEY environment variable not set")
        return key
    
    @property
    def GOOGLE_CSE_ID(self):
        cse_id = os.getenv('GOOGLE_CSE_ID')
        if not cse_id:
            raise ValueError("GOOGLE_CSE_ID environment variable not set")
        return cse_id
    
    @property
    def PERPLEXITY_API_KEY(self):
        return os.getenv('PERPLEXITY_API_KEY', '')
    
    @property
    def GOOGLE_SHEETS_API_KEY(self):
        return os.getenv('GOOGLE_SHEETS_API_KEY', '')
    
    @property
    def GOOGLE_SERVICE_ACCOUNT_FILE(self):
        return os.getenv('GOOGLE_SERVICE_ACCOUNT_FILE', '')
    
    # Processing Configuration
    MAX_SPEAKERS_PER_SEMINAR = 128
    MAX_IMAGES_TO_TRY = 3
    REQUESTS_TIMEOUT = 15
    MAX_WORKERS_IMAGES = 12  # Increased from 8 for faster photo downloads
    MAX_WORKERS_NAMES = 4
    IMAGE_BATCH_DELAY = 0.5
    NAME_BATCH_DELAY = 3
    DEFAULT_CONFIDENCE = 0.8
    
    # URM Categories for analysis
    # Pre-registered URM categories (standardized to lowercase)
    URM_CATEGORIES = ['black', 'latino', 'native american']
    
    def __init__(self):
        """Initialize configuration and create necessary directories"""
        self.create_directories()
    
    def create_directories(self):
        """Create all necessary directories if they don't exist"""
        directories = [
            self.RAW_DATA_DIR,
            self.PROCESSED_DATA_DIR,
            self.SPEAKER_PHOTOS_DIR,
            self.CACHE_DIR,
            self.DEMOGRAPHIC_OUTPUTS_DIR
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
    
    def get_api_status(self):
        """Check which API keys are configured"""
        status = {}
        try:
            status['openai'] = bool(self.OPENAI_API_KEY)
        except ValueError:
            status['openai'] = False
            
        try:
            status['serpapi'] = bool(self.SERPAPI_KEY)
        except ValueError:
            status['serpapi'] = False
            
        try:
            status['google_search'] = bool(self.GOOGLE_SEARCH_API_KEY)
        except ValueError:
            status['google_search'] = False
            
        try:
            status['google_cse'] = bool(self.GOOGLE_CSE_ID)
        except ValueError:
            status['google_cse'] = False
            
        status['perplexity'] = bool(self.PERPLEXITY_API_KEY)
        status['google_sheets'] = bool(self.GOOGLE_SHEETS_API_KEY or self.GOOGLE_SERVICE_ACCOUNT_FILE)
        
        return status

# Global configuration instance
config = Config()