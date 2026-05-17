#!/usr/bin/env python3
"""
Fast template finder for ALL SINTA journals.
Uses concurrent requests and multiple search methods.
"""
import json
import time
import os
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

# Configuration
JSON_FILE = "/home/otomasi/papergenerator/sinta_all_journals.json"
OUTPUT_JSON = "/home/otomasi/papergenerator/sinta_all_journals_final.json"
BASE_TEMPLATE_DIR = "/home/otomasi/papergenerator/template/jurnal sinta"
LOG_DIR = "/home/otomasi/papergenerator/template/jurnal sinta"
MAX_WORKERS = 20
TIMEOUT = 10

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

log_lock = Lock()
journal_lock = Lock()

def log_message(log_file, message):
    with log_lock:
        with open(log_file, 'a') as f:
            f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

def load_journals():
    with open(JSON_FILE, 'r') as f:
        data = json.load(f)
    return data.get('journals', [])

def save_journals(journals):
    with open(OUTPUT_JSON, 'w') as f:
        json.dump({'journals': journals, 'total': len(journals), 'updated': time.strftime('%Y-%m-%d %H:%M:%S')}, f, indent=2)

def get_website_from_profile(profile_url):
    try:
        r = requests.get(profile_url, headers=HEADERS, timeout=TIMEOUT)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html.parser')
            for a in soup.find_all('a', href=True):
                if 'website' in a.text.lower() or 'visit' in a.text.lower():
                    return a['href']
    except:
        pass
    return None

def find_template_in_url(base_url, path):
    """Try to find template at a specific URL"""
    try:
        url = urljoin(base_url, path)
        r = requests.get(url, headers=HEADERS, timeout=5)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html.parser')
            for a in soup.find_all('a', href=True):
                href = a['href']
                if any(href.lower().endswith(ext) for ext in ['.doc', '.docx', '.pdf', '.odt']):
                    if any(kw in href.lower() or kw in a.text.lower() for kw in ['template', 'format', 'panduan', 'author']):
                        return urljoin(base_url, href)
    except:
        pass
    return None

def find_template_url(website_url):
    """Find template URL using multiple methods"""
    if not website_url:
        return None, "No website URL"
    
    try:
        r = requests.get(website_url, headers=HEADERS, timeout=TIMEOUT)
        if r.status_code != 200:
            return None, f"Failed to fetch website: {r.status_code}"
        
        soup = BeautifulSoup(r.content, 'html.parser')
        base_url = website_url
        
        # Method 1: Check common paths
        common_paths = [
            '/about/submissions', '/about/authors', '/author-guidelines',
            '/panduan-penulis', '/template', '/format', '/submissions'
        ]
        for path in common_paths:
            template_url = find_template_in_url(base_url, path)
            if template_url:
                return template_url, f"Found via {path}"
        
        # Method 2: Search in main page
        for a in soup.find_all('a', href=True):
            href = a['href']
            text = a.text.lower()
            if any(kw in href.lower() or kw in text for kw in ['template', 'format', 'panduan', 'author', 'guidelines']):
                if any(href.lower().endswith(ext) for ext in ['.doc', '.docx', '.pdf', '.odt']):
                    return urljoin(base_url, href), "Found in main page"
        
        return None, "Template not found"
        
    except Exception as e:
        return None, str(e)

def download_template(template_url, journal_name, sinta_rank):
    try:
        dir_path = os.path.join(BASE_TEMPLATE_DIR, sinta_rank)
        os.makedirs(dir_path, exist_ok=True)
        
        clean_name = re.sub(r'[^a-zA-Z0-9_]+', '_', journal_name)
        ext = os.path.splitext(template_url)[1] or '.pdf'
        filename = f"{clean_name}_template{ext}"
        filepath = os.path.join(dir_path, filename)
        
        r = requests.get(template_url, headers=HEADERS, timeout=30)
        if r.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(r.content)
            return filepath, "Downloaded"
        else:
            return None, f"Failed: {r.status_code}"
    except Exception as e:
        return None, str(e)

def process_journal(journal):
    name = journal.get('name', 'Unknown')
    sinta_rank = journal.get('sinta_rank', 'S1')
    profile_url = journal.get('profile_url')
    
    # Get website URL if not have
    if not journal.get('website_url') and profile_url:
        website_url = get_website_from_profile(profile_url)
        if website_url:
            journal['website_url'] = website_url
    
    # Find template
    website_url = journal.get('website_url')
    if website_url and not journal.get('template_url'):
        template_url, msg = find_template_url(website_url)
        if template_url:
            journal['template_url'] = template_url
            journal['template_status'] = 'found'
            
            # Download
            filepath, dl_msg = download_template(template_url, name, sinta_rank)
            if filepath:
                journal['template_downloaded'] = True
                journal['template_path'] = filepath
            else:
                journal['template_downloaded'] = False
        else:
            journal['template_status'] = 'not_found'
            journal['template_error'] = msg
    
    return journal

def main():
    print("Loading journals...")
    journals = load_journals()
    print(f"Total: {len(journals)}")
    
    # Filter journals without templates
    to_process = [j for j in journals if not j.get('template_url')]
    print(f"To process: {len(to_process)}")
    
    # Process concurrently
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(process_journal, j): j for j in to_process}
        
        for idx, future in enumerate(as_completed(futures)):
            journal = future.result()
            
            # Update in original list
            for i, j in enumerate(journals):
                if j.get('name') == journal.get('name'):
                    journals[i] = journal
                    break
            
            # Save progress every 50
            if (idx + 1) % 50 == 0:
                save_journals(journals)
                print(f"Progress: {idx+1}/{len(to_process)}")
    
    # Final save
    save_journals(journals)
    print("Done!")

if __name__ == '__main__':
    main()
