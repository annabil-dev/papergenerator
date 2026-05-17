#!/usr/bin/env python3
"""
Search Google for journal templates using Custom Search API.
"""
import json
import time
import requests
from bs4 import BeautifulSoup

# Note: Google Custom Search API requires API key
# This script uses web search as fallback

JSON_FILE = "/home/otomasi/papergenerator/sinta_all_journals_final.json"
OUTPUT_JSON = "/home/otomasi/papergenerator/sinta_all_journals_google.json"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

def search_google(query):
    """Search Google and return first 5 results"""
    try:
        url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
        r = requests.get(url, headers=HEADERS, timeout=10)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content, 'html.parser')
            results = []
            for g in soup.find_all('div', class_='g', limit=5):
                link = g.find('a')
                if link:
                    results.append(link['href'])
            return results
    except:
        pass
    return []

def find_template_google(journal_name):
    """Search Google for journal template"""
    queries = [
        f"{journal_name} template filetype:doc",
        f"{journal_name} template filetype:docx",
        f"{journal_name} panduan penulis",
        f"{journal_name} author guidelines"
    ]
    
    for query in queries:
        results = search_google(query)
        for result in results:
            if any(ext in result.lower() for ext in ['.doc', '.docx', '.pdf']):
                if 'template' in result.lower() or 'format' in result.lower():
                    return result
        time.sleep(2)  # Be nice to Google
    
    return None

def main():
    print("Loading journals...")
    with open(JSON_FILE, 'r') as f:
        data = json.load(f)
    
    journals = data.get('journals', [])
    
    # Find journals without templates
    without_template = [j for j in journals if not j.get('template_url')]
    print(f"Journals without templates: {len(without_template)}")
    
    # Try Google search for first 100
    updated = 0
    for idx, journal in enumerate(without_template[:100]):
        name = journal.get('name', 'Unknown')
        print(f"[{idx+1}/100] Searching: {name}")
        
        template_url = find_template_google(name)
        if template_url:
            journal['template_url'] = template_url
            journal['template_source'] = 'google_search'
            updated += 1
            print(f"  Found: {template_url}")
        
        time.sleep(3)  # Be nice to Google
    
    # Save
    with open(OUTPUT_JSON, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"\nDone! Found {updated} more templates via Google search.")

if __name__ == '__main__':
    main()
