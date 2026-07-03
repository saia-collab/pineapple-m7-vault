"""Second-pass green neutralizer: handles rgba green-dominant values and prose uses."""
import re, pathlib, os

os.chdir(r"C:\Pineapple Contractors M7")

# rgba heuristic: if G > 90 and G >= R+40 and G >= B+40 => green => replace with rgba cyan
RGBA_RE = re.compile(r'rgba?\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*(?:,\s*[\d.]+)?\s*\)', re.IGNORECASE)

def rgba_is_green(r, g, b):
    return g > 90 and g >= r + 40 and g >= b + 40

def replace_rgba(m):
    try:
        r, g, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
    except Exception:
        return m.group(0)
    if rgba_is_green(r, g, b):
        # Replace with brand cyan at same alpha if present
        full = m.group(0)
        alpha_match = re.search(r',\s*([\d.]+)\s*\)', full)
        alpha = alpha_match.group(1) if alpha_match else '1'
        return f'rgba(0, 191, 255, {alpha})'
    return m.group(0)

# Prose "green-lit" -> "approved"
PROSE_RE = re.compile(r'\bgreen[-\s]?lit\b', re.IGNORECASE)

targets = [
    r"04_Tech_Lab\skills\skill_assets\examples\dr_mehra_clinic\data_map.html",
    r"04_Tech_Lab\skills\skill_assets\examples\sally_law\data_map.html",
    r"04_Tech_Lab\skills\skill_assets\examples\devon_saas\data_map.html",
    r"04_Tech_Lab\skills\skill_assets\examples\dr_anwar_derma\data_map.html",
    r"04_Tech_Lab\skills\skill_assets\examples\marco_ecommerce\data_map.html",
    r"03_Knowledge_Mat\00_Atlas\templates\KomputerMechanic-Hermes-Student-Companion-Template\KomputerMechanic-Hermes-Student-Companion-Template.html",
    r"04_Tech_Lab\skills\emai-starter-vault\Machine\Templates\Skool Weekly Recap Template.md",
]

total = 0
for rel in targets:
    p = pathlib.Path(rel)
    if not p.exists():
        print(f"MISSING: {rel}")
        continue
    text = p.read_text(encoding='utf-8', errors='replace')
    orig = text
    text = RGBA_RE.sub(replace_rgba, text)
    text = PROSE_RE.sub('approved', text)
    if text != orig:
        p.write_text(text, encoding='utf-8')
        changed = sum(1 for a, b in zip(orig.splitlines(), text.splitlines()) if a != b)
        total += changed
        print(f"PATCHED ({changed} lines): {rel}")
    else:
        print(f"CLEAN: {rel}")

print(f"\nTotal lines patched: {total}")
