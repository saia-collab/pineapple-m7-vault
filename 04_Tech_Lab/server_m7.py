#!/usr/bin/env python3
"""
M7 Command Center — local backend (standard library only, no pip installs).
Makes the dashboard buttons REAL: live Kanban <-> vault, Approve -> Outbox, firewall check.
Run:  python server_m7.py    then open  http://localhost:51763
Everything stays PAUSED. This server never publishes, sends, or spends. Outbox Shield holds.
"""
import json, os, re, subprocess, sys
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse, parse_qs

PORT = 51763
VAULT = Path(__file__).resolve().parent.parent          # 04_Tech_Lab/server_m7.py -> vault root
CMD = VAULT / "01_Command_Center"
KANBAN = CMD / "M7_Agent_Kanban.md"
OUTBOX = CMD / "Outbox_Drafts"
RESEARCH = VAULT / "05_Campaign_Factory" / "10_Research_Stage"
FIREWALL     = VAULT / "04_Tech_Lab" / "scripts" / "brand_firewall.py"
DASHBOARD    = CMD / "M7_COMMAND_CENTER.html"
SHARED_MEM   = VAULT / "03_Knowledge_Mat" / "SHARED_MEMORY.md"
MEMORY_SYNC  = VAULT / "04_Tech_Lab" / "scripts" / "memory_sync.py"

OUTBOX.mkdir(parents=True, exist_ok=True)
RESEARCH.mkdir(parents=True, exist_ok=True)


# ---------- Kanban parsing / writing ----------
def parse_kanban():
    """Read the Obsidian kanban .md into {columns:[{name,cards:[{text,agent}]}]}."""
    cols = []
    if not KANBAN.exists():
        return {"columns": cols, "error": "kanban file not found"}
    cur = None
    for line in KANBAN.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            cur = {"name": line[3:].strip(), "cards": []}
            cols.append(cur)
        elif cur is not None and line.strip().startswith("- ["):
            txt = re.sub(r"^- \[.?\]\s*", "", line.strip())
            tags = re.findall(r"#(\w+)", txt)
            cards = {"text": txt, "agent": tags[0] if tags else ""}
            cur["cards"].append(cards)
    return {"columns": cols}


def write_kanban(cols):
    """Re-emit the kanban .md, preserving frontmatter + settings block."""
    raw = KANBAN.read_text(encoding="utf-8") if KANBAN.exists() else ""
    fm = ""
    m = re.match(r"(---\n.*?\n---\n)", raw, re.S)
    if m:
        fm = m.group(1)
    settings = ""
    sm = re.search(r"(%%\s*kanban:settings.*?%%)", raw, re.S)
    if sm:
        settings = sm.group(1)
    body = fm + "\n"
    for c in cols:
        body += f"\n## {c['name']}\n\n"
        for card in c["cards"]:
            body += f"- [ ] {card['text']}\n"
        body += "\n"
    if settings:
        body += "\n" + settings + "\n"
    KANBAN.write_text(body, encoding="utf-8")


def move_card(text, to_column):
    data = parse_kanban()
    moved = None
    for c in data["columns"]:
        for card in list(c["cards"]):
            if card["text"].strip() == text.strip():
                moved = card
                c["cards"].remove(card)
    if moved is None:
        return {"ok": False, "error": "card not found"}
    for c in data["columns"]:
        if c["name"].strip() == to_column.strip():
            c["cards"].insert(0, moved)
            write_kanban(data["columns"])
            return {"ok": True}
    return {"ok": False, "error": "target column not found"}


# ---------- firewall ----------
def firewall_check(text):
    """Run brand_firewall.py --check on text. Returns {pass, output}."""
    if not FIREWALL.exists():
        return {"pass": None, "output": "brand_firewall.py not found"}
    try:
        r = subprocess.run([sys.executable, str(FIREWALL), "--check", text],
                           capture_output=True, text=True, timeout=30)
        out = (r.stdout or "") + (r.stderr or "")
        passed = ("STATUS: OK" in out) and ("mutated" not in out) and ("FAIL" not in out)
        return {"pass": bool(passed), "output": out.strip()[:1200]}
    except Exception as e:
        return {"pass": None, "output": f"error: {e}"}


# ---------- outbox ----------
def write_outbox(filename, text):
    safe = re.sub(r"[^A-Za-z0-9_.\-]", "_", filename or "draft.md")
    if not safe.endswith(".md"):
        safe += ".md"
    p = OUTBOX / safe
    header = ("---\nstatus: PAUSED\ndelivery_state: PAUSED\nhuman_authorization_required: true\n---\n\n"
              "> PAUSED — Saia is the only publisher. Review before sending/posting.\n\n")
    p.write_text(header + (text or ""), encoding="utf-8")
    return {"ok": True, "path": str(p)}


