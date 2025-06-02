# Demographic Analysis Scripts

This folder contains the scripts for demographic analysis of seminar speakers using face and name analysis.

## Main Analysis Script

### `run_analysis.py`
**Purpose**: Main entry point for all demographic analysis tasks  
**Features**:
- Face analysis using DeepFace (with subprocess isolation for stability)
- Name analysis using GPT-4o (with FAST async processing - 50x concurrent)
- Intelligent caching to avoid duplicate API calls
- Combines results and calculates URM statistics

**Usage**:
```bash
# Full analysis (photos, face, name, combine)
poetry run python run_analysis.py

# Specific modes
poetry run python run_analysis.py --mode photos      # Download photos only
poetry run python run_analysis.py --mode names       # Run name analysis only (FAST)
poetry run python run_analysis.py --mode combine     # Combine existing results
poetry run python run_analysis.py --mode status      # Check analysis progress

# Force reprocess (ignore cache)
poetry run python run_analysis.py --mode names --force-reprocess
```

## Supporting Scripts

### `fast_name_analysis.py`
**Purpose**: High-performance async name analysis using GPT-4o  
**Features**:
- 150 concurrent API requests (optimized for speed)
- 300 name batches for efficient processing
- Progress saving every 10 batches
- Automatic rate limiting
- ETA and progress tracking
- Called automatically by `run_analysis.py --mode names`

### `run_face_analysis_isolated_batch.py`
**Purpose**: Face analysis with subprocess isolation to prevent memory corruption  
**Features**:
- Analyzes faces in isolated subprocesses (batches of 5)
- Prevents "double free detected in tcache 2" errors
- ~2-3 seconds per face
- Progress saved regularly
- Called by pipeline scripts for face analysis

## Utility Scripts

### `link_existing_photos.py`
**Purpose**: Links existing speaker photos to the database  
**Usage**: `poetry run python link_existing_photos.py`
- Use if photos were downloaded but database lost track

### `reset_face_analysis_flags.py`
**Purpose**: Reset face analysis flags in the database  
**Usage**: `poetry run python reset_face_analysis_flags.py`
- Use to force re-analysis of faces if needed

## Archived Scripts
Temporary utilities and one-time fixes have been moved to `_archive_temp_utils/`:
- Data cleaning and normalization scripts
- Debugging utilities
- One-time fixes for specific issues

## Technical Details

### Memory Corruption Fix (Face Analysis)
Face analysis uses subprocess isolation to prevent memory errors:
```python
# Handled automatically by run_face_analysis_isolated_batch.py
# Processes in batches of 5 faces per subprocess
```

### Fast Async Name Analysis
Name analysis uses async/await for high performance:
- 50 concurrent OpenAI API requests
- Batches of 100 speakers
- ~10-15 minutes for 20,000 speakers (vs hours with serial)

### Environment Requirements
```bash
# Load environment variables
export OPENAI_API_KEY="your-key"
# Or use .env file in project root

# Poetry handles all dependencies
poetry install
```

## Output Files

All analysis results are saved to:
- `/04_demographic_analysis/outputs/people_combined_analysis.csv` - Individual speaker demographics
- `/04_demographic_analysis/outputs/speaker_appearances_analysis.csv` - Seminar appearance-level data

## Cache Files

- `/04_demographic_analysis/cache/speakers_database.csv` - Speaker registry
- `/04_demographic_analysis/cache/face_analysis_cache.csv` - Face analysis results
- `/04_demographic_analysis/cache/name_analysis_cache.csv` - Name analysis results
- `/04_demographic_analysis/cache/photo_metadata.csv` - Photo download metadata

## Data Flow

1. **Input Data**: Seminars from `/03_data_collection/processed/`
2. **Photo Download**: SerpAPI/Google Images → `/speaker_photos/`
3. **Face Analysis**: DeepFace extracts gender/race (subprocess isolation)
4. **Name Analysis**: GPT-4o infers demographics (async processing)
5. **Combine**: Merge face + name results with confidence thresholds
6. **Output**: URM statistics for statistical analysis

## Common Commands

```bash
# Check current progress
poetry run python run_analysis.py --mode status

# Run only name analysis (after face is done)
poetry run python run_analysis.py --mode names

# Combine and export results (after both analyses)
poetry run python run_analysis.py --mode combine

# Full pipeline (if starting fresh)
poetry run python run_analysis.py
```