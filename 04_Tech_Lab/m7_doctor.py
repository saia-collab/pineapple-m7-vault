#!/usr/bin/env python3
"""
M7 DOCTOR — non-human connection + health checklist.
Checks that every part of the Pineapple M7 OS is connected and talking.
Run:  python m7_doctor.py   (or double-click M7_DOCTOR.bat)
Standard library only — no installs. Prints a green/red checklist.
"""
import json, socket, subprocess, sys, urllib.request
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
OBSIDIAN_KEY = "1f8aa9201f4d4769ec53b2eb57dc1333c5a6b6e6b379294e71229a584d17cd8d"  # from Local REST API plugin
OK, BAD, WARN = "[ OK ]", "[FAIL]", "[WARN]"
rows = []

def add(label, status, detail=""):
    rows.append((status, label, detail))

# 1) 4-Fala folder structure
fala = ["01_Command_Center", "02_Media_Vault", "02_Workspaces",
        "03_Knowledge_Mat", "04_Tech_Lab", "05_Campaign_Factory"]
missing = [f for f in fala if not (VAULT / f).is_dir()]
add("4-Fala folder structure", OK if not missing else BAD, "missing: " + ", ".join(missing) if missing else "all present")

# 2) Key files
keyfiles = ["01_Command_Center/GROUNDING.md", "01_Command_Center/MASTER_PLAYBOOK.md",
            "01_Command_Center/M7_COMMAND_CENTER.html", "01_Command_Center/M7_Agent_Kanban.md",
            "02_Workspaces/Pineapple_Mana_Master_CRM_M7.xlsx"]
miss2 = [f for f in keyfiles if not (VAULT / f).exists()]
add("Core files present", OK if not miss2 else BAD, "missing: " + ", ".join(miss2) if miss2 else "all present")

# 3) brand_firewall present + runs
fw = None
for cand in ["04_Tech_Lab/Scripts/brand_firewall.py", "04_Tech_Lab/scripts/brand_firewall.py"]:
    if (VAULT / cand).exists():
        fw = VAULT / cand
if fw:
    try:
        r = subprocess.run([sys.executable, str(fw), "--check", "IKO Certified, CPPA, 972-928-0788"],
                           capture_output=True, text=True, timeout=20)
        add("Brand firewall runs", OK if "OK" in (r.stdout + r.stderr) else WARN, "responded")
    except Exception as e:
        add("Brand firewall runs", BAD, str(e))
else:
    add("Brand firewall present", BAD, "brand_firewall.py not found")

def http_ok(url, headers=None, timeout=2):
    try:
        req = urllib.request.Request(url, headers=headers or {})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, resp.read(200).decode("utf-8", "ignore")
    except Exception as e:
        return None, str(e)

def port_open(host, port):
    s = socket.socket(); s.settimeout(1)
    try:
        s.connect((host, port)); s.close(); return True
    except Exception:
        return False

# 4) M7 backend (51763)
if port_open("127.0.0.1", 51763):
    st, body = http_ok("http://127.0.0.1:51763/api/health")
    add("M7 backend (port 51763)", OK if st == 200 else WARN, "health responded" if st == 200 else body[:60])
else:
    add("M7 backend (port 51763)", WARN, "not running — start with START_M7_SERVER.bat")

# 5) Obsidian Local REST API (27123)
if port_open("127.0.0.1", 27123):
    st, body = http_ok("http://127.0.0.1:27123/", {"Authorization": "Bearer " + OBSIDIAN_KEY})
    add("Obsidian REST API (port 27123)", OK if st in (200, 204) else WARN,
        "connected + authorized" if st in (200, 204) else "reachable but auth/endpoint issue")
else:
    add("Obsidian REST API (port 27123)", WARN, "Obsidian closed or Local REST API plugin off")

# 6) Outbox writable
ob = VAULT / "01_Command_Center" / "Outbox_Drafts"
try:
    ob.mkdir(parents=True, exist_ok=True)
    t = ob / ".m7_doctor_write_test"
    t.write_text("ok"); t.unlink()
    add("Outbox_Drafts writable", OK, str(ob))
except Exception as e:
    add("Outbox_Drafts writable", BAD, str(e))

# ---- print report ----
print("\n" + "=" * 60)
print(" 🍍 PINEAPPLE M7 — CONNECTION DOCTOR")
print(f" Vault: {VAULT}")
print("=" * 60)
fails = 0
for status, label, detail in rows:
    if status == BAD:
        fails += 1
    print(f" {status}  {label:<34} {detail}")
print("=" * 60)
if fails == 0:
    print(" RESULT: healthy — everything that needs to be connected is. ✅")
else:
    print(f" RESULT: {fails} item(s) need attention (see [FAIL] above).")
print(" WARN = a service is just not running yet (start its launcher).")
print(" .")
