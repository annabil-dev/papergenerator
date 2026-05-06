#!/usr/bin/env python3
"""
Download journal templates - batch processor.
Reads all source files, extracts template URLs, downloads them organized by department.
"""
import os, re, sys, time, json
import urllib.request, urllib.error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE = "/home/otomasi/papergenerator"
TMPL = os.path.join(BASE, "templates")
TOOL_DIR = "/home/otomasi/.local/share/kilo/tool-output"

# All source files to parse
SOURCES = [
    os.path.join(BASE, "all_journals.md"),
]
# Add tool output files from today's session
for f in os.listdir(TOOL_DIR):
    fp = os.path.join(TOOL_DIR, f)
    if os.path.getmtime(fp) > 1746450000:  # Files from May 6 2026
        SOURCES.append(fp)

def sanitize(name):
    name = re.sub(r'[<>:"/\\|?*\[\]()]', '', name)
    return name.strip()[:80]

def detect_dept(line, current):
    """Detect department from ## header line."""
    dept_map = {
        "Matematika": "Matematika",
        "Biologi": "Biologi", 
        "Kimia": "Kimia",
        "Fisika": "Fisika",
        "Statistika": "Statistika",
        "Informatika": "Informatika",
        "Bioteknologi": "Bioteknologi",
        "Psikologi": "Psikologi",
        "Kesehatan Masyarakat": "Kesehatan_Masyarakat",
        "Keselamatan dan Kesehatan Kerja": "Keselamatan_Kesehatan_Kerja",
        "Kedokteran Gigi": "Kedokteran_Gigi",
        "Kedokteran": "Kedokteran",
        "Keperawatan": "Keperawatan",
        "Gizi": "Gizi",
        "Farmasi": "Farmasi",
        "Peternakan": "Peternakan",
        "Teknologi Pangan": "Teknologi_Pangan",
        "Agribisnis": "Agribisnis",
        "Agroekoteknologi": "Agroekoteknologi",
        "Ilmu Hukum": "Ilmu_Hukum",
        "Manajemen Sumberdaya Perairan": "Manajemen_Sumberdaya_Perairan",
        "Akuakultur": "Akuakultur",
        "Perikanan Tangkap": "Perikanan_Tangkap",
        "Ilmu Kelautan": "Ilmu_Kelautan",
        "Oseanografi": "Oseanografi",
        "Teknologi Hasil Perikanan": "Teknologi_Hasil_Perikanan",
        "Teknologi dan Bisnis Perikanan": "Teknologi_Bisnis_Perikanan",
        "Manajemen": "Manajemen",
        "Ekonomi Pembangunan": "Ekonomi_Pembangunan",
        "Akuntansi Perpajakan": "Akuntansi_Perpajakan",
        "Akuntansi": "Akuntansi",
        "Ekonomi Islam": "Ekonomi_Islam",
        "Bisnis Digital": "Bisnis_Digital",
        "Sastra Indonesia": "Sastra_Indonesia",
        "Sastra Inggris": "Sastra_Inggris",
        "Sejarah": "Sejarah",
        "Ilmu Perpustakaan": "Ilmu_Perpustakaan",
        "Bahasa dan Kebudayaan Jepang": "Bahasa_Jepang",
        "Antropologi Sosial": "Antropologi_Sosial",
        "Administrasi Publik": "Administrasi_Publik",
        "Administrasi Bisnis": "Administrasi_Bisnis",
        "Ilmu Pemerintahan": "Ilmu_Pemerintahan",
        "Ilmu Komunikasi": "Ilmu_Komunikasi",
        "Hubungan Internasional": "Hubungan_Internasional",
        "Teknik Sipil": "Teknik_Sipil",
        "Arsitektur": "Arsitektur",
        "Teknik Mesin": "Teknik_Mesin",
        "Teknik Kimia": "Teknik_Kimia",
        "Teknik Elektro": "Teknik_Elektro",
        "Perencanaan Wilayah dan Kota": "Perencanaan_Wilayah_Kota",
        "Teknik Industri": "Teknik_Industri",
        "Teknik Lingkungan": "Teknik_Lingkungan",
        "Teknik Perkapalan": "Teknik_Perkapalan",
        "Teknik Geologi": "Teknik_Geologi",
        "Teknik Geodesi": "Teknik_Geodesi",
        "Teknik Komputer": "Teknik_Komputer",
        "Teknologi Rekayasa Kimia Industri": "Teknologi_Rekayasa_Kimia",
        "Rekayasa Perancangan Mekanik": "Rekayasa_Mekanik",
        "Teknologi Rekayasa Otomasi": "Teknologi_Otomasi",
        "Teknologi Rekayasa Konstruksi Perkapalan": "Rekayasa_Perkapalan",
        "Teknik Listrik Industri": "Teknik_Listrik_Industri",
        "Perencanaan Tata Ruang": "Perencanaan_Tata_Ruang",
        "Teknik Infrastruktur Sipil": "Teknik_Infrastruktur",
        "Manajemen dan Administrasi Logistik": "Manajemen_Logistik",
        "Bahasa Asing Terapan": "Bahasa_Asing_Terapan",
        "Informasi dan Humas": "Informasi_Humas",
    }
    
    if line.startswith("## ") or line.startswith("**## "):
        for key, folder in dept_map.items():
            if key.lower() in line.lower():
                return folder
    return current

