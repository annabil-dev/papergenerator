import json, re
with open('output/20260227_005756_Real_Time_LiDAR_SLAM_with_Reinforcement_Learning_P.json', encoding='utf-8') as f:
    paper = json.load(f)

def count_paras(content):
    if not content:
        return 0
    blocks = re.split(r'(\$\$[^$]+?\$\$)', content)
    n = 0
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        if block.startswith("$$") and block.endswith("$$"):
            n += 1
        else:
            for para in re.split(r'\n{2,}', block):
                para = para.strip()
                if not para:
                    continue
                if "•" in para:
                    n += para.count("•") + 1
                else:
                    for line in para.split("\n"):
                        if line.strip():
                            n += 1
    return n

total = 0
for section in paper.get('sections', []):
    n = count_paras(section.get('content',''))
    print(f"Sec {section['number']}: {n}")
    total += n
    for sub in section.get('subsections', []):
        sn = count_paras(sub.get('content',''))
        print(f"  Sub {sub['letter']}: {sn}")
        total += sn
print(f"TOTAL expected: {total}")
