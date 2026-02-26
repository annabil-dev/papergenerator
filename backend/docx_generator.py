"""
IEEE Conference Paper DOCX Generator
=====================================
Generates DOCX files that match IEEE two-column conference paper format.
Matches the format of the reference PDF exactly.
"""

import os
import re
import copy
from pathlib import Path
from typing import Optional

from docx import Document
from docx.shared import Pt, Inches, Cm, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml


def generate_ieee_docx(paper: dict, output_path: str, images_dir: str = "uploads"):
    """
    Generate IEEE conference paper DOCX from paper data.
    
    Args:
        paper: Paper data dict with title, authors, abstract, sections, references, etc.
        output_path: Path to save the DOCX file.
        images_dir: Directory where uploaded images are stored.
    """
    doc = Document()
    
    # ── Page Setup (IEEE Letter: 8.5 x 11 inches) ────────────────────────────
    section = doc.sections[0]
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.top_margin = Inches(0.75)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(0.625)
    section.right_margin = Inches(0.625)
    
    # Two-column layout
    sectPr = section._sectPr
    cols = parse_xml(f'<w:cols {nsdecls("w")} w:num="2" w:space="340"/>')
    sectPr.append(cols)
    
    # ── Default font setup ────────────────────────────────────────────────────
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(10)
    style.paragraph_format.space_before = Pt(0)
    style.paragraph_format.space_after = Pt(0)
    style.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
    
    # Set East Asian font
    rPr = style.element.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = parse_xml(f'<w:rFonts {nsdecls("w")} w:eastAsia="Times New Roman"/>')
        rPr.append(rFonts)
    else:
        rFonts.set(qn('w:eastAsia'), 'Times New Roman')
    
    # ── Title ─────────────────────────────────────────────────────────────────
    title = paper.get("title", "Untitled Paper")
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(12)
    run = p.add_run(title)
    run.bold = True
    run.font.size = Pt(24)
    run.font.name = 'Times New Roman'
    
    # ── Authors ───────────────────────────────────────────────────────────────
    authors = paper.get("authors", [])
    if authors:
        # Author names
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        
        for i, author in enumerate(authors):
            name = author.get("name", "")
            if i > 0:
                run = p.add_run("\n")
            run = p.add_run(name)
            run.font.size = Pt(11)
            run.font.name = 'Times New Roman'
            
            # Affiliation
            affiliation = author.get("affiliation", "")
            if affiliation:
                run = p.add_run(f"\n{affiliation}")
                run.font.size = Pt(10)
                run.font.name = 'Times New Roman'
                run.italic = True
            
            # Location
            location = author.get("location", "")
            if location:
                run = p.add_run(f"\n{location}")
                run.font.size = Pt(10)
                run.font.name = 'Times New Roman'
                run.italic = True
            
            # Email
            email = author.get("email", "")
            if email:
                run = p.add_run(f"\ne-mail: {email}")
                run.font.size = Pt(10)
                run.font.name = 'Times New Roman'
                run.italic = True
            
            if i < len(authors) - 1:
                run = p.add_run("\n")
        
        p.paragraph_format.space_after = Pt(12)
    
    # ── Abstract ──────────────────────────────────────────────────────────────
    abstract = paper.get("abstract", "")
    if abstract:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(6)
        
        # "Abstract—" bold italic
        run = p.add_run("Abstract\u2014")
        run.bold = True
        run.italic = True
        run.font.size = Pt(9)
        run.font.name = 'Times New Roman'
        
        # Abstract text italic
        run = p.add_run(abstract)
        run.italic = True
        run.font.size = Pt(9)
        run.font.name = 'Times New Roman'
    
    # ── Keywords ──────────────────────────────────────────────────────────────
    keywords = paper.get("keywords", [])
    if keywords:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(12)
        
        run = p.add_run("Keywords\u2014")
        run.bold = True
        run.italic = True
        run.font.size = Pt(9)
        run.font.name = 'Times New Roman'
        
        run = p.add_run(", ".join(keywords))
        run.italic = True
        run.font.size = Pt(9)
        run.font.name = 'Times New Roman'
    
    # ── Sections ──────────────────────────────────────────────────────────────
    sections = paper.get("sections", [])
    for sec in sections:
        _add_section(doc, sec, images_dir, paper)
    
    # ── Acknowledgment ────────────────────────────────────────────────────────
    ack = paper.get("acknowledgment", "")
    if ack:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run("ACKNOWLEDGMENT")
        run.bold = True
        run.font.size = Pt(10)
        run.font.name = 'Times New Roman'
        
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.first_line_indent = Inches(0.25)
        run = p.add_run(ack)
        run.font.size = Pt(10)
        run.font.name = 'Times New Roman'
    
    # ── References ────────────────────────────────────────────────────────────
    references = paper.get("references", [])
    if references:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(6)
        run = p.add_run("REFERENCES")
        run.bold = True
        run.font.size = Pt(10)
        run.font.name = 'Times New Roman'
        
        for ref in references:
            ref_id = ref.get("id", "")
            ref_text = ref.get("text", "")
            
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(1)
            p.paragraph_format.left_indent = Inches(0.25)
            p.paragraph_format.first_line_indent = Inches(-0.25)
            
            # Reference number
            run = p.add_run(f"[{ref_id}]")
            run.font.size = Pt(8)
            run.font.name = 'Times New Roman'
            
            # Tab
            run = p.add_run("\t")
            
            # Reference text
            run = p.add_run(ref_text)
            run.font.size = Pt(8)
            run.font.name = 'Times New Roman'
    
    # ── Save ──────────────────────────────────────────────────────────────────
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
    doc.save(output_path)
    print(f"✅ DOCX saved to: {output_path}")
    return output_path


