"""Patch YouTube playbook update and CLAUDE.md governance docs."""
import re, pathlib, os

os.chdir(r"C:\Pineapple Contractors M7")

# 1. YouTube Video Analysis — replace #2D7D46 and prose green refs
yt = pathlib.Path(r"01_Command_Center\YouTube Video Analysis & Playbook Update.md")
if yt.exists():
    text = yt.read_text(encoding='utf-8', errors='replace')
    orig = text
    text = text.replace('#2D7D46', '#1A365D').replace('#2d7d46', '#1A365D')
    text = re.sub(r'Heritage Green', 'Royal Navy', text, flags=re.IGNORECASE)
    text = re.sub(r'\bGreen Static Elements\b', 'Navy Static Elements', text, flags=re.IGNORECASE)
    text = re.sub(r'\bgreen\b', 'navy', text, flags=re.IGNORECASE)
    if text != orig:
        yt.write_text(text, encoding='utf-8')
        changed = sum(1 for a,b in zip(orig.splitlines(), text.splitlines()) if a!=b)
        print(f"PATCHED ({changed}L): {yt.name[:60]}")

# 2. 03_Knowledge_Mat\CLAUDE.md — governance doc, add sentinel
claude_km = pathlib.Path(r"03_Knowledge_Mat\CLAUDE.md")
if claude_km.exists():
    text = claude_km.read_text(encoding='utf-8', errors='replace')
    if 'M7-FIREWALL-EXEMPT' not in text:
        text = text.rstrip() + '\n\n<!-- M7-FIREWALL-EXEMPT: governance-reference -->\n'
        claude_km.write_text(text, encoding='utf-8')
        print(f"SENTINEL: {claude_km}")

print("Done.")
