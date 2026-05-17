#!/usr/bin/env python3
"""
Process S5 and S6 journals - Robust version v3
- Handles signals gracefully
- Saves progress frequently
- Can resume from where it left off
"""

import json
import os
import re
import time
import sys
import signal
from datetime import datetime
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup

JSON_FILE = "/home/otomasi/papergenerator/sinta_all_journals.json"
PROGRESS_FILE = "/home/otomasi/papergenerator/.s5_s6_progress.json"
S5_LOG = "/home/otomasi/papergenerator/template/jurnal sinta/S5/all_journals_log.txt"
S6_LOG = "/home/otomasi/papergenerator/template/jurnal sinta/S6/all_journals_log.txt"
S5_DIR = "/home/otomasi/papergenerator/template/jurnal sinta/S5"
S6_DIR = "/home/otomasi/papergenerator/template/jurnal sinta/S6"

# Global
should_stop = False

def signal_handler(signum, frame):
    global should_stop
    print(f"\n[{datetime.now()}] Signal received, will stop after current journal...", flush=True)
    should_stop = True

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

def log(msg, log_file=None):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    if log_file:
        try:
            with open(log_file, 'a') as f:
                f.write(line + "\n")
                f.flush()
        except:
            pass

def sanitize(name):
    return re.sub(r'[<>:"/\\|?*]', '_', name).strip('_')[:200]

def load_progress():
    try:
        with open(PROGRESS_FILE, 'r') as f:
            return json.load(f)
    except:
        return {"s5": 0, "s6": 0}

def save_progress(s5_idx, s6_idx):
    try:
        with open(PROGRESS_FILE, 'w') as f:
            json.dump({"s5": s5_idx, "s6": s6_idx}, f)
    except:
        pass

def save_json(data):
    try:
        with open(JSON_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        log(f"Error saving JSON: {e}")

def get_website(profile_url):
    try:
        r = requests.get(profile_url, 
                        headers={'User-Agent': 'Mozilla/5.0'}, 
                        timeout=30)
        soup = BeautifulSoup(r.text, 'html.parser')
        for a in soup.find_all('a', href=True):
            href = a['href']
            if href.startswith('http') and 'sinta' not in href:
                return href
    except Exception as e:
        log(f"Error getting website from profile: {e}")
    return None

def find_template(website_url):
    try:
        r = requests.get(website_url,
                        headers={'User-Agent': 'Mozilla/5.0'},
                        timeout=30)
        soup = BeautifulSoup(r.text, 'html.parser')
        for a in soup.find_all('a', href=True):
            href = a['href']
            text = a.get_text().lower()
            if any(x in href.lower() for x in ['.doc', '.docx', '.pdf']):
                return href, os.path.basename(urlparse(href).path)
            if any(x in text for x in ['template', 'guideline', 'author']) and 'download' in text:
                return href, os.path.basename(urlparse(href).path) or 'template'
    except Exception as e:
        log(f"Error finding template: {e}")
    return None, None

def download(url, path):
    try:
        r = requests.get(url,
                        headers={'User-Agent': 'Mozilla/5.0'},
                        timeout=60)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'wb') as f:
            f.write(r.content)
        return True
    except Exception as e:
        log(f"Error downloading: {e}")
        return False