def _add_section(doc, section: dict, images_dir: str, paper: dict):
    """Add a main section (Roman numeral heading) to the document."""
    number = section.get("number", "")
    title = section.get("title", "")
    content = section.get("content", "")
    subsections = section.get("subsections", [])
    
    # Section heading: "I. INTRODUCTION" style
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(6)
    
    heading_text = f"{number}. {title.upper()}" if number else title.upper()
    run = p.add_run(heading_text)
    run.bold = True
    run.font.size = Pt(10)
    run.font.name = 'Times New Roman'
    
    # Section content
    if content:
        _add_content_paragraphs(doc, content, images_dir, paper)
    
    # Subsections
    for sub in subsections:
        _add_subsection(doc, sub, images_dir, paper)


def _add_subsection(doc, subsection: dict, images_dir: str, paper: dict):
    """Add a subsection (letter heading) to the document."""
    letter = subsection.get("letter", "")
    title = subsection.get("title", "")
    content = subsection.get("content", "")
    numbered_items = subsection.get("numberedItems", [])
    
    # Subsection heading: "A. Regional Selection of Interest" style
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(3)
    
    heading_text = f"{letter}. {title}" if letter else title
    run = p.add_run(heading_text)
    run.bold = True
    run.italic = True
    run.font.size = Pt(10)
    run.font.name = 'Times New Roman'
    
    # Content
    if content:
        _add_content_paragraphs(doc, content, images_dir, paper)
    
    # Numbered items (like "1) Weak Classifier Design")
    for item in numbered_items:
        item_number = item.get("number", "")
        item_title = item.get("title", "")
        item_content = item.get("content", "")
        
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        
        heading_text = f"{item_number}) {item_title}" if item_number else item_title
        run = p.add_run(heading_text)
        run.bold = True
        run.italic = True
        run.font.size = Pt(10)
        run.font.name = 'Times New Roman'
        
        if item_content:
            _add_content_paragraphs(doc, item_content, images_dir, paper)


def _add_content_paragraphs(doc, content: str, images_dir: str, paper: dict):
    """Add content text as paragraphs, handling inline formulas and references."""
    # Split by double newlines for paragraphs
    paragraphs = content.split("\n\n") if "\n\n" in content else [content]
    
    for para_text in paragraphs:
        para_text = para_text.strip()
        if not para_text:
            continue
        
        # Check if it's a figure reference
        if para_text.startswith("[FIGURE:"):
            _add_figure(doc, para_text, images_dir, paper)
            continue
        
        # Check if it's a table reference
        if para_text.startswith("[TABLE:"):
            _add_table(doc, para_text, paper)
            continue
        
        # Check if it's a display equation
        if para_text.startswith("$$") and para_text.endswith("$$"):
            _add_equation(doc, para_text[2:-2].strip(), paper)
            continue
        
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.first_line_indent = Inches(0.25)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2)
        
        # Parse inline formulas and references
        _add_formatted_text(p, para_text)


def _add_formatted_text(paragraph, text: str):
    """Add text to paragraph with inline formula and reference formatting."""
    # Pattern for inline math $...$, bold **...**, italic *...*
    parts = re.split(r'(\$[^$]+\$|\*\*[^*]+\*\*|\*[^*]+\*|\[[0-9,\s\-–]+\])', text)
    
    for part in parts:
        if not part:
            continue
        
        if part.startswith('$') and part.endswith('$'):
            # Inline math - render as italic
            formula = part[1:-1]
            run = paragraph.add_run(formula)
            run.italic = True
            run.font.size = Pt(10)
            run.font.name = 'Times New Roman'
        elif part.startswith('**') and part.endswith('**'):
            # Bold text
            run = paragraph.add_run(part[2:-2])
            run.bold = True
            run.font.size = Pt(10)
            run.font.name = 'Times New Roman'
        elif part.startswith('*') and part.endswith('*') and not part.startswith('**'):
            # Italic text
            run = paragraph.add_run(part[1:-1])
            run.italic = True
            run.font.size = Pt(10)
            run.font.name = 'Times New Roman'
        elif re.match(r'\[[0-9,\s\-–]+\]', part):
            # Citation reference [1], [1,2], [1-3]
            run = paragraph.add_run(part)
            run.font.size = Pt(10)
            run.font.name = 'Times New Roman'
        else:
            # Normal text
            run = paragraph.add_run(part)
            run.font.size = Pt(10)
            run.font.name = 'Times New Roman'


