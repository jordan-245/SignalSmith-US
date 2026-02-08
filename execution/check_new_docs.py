#!/usr/bin/env python3
"""
Check for new documents since last ingestion.
Returns exit code 0 if new docs found, 1 otherwise.
"""
import os
import sys
from pathlib import Path
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment
load_dotenv()

def check_new_docs():
    """Check if there are new documents to ingest."""
    # Check the last ingestion timestamp
    state_file = Path("output/state/last_doc_ingest.txt")
    
    if not state_file.exists():
        print("No previous ingestion timestamp found - treat as new docs available")
        return True
    
    try:
        with open(state_file, 'r') as f:
            last_ingest_str = f.read().strip()
            last_ingest = datetime.fromisoformat(last_ingest_str)
    except Exception as e:
        print(f"Error reading last ingestion timestamp: {e}")
        return True
    
    # Check if last ingestion was more than 24 hours ago
    hours_since = (datetime.now() - last_ingest).total_seconds() / 3600
    
    if hours_since > 24:
        print(f"Last ingestion was {hours_since:.1f}h ago - check for new docs")
        return True
    else:
        print(f"Last ingestion was {hours_since:.1f}h ago - no check needed")
        return False

if __name__ == "__main__":
    has_new = check_new_docs()
    sys.exit(0 if has_new else 1)
