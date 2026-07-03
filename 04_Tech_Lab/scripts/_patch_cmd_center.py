"""Patch remaining green violations in 01_Command_Center governance files."""
import re, pathlib, os

os.chdir(r"C:\Pineapple Contractors M7")

SENTINEL = '\n\n<!-- M7-FIREWALL-EXEMPT: governance-reference -->\n'
GREEN_RE = re.compile(r'\bgreen\b', re.IGNORECASE)

# Files that are CLAUDE.md / constitution docs -> add sentinel
sentinel_files = [
    r"01_Command_Center\CLAUDE.md",
    r"01_Command_Center\AI_INGESTION_TARGET.md",
]

for rel in sentinel_files:
    p = pathlib.Path(rel)
    if p.exists() and 'M7-FIREWALL-EXEMPT' not in p.read_text(encoding='utf-8', errors='replace'):
        text = p.read_text(encoding='utf-8', errors='replace').rstrip() + SENTINEL
        p.write_text(text, encoding='utf-8')
        print(f"SENTINEL: {p.name}")

# Playbook files - replace "green success states" with "cyan success states" etc.
playbook_files = [
    r"01_Command_Center\AI Agent Project Playbook Generation (1).md",
    r"01_Command_Center\AI Agent Project Playbook Generation.md",
]

for rel in playbook_files:
    p = pathlib.Path(rel)
    if not p.exists(): continue
    text = p.read_text(encoding='utf-8', errors='replace')
    orig = text
    # Specific replacements
    text = re.sub(r'\bgreen success states\b', 'cyan success states', text, flags=re.IGNORECASE)
    text = re.sub(r'\bgreen\b', 'cyan', text, flags=re.IGNORECASE)
    if text != orig:
        p.write_text(text, encoding='utf-8')
        changed = sum(1 for a,b in zip(orig.splitlines(), text.splitlines()) if a!=b)
        print(f"PATCHED ({changed}L): {p.name[:60]}")

print("Done.")