def _add_equation(doc, latex: str, paper: dict):
    """Add a display equation."""
    equations = paper.get("equations", [])
    eq_num = ""
    for eq in equations:
        if eq.get("latex", "").strip() == latex.strip():
            eq_num = str(eq.get("number", ""))
            break
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(6)
    
    # Formula text (italic)
    run = p.add_run(latex)
    run.italic = True
    run.font.size = Pt(10)
    run.font.name = 'Times New Roman'
    
    # Equation number
    if eq_num:
        run = p.add_run(f"    ({eq_num})")
        run.font.size = Pt(10)
        run.font.name = 'Times New Roman'


def _add_figure(doc, figure_ref: str, images_dir: str, paper: dict):
    """Add a figure with caption."""
    # Parse figure reference: [FIGURE:figure-id]
    match = re.match(r'\[FIGURE:([^\]]+)\]', figure_ref)
    if not match:
        return
    
    fig_id = match.group(1).strip()
    figures = paper.get("figures", [])
    figure = None
    for f in figures:
        if f.get("id") == fig_id:
            figure = f
            break
    
    if not figure:
        return
    
    # Figure paragraph (centered)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(3)
    
    # Try to add image
    filename = figure.get("filename", "")
    if filename:
        img_path = os.path.join(images_dir, filename)
        if os.path.exists(img_path):
            run = p.add_run()
            run.add_picture(img_path, width=Inches(3.0))
    
    # Caption: "Fig. 1. Caption text"
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(6)
    
    caption = figure.get("caption", "")
    run = p.add_run(caption)
    run.font.size = Pt(8)
    run.font.name = 'Times New Roman'


def _add_table(doc, table_ref: str, paper: dict):
    """Add a table with caption."""
    match = re.match(r'\[TABLE:([^\]]+)\]', table_ref)
    if not match:
        return
    
    tbl_id = match.group(1).strip()
    tables = paper.get("tables", [])
    table_data = None
    for t in tables:
        if t.get("id") == tbl_id:
            table_data = t
            break
    
    if not table_data:
        return
    
    # Table caption (centered, above table)
    caption = table_data.get("caption", "")
    if caption:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(3)
        run = p.add_run(caption)
        run.bold = True
        run.font.size = Pt(8)
        run.font.name = 'Times New Roman'
    
    # Create table
    headers = table_data.get("headers", [])
    rows = table_data.get("rows", [])
    
    if not headers:
        return
    
    num_cols = len(headers)
    table = doc.add_table(rows=1 + len(rows), cols=num_cols)
    table.style = 'Table Grid'
    table.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Header row
    for i, header in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = ""
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(header)
        run.bold = True
        run.font.size = Pt(8)
        run.font.name = 'Times New Roman'
    
    # Data rows
    for r_idx, row in enumerate(rows):
        for c_idx, val in enumerate(row):
            if c_idx < num_cols:
                cell = table.rows[r_idx + 1].cells[c_idx]
                cell.text = ""
                p = cell.paragraphs[0]
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                run = p.add_run(str(val))
                run.font.size = Pt(8)
                run.font.name = 'Times New Roman'


# ── Bullet/List support ──────────────────────────────────────────────────────

def _add_bullet_list(doc, items: list):
    """Add a bulleted list."""
    for item in items:
        p = doc.add_paragraph()
        p.style = 'List Bullet'
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(1)
        p.paragraph_format.left_indent = Inches(0.5)
        
        run = p.add_run(item)
        run.font.size = Pt(10)
        run.font.name = 'Times New Roman'


if __name__ == "__main__":
    # Test with sample data
    sample_paper = {
        "title": "Lane Detection Algorithm Based on Haar Feature Based Coupled Cascade Classifier",
        "authors": [
            {
                "name": "Hongyu Zhou",
                "affiliation": "School of Computer and Information Engineering\nAnyang Normal University",
                "location": "Anyang, China",
                "email": "zhouhongyupear@163.com"
            },
            {
                "name": "Xu Song",
                "affiliation": "School of Computer and Information Engineering\nAnyang Normal University",
                "location": "Anyang, China",
                "email": "songxu518@126.com"
            }
        ],
        "abstract": "To improve the accuracy of lane detection in complex environment, The lane detection algorithm based on Haar feature coupled cascade classifier was proposed.",
        "keywords": ["Lane detection", "Haar feature", "Machine learning", "Lane fitting", "Cascade classifier"],
        "sections": [
            {
                "id": "intro",
                "number": "I",
                "title": "INTRODUCTION",
                "content": "Currently, lane detection methods can be roughly classified as feature-based method [1,2], region-based method [3-6] and model-based method [7,8].",
                "subsections": []
            }
        ],
        "references": [
            {"id": 1, "text": "Z. J. Yang, \"Structured Road Lane Detection Based on RGB Color Channel,\" Electronic technology, vol. 28, no. 1, pp. 95-98, 2015."}
        ],
        "figures": [],
        "tables": [],
        "equations": []
    }
    
    generate_ieee_docx(sample_paper, "test_output.docx")
