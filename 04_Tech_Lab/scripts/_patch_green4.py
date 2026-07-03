"""Fourth-pass: patch inject.css and Sora Studio template."""
import re, pathlib, os

os.chdir(r"C:\Pineapple Contractors M7")

fixes = {
    r"03_Knowledge_Mat\00_Atlas\templates\promptify_v1\inject.css": [
        ('#4CAF50', '#00BFFF'),
        ('/* Green */', '/* Cyan */'),
        ('#66bb6a', '#00BFFF'),
        ('#388e3c', '#1A365D'),
        ('/* Green gradient */', '/* Brand gradient */'),
    ],
}

# Sora Studio md - figurative "green" in prose
sora = r"03_Knowledge_Mat\00_Atlas\templates\Sora_Studio_Builder\# \U0001f3ac Master Prompt_ Build Sora Studio - OpenAI Video API Web Interface.md"
# Use glob to find it
sora_path = None
for p in pathlib.Path(r"03_Knowledge_Mat\00_Atlas\templates\Sora_Studio_Builder").iterdir():
    if p.suffix == '.md':
        sora_path = p
        break

GREEN_WORD_RE = re.compile(r'\bgreen\b', re.IGNORECASE)

total = 0
for rel, subs in fixes.items():
    p = pathlib.Path(rel)
    if not p.exists():
        print(f"MISSING: {rel}")
        continue
    text = p.read_text(encoding='utf-8', errors='replace')
    orig = text
    for old, new in subs:
        text = text.replace(old, new)
    if text != orig:
        p.write_text(text, encoding='utf-8')
        changed = sum(1 for a, b in zip(orig.splitlines(), text.splitlines()) if a != b)
        total += changed
        print(f"PATCHED ({changed}L): {rel}")

# Sora Studio: replace "green" word with "cyan" in prose (it's a UI color label)
if sora_path and sora_path.exists():
    text = sora_path.read_text(encoding='utf-8', errors='replace')
    orig = text
    text = GREEN_WORD_RE.sub('cyan', text)
    if text != orig:
        sora_path.write_text(text, encoding='utf-8')
        changed = sum(1 for a, b in zip(orig.splitlines(), text.splitlines()) if a != b)
        total += changed
        print(f"PATCHED ({changed}L): {sora_path.name[:60]}")

print(f"\nTotal lines patched: {total}")
