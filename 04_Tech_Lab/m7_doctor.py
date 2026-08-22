#!/usr/bin/env python3
"""M7 Doctor: local structure, service, and credential-safe health checks."""

from __future__ import annotations

import os
import socket
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

VAULT = Path(__file__).resolve().parent.parent
OBSIDIAN_KEY = os.environ.get("OBSIDIAN_REST_API_KEY", "").strip()
OK, BAD, WARN = "[ OK ]", "[FAIL]", "[WARN]"
rows: list[tuple[str, str, str]] = []


def add(label: str, status: str, detail: str = "") -> None:
    rows.append((status, label, detail))


def port_open(host: str, port: int) -> bool:
    with socket.socket() as sock:
        sock.settimeout(1)
        try:
            sock.connect((host, port))
            return True
        except OSError:
            return False


def http_status(url: str, headers: dict[str, str] | None = None, timeout: int = 3) -> tuple[int | None, str]:
    try:
        request = urllib.request.Request(url, headers=headers or {})
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, response.read(200).decode("utf-8", "ignore")
    except urllib.error.HTTPError as exc:
        return exc.code, str(exc)
    except Exception as exc:  # diagnostic must continue through every check
        return None, str(exc)


required_dirs = [
    "01_Command_Center",
    "02_Media_Vault",
    "02_Workspaces",
    "03_Knowledge_Mat",
    "04_Tech_Lab",
    "05_Campaign_Factory",
]
missing_dirs = [name for name in required_dirs if not (VAULT / name).is_dir()]
add("M7 folder structure", BAD if missing_dirs else OK, ", ".join(missing_dirs) or "all required rooms present")

required_files = [
    "CLAUDE.md",
    "CONTEXT.md",
    "m7_core_rules.config",
    "01_Command_Center/M7_START_HERE.md",
    "01_Command_Center/M7_SYSTEM_RECOVERY_AND_ROUTING_SOP_2026-08-22.md",
    "03_Knowledge_Mat/SHARED_MEMORY.md",
    "04_Tech_Lab/config/models.json",
]
missing_files = [name for name in required_files if not (VAULT / name).exists()]
add("Current authority files", BAD if missing_files else OK, ", ".join(missing_files) or "all present")

firewall = VAULT / "04_Tech_Lab" / "scripts" / "brand_firewall.py"
if firewall.exists():
    try:
        result = subprocess.run(
            [sys.executable, str(firewall), "--check", "IKO Certified. Call for a free roof inspection."],
            capture_output=True,
            text=True,
            timeout=20,
            check=False,
        )
        add("Brand firewall", OK if result.returncode == 0 else BAD, "current approved copy test")
    except Exception as exc:
        add("Brand firewall", BAD, str(exc))
else:
    add("Brand firewall", BAD, "script missing")

services = [
    ("Local Studio", 3737, "http://127.0.0.1:3737/hermes", True),
    ("Hermes", 9119, "http://127.0.0.1:9119", True),
    ("Free Claude proxy", 8082, "http://127.0.0.1:8082", False),
    ("OmniRoute", 20128, "http://127.0.0.1:20128/v1/models", True),
    ("M7 backend", 51763, "http://127.0.0.1:51763/api/health", False),
    ("Notebook/Obsidian bridge", 8643, "http://127.0.0.1:8643", False),
    ("Ollama", 11434, "http://127.0.0.1:11434/api/tags", False),
]
for label, port, url, core in services:
    if not port_open("127.0.0.1", port):
        add(f"{label} (:{port})", BAD if core else WARN, "not listening")
        continue
    status, _ = http_status(url)
    healthy = status is not None and (200 <= status < 500)
    add(f"{label} (:{port})", OK if healthy else WARN, f"HTTP {status}" if status else "port open; HTTP probe failed")

if port_open("127.0.0.1", 27123):
    if OBSIDIAN_KEY:
        status, _ = http_status(
            "http://127.0.0.1:27123/",
            {"Authorization": f"Bearer {OBSIDIAN_KEY}"},
        )
        add("Obsidian Local REST API", OK if status in (200, 204) else WARN, f"HTTP {status}")
    else:
        add("Obsidian Local REST API", WARN, "reachable; set OBSIDIAN_REST_API_KEY to test authorization")
else:
    add("Obsidian Local REST API", WARN, "not running")

outbox = VAULT / "01_Command_Center" / "Outbox_Drafts"
try:
    outbox.mkdir(parents=True, exist_ok=True)
    probe = outbox / ".m7_doctor_write_test"
    probe.write_text("ok", encoding="utf-8")
    probe.unlink()
    add("Outbox_Drafts writable", OK, str(outbox))
except Exception as exc:
    add("Outbox_Drafts writable", BAD, str(exc))

print("\n" + "=" * 72)
print(" PINEAPPLE M7 — CONNECTION DOCTOR")
print(f" Vault: {VAULT}")
print("=" * 72)
for status, label, detail in rows:
    print(f" {status}  {label:<34} {detail}")
print("=" * 72)
failures = sum(status == BAD for status, _, _ in rows)
warnings = sum(status == WARN for status, _, _ in rows)
if failures:
    print(f" RESULT: FAILED — {failures} required check(s) failed; {warnings} optional warning(s).")
elif warnings:
    print(f" RESULT: CORE HEALTHY — {warnings} optional service(s) need attention or are offline.")
else:
    print(" RESULT: HEALTHY — all required and optional checks passed.")
sys.exit(1 if failures else 0)
