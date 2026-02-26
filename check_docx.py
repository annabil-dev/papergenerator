from docx import Document
from docx.oxml.ns import qn
import os

docx_path = ".playwright-mcp/paper.docx"

if not os.path.exists(docx_path):
    print(f"File not found: {docx_path}")
else:
    doc = Document(docx_path)
    
    print("=" * 80)
    print("DOCX CONTENT VERIFICATION")
    print("=" * 80)
    
    print(f"\nTotal Paragraphs: {len(doc.paragraphs)}")
    print(f"Total Tables: {len(doc.tables)}\n")
    
    # Show first 30 paragraphs
    for i, para in enumerate(doc.paragraphs[:30]):
        text = para.text[:120] if para.text else "(empty)"
        style = para.style.name if para.style else "No style"
        # Check if it has a background color or is bold
        runs = para.runs
        props = []
        if runs and runs[0].bold:
            props.append("BOLD")
        if runs and runs[0].italic:
            props.append("ITALIC")
        prop_str = f" [{', '.join(props)}]" if props else ""
        
        print(f"[{i:2d}] {style:20} | {text}{prop_str}")
    
    print("\n" + "=" * 80)
    print("KEY FINDINGS:")
    print("=" * 80)
    
    # Extract abstract and acknowledgment
    full_text = "\n".join([p.text for p in doc.paragraphs])
    
    if "Abstract" in full_text or "ABSTRACT" in full_text:
        print("✓ Abstract section found")
    
    if "Acknowledgment" in full_text or "ACKNOWLEDGMENT" in full_text:
        print("✓ Acknowledgment section found")
    
    # Check for formulas
    if "$" in full_text or "\\sigma" in full_text or "A_{att}" in full_text:
        print("✓ LaTeX formulas detected in content")
    else:
        print("⚠ LaTeX formulas not fully preserved (formulas might be in different format)")
    
    # Show sample content
    print("\n" + "=" * 80)
    print("SAMPLE EXTRACTED TEXT:")
    print("=" * 80)
    print(full_text[:1000])
    print("\n[... truncated ...]")
