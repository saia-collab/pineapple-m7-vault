"""
M7 MOBILE SNAPSHOT
Writes 01_Command_Center/MOBILE_STATUS.md (+ .json) so Saia has live,
phone-readable oversight of the M7 build via the Drive-synced vault.
No Drive API calls needed — Drive's own desktop sync client pushes this
file to the cloud automatically because it lives inside the vault root.

Place at: 04_Tech_Lab/Scripts/m7_mobile_snapshot.py
Ko e hala 'o e fononga ko e faka'apa'apa.
"""

import json
import os
import glob
import datetime

ROOT = os.environ.get("M7_ROOT", r"C:\Pineapple Contractors M7")
CC = os.path.join(ROOT, "01_Command_Center")
TL = os.path.join(ROOT, "04_Tech_Lab")
OUTBOX = os.path.join(CC, "Outbox_Drafts")


def read_json(path, default=None):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return default if default is not None else {}


def tail(path, n=10):
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        return "".join(lines[-n:]).strip()
    except Exception:
        return "(no log yet)"


def outbox_inventory():
    if not os.path.isdir(OUTBOX):
        return []
    items = []
    for f in sorted(glob.glob(os.path.join(OUTBOX, "*")), key=os.path.getmtime, reverse=True):
        if os.path.isfile(f):
            items.append({
                "name": os.path.basename(f),
                "modified": datetime.datetime.fromtimestamp(os.path.getmtime(f)).strftime("%Y-%m-%d %H:%M"),
            })
    return items[:15]


def main():
    now = datetime.datetime.now()
    sync_status = read_json(os.path.join(CC, "sync_status.json"))
    scoring = read_json(os.path.join(TL, "logs", "last_scoring.json"))
    outbox = outbox_inventory()
    log_tail = tail(os.path.join(TL, "logs", "daily_sync_log.md"))

    lines = [
        "---",
        "type: mobile_status_snapshot",
        f"generated: {now.isoformat(timespec='minutes')}",
        'color_primary: "#1A365D"',
        'color_secondary: "#FBC02D"',
        "---",
        "",
        "# 🍍 M7 MOBILE STATUS",
        f"_Last snapshot: {now.strftime('%a %Y-%m-%d %H:%M')}_",
        "",
        "## Outbox Shield",
        f"- State: **{sync_status.get('outbox_shield', 'UNKNOWN')}**",
        f"- Last daily sync: {sync_status.get('last_sync', 'unknown')}",
        "",
        f"## Outbox Drafts awaiting your GO ({len(outbox)})",
    ]
    if outbox:
        for item in outbox:
            lines.append(f"- [ ] {item['name']}  _(modified {item['modified']})_")
    else:
        lines.append("- Nothing waiting. Outbox is clear.")

    lines += ["", "## Avatar / Lead Telemetry (last scoring run)"]
    if scoring:
        lines.append("```")
        lines.append(json.dumps(scoring, indent=2)[:1200])
        lines.append("```")
    else:
        lines.append("- No scoring data yet.")

    lines += ["", "## Daily Sync Log (tail)", "```", log_tail, "```", "",
              "Ko e hala 'o e fononga ko e faka'apa'apa.", "",
              "<!-- M7-FIREWALL-EXEMPT: governance-reference -->"]

    md_path = os.path.join(CC, "MOBILE_STATUS.md")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    json_path = os.path.join(CC, "MOBILE_STATUS.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "generated": now.isoformat(timespec="minutes"),
            "outbox_shield": sync_status.get("outbox_shield", "UNKNOWN"),
            "last_sync": sync_status.get("last_sync"),
            "outbox_drafts_pending": len(outbox),
            "outbox_drafts": outbox,
            "scoring": scoring,
        }, f, indent=2)

    print(f"[M7] Mobile snapshot written: {md_path}")


if __name__ == "__main__":
    main()
