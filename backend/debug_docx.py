import json, re, generate_docx_from_json as g
from docx import Document

with open('output/20260227_005756_Real_Time_LiDAR_SLAM_with_Reinforcement_Learning_P.json',encoding='utf-8') as f:
    paper = json.load(f)

# Try converting a formula via latex2mathml + XSLT
import latex2mathml.converter
from lxml import etree

doc = Document()
p = doc.add_paragraph()
formula = r'\hat{\mathbf{P}}_t'
print(f"Testing formula: {formula}")

# Check what latex2mathml produces
mathml = latex2mathml.converter.convert(formula)
print(f"MathML output ({len(mathml)} chars):")
print(mathml[:500])

# Check XSLT transform
transform = g._get_omml_transform()
print(f"\nXSLT transform loaded: {transform is not None}")
if transform:
    mml_el = etree.fromstring(mathml.encode('utf-8'))
    omml_tree = transform(mml_el)
    root = omml_tree.getroot()
    print(f"OMML root tag: {root.tag}")
    omml_str = etree.tostring(root, pretty_print=True).decode('utf-8')
    print(f"OMML output ({len(omml_str)} chars):")
    print(omml_str[:1000])
    # Count w:p elements in OMML output
    wp_count = omml_str.count('<w:p')
    print(f"\nw:p elements in OMML: {wp_count}")


# Load paper
with open('output/20260227_005756_Real_Time_LiDAR_SLAM_with_Reinforcement_Learning_P.json',encoding='utf-8') as f:
    paper = json.load(f)

doc = Document()

def count_p(doc):
    return len(doc.paragraphs)

# Simulate what generate_ieee_docx does, step by step
print(f"Start: {count_p(doc)} paras")

# Title
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.add_run(paper['title'])
print(f"After title: {count_p(doc)} paras")

# Authors
doc.add_paragraph()
print(f"After authors: {count_p(doc)} paras")

# Abstract + keywords
doc.add_paragraph()
doc.add_paragraph()
print(f"After abstract/keywords: {count_p(doc)} paras")

# Now test _add_content_paragraphs on the intro content
intro_content = paper['sections'][0]['content']
print(f"\nIntro content length: {len(intro_content)} chars")
print(f"Bullet count in intro: {intro_content.count(chr(8226))}")  # •

# Test splitting
blocks = re.split(r'(\$\$[^$]+?\$\$)', intro_content, flags=re.DOTALL)
print(f"Blocks after $$ split: {len(blocks)}")
for i, b in enumerate(blocks):
    b_s = b.strip()
    if b_s.startswith('$$'):
        print(f"  Block {i}: DISPLAY EQ, len={len(b_s)}")
    else:
        para_count = 0
        for para in re.split(r'\n{2,}', b_s):
            if para.strip():
                para_count += 1
        print(f"  Block {i}: {para_count} para(s), has_bullet={'•' in b_s}, len={len(b_s)}")

# Now actually run add_content_paragraphs but with instrumentation
# Patch the bullet regex to print what it's splitting
import generate_docx_from_json as g

orig_add_paragraph = doc.add_paragraph.__class__
para_count_before = count_p(doc)
g._add_content_paragraphs(doc, intro_content, '.', paper)
para_count_after = count_p(doc)
print(f"\nParas added by _add_content_paragraphs on intro: {para_count_after - para_count_before}")
print(f"Total paras now: {para_count_after}")


