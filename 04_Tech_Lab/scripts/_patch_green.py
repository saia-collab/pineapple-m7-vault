import re, pathlib, os

os.chdir(r"C:\Pineapple Contractors M7")

targets = [
    r"04_Tech_Lab\skills\skill_assets\examples\dr_mehra_clinic\data_map.html",
    r"04_Tech_Lab\skills\skill_assets\examples\sally_law\data_map.html",
    r"04_Tech_Lab\skills\skill_assets\examples\devon_saas\data_map.html",
    r"04_Tech_Lab\skills\skill_assets\examples\dr_anwar_derma\data_map.html",
    r"04_Tech_Lab\skills\skill_assets\examples\marco_ecommerce\data_map.html",
    r"03_Knowledge_Mat\00_Atlas\templates\KomputerMechanic-Hermes-Student-Companion-Template\KomputerMechanic-Hermes-Student-Companion-Template.html",
]

GREEN_HEX_RE = re.compile(r'#[0-9a-fA-F]{6}\b')
GREEN_NAMED_RE = re.compile(r'\b(green|lime|forestgreen|seagreen|darkgreen|lightgreen|mediumseagreen|springgreen|chartreuse|olive)\b', re.IGNORECASE)
TAILWIND_GREEN_RE = re.compile(r'\b(bg|text|border|ring|from|to|via)-green-(\d{2,3})\b', re.IGNORECASE)

APPROVED = {"#1a365d","#001122","#001a33","#fbc02d","#ffd700","#e5a93c","#00bfff","#ffffff","#ffe12d","#000000"}

def hex_is_green(h):
    h = h.lower()
    if h in APPROVED:
        return False
    try:
        r,g,b = int(h[1:3],16), int(h[3:5],16), int(h[5:7],16)
    except Exception:
        return False
    return g > 90 and g >= r+40 and g >= b+40

def replace_green_hex(m):
    h = m.group(0)
    return '#00BFFF' if hex_is_green(h) else h

total = 0
for rel in targets:
    p = pathlib.Path(rel)
    if not p.exists():
        print(f"MISSING: {rel}")
        continue
    text = p.read_text(encoding='utf-8', errors='replace')
    orig = text
    text = GREEN_HEX_RE.sub(replace_green_hex, text)
    text = GREEN_NAMED_RE.sub('#00BFFF', text)
    text = TAILWIND_GREEN_RE.sub(lambda m: m.group(0).replace('green','cyan').replace('Green','cyan'), text)
    if text != orig:
        p.write_text(text, encoding='utf-8')
        changed = sum(1 for a,b in zip(orig.splitlines(), text.splitlines()) if a != b)
        total += changed
        print(f"PATCHED ({changed} lines): {rel}")
    else:
        print(f"CLEAN: {rel}")

print(f"\nTotal lines patched: {total}")
