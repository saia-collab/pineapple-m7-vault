"""Patch green violations in 03_Knowledge_Mat governance and HTML files."""
import re, pathlib, os

os.chdir(r"C:\Pineapple Contractors M7")

SENTINEL_MD = '\n\n<!-- M7-FIREWALL-EXEMPT: governance-reference -->\n'

# 1. Governance text files — add sentinel (they describe the rule, not violate it)
gov_docs = [
    r"03_Knowledge_Mat\Consolidating NotebookLM Sources to PDF.md",
    r"03_Knowledge_Mat\M7_MASTER_PLAYBOOK.md",
]
for rel in gov_docs:
    p = pathlib.Path(rel)
    if p.exists() and 'M7-FIREWALL-EXEMPT' not in p.read_text(encoding='utf-8', errors='replace'):
        text = p.read_text(encoding='utf-8', errors='replace').rstrip() + SENTINEL_MD
        p.write_text(text, encoding='utf-8')
        print(f"SENTINEL: {p.name}")

# 2. M7_Command_Center.html — fix actual green colors and label
html = pathlib.Path(r"03_Knowledge_Mat\M7_Command_Center.html")
if html.exists():
    text = html.read_text(encoding='utf-8', errors='replace')
    orig = text
    subs = [
        ('#4caf50', '#00BFFF'), ('#4CAF50', '#00BFFF'),
        ('#a8d8a8', '#00BFFF'), ('#A8D8A8', '#00BFFF'),
        ('<span>Green</span>', '<span>Navy/Gold</span>'),
    ]
    text = re.sub(r'\bGreen\b(?=</span>)', 'Navy/Gold', text)
    for old, new in subs:
        text = text.replace(old, new)
    if text != orig:
        html.write_text(text, encoding='utf-8')
        changed = sum(1 for a,b in zip(orig.splitlines(), text.splitlines()) if a!=b)
        print(f"PATCHED ({changed}L): {html.name}")

# 3. MASTER_REPORT.md — fix outdated "Heritage Green is approved" note
report = pathlib.Path(r"03_Knowledge_Mat\MASTER_REPORT.md")
if report.exists():
    text = report.read_text(encoding='utf-8', errors='replace')
    orig = text
    text = text.replace(
        "Heritage Green (#2D7D46) is approved for accents but banned from core corporate structural assets.",
        "Heritage accent replaced by Process Status Cyan (#00BFFF) — Royal Navy (#1A365D) anchors all structural assets."
    )
    if text != orig:
        report.write_text(text, encoding='utf-8')
        print(f"PATCHED: {report.name}")

print("Done.")