# ---------- shared memory ----------
def read_memory():
    """Return SHARED_MEMORY.md as both raw markdown and a parsed JSON structure."""
    try:
        if not SHARED_MEM.exists():
            return {"ok": False, "error": "SHARED_MEMORY.md not found"}
        raw = SHARED_MEM.read_text(encoding="utf-8")
        # Parse frontmatter
        meta = {}
        m = re.match(r"^---\n(.*?)\n---\n", raw, re.S)
        if m:
            for line in m.group(1).splitlines():
                if ":" in line:
                    k, _, v = line.partition(":")
                    meta[k.strip()] = v.strip().strip('"')
        # Parse agent log table rows
        log_rows = []
        in_log = False
        for line in raw.splitlines():
            if line.strip().startswith("| UTC Timestamp"):
                in_log = True
                continue
            if in_log and line.strip().startswith("|---|"):
                continue
            if in_log and line.startswith("|"):
                parts = [p.strip() for p in line.strip().strip("|").split("|")]
                if len(parts) >= 4:
                    log_rows.append({"ts": parts[0], "agent": parts[1],
                                     "action": parts[2], "note": parts[3]})
            elif in_log and not line.startswith("|"):
                in_log = False
        return {"ok": True, "meta": meta, "markdown": raw,
                "log": log_rows, "size": len(raw)}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def append_memory_log(agent: str, action: str, note: str):
    """Delegate log append to memory_sync.py, fallback to direct write if script missing."""
    import datetime as dt
    ts = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        if MEMORY_SYNC.exists():
            result = subprocess.run(
                [sys.executable, str(MEMORY_SYNC), "--log", agent, action, note],
                capture_output=True, text=True, timeout=10
            )
            return {"ok": result.returncode == 0, "ts": ts,
                    "output": (result.stdout + result.stderr).strip()[:400]}
        # Fallback: direct append
        if not SHARED_MEM.exists():
            return {"ok": False, "error": "SHARED_MEMORY.md not found"}
        row = f"| {ts} | {agent} | {action} | {note} |"
        text = SHARED_MEM.read_text(encoding="utf-8")
        LOG_SEP = "|---|---|---|---|"
        if LOG_SEP in text:
            idx = text.index(LOG_SEP) + len(LOG_SEP) + 1
            text = text[:idx] + row + "\n" + text[idx:]
        else:
            text += f"\n{row}\n"
        SHARED_MEM.write_text(text, encoding="utf-8")
        return {"ok": True, "ts": ts, "output": "direct write (memory_sync.py not found)"}
    except Exception as e:
        return {"ok": False, "error": str(e)}


def list_dir(rel):
    base = (VAULT / rel).resolve()
    if VAULT not in base.parents and base != VAULT:
        return {"ok": False, "error": "out of vault"}
    if not base.exists():
        return {"ok": True, "items": []}
    items = []
    for x in sorted(base.iterdir()):
        items.append({"name": x.name, "dir": x.is_dir(),
                      "size": x.stat().st_size if x.is_file() else 0})
    return {"ok": True, "items": items}


# ---------- HTTP ----------
class H(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype="application/json"):
        b = body if isinstance(body, bytes) else json.dumps(body).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        self.end_headers()
        self.wfile.write(b)

    def log_message(self, *a):  # quiet console
        pass

    def do_OPTIONS(self):
        self._send(204, b"")

    def do_GET(self):
        try:
            u = urlparse(self.path)
            q = parse_qs(u.query)
            if u.path in ("/", "/index.html", "/M7_COMMAND_CENTER.html"):
                if DASHBOARD.exists():
                    return self._send(200, DASHBOARD.read_bytes(), "text/html; charset=utf-8")
                return self._send(404, {"error": "dashboard not found"})
            if u.path == "/api/health":
                return self._send(200, {"ok": True, "vault": str(VAULT)})
            if u.path == "/api/kanban":
                return self._send(200, parse_kanban())
            if u.path == "/api/filecontent":
                rel = q.get("path", [""])[0]
                p = (VAULT / rel).resolve()
                if (VAULT == p or VAULT in p.parents) and p.is_file():
                    return self._send(200, {"ok": True, "content": p.read_text(encoding="utf-8", errors="ignore")})
                return self._send(200, {"ok": False, "content": None, "error": "not found"})
            if u.path == "/api/outbox":
                return self._send(200, list_dir("01_Command_Center/Outbox_Drafts"))
            if u.path == "/api/files":
                return self._send(200, list_dir(q.get("dir", [""])[0]))
            if u.path == "/api/memory":
                return self._send(200, read_memory())
            return self._send(404, {"error": "unknown endpoint"})
        except Exception as e:
            return self._send(500, {"error": str(e)})

    def do_POST(self):
        try:
            n = int(self.headers.get("Content-Length", 0))
            payload = json.loads(self.rfile.read(n) or b"{}")
            u = urlparse(self.path)
            if u.path == "/api/kanban/move":
                return self._send(200, move_card(payload.get("text", ""), payload.get("toColumn", "")))
            if u.path == "/api/kanban/save":
                try:
                    write_kanban(payload.get("columns", []))
                    return self._send(200, {"ok": True})
                except Exception as e:
                    return self._send(200, {"ok": False, "error": str(e)})
            if u.path == "/api/firewall":
                return self._send(200, firewall_check(payload.get("text", "")))
            if u.path == "/api/approve":
                return self._send(200, write_outbox(payload.get("filename", ""), payload.get("text", "")))
            if u.path == "/api/memory/log":
                return self._send(200, append_memory_log(
                    payload.get("agent", "unknown"),
                    payload.get("action", ""),
                    payload.get("note", ""),
                ))
            if u.path == "/api/research":
                fn = payload.get("filename", "research_brief.md")
                safe_fn = re.sub(r"[^A-Za-z0-9_.\-]", "_", fn or "research_brief.md")
                if not safe_fn.endswith(".md"):
                    safe_fn += ".md"
                dest = RESEARCH / safe_fn
                try:
                    dest.write_text(payload.get("text", ""), encoding="utf-8")
                    return self._send(200, {"ok": True, "path": str(dest)})
                except Exception as e:
                    return self._send(500, {"ok": False, "error": str(e)})
            return self._send(404, {"error": "unknown endpoint"})
        except Exception as e:
            return self._send(500, {"error": str(e)})


if __name__ == "__main__":
    print("=" * 54)
    print(" PINEAPPLE M7 — Command Center backend")
    print(f" Vault : {VAULT}")
    print(f" Open  : http://localhost:{PORT}")
    print(" Outbox Shield ON — nothing publishes or spends.")
    print(" Ctrl+C to stop.")
    print("=" * 54)
    try:
        ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
    except KeyboardInterrupt:
        print("\nstopped.")
