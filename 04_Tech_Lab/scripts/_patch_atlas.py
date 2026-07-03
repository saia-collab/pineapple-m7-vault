"""Patch Atlas KB source files:
- Playbook: governance text describing green rule -> add M7-FIREWALL-EXEMPT sentinel
- YouTube_Analysis: actual #2D7D46 hex -> replace with #1A365D (Royal Navy)
"""
import re, pathlib, os

os.chdir(r"C:\Pineapple Contractors M7")

# YouTube Analysis: replace legacy heritage green with Royal Navy
yt = pathlib.Path(r"03_Knowledge_Mat\00_Atlas\2026-06-18_KB_2026-06-17_YouTube_Analysis_A_SOURCE.md")
if yt.exists():
    text = yt.read_text(encoding='utf-8', errors='replace')
    orig = text
    text = text.replace('#2D7D46', '#1A365D')
    text = re.sub(r'Heritage Green', 'Royal Navy', text, flags=re.IGNORECASE)
    text = re.sub(r'\bGreen Static Elements\b', 'Navy Static Elements', text, flags=re.IGNORECASE)
    if text != orig:
        yt.write_text(text, encoding='utf-8')
        changed = sum(1 for a,b in zip(orig.splitlines(), text.splitlines()) if a!=b)
        print(f"PATCHED ({changed}L): {yt.name[:60]}")

# Playbook SOURCE: governance text describes the green prohibition rule - add sentinel
playbook = pathlib.Path(r"03_Knowledge_Mat\00_Atlas\2026-06-18_KB_2026-06-17_Playbook_Claude_Project_Master_SOURCE.md")
if playbook.exists():
    text = playbook.read_text(encoding='utf-8', errors='replace')
    if 'M7-FIREWALL-EXEMPT' not in text:
        text = text.rstrip() + '\n\n<!-- M7-FIREWALL-EXEMPT: governance-reference -->\n'
        playbook.write_text(text, encoding='utf-8')
        print(f"SENTINEL: {playbook.name[:60]}")

print("Done.")
