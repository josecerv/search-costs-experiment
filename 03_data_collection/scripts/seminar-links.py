import pandas as pd
import requests
import time
import re
import os
from urllib.parse import urlparse, urljoin

# --- Configuration ---
# API key should be set as environment variable
API_KEY = os.environ.get("PERPLEXITY_API_KEY")
if not API_KEY:
    raise ValueError("PERPLEXITY_API_KEY environment variable is not set")

API_ENDPOINT = "https://api.perplexity.ai/chat/completions"
CSV_FILE_PATH = 'fall-2024-academic-term-may-be-incorrect.csv'
REQUEST_TIMEOUT = 15 # seconds for HEAD/GET requests
MAX_CONTENT_CHECK_SIZE = 20480 # Bytes (20KB) to check for keywords
RETRY_ATTEMPTS = 3 # Max retries for Perplexity API calls on 429 errors
INITIAL_BACKOFF = 5 # seconds for first retry delay

# --- Helper Functions ---

def is_valid_url(url):
    """Check if a URL has a valid scheme and netloc."""
    try:
        result = urlparse(url)
        return all([result.scheme in ['http', 'https'], result.netloc])
    except:
        return False

def extract_urls_from_text(text):
    """Extract URLs using a more robust regex."""
    # Regex to find URLs, trying to avoid trailing punctuation
    url_pattern = r'(https?://[^\s<>"]+)'
    urls = re.findall(url_pattern, text)
    # Clean potential trailing characters like parentheses often added by LLMs
    cleaned_urls = [re.sub(r'[.,;!)\]]$', '', url) for url in urls]
    return [url for url in cleaned_urls if is_valid_url(url)]

def verify_url(url, university, department, seminar, term="Fall 2024"):
    """Verify if the URL is reachable and likely contains relevant info."""
    print(f"    Verifying URL: {url}...")
    try:
        headers = {'User-Agent': 'SeminarURLVerifierBot/1.0'} # Be a good internet citizen
        
        # 1. Try HEAD request first (faster)
        response = requests.head(url, headers=headers, timeout=REQUEST_TIMEOUT, allow_redirects=True)
        response.raise_for_status() # Check for 4xx/5xx errors
        is_accessible = True
        content_type = response.headers.get('content-type', '').lower()
        
        # Avoid trying to read non-HTML content
        if 'html' not in content_type:
             print(f"    Skipping content check (Content-Type: {content_type})")
             # We know it's accessible, which is better than nothing.
             # Depending on strictness, you could return False here.
             return True 

    except requests.exceptions.RequestException as e:
        print(f"    HEAD request failed for {url}: {e}")
        is_accessible = False
        # If HEAD failed (e.g., 405 Method Not Allowed), try GET
        if isinstance(e, requests.exceptions.HTTPError) and e.response.status_code == 405:
             pass # Fall through to try GET
        elif isinstance(e, requests.exceptions.HTTPError) and e.response.status_code == 403:
             print("    Access Forbidden (403). Assuming URL is valid but content check skipped.")
             return True # Treat as potentially valid if forbidden, as it exists
        else:
            return False # Other errors mean it's likely not accessible/valid

    try:
        # 2. Try GET request if HEAD worked (and was HTML) or if HEAD failed with 405
        # Only download the beginning of the content for keyword checking
        print(f"    Performing GET request for content check...")
        response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT, stream=True, allow_redirects=True)
        response.raise_for_status()
        
        content_type = response.headers.get('content-type', '').lower()
        if 'html' not in content_type:
            print(f"    Skipping content check (Content-Type: {content_type})")
            return True # Accessible, non-HTML page like PDF might be valid

        # Read only a chunk of the content
        content_chunk = response.raw.read(MAX_CONTENT_CHECK_SIZE, decode_content=True)
        # Decode defensively
        try:
            content_text = content_chunk.decode('utf-8', errors='ignore').lower()
        except Exception:
             content_text = content_chunk.decode('latin-1', errors='ignore').lower() # Fallback encoding

        # 3. Check for keywords
        term_year = term.split()[-1] # "2024"
        department_parts = department.lower().split() # Split department name for flexible matching
        seminar_parts = seminar.lower().split() # Split seminar name

        # Define required keywords (adjust sensitivity as needed)
        found_term = term.lower() in content_text or term_year in content_text
        found_dept = any(part in content_text for part in department_parts if len(part) > 3) # Check for significant parts
        found_seminar = "seminar" in content_text or "colloquium" in content_text or "talks" in content_text or any(part in content_text for part in seminar_parts if len(part)>3)
        
        # Require term/year AND department AND seminar type keywords for higher confidence
        if found_term and found_dept and found_seminar:
            print("    Verification successful: Found relevant keywords.")
            return True
        else:
            print(f"    Verification failed: Missing keywords (Term: {found_term}, Dept: {found_dept}, Seminar: {found_seminar})")
            return False

    except requests.exceptions.RequestException as e:
        print(f"    GET request or content check failed for {url}: {e}")
        # If it was accessible via HEAD but GET failed, maybe still return True? Or False for stricter check.
        # Let's be stricter: if GET fails, we can't verify content.
        return False
    finally:
        # Ensure the connection is closed if using stream=True
        if 'response' in locals() and hasattr(response, 'close'):
            response.close()


