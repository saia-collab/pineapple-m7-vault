"""Third-pass: patch green color values and figurative green phrases in SKILL files and templates."""
import re, pathlib, os

os.chdir(r"C:\Pineapple Contractors M7")

# Mapping of exact string substitutions (case-sensitive where needed)
EXACT_SUBS = {
    # SKILL (4).md - chart colors
    "'#2ecc71'": "'#00BFFF'",
    "'#27ae60'": "'#FBC02D'",
    "color='mediumseagreen'": "color='#00BFFF'",
    # SKILL (3).md - RGB accent
    "RGBColor(155, 187, 89)  # Green": "RGBColor(0, 191, 255)  # Cyan",
}

REGEX_SUBS = [
    # Figurative phrases
    (re.compile(r'\bgreenfield\b', re.IGNORECASE), 'fresh-baseline'),
    (re.compile(r'\bgreen\s+light\b', re.IGNORECASE), 'authorization'),
    (re.compile(r'\bgreen\s+"already\s+wired"\s+badge\b', re.IGNORECASE), 'status "already wired" badge'),
    # Hex greens in templates
    (re.compile(r'#10B981\b', re.IGNORECASE), '#00BFFF'),
    (re.compile(r'#2ecc71\b', re.IGNORECASE), '#00BFFF'),
    (re.compile(r'#27ae60\b', re.IGNORECASE), '#FBC02D'),
]

targets = [
    r"04_Tech_Lab\skills\Claude_Agent_Skills_Pack\SKILL (3).md",
    r"04_Tech_Lab\skills\Claude_Agent_Skills_Pack\SKILL (4).md",
    r"04_Tech_Lab\skills\skill_assets\SKILL.md",
    r"04_Tech_Lab\skills\shot-builder_for_sharing\SKILL.md",
]

# Also find the Sora Studio template
sora_dir = pathlib.Path(r"03_Knowledge_Mat\00_Atlas\templates")
for f in sora_dir.rglob("*.md"):
    targets.append(str(f))

total = 0
seen = set()
for rel in targets:
    p = pathlib.Path(rel)
    if not p.exists() or str(p) in seen:
        continue
    seen.add(str(p))
    text = p.read_text(encoding='utf-8', errors='replace')
    orig = text
    for old, new in EXACT_SUBS.items():
        text = text.replace(old, new)
    for rx, repl in REGEX_SUBS:
        text = rx.sub(repl, text)
    if text != orig:
        p.write_text(text, encoding='utf-8')
        changed = sum(1 for a, b in zip(orig.splitlines(), text.splitlines()) if a != b)
        total += changed
        print(f"PATCHED ({changed}L): {rel}")

print(f"\nTotal lines patched: {total}")
