#!/usr/bin/env python3
"""
M7 DOCTOR — one-command health check for the Pineapple M7 Agentic OS.
100% READ-ONLY: it inspects, it never changes, publishes, or runs anything.

Answers the question "is my studio configured right?" in one glance:
  - 4-Fala folders + key files present
  - Studio / model ports online (3737 studio, 8082 fcc, 11434 ollama, 20128 omniroute, 9119 hermes)
  - Hermes profiles present and PROVERB-CLEAN (brand rule check)
  - Outbox drafts scanned for real brand violations (green hex, free-offer wording)
  - Git status (clean? pushed?)

Exit code 0 = healthy (warnings ok), 1 = at least one hard FAIL.
"""
import os, re, sys, socket, subprocess, glob

try:  # Windows consoles default to cp1252 and choke on emoji — force UTF-8
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

VAULT = r"C:\Pineapple Contractors M7"
PROFILES = os.path.join(os.environ.get("LOCALAPPDATA", r"C:\Users\estim\AppData\Local"), "hermes", "profiles")

OK, WARN, FAIL = "✅", "⚠️", "❌"
fails = 0
warns = 0

def line(icon, msg):
    global fails, warns
    if icon == FAIL: fails += 1
    if icon == WARN: warns += 1
    print(f"  {icon} {msg}")

def port_open(p, host="127.0.0.1"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM); s.settimeout(0.4)
    try:
        return s.connect_ex((host, p)) == 0
    finally:
        s.close()

print("\n===================================================================")
print("  🍍 M7 DOCTOR — Agentic OS health check (read-only)")
print("===================================================================")

# 1. 4-Fala folders ---------------------------------------------------------
print("\n[1/6] 📁 4-Fala folder topography")
for d in ["01_Command_Center", "02_Media_Vault", "03_Knowledge_Mat", "04_Tech_Lab"]:
    line(OK if os.path.isdir(os.path.join(VAULT, d)) else FAIL, d)

# 2. Key files --------------------------------------------------------------
print("\n[2/6] 📄 Key files")
key = {
    "01_Command_Center/MASTER_PLAYBOOK.md": FAIL,
    "01_Command_Center/M7_PROMPT_CONTROL_PANEL.md": WARN,
    "01_Command_Center/M7_STUDIO_STUDY_GUIDE.md": WARN,
    "01_Command_Center/Brand_DNA/M7_HERMES_SOUL.md": WARN,
    "04_Tech_Lab/scripts/brand_firewall.py": FAIL,
    "CLAUDE.md": FAIL,
}
for rel, sev in key.items():
    ok = os.path.isfile(os.path.join(VAULT, rel))
    line(OK if ok else sev, rel + ("" if ok else "  (missing)"))

# 3. Ports ------------------------------------------------------------------
print("\n[3/6] 🔌 Local services (offline = just not started, not an error)")
ports = [(3737, "Agentic OS Studio"), (8082, "Free Claude Code proxy"),
         (11434, "Ollama (free local models)"), (20128, "OmniRoute"), (9119, "Hermes console")]
for p, name in ports:
    up = port_open(p)
    line(OK if up else WARN, f":{p:<5} {name} — {'ONLINE' if up else 'offline'}")

# 4. Hermes profiles + proverb cleanliness ----------------------------------
print("\n[4/6] 🛰️  Hermes profiles (brand rule: NO Tongan proverbs)")
PROV = re.compile(r"(faka.?apa.?apa|Ko e hala.*fononga|Si.i pe kae)", re.I)
if os.path.isdir(PROFILES):
    souls = [f for f in glob.glob(os.path.join(PROFILES, "*", "*")) if os.path.basename(f).lower() == "soul.md"]
    dirty = []
    for f in souls:
        try:
            if PROV.search(open(f, encoding="utf-8", errors="ignore").read()):
                dirty.append(os.path.basename(os.path.dirname(f)))
        except Exception:
            pass
    line(OK, f"{len(souls)} profiles found")
    line(OK if not dirty else FAIL,
         "all profiles proverb-clean" if not dirty else f"proverb still in: {', '.join(dirty)}")
else:
    line(WARN, f"profiles dir not found ({PROFILES})")

# 5. Outbox brand scan (real violations only) -------------------------------
print("\n[5/6] 🎨 Outbox draft brand scan (green hex / free-offer wording)")
GREEN = re.compile(r"(#00ff00|#0f0\b|#008000|bg-green|text-green|border-green)", re.I)
OFFER = re.compile(r"\bfree\s+(roof\s+|roofing\s+)?(inspection|estimate|quote|audit|consultation)s?\b", re.I)
outbox = os.path.join(VAULT, "01_Command_Center", "Outbox_Drafts")
gv = ov = scanned = 0
for f in glob.glob(os.path.join(outbox, "**", "*.md"), recursive=True):
    try:
        t = open(f, encoding="utf-8", errors="ignore").read(); scanned += 1
        gv += len(GREEN.findall(t)); ov += len(OFFER.findall(t))
    except Exception:
        pass
line(OK if gv == 0 else FAIL, f"green color hits: {gv} (in {scanned} drafts)")
line(OK if ov == 0 else WARN, f"'free <offer>' hits: {ov} (should be CPPA)")

# 6. Git status -------------------------------------------------------------
print("\n[6/6] 🔄 Git (shared memory)")
def git(*a):
    return subprocess.run(["git", "-C", VAULT, *a], capture_output=True, text=True, timeout=15)
try:
    dirty = [x for x in git("status", "--porcelain").stdout.splitlines() if x.strip()]
    line(OK if not dirty else WARN, f"{'clean tree' if not dirty else str(len(dirty)) + ' uncommitted change(s) — run commit+push'}")
    last = git("log", "-1", "--oneline").stdout.strip()
    line(OK, f"last commit: {last[:70]}")
    ahead = git("rev-list", "--count", "@{u}..HEAD").stdout.strip()
    if ahead.isdigit() and int(ahead) > 0:
        line(WARN, f"{ahead} commit(s) not pushed to GitHub")
except Exception as e:
    line(WARN, f"git check skipped ({e})")

# Summary -------------------------------------------------------------------
print("\n===================================================================")
verdict = "❌ NEEDS ATTENTION" if fails else ("⚠️  HEALTHY (with warnings)" if warns else "✅ ALL HEALTHY")
print(f"  {verdict}   —   {fails} fail · {warns} warn")
print("===================================================================\n")
sys.exit(1 if fails else 0)