def process():
    global should_stop
    
    log("Loading JSON...")
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    s5 = [j for j in data['journals'] if j['sinta_rank'] == 'S5']
    s6 = [j for j in data['journals'] if j['sinta_rank'] == 'S6']
    
    log(f"S5: {len(s5)}, S6: {len(s6)}")
    
    prog = load_progress()
    s5_idx = prog.get('s5', 0)
    s6_idx = prog.get('s6', 0)
    
    log(f"Resuming from S5={s5_idx}, S6={s6_idx}")
    
    # Process S5
    log("=" * 60)
    log("PROCESSING S5")
    log("=" * 60)
    
    for i in range(s5_idx, len(s5)):
        if should_stop:
            break
        
        j = s5[i]
        name = j.get('name', 'Unknown')
        log(f"[{i+1}/{len(s5)}] {name}", S5_LOG)
        
        # Init fields
        if not j.get('website_url'):
            j['website_url'] = None
        if not j.get('template_url'):
            j['template_url'] = None
        if not j.get('template_downloaded'):
            j['template_downloaded'] = False
        
        # Get website
        if not j['website_url']:
            log(f"  Getting website...", S5_LOG)
            url = get_website(j['profile_url'])
            if url:
                j['website_url'] = url
                log(f"  Found: {url}", S5_LOG)
                time.sleep(1)
            else:
                log(f"  No website found", S5_LOG)
                save_progress(i + 1, s6_idx)
                continue
        
        # Find template
        if not j['template_downloaded']:
            log(f"  Finding template...", S5_LOG)
            tpl_url, tpl_name = find_template(j['website_url'])
            if tpl_url:
                j['template_url'] = tpl_url
                if not tpl_name:
                    tpl_name = f"template_{sanitize(name)}.docx"
                path = os.path.join(S5_DIR, sanitize(tpl_name))
                log(f"  Downloading...", S5_LOG)
                if download(tpl_url, path):
                    j['template_downloaded'] = True
                    j['template_filename'] = os.path.basename(path)
                    log(f"  Downloaded: {path}", S5_LOG)
                else:
                    j['template_downloaded'] = False
                time.sleep(2)
            else:
                log(f"  No template found", S5_LOG)
        
        # Save progress every 5 journals
        if (i + 1) % 5 == 0:
            save_progress(i + 1, s6_idx)
            save_json(data)
            log(f"  Progress saved: S5={i+1}/{len(s5)}")
    
    s5_done = len(s5) if should_stop else s5_idx
    
    # Process S6
    if not should_stop:
        log("=" * 60)
        log("PROCESSING S6")
        log("=" * 60)
        
        for i in range(s6_idx, len(s6)):
            if should_stop:
                break
            
            j = s6[i]
            name = j.get('name', 'Unknown')
            log(f"[{i+1}/{len(s6)}] {name}", S6_LOG)
            
            # Init fields
            if not j.get('website_url'):
                j['website_url'] = None
            if not j.get('template_url'):
                j['template_url'] = None
            if not j.get('template_downloaded'):
                j['template_downloaded'] = False
            
            # Get website
            if not j['website_url']:
                log(f"  Getting website...", S6_LOG)
                url = get_website(j['profile_url'])
                if url:
                    j['website_url'] = url
                    log(f"  Found: {url}", S6_LOG)
                    time.sleep(1)
                else:
                    log(f"  No website found", S6_LOG)
                    save_progress(len(s5), i + 1)
                    continue
            
            # Find template
            if not j['template_downloaded']:
                log(f"  Finding template...", S6_LOG)
                tpl_url, tpl_name = find_template(j['website_url'])
                if tpl_url:
                    j['template_url'] = tpl_url
                    if not tpl_name:
                        tpl_name = f"template_{sanitize(name)}.docx"
                    path = os.path.join(S6_DIR, sanitize(tpl_name))
                    log(f"  Downloading...", S6_LOG)
                    if download(tpl_url, path):
                        j['template_downloaded'] = True
                        j['template_filename'] = os.path.basename(path)
                        log(f"  Downloaded: {path}", S6_LOG)
                    else:
                        j['template_downloaded'] = False
                    time.sleep(2)
                else:
                    log(f"  No template found", S6_LOG)
            
            # Save progress every 5 journals
            if (i + 1) % 5 == 0:
                save_progress(len(s5), i + 1)
                save_json(data)
                log(f"  Progress saved: S6={i+1}/{len(s6)}")
    
    # Final save
    save_json(data)
    
    # Remove progress file if complete
    if not should_stop and s5_idx >= len(s5) and s6_idx >= len(s6):
        try:
            os.remove(PROGRESS_FILE)
        except:
            pass
    
    log("=" * 60)
    log("DONE" if not should_stop else "STOPPED")
    log("=" * 60)

if __name__ == '__main__':
    process()