def search_seminar_url(university, department, seminar, academic_term="Fall 2024"):
    """Search for seminar URL using Perplexity API, verify, and handle retries."""
    if not API_KEY or API_KEY == "pplx-YOUR-API-KEY-HERE":
        print("Error: Perplexity API Key not configured.")
        return None
        
    # Construct a focused search query
    # Emphasize official source and the specific term
    search_query = (
        f"What is the official webpage URL for the {department} {seminar} series "
        f"at {university} for the {academic_term} academic term? "
        f"Provide only the direct URL. Prioritize pages that explicitly mention '{academic_term}' or '{academic_term.split()[-1]}'."
    )
    
    # Define the payload
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "sonar-reasoning-pro", # Using the desired reasoning model
        "messages": [
            {"role": "system", "content": "You are an expert academic research assistant. Your task is to find the single, most accurate, official URL for a specific university seminar series for a given academic term. Respond *only* with the URL itself, nothing else. Do not add explanations or introductory text."},
            {"role": "user", "content": search_query}
        ]
    }
    
    current_attempt = 0
    wait_time = INITIAL_BACKOFF
    
    while current_attempt < RETRY_ATTEMPTS:
        current_attempt += 1
        print(f"  Attempt {current_attempt}/{RETRY_ATTEMPTS} for {university} - {department} - {seminar}")
        
        try:
            response = requests.post(API_ENDPOINT, headers=headers, json=data, timeout=30) # Increased timeout for API call
            
            # Check for specific 429 Too Many Requests error
            if response.status_code == 429:
                print(f"    Received 429 (Too Many Requests). Waiting {wait_time} seconds before retrying...")
                time.sleep(wait_time)
                wait_time *= 2 # Exponential backoff
                continue # Go to next attempt

            response.raise_for_status() # Raise HTTPError for other bad responses (4xx, 5xx)
            
            # Parse the response
            response_data = response.json()
            content = response_data.get("choices", [{}])[0].get("message", {}).get("content", "")
            
            # Extract potential URLs
            potential_urls = extract_urls_from_text(content)
            print(f"    LLM response received. Found {len(potential_urls)} potential URLs.")
            
            if not potential_urls:
                 # Sometimes the URL might be the entire response, without markdown/extra text
                 if is_valid_url(content.strip()):
                     potential_urls = [content.strip()]
                 else:
                     print(f"    No valid URLs extracted from response: {content}")
                     return None # Failed to get a usable URL from LLM

            # Try to verify each extracted URL
            for url in potential_urls:
                if verify_url(url, university, department, seminar, academic_term):
                    print(f"    Successfully verified URL: {url}")
                    return url # Return the first verified URL
                else:
                     # If verification fails, maybe the LLM gave a base page? Try appending common paths.
                     # Example: try adding '/seminars', '/schedule', '/fall2024' etc. 
                     # This adds complexity, implement carefully if needed.
                     # For now, we just try the next URL from the list.
                     print(f"    Verification failed for {url}.")
            
            print("    None of the extracted URLs could be verified.")
            return None # None of the URLs passed verification

        except requests.exceptions.Timeout:
            print(f"    Error: API request timed out for {university} {department} {seminar}.")
            if current_attempt >= RETRY_ATTEMPTS:
                 return None # Failed after retries
            time.sleep(wait_time) # Wait before retrying on timeout
            wait_time *= 2

        except requests.exceptions.RequestException as e:
            print(f"    Error searching for {university} {department} {seminar}: {e}")
            # Decide if retry is appropriate for this error type, here we stop
            return None # Don't retry on general request errors or HTTP errors other than 429
            
    print(f"  Failed to get valid response after {RETRY_ATTEMPTS} attempts.")
    return None


