"""
IEEE Conference Paper DOCX Generator
=====================================
Generates DOCX files that match IEEE two-column conference paper format.
Supports Word-native OMML math via MML2OMML.XSL (bundled or auto-detected).

MML2OMML.XSL is searched in this order:
  1. Same directory as this script  (bundle it next to the .py)
  2. Common Microsoft Office installation paths on Windows
  3. Graceful fallback: LaTeX rendered as italic plain text
"""

import os
import re
import sys
from pathlib import Path

from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml

#  Dynamic MML2OMML.XSL discovery 
_M_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"
_omml_transform = None   # cached; False = tried + failed


def _find_mml2omml_xsl():
    """Return the path to MML2OMML.XSL, or None if not found."""
    # 1. Bundled next to this script
    bundled = Path(__file__).parent / "MML2OMML.XSL"
    if bundled.exists():
        return str(bundled)
    # 2. Typical Windows Office paths (any version / Click-to-Run / MSI)
    candidate_roots = [
        Path(os.environ.get("ProgramFiles", r"C:\Program Files")),
        Path(os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")),
    ]
    office_sub_patterns = [
        "Microsoft Office/root/Office16",
        "Microsoft Office/root/Office15",
        "Microsoft Office/Office16",
        "Microsoft Office/Office15",
        "Microsoft Office/root",
    ]
    for root in candidate_roots:
        for sub in office_sub_patterns:
            p = root / sub / "MML2OMML.XSL"
            if p.exists():
                return str(p)
    return None


def _get_omml_transform():
    """Load and cache the XSLT transform. Returns transform or None."""
    global _omml_transform
    if _omml_transform is not None:
        return _omml_transform if _omml_transform is not False else None
    try:
        from lxml import etree
        xsl_path = _find_mml2omml_xsl()
        if xsl_path:
            xslt_doc = etree.parse(xsl_path)
            _omml_transform = etree.XSLT(xslt_doc)
            return _omml_transform
    except Exception:
        pass
    _omml_transform = False
    return None


def _latex_to_omml_el(latex: str):
    """Convert LaTeX string -> lxml oMath element (OMML). Returns None on failure."""
    try:
        import latex2mathml.converter
        from lxml import etree
        transform = _get_omml_transform()
        if transform is None:
            return None
        mathml_str = latex2mathml.converter.convert(latex)
        try:
            mml_el = etree.fromstring(mathml_str.encode("utf-8"))
        except etree.XMLSyntaxError:
            return None
        omml_tree = transform(mml_el)
        return omml_tree.getroot()
    except Exception:
        return None


def _insert_display_eq(doc, latex: str, eq_num: str = ""):
    """Add a centred display equation paragraph using Word OMML."""
    from lxml import etree
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(6)
    el = _latex_to_omml_el(latex)
    if el is not None:
        local = el.tag.split("}")[-1] if "}" in el.tag else el.tag
        if local == "oMath":
            omml_para = etree.fromstring(
                f'<m:oMathPara xmlns:m="{_M_NS}"><m:oMathParaPr>'
                f'<m:jc m:val="center"/></m:oMathParaPr></m:oMathPara>'
            )
            omml_para.append(el)
            p._p.append(omml_para)
        elif local == "oMathPara":
            p._p.append(el)
        else:
            p._p.append(el)
    else:
        run = p.add_run(latex)
        run.italic = True
        run.font.size = Pt(10)
        run.font.name = "Times New Roman"
    if eq_num:
        tab_run = p.add_run(f"    ({eq_num})")
        tab_run.font.size = Pt(10)
        tab_run.font.name = "Times New Roman"
    return p


def _append_inline_eq(paragraph, latex: str) -> bool:
    """Append inline equation as OMML. Returns True on success."""
    from lxml import etree
    el = _latex_to_omml_el(latex)
    if el is not None:
        local = el.tag.split("}")[-1] if "}" in el.tag else el.tag
        if local == "oMath":
            paragraph._p.append(el)
        else:
            omath = etree.fromstring(f'<m:oMath xmlns:m="{_M_NS}"/>')
            omath.append(el)
            paragraph._p.append(omath)
        return True
    return False


#  Public API 

def generate_ieee_docx(paper: dict, output_path: str, images_dir: str = "uploads") -> str:
    """
    Generate IEEE conference paper DOCX from paper data.

    Args:
        paper:       Paper dict (title, authors, abstract, keywords, sections,
                     acknowledgment, references, figures, tables, equations).
        output_path: Target .docx path.
        images_dir:  Directory containing uploaded images.

    Returns:
        output_path (str)
    """
    doc = Document()

    #  Page setup (IEEE Letter 8.5x11 in) 
    sec = doc.sections[0]
    sec.page_width  = Inches(8.5)
    sec.page_height = Inches(11)
    sec.top_margin    = Inches(0.75)
    sec.bottom_margin = Inches(1.0)
    sec.left_margin   = Inches(0.625)
    sec.right_margin  = Inches(0.625)

    cols_xml = parse_xml(f'<w:cols {nsdecls("w")} w:num="2" w:space="340"/>')
    sec._sectPr.append(cols_xml)

    #  Default style 
    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(10)
    normal.paragraph_format.space_before = Pt(0)
    normal.paragraph_format.space_after  = Pt(0)
    normal.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE

    rPr = normal.element.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = parse_xml(f'<w:rFonts {nsdecls("w")} w:eastAsia="Times New Roman"/>')
        rPr.append(rFonts)
    else:
        rFonts.set(qn("w:eastAsia"), "Times New Roman")

    #  Title 
    title_text = paper.get("title", "Untitled Paper")
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after  = Pt(12)
    run = p.add_run(title_text)
    run.bold = True
    run.font.size = Pt(24)
    run.font.name = "Times New Roman"

    #  Authors 
    authors = paper.get("authors", [])
    if authors:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after  = Pt(12)
        for i, author in enumerate(authors):
            if i > 0:
                p.add_run("\n")
            r = p.add_run(author.get("name", ""))
            r.font.size = Pt(11); r.font.name = "Times New Roman"
            for field in ("affiliation", "location"):
                val = author.get(field, "")
                if val:
                    r = p.add_run(f"\n{val}")
                    r.font.size = Pt(10); r.font.name = "Times New Roman"; r.italic = True
            email = author.get("email", "")
            if email:
                r = p.add_run(f"\ne-mail: {email}")
                r.font.size = Pt(10); r.font.name = "Times New Roman"; r.italic = True

    #  Abstract 
    abstract = paper.get("abstract", "")
    if abstract:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after  = Pt(6)
        r = p.add_run("Abstract\u2014")
        r.bold = True; r.italic = True; r.font.size = Pt(9); r.font.name = "Times New Roman"
        r = p.add_run(abstract)
        r.italic = True; r.font.size = Pt(9); r.font.name = "Times New Roman"

    #  Keywords 
    keywords = paper.get("keywords", [])
    if keywords:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after  = Pt(12)
        r = p.add_run("Keywords\u2014")
        r.bold = True; r.italic = True; r.font.size = Pt(9); r.font.name = "Times New Roman"
        r = p.add_run(", ".join(keywords))
        r.italic = True; r.font.size = Pt(9); r.font.name = "Times New Roman"

    #  Sections 
    for section in paper.get("sections", []):
        _add_section(doc, section, images_dir, paper)

    #  Acknowledgment 
    ack = paper.get("acknowledgment", "")
    if ack:
        _section_heading(doc, "ACKNOWLEDGMENT")
        _body_paragraph(doc, ack)

    #  References 
    refs = paper.get("references", [])
    if refs:
        _section_heading(doc, "REFERENCES")
        for ref in refs:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after  = Pt(1)
            p.paragraph_format.left_indent       = Inches(0.25)
            p.paragraph_format.first_line_indent = Inches(-0.25)
            r = p.add_run(f"[{ref.get('id', '')}]\t")
            r.font.size = Pt(8); r.font.name = "Times New Roman"
            r = p.add_run(ref.get("text", ""))
            r.font.size = Pt(8); r.font.name = "Times New Roman"

    #  Save 
    os.makedirs(
        os.path.dirname(output_path) if os.path.dirname(output_path) else ".",
        exist_ok=True,
    )
    doc.save(output_path)
    print(f"[OK] DOCX saved: {output_path}")
    return output_path


#  Internal helpers 

def _section_heading(doc, text: str):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after  = Pt(6)
    r = p.add_run(text)
    r.bold = True; r.font.size = Pt(10); r.font.name = "Times New Roman"


def _body_paragraph(doc, text: str, indent: bool = True):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if indent:
        p.paragraph_format.first_line_indent = Inches(0.25)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after  = Pt(2)
    _add_formatted_text(p, text)
    return p


def _add_section(doc, section: dict, images_dir: str, paper: dict):
    number = section.get("number", "")
    title  = section.get("title", "")
    heading = f"{number}. {title.upper()}" if number else title.upper()
    _section_heading(doc, heading)
    content = section.get("content", "")
    if content:
        _add_content_paragraphs(doc, content, images_dir, paper)
    for sub in section.get("subsections", []):
        _add_subsection(doc, sub, images_dir, paper)


def _add_subsection(doc, sub: dict, images_dir: str, paper: dict):
    letter = sub.get("letter", "")
    title  = sub.get("title", "")
    heading = f"{letter}. {title}" if letter else title
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after  = Pt(3)
    r = p.add_run(heading)
    r.bold = True; r.italic = True; r.font.size = Pt(10); r.font.name = "Times New Roman"
    content = sub.get("content", "")
    if content:
        _add_content_paragraphs(doc, content, images_dir, paper)
    for item in sub.get("numberedItems", []):
        item_heading = f"{item.get('number', '')}) {item.get('title', '')}".strip()
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after  = Pt(3)
        r = p.add_run(item_heading)
        r.bold = True; r.italic = True; r.font.size = Pt(10); r.font.name = "Times New Roman"
        if item.get("content"):
            _add_content_paragraphs(doc, item["content"], images_dir, paper)


def _add_content_paragraphs(doc, content: str, images_dir: str, paper: dict):
    """
    Parse content string into DOCX elements.

    Priority:
      - [FIGURE:id]  -> image + caption
      - [TABLE:id]   -> table + caption
      - $$...$$      -> display equation
      - \n* bullet   -> bullet paragraph
      - \n\n         -> paragraph break
      - inline $...$  -> OMML or italic fallback
    """
    # Split on display equation blocks first
    blocks = re.split(r'(\$\$[^$]+?\$\$)', content)
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        if block.startswith("$$") and block.endswith("$$"):
            latex = block[2:-2].strip()
            _insert_display_eq(doc, latex, _find_eq_number(latex, paper))
            continue
        # Split on paragraph breaks
        for para in re.split(r'\n{2,}', block):
            para = para.strip()
            if not para:
                continue
            if para.startswith("[FIGURE:"):
                _add_figure(doc, para, images_dir, paper)
                continue
            if para.startswith("[TABLE:"):
                _add_table(doc, para, paper)
                continue
            # Bullet block
            if "" in para:
                _add_bullet_block(doc, para)
                continue
            # Normal text - split on single newlines
            for line in para.split("\n"):
                line = line.strip()
                if not line:
                    continue
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                p.paragraph_format.first_line_indent = Inches(0.25)
                p.paragraph_format.space_before = Pt(0)
                p.paragraph_format.space_after  = Pt(2)
                _add_formatted_text(p, line)


def _add_bullet_block(doc, text: str):
    """Render text containing bullet markers ()."""
    parts = re.split(r'(?=)', text)
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if part.startswith(""):
            item_text = part[1:].strip()
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.left_indent       = Inches(0.25)
            p.paragraph_format.first_line_indent = Inches(-0.15)
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after  = Pt(1)
            r = p.add_run(" ")
            r.font.size = Pt(10); r.font.name = "Times New Roman"
            _add_formatted_text(p, item_text)
        else:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.first_line_indent = Inches(0.25)
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after  = Pt(2)
            _add_formatted_text(p, part)


def _add_formatted_text(paragraph, text: str):
    """Add mixed inline content to an existing paragraph."""
    token_re = re.compile(
        r'(\$[^$]+\$'                    # inline math $...$
        r'|\*\*[^*]+\*\*'                # **bold**
        r'|\*[^*]+\*'                    # *italic*
        r'|\[[0-9][0-9,\s\-\u2013]*\]'  # citation [1], [1,2], [1-3]
        r')'
    )
    for part in token_re.split(text):
        if not part:
            continue
        if part.startswith("$") and part.endswith("$") and not part.startswith("$$"):
            formula = part[1:-1].strip()
            if not _append_inline_eq(paragraph, formula):
                r = paragraph.add_run(formula)
                r.italic = True; r.font.size = Pt(10); r.font.name = "Times New Roman"
        elif part.startswith("**") and part.endswith("**"):
            r = paragraph.add_run(part[2:-2])
            r.bold = True; r.font.size = Pt(10); r.font.name = "Times New Roman"
        elif part.startswith("*") and part.endswith("*"):
            r = paragraph.add_run(part[1:-1])
            r.italic = True; r.font.size = Pt(10); r.font.name = "Times New Roman"
        elif re.match(r'\[[0-9][0-9,\s\-\u2013]*\]', part):
            r = paragraph.add_run(part)
            r.font.size = Pt(10); r.font.name = "Times New Roman"
        else:
            r = paragraph.add_run(part)
            r.font.size = Pt(10); r.font.name = "Times New Roman"


def _find_eq_number(latex: str, paper: dict) -> str:
    for eq in paper.get("equations", []):
        if eq.get("latex", "").strip() == latex.strip():
            return str(eq.get("number", ""))
    return ""


def _add_figure(doc, figure_ref: str, images_dir: str, paper: dict):
    m = re.match(r'\[FIGURE:([^\]]+)\]', figure_ref)
    if not m:
        return
    fig_id = m.group(1).strip()
    figure = next((f for f in paper.get("figures", []) if f.get("id") == fig_id), None)
    if not figure:
        return
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after  = Pt(3)
    filename = figure.get("filename", "")
    if filename:
        img_path = os.path.join(images_dir, filename)
        if os.path.exists(img_path):
            p.add_run().add_picture(img_path, width=Inches(3.0))
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after  = Pt(6)
    r = p.add_run(figure.get("caption", ""))
    r.font.size = Pt(8); r.font.name = "Times New Roman"


def _add_table(doc, table_ref: str, paper: dict):
    m = re.match(r'\[TABLE:([^\]]+)\]', table_ref)
    if not m:
        return
    tbl_id = m.group(1).strip()
    table_data = next((t for t in paper.get("tables", []) if t.get("id") == tbl_id), None)
    if not table_data:
        return
    caption = table_data.get("caption", "")
    if caption:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after  = Pt(3)
        r = p.add_run(caption)
        r.bold = True; r.font.size = Pt(8); r.font.name = "Times New Roman"
    headers = table_data.get("headers", [])
    rows    = table_data.get("rows", [])
    if not headers:
        return
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    table.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for i, hdr in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = ""
        cp = cell.paragraphs[0]
        cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = cp.add_run(hdr)
        r.bold = True; r.font.size = Pt(8); r.font.name = "Times New Roman"
    for r_idx, row in enumerate(rows):
        for c_idx, val in enumerate(row):
            if c_idx < len(headers):
                cell = table.rows[r_idx + 1].cells[c_idx]
                cell.text = ""
                cp = cell.paragraphs[0]
                cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
                r = cp.add_run(str(val))
                r.font.size = Pt(8); r.font.name = "Times New Roman"


#  CLI 

if __name__ == "__main__":
    import json

    if len(sys.argv) >= 2:
        json_path = sys.argv[1]
        out_path  = sys.argv[2] if len(sys.argv) >= 3 else str(Path(json_path).with_suffix(".docx"))
        with open(json_path, encoding="utf-8") as f:
            paper = json.load(f)
        generate_ieee_docx(paper, out_path)
        print(f"DOCX: {out_path}")
    else:
        output_dir = Path(__file__).parent / "output"
        if not output_dir.exists():
            print("ERROR: output/ folder not found.")
            sys.exit(1)
        pending = [j for j in sorted(output_dir.glob("*.json"))
                   if not j.with_suffix(".docx").exists()]
        if not pending:
            print("All JSON in output/ already have a matching DOCX.")
            sys.exit(0)
        for j in pending:
            print(f"[GENERATE] {j.name} ...")
            try:
                with open(j, encoding="utf-8") as f:
                    paper = json.load(f)
                generate_ieee_docx(paper, str(j.with_suffix(".docx")))
            except Exception as e:
                print(f"  ERROR: {e}")
        print("Done.")