def parse_table_row(line):
    """Parse a markdown table row and extract journal info."""
    if not line.strip().startswith('|'):
        return None
    parts = [p.strip() for p in line.split('|')]
    parts = [p for p in parts if p]  # Remove empty
    
    if len(parts) < 5:
        return None
    
    # Try to find template link (last column with URL)
    template_url = None
    journal_name = None
    q_rank = None
    
    for i, p in enumerate(parts):
        # Extract URLs from markdown links [text](url) or plain URLs
        urls = re.findall(r'https?://[^\s\)]+', p)
        if i == 1:  # Journal name column
            # Remove markdown link formatting
            journal_name = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', p)
            journal_name = journal_name.strip()
        elif i == 2:  # Q rank
            q_rank = p.strip()
    
    # Template link is typically the last URL-containing column
    for p in reversed(parts):
        urls = re.findall(r'https?://[^\s\)]+', p)
        if urls:
            template_url = urls[0]
            break
    
    # Actually we need the LAST column specifically for template
    if len(parts) >= 6:
        last_urls = re.findall(r'https?://[^\s\)]+', parts[-1])
        if last_urls:
            template_url = last_urls[0]
    
    if journal_name and template_url and q_rank:
        # Skip header rows
        if 'Journal Name' in journal_name or '---' in journal_name:
            return None
        return {
            'name': journal_name,
            'q_rank': q_rank,
            'template_url': template_url
        }
    return None

def extract_all_journals():
    """Extract all journals from all source files."""
    all_journals = []
    
    for src in SOURCES:
        if not os.path.exists(src):
            continue
        try:
            with open(src, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
        except:
            continue
        
        current_dept = "Uncategorized"
        for line in lines:
            new_dept = detect_dept(line, current_dept)
            if new_dept != current_dept:
                current_dept = new_dept
            
            info = parse_table_row(line)
            if info:
                info['dept'] = current_dept
                all_journals.append(info)
    
    return all_journals

def download_one(url, filepath):
    """Download single file."""
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            # Check content type
            ct = resp.headers.get('Content-Type', '')
            if 'pdf' in ct:
                ext = '.pdf'
            elif 'word' in ct or 'docx' in ct:
                ext = '.docx'
            elif 'html' in ct:
                ext = '.html'
            else:
                ext = '.pdf'
            
            # Rename with correct extension if needed
            base = os.path.splitext(filepath)[0]
            filepath = base + ext
            
            with open(filepath, 'wb') as f:
                f.write(data)
            return True, filepath, len(data)
    except Exception as e:
        return False, filepath, str(e)

def main():
    print("Extracting journals from all sources...")
    journals = extract_all_journals()
    print(f"Total journals found: {len(journals)}")
    
    # Deduplicate by (dept, name)
    seen = set()
    unique = []
    for j in journals:
        key = (j['dept'], j['name'])
        if key not in seen:
            seen.add(key)
            unique.append(j)
    
    print(f"Unique journals: {len(unique)}")
    
    # Group by dept
    by_dept = {}
    for j in unique:
        d = j['dept']
        if d not in by_dept:
            by_dept[d] = []
        by_dept[d].append(j)
    
    print(f"Departments: {len(by_dept)}")
    for d, jl in sorted(by_dept.items()):
        print(f"  {d}: {len(jl)} journals")
    
    # Save journal list as JSON for reference
    with open(os.path.join(BASE, "journal_list.json"), 'w') as f:
        json.dump(unique, f, indent=2, ensure_ascii=False)
    print(f"\nSaved journal_list.json")
    
    # Download templates
    total = 0
    success = 0
    failed = []
    
    for dept, jlist in sorted(by_dept.items()):
        dept_folder = os.path.join(TMPL, dept)
        os.makedirs(dept_folder, exist_ok=True)
        
        print(f"\n{'='*60}")
        print(f"Department: {dept} ({len(jlist)} journals)")
        print(f"{'='*60}")
        
        for idx, j in enumerate(jlist, 1):
            total += 1
            name = sanitize(j['name'])
            q = j['q_rank'].replace('/', '-')
            filename = f"{name}({q})"
            filepath = os.path.join(dept_folder, filename + ".pdf")
            
            # Skip if any version exists
            existing = [f for f in os.listdir(dept_folder) if f.startswith(name[:30])]
            if existing:
                success += 1
                continue
            
            ok, fpath, result = download_one(j['template_url'], filepath)
            if ok:
                print(f"  [{idx}] OK: {name} ({result} bytes)")
                success += 1
            else:
                print(f"  [{idx}] FAIL: {name} - {result}")
                failed.append(j)
            
            time.sleep(0.3)
    
    print(f"\n{'='*60}")
    print(f"DOWNLOAD SUMMARY")
    print(f"{'='*60}")
    print(f"Total: {total}")
    print(f"Success: {success}")
    print(f"Failed: {len(failed)}")
    
    # Save failed list
    if failed:
        with open(os.path.join(BASE, "failed_downloads.json"), 'w') as f:
            json.dump(failed, f, indent=2, ensure_ascii=False)
        print(f"Failed list saved to failed_downloads.json")

if __name__ == "__main__":
    main()
