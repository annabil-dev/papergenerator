#!/usr/bin/env python3
"""
Automated template downloader for SINTA journals.
Uses Playwright to visit journal websites and download templates.
"""

import json
import os
import re
import time
import sys
from pathlib import Path
from datetime import datetime
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

# Template keywords to search for in links
TEMPLATE_KEYWORDS = [
    'template', 'author guidelines', 'panduan penulis', 'format',
    'submission', 'author', 'panduan', 'guidelines', 'template artikel',
    'format artikel', 'author template', 'article template', 'manuscript',
    'download', 'dokumen', 'document', 'panduan author', 'template file'
]

# File extensions to download
TEMPLATE_EXTENSIONS = ['.pdf', '.doc', '.docx', '.dot', '.dotx']

def sanitize_filename(name):
    """Sanitize filename for safe file system use."""
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    return name[:100]

def log_message(log_file, message):
    """Write message to log file."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"[{timestamp}] {message}\n"
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(log_entry)
    print(log_entry.strip(), flush=True)

def find_template_links(page):
    """Find template download links on the page."""
    template_links = []
    
    try:
        # Get all links on the page
        links = page.query_selector_all('a')
        
        for link in links:
            try:
                href = link.get_attribute('href')
                text = link.inner_text().lower() if link.inner_text() else ""
                
                if not href:
                    continue
                
                # Check if link text contains template keywords
                is_template_text = any(keyword in text for keyword in TEMPLATE_KEYWORDS)
                
                # Check if href contains template keywords or has template extension
                is_template_href = any(keyword in href.lower() for keyword in TEMPLATE_KEYWORDS)
                has_template_ext = any(href.lower().endswith(ext) for ext in TEMPLATE_EXTENSIONS)
                
                if is_template_text or is_template_href or has_template_ext:
                    # Make relative URLs absolute
                    if href.startswith('//'):
                        href = 'https:' + href
                    elif href.startswith('/'):
                        base = page.url.rstrip('/')
                        if base.endswith('.php') or '.html' in base:
                            base = '/'.join(base.split('/')[:-1])
                        href = base + href
                    elif not href.startswith('http'):
                        href = page.url.rstrip('/') + '/' + href.lstrip('/')
                    
                    template_links.append({
                        'url': href,
                        'text': text[:100]
                    })
            except:
                continue
    except:
        pass
    
    return template_links

def process_journal(page, journal, output_dir, log_file):
    """Process a single journal to find and download templates."""
    name = journal.get('name', 'Unknown')
    website = journal.get('website', '')
    rank = journal.get('accreditation', 'Unknown')
    
    if not website:
        log_message(log_file, f"  SKIP: {name} - No website URL")
        return 0
    
    log_message(log_file, f"  Processing: {name}")
    log_message(log_file, f"    URL: {website}")
    
    templates_downloaded = 0
    
    try:
        # Navigate to journal website
        try:
            page.goto(website, wait_until='domcontentloaded', timeout=20000)
            time.sleep(3)
        except Exception as e:
            log_message(log_file, f"    Error loading page: {e}")
            return 0
        
        # Look for template links on main page
        template_links = find_template_links(page)
        
        # Check common subpages for templates
        subpages = ['/about/submissions', '/about', '/submissions', '/author-guidelines', 
                    '/panduan-penulis', '/template', '/download', '/guidelines']
        
        for subpage in subpages[:3]:  # Limit to avoid too many requests
            try:
                test_url = website.rstrip('/') + subpage
                page.goto(test_url, wait_until='domcontentloaded', timeout=10000)
                time.sleep(2)
                template_links.extend(find_template_links(page))
            except:
                continue
        
        # Remove duplicates
        seen_urls = set()
        unique_links = []
        for link in template_links:
            url = link['url']
            if url not in seen_urls and ('http' in url or 'drive.google' in url):
                seen_urls.add(url)
                unique_links.append(link)
        
        # Download only the first template found
        if unique_links:
            link = unique_links[0]
            try:
                url = link['url']
                
                # Determine file extension
                ext = '.pdf'  # Default
                for template_ext in TEMPLATE_EXTENSIONS:
                    if template_ext in url.lower():
                        ext = template_ext
                        break
                
                filename = sanitize_filename(name) + f"_template{ext}"
                output_path = os.path.join(output_dir, filename)
                
                # Skip if already downloaded
                if os.path.exists(output_path):
                    templates_downloaded += 1
                    log_message(log_file, f"    Already exists: {filename}")
                    return templates_downloaded
                
                # Try to download the file
                try:
                    response = page.context.request.get(url, timeout=15000)
                    if response.status == 200:
                        content = response.body()
                        if len(content) > 1000:  # Make sure it's not an error page
                            with open(output_path, 'wb') as f:
                                f.write(content)
                            templates_downloaded += 1
                            log_message(log_file, f"    Downloaded: {filename}")
                except Exception as e:
                    log_message(log_file, f"    Error downloading {url}: {e}")
                    
            except Exception as e:
                pass
        
        if templates_downloaded == 0:
            log_message(log_file, f"    No templates found")
        
    except Exception as e:
        log_message(log_file, f"  Error processing journal: {e}")
    
    return templates_downloaded

def main():
    # Load journal data
    json_path = '/home/otomasi/papergenerator/sinta_journals_data.json'
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Base output directory
    base_dir = '/home/otomasi/papergenerator/template/jurnal sinta'
    log_dir = '/home/otomasi/papergenerator/template'
    log_file = os.path.join(log_dir, 'download_log.txt')
    
    # Initialize log
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write(f"Template Download Log - Started {datetime.now()}\n")
        f.write("=" * 80 + "\n\n")
    
    with sync_playwright() as p:
        # Launch browser in headless mode
        browser = p.chromium.launch(headless=True, args=['--no-sandbox'])
        
        context = browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            accept_downloads=True
        )
        
        page = context.new_page()
        
        # Process each SINTA rank
        rank_mapping = [
            ('sinta_1_journals', 'S1', 10),
            ('sinta_2_journals', 'S2', 5),
            ('sinta_3_journals', 'S3', 5),
            ('sinta_4_journals', 'S4', 5),
            ('sinta_5_journals', 'S5', 5),
            ('sinta_6_journals', 'S6', 5)
        ]
        
        total_templates = 0
        
        for rank_key, rank_name, max_journals in rank_mapping:
            if rank_key not in data:
                continue
            
            journals = data[rank_key]
            output_dir = os.path.join(base_dir, rank_name)
            os.makedirs(output_dir, exist_ok=True)
            
            log_message(log_file, f"\nProcessing {rank_name} journals ({len(journals)} found)")
            log_message(log_file, f"Target: Download from up to {max_journals} journals")
            
            rank_templates = 0
            
            for i, journal in enumerate(journals[:max_journals]):
                journal['accreditation'] = rank_name
                templates = process_journal(page, journal, output_dir, log_file)
                rank_templates += templates
                total_templates += templates
                
                # Progress update every 5 journals
                if (i + 1) % 5 == 0:
                    log_message(log_file, f"  Progress: {i+1}/{max_journals} journals processed, {rank_templates} templates downloaded")
                
                # Small delay between journals
                time.sleep(2)
            
            log_message(log_file, f"  Completed {rank_name}: {rank_templates} templates downloaded")
        
        browser.close()
    
    log_message(log_file, f"\n{'='*80}")
    log_message(log_file, f"Download process completed!")
    log_message(log_file, f"Total templates downloaded: {total_templates}")

if __name__ == '__main__':
    main()
