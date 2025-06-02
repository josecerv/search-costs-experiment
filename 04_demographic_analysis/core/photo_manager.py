"""
Smart Photo Manager for Search Costs RCT
Handles intelligent photo downloading with caching to avoid duplicate API calls
"""

import pandas as pd
import numpy as np
import os
import requests
import time
from PIL import Image
from io import BytesIO
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import sys
from pathlib import Path
import threading

# Add config to path
sys.path.append(str(Path(__file__).parent.parent.parent / "03_data_collection"))
sys.path.append(str(Path(__file__).parent))
from config.settings import config
from speaker_database import speaker_db

class PhotoManager:
    """
    Manages photo downloads with intelligent caching and API rate limiting
    """
    
    def __init__(self):
        self.photos_dir = config.SPEAKER_PHOTOS_DIR
        self.photos_dir.mkdir(exist_ok=True)
        
        # API configuration
        self.serpapi_key = None
        self.google_api_key = None
        self.google_cse_id = None
        
        try:
            self.serpapi_key = config.SERPAPI_KEY
        except ValueError:
            print("Warning: SERPAPI_KEY not configured")
        
        try:
            self.google_api_key = config.GOOGLE_SEARCH_API_KEY
            self.google_cse_id = config.GOOGLE_CSE_ID
        except ValueError:
            print("Warning: Google Search API not configured")
        
        # Rate limiting for SerpAPI (6000 per hour)
        self.serpapi_calls = []  # List of timestamps
        self.serpapi_limit_per_hour = 6000
        self.rate_limit_buffer = 100  # Leave some buffer
        self.rate_limit_lock = threading.Lock()  # Thread-safe access to rate limit data
        self.hit_429_error = False  # Flag to track if we hit a 429 error
    
    def _check_rate_limit(self):
        """Check if we're within SerpAPI rate limits (thread-safe)"""
        with self.rate_limit_lock:
            # Check if we previously hit a 429 error
            if self.hit_429_error:
                return  # Skip rate limiting, we're already in recovery mode
                
            current_time = time.time()
            one_hour_ago = current_time - 3600
            
            # Remove timestamps older than 1 hour
            self.serpapi_calls = [t for t in self.serpapi_calls if t > one_hour_ago]
            
            # Check if we're at the limit
            if len(self.serpapi_calls) >= (self.serpapi_limit_per_hour - self.rate_limit_buffer):
                # Calculate how long to wait
                oldest_call = min(self.serpapi_calls)
                wait_time = (oldest_call + 3600) - current_time + 60  # Add 1 minute buffer
                
                if wait_time > 0:
                    print(f"\n⚠️  Rate limit approaching: {len(self.serpapi_calls)} calls in the last hour")
                    print(f"Pausing for {wait_time:.0f} seconds to stay within limits...")
                    time.sleep(wait_time)
                    # Clear old calls after waiting
                    self.serpapi_calls = [t for t in self.serpapi_calls if t > (time.time() - 3600)]
    
    def get_rate_limit_status(self):
        """Get current rate limit status"""
        current_time = time.time()
        one_hour_ago = current_time - 3600
        calls_in_hour = len([t for t in self.serpapi_calls if t > one_hour_ago])
        
        return {
            'calls_in_last_hour': calls_in_hour,
            'limit_per_hour': self.serpapi_limit_per_hour,
            'calls_remaining': self.serpapi_limit_per_hour - calls_in_hour,
            'percentage_used': (calls_in_hour / self.serpapi_limit_per_hour) * 100
        }
    
    def get_image_urls_serpapi(self, speaker_info, num_results=3):
        """Get image URLs using SerpAPI with rate limiting"""
        if not self.serpapi_key:
            return []
        
        # Check rate limit before making API call
        self._check_rate_limit()
        
        name = speaker_info.get('name', '')
        university = speaker_info.get('university', '')
        discipline = speaker_info.get('discipline', '')
        
        # Ensure all values are strings (handle NaN/float values)
        name = str(name) if pd.notna(name) else ''
        university = str(university) if pd.notna(university) else ''
        discipline = str(discipline) if pd.notna(discipline) else ''
        
        # Create focused search query
        query_parts = [name] if name else []
        if university:
            query_parts.append(university)
        if discipline:
            query_parts.append(discipline)
        query_parts.extend(['professor', 'academic', 'faculty'])
        
        query = ' '.join(query_parts)
        
        params = {
            "api_key": self.serpapi_key,
            "engine": "google_images", 
            "q": query,
            "tbm": "isch",
            "num": num_results
        }
        
        urls = []
        try:
            # Record this API call (thread-safe)
            with self.rate_limit_lock:
                self.serpapi_calls.append(time.time())
            
            response = requests.get(
                "https://serpapi.com/search", 
                params=params, 
                timeout=config.REQUESTS_TIMEOUT
            )
            response.raise_for_status()
            results = response.json()
            
            if "images_results" in results:
                urls = [
                    img.get("original") 
                    for img in results["images_results"] 
                    if img.get("original")
                ]
                
        except requests.exceptions.Timeout:
            print(f"SerpAPI timeout for {name}")
        except requests.exceptions.RequestException as e:
            print(f"SerpAPI error for {name}: {e}")
            
            # Handle rate limit error (429)
            if e.response is not None and e.response.status_code == 429:
                with self.rate_limit_lock:
                    if not self.hit_429_error:  # First thread to hit the error
                        self.hit_429_error = True
                        print(f"\n🛑 RATE LIMIT HIT! Got 429 error from SerpAPI")
                        print(f"Pausing ALL threads for 1 hour to respect API limits...")
                        print(f"Current time: {pd.Timestamp.now()}")
                        print(f"Will resume at: {pd.Timestamp.now() + pd.Timedelta(hours=1)}")
                        
                        # Clear API call history since we hit the limit
                        self.serpapi_calls = []
                
                # Sleep for 1 hour (all threads will wait)
                time.sleep(3600)
                
                with self.rate_limit_lock:
                    if self.hit_429_error:  # Reset the flag after waiting
                        self.hit_429_error = False
                        print(f"\n✅ Resuming after 1-hour pause...")
                
                # Try the request one more time
                try:
                    with self.rate_limit_lock:
                        self.serpapi_calls.append(time.time())
                        
                    response = requests.get(
                        "https://serpapi.com/search", 
                        params=params, 
                        timeout=config.REQUESTS_TIMEOUT
                    )
                    response.raise_for_status()
                    results = response.json()
                    
                    if "images_results" in results:
                        urls = [
                            img.get("original") 
                            for img in results["images_results"] 
                            if img.get("original")
                        ]
                except Exception as retry_e:
                    print(f"Retry failed for {name}: {retry_e}")
                    
        except Exception as e:
            print(f"Unexpected error in SerpAPI for {name}: {e}")
        
        return urls
    
    def get_image_urls_google(self, speaker_info, num_results=3):
        """Get image URLs using Google Custom Search API"""
        if not self.google_api_key or not self.google_cse_id:
            return []
        
        name = speaker_info.get('name', '')
        university = speaker_info.get('university', '')
        discipline = speaker_info.get('discipline', '')
        
        # Ensure all values are strings (handle NaN/float values)
        name = str(name) if pd.notna(name) else ''
        university = str(university) if pd.notna(university) else ''
        discipline = str(discipline) if pd.notna(discipline) else ''
        
        # Create search query
        query_parts = [name] if name else []
        if university:
            query_parts.append(university)
        if discipline:
            query_parts.append(discipline)
        query_parts.extend(['professor', 'faculty'])
        
        query = ' '.join(query_parts)
        
        params = {
            'key': self.google_api_key,
            'cx': self.google_cse_id,
            'q': query,
            'searchType': 'image',
            'num': min(num_results, 10),  # Google CSE limits to 10
            'safe': 'medium'
        }
        
        urls = []
        try:
            response = requests.get(
                'https://www.googleapis.com/customsearch/v1',
                params=params,
                timeout=config.REQUESTS_TIMEOUT
            )
            response.raise_for_status()
            results = response.json()
            
            if 'items' in results:
                urls = [item['link'] for item in results['items']]
                
        except requests.exceptions.Timeout:
            print(f"Google API timeout for {name}")
        except requests.exceptions.RequestException as e:
            print(f"Google API error for {name}: {e}")
        except Exception as e:
            print(f"Unexpected error in Google API for {name}: {e}")
        
        return urls
    
    def download_image(self, url, filename):
        """Download single image with proper error handling"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(
                url, 
                headers=headers, 
                timeout=config.REQUESTS_TIMEOUT,
                stream=True
            )
            response.raise_for_status()
            
            # Check content type
            content_type = response.headers.get('content-type', '').lower()
            if 'image' not in content_type:
                return False, f"Not an image: {content_type}"
            
            # Load and validate image
            image_data = BytesIO(response.content)
            image = Image.open(image_data)
            
            # Basic validation
            if image.size[0] < 50 or image.size[1] < 50:
                return False, "Image too small"
            
            # Convert to RGB if necessary
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Save image
            image.save(filename, 'JPEG', quality=85)
            
            return True, {
                'file_size': len(response.content),
                'image_width': image.size[0],
                'image_height': image.size[1]
            }
            
        except requests.exceptions.Timeout:
            return False, "Download timeout"
        except requests.exceptions.RequestException as e:
            return False, f"Download error: {e}"
        except Exception as e:
            return False, f"Image processing error: {e}"
    
    def process_single_speaker_photo(self, speaker_row):
        """Download photo for a single speaker"""
        speaker_id = speaker_row['speaker_id']
        
        # Check if already downloaded
        existing_metadata = speaker_db.photo_metadata[
            speaker_db.photo_metadata['speaker_id'] == speaker_id
        ]
        
        if len(existing_metadata) > 0 and existing_metadata.iloc[0]['download_success']:
            # Verify the file actually exists on disk
            photo_filename = existing_metadata.iloc[0]['photo_filename']
            if photo_filename:
                photo_path = self.photos_dir / photo_filename
                if photo_path.exists():
                    return {
                        'speaker_id': speaker_id,
                        'success': True,
                        'message': 'Already downloaded',
                        'cached': True
                    }
                else:
                    print(f"Photo file missing for {speaker_id}: {photo_filename}, re-downloading...")
        
        # Get image URLs
        urls = []
        
        # Try SerpAPI first
        if self.serpapi_key:
            urls.extend(self.get_image_urls_serpapi(speaker_row, num_results=2))
        
        # Try Google API as backup
        if not urls and self.google_api_key:
            urls.extend(self.get_image_urls_google(speaker_row, num_results=2))
        
        if not urls:
            # Record failed search
            metadata = {
                'speaker_id': speaker_id,
                'photo_filename': '',
                'photo_url': '',
                'download_timestamp': pd.Timestamp.now().isoformat(),
                'download_success': False,
                'file_size': 0,
                'image_width': 0,
                'image_height': 0,
                'search_query_used': f"{speaker_row.get('name', '')} {speaker_row.get('university', '')}"
            }
            speaker_db.add_photo_metadata(metadata)
            speaker_db.mark_photo_downloaded(speaker_id, success=False)
            
            return {
                'speaker_id': speaker_id,
                'success': False,
                'message': 'No images found',
                'cached': False
            }
        
        # Try downloading images
        for i, url in enumerate(urls[:config.MAX_IMAGES_TO_TRY]):
            filename = self.photos_dir / f"{speaker_id}_{i+1}.jpg"
            
            success, result = self.download_image(url, filename)
            
            if success:
                # Record successful download
                metadata = {
                    'speaker_id': speaker_id,
                    'photo_filename': filename.name,
                    'photo_url': url,
                    'download_timestamp': pd.Timestamp.now().isoformat(),
                    'download_success': True,
                    'search_query_used': f"{speaker_row.get('name', '')} {speaker_row.get('university', '')}"
                }
                metadata.update(result)  # Add file size and dimensions
                
                speaker_db.add_photo_metadata(metadata)
                speaker_db.mark_photo_downloaded(speaker_id, success=True)
                
                return {
                    'speaker_id': speaker_id,
                    'success': True,
                    'message': f'Downloaded from {url}',
                    'filename': filename.name,
                    'cached': False
                }
            
            # Small delay between download attempts
            time.sleep(0.5)
        
        # All downloads failed
        metadata = {
            'speaker_id': speaker_id,
            'photo_filename': '',
            'photo_url': urls[0] if urls else '',
            'download_timestamp': pd.Timestamp.now().isoformat(),
            'download_success': False,
            'file_size': 0,
            'image_width': 0,
            'image_height': 0,
            'search_query_used': f"{speaker_row.get('name', '')} {speaker_row.get('university', '')}"
        }
        speaker_db.add_photo_metadata(metadata)
        speaker_db.mark_photo_downloaded(speaker_id, success=False)
        
        return {
            'speaker_id': speaker_id,
            'success': False,
            'message': f'Failed to download from {len(urls)} URLs',
            'cached': False
        }
    
    def download_photos_parallel(self, speakers_df, max_workers=None):
        """Download photos for multiple speakers in parallel"""
        if max_workers is None:
            max_workers = config.MAX_WORKERS_IMAGES
        
        print(f"Starting parallel photo download for {len(speakers_df)} speakers...")
        
        # Show rate limit status
        if self.serpapi_key:
            status = self.get_rate_limit_status()
            print(f"\n📊 SerpAPI Rate Limit Status:")
            print(f"   Limit: {status['limit_per_hour']} calls/hour")
            print(f"   Buffer: {self.rate_limit_buffer} calls")
            print(f"   Current usage: {status['calls_in_last_hour']} ({status['percentage_used']:.1f}%)")
            print(f"   Remaining: {status['calls_remaining']} calls")
            print(f"   Auto-pause will trigger at {self.serpapi_limit_per_hour - self.rate_limit_buffer} calls\n")
        
        results = []
        completed = 0
        cached_count = 0
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Submit all tasks
            future_to_speaker = {
                executor.submit(self.process_single_speaker_photo, row): row['speaker_id']
                for _, row in speakers_df.iterrows()
            }
            
            # Process completed tasks
            for future in concurrent.futures.as_completed(future_to_speaker):
                speaker_id = future_to_speaker[future]
                
                try:
                    result = future.result()
                    results.append(result)
                    
                    if result.get('cached', False):
                        cached_count += 1
                    
                    completed += 1
                    
                    if completed % 10 == 0:
                        api_calls_in_hour = len([t for t in self.serpapi_calls if t > (time.time() - 3600)])
                        print(f"Photo download progress: {completed}/{len(speakers_df)} "
                              f"({completed/len(speakers_df)*100:.1f}%) | "
                              f"API calls/hour: {api_calls_in_hour}/{self.serpapi_limit_per_hour}")
                    
                except Exception as e:
                    print(f"Photo download error for speaker {speaker_id}: {e}")
                    results.append({
                        'speaker_id': speaker_id,
                        'success': False,
                        'message': f'Exception: {e}',
                        'cached': False
                    })
                    completed += 1
                
                # Rate limiting
                if not result.get('cached', False):
                    time.sleep(config.IMAGE_BATCH_DELAY / max_workers)
        
        # Save updated metadata
        speaker_db.save_all()
        
        # Summary
        successful = sum(1 for r in results if r['success'])
        print(f"\nPhoto download complete:")
        print(f"  Total speakers: {len(speakers_df)}")
        print(f"  Successful downloads: {successful}")
        print(f"  Failed downloads: {len(results) - successful}")
        print(f"  Already cached: {cached_count}")
        
        return results
    
    def get_photo_path(self, speaker_id):
        """Get the path to a speaker's photo if it exists"""
        metadata = speaker_db.photo_metadata[
            (speaker_db.photo_metadata['speaker_id'] == speaker_id) &
            (speaker_db.photo_metadata['download_success'] == True)
        ]
        
        if len(metadata) > 0:
            filename = metadata.iloc[0]['photo_filename']
            photo_path = self.photos_dir / filename
            if photo_path.exists():
                return photo_path
        
        return None
    
    def cleanup_failed_downloads(self):
        """Remove failed download files and clean up metadata"""
        cleaned = 0
        for photo_file in self.photos_dir.glob("*.jpg"):
            if photo_file.stat().st_size < 1024:  # Less than 1KB
                photo_file.unlink()
                cleaned += 1
        
        print(f"Cleaned up {cleaned} failed download files")

# Global photo manager instance
photo_manager = PhotoManager()