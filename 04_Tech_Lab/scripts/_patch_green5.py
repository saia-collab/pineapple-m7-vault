"""Fifth-pass: fix remaining green refs in templates — C# code and prose descriptions."""
import re, pathlib, os

os.chdir(r"C:\Pineapple Contractors M7")

SUBS = [
    # C# console color
    ('ConsoleColor.Green', 'ConsoleColor.Cyan'),
    # Prose color references
    ('Success is green 22c55e', 'Success is cyan #00BFFF'),
    ('success is green 22c55e', 'success is cyan #00BFFF'),
    ('green 22c55e', '#00BFFF'),
    ('22c55e', '#00BFFF'),
]

REGEX_SUBS = [
    # "green pulsing" -> "cyan pulsing"
    (re.compile(r'\bgreen\b(?=\s+pulsing)', re.IGNORECASE), 'cyan'),
    # "Success (green)" type patterns
    (re.compile(r'\bgreen\b(?=\s+\d{2}[a-f0-9]{4}\b)', re.IGNORECASE), 'cyan'),
]

templates_root = pathlib.Path(r"03_Knowledge_Mat\00_Atlas\templates")
total = 0
for p in templates_root.rglob("*.md"):
    text = p.read_text(encoding='utf-8', errors='replace')
    orig = text
    for old, new in SUBS:
        text = text.replace(old, new)
    for rx, repl in REGEX_SUBS:
        text = rx.sub(repl, text)
    if text != orig:
        p.write_text(text, encoding='utf-8')
        changed = sum(1 for a, b in zip(orig.splitlines(), text.splitlines()) if a != b)
        total += changed
        name = p.name[:70].encode('ascii', errors='replace').decode('ascii')
        print(f"PATCHED ({changed}L): {name}")

for p in templates_root.rglob("*.css"):
    text = p.read_text(encoding='utf-8', errors='replace')
    orig = text
    for old, new in SUBS:
        text = text.replace(old, new)
    for rx, repl in REGEX_SUBS:
        text = rx.sub(repl, text)
    if text != orig:
        p.write_text(text, encoding='utf-8')
        changed = sum(1 for a, b in zip(orig.splitlines(), text.splitlines()) if a != b)
        total += changed
        print(f"PATCHED ({changed}L): {p.name[:70]}")

print(f"\nTotal lines patched: {total}")