def main():
    # Read the CSV file
    try:
        df = pd.read_csv(CSV_FILE_PATH)
        print(f"Successfully loaded CSV '{CSV_FILE_PATH}' with {len(df)} rows.")
    except FileNotFoundError:
        print(f"Error: CSV file not found at '{CSV_FILE_PATH}'")
        return
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return
    
    # Check if required columns exist
    required_columns = ['University', 'Department', 'Seminar', 'AcademicTerm']
    if not all(column in df.columns for column in required_columns):
        print(f"Error: CSV must contain columns: {', '.join(required_columns)}")
        return
    
    # Ensure 'updated_url' column exists, initialize if not
    if 'updated_url' not in df.columns:
        df['updated_url'] = pd.NA # Use pandas NA for missing values

    # Use .isna() for checking missing values which works for None, np.nan, pd.NA
    rows_to_process = df[df['updated_url'].isna() & df['AcademicTerm'].str.contains("Fall 2024", na=False)]
    
    print(f"Found {len(rows_to_process)} rows for Fall 2024 needing URL update.")
    
    processed_count = 0
    updated_count = 0
    total_to_process = len(rows_to_process)

    start_time = time.time()

    for index, row in rows_to_process.iterrows():
        processed_count += 1
        university = row['University']
        department = row['Department']
        seminar = row['Seminar']
        academic_term = row['AcademicTerm'] # Should contain "Fall 2024" based on filter
        
        print(f"\nProcessing row {index} ({processed_count}/{total_to_process}): {university} - {department} - {seminar}...")
        
        # Search for and verify the correct URL
        # Pass necessary info for verification
        verified_url = search_seminar_url(university, department, seminar, academic_term) 
        
        if verified_url:
            df.loc[index, 'updated_url'] = verified_url
            print(f"-> Found and verified URL: {verified_url}")
            updated_count += 1
        else:
            df.loc[index, 'updated_url'] = "NOT_FOUND" # Mark as not found after trying
            print(f"-> Could not find or verify URL for {university} - {department} - {seminar}")
        
        # Save progress periodically (e.g., every 5 rows)
        if processed_count % 5 == 0 or processed_count == total_to_process:
            try:
                 df.to_csv(CSV_FILE_PATH, index=False)
                 now = time.time()
                 elapsed = now - start_time
                 avg_time = elapsed / processed_count if processed_count else 0
                 print(f"\n--- Progress saved ({processed_count}/{total_to_process} processed). {updated_count} URLs updated. Elapsed: {elapsed:.2f}s (Avg: {avg_time:.2f}s/row) ---")
            except Exception as e:
                 print(f"Error saving progress to CSV: {e}")
                 # Decide if you want to stop or continue if saving fails

        # Respect potential rate limits - the sleep is now mainly between different seminar searches
        # The search_seminar_url function handles retries for 429s internally.
        # A small base delay is still polite.
        time.sleep(1) # Short delay between processing different rows
    
    end_time = time.time()
    print(f"\nProcessing complete.")
    print(f"Processed {processed_count} rows requiring updates.")
    print(f"Found and verified {updated_count} URLs.")
    print(f"Total time: {end_time - start_time:.2f} seconds.")
    # Final save
    try:
        df.to_csv(CSV_FILE_PATH, index=False)
        print(f"Final results saved to '{CSV_FILE_PATH}'.")
    except Exception as e:
        print(f"Error saving final results to CSV: {e}")


if __name__ == "__main__":
    # IMPORTANT: Set the PERPLEXITY_API_KEY environment variable before running,
    # or replace the placeholder in the script (less secure).
    # Example (Linux/macOS): export PERPLEXITY_API_KEY='pplx-...'
    # Example (Windows Cmd): set PERPLEXITY_API_KEY=pplx-...
    # Example (Windows PowerShell): $env:PERPLEXITY_API_KEY='pplx-...'
    main()
