# INTENT: Route completed files from 03_Knowledge_Mat/raw/ into 01_Command_Center/Outbox_Drafts/
# with domain isolation — Cowboys Supplements or cross-brand files are rejected and logged.
import os
import shutil
import datetime

ROOT        = r"C:\Pineapple Contractors M7"
RAW_IN      = os.path.join(ROOT, "03_Knowledge_Mat", "raw")
OUTBOX      = os.path.join(ROOT, "01_Command_Center", "Outbox_Drafts")
LOG_FILE    = os.path.join(ROOT, "knowledge-base", "wiki", "log.md")

# Keywords that trigger domain rejection (Cowboys Supplements firewall)
REJECT_KEYWORDS = [
    "cowboys supplements", "supplement", "nutrition", "protein", "vitamin",
    "cowboys brand", "cowboys health",
]

def log(msg: str):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"- [{ts}] {msg}\n"
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)
    print(entry.strip())

def is_rejected(filepath: str) -> bool:
    """Return True if the file contains cross-brand / Cowboys Supplements content."""
    name_lower = os.path.basename(filepath).lower()
    for kw in REJECT_KEYWORDS:
        if kw in name_lower:
            return True
    # Scan text file contents for keyword hits
    if filepath.endswith((".md", ".txt", ".html", ".json", ".csv")):
        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read().lower()
            for kw in REJECT_KEYWORDS:
                if kw in content:
                    return True
        except OSError:
            pass
    return False

def route_raw_to_outbox():
    if not os.path.isdir(RAW_IN):
        log(f"[ERROR] Raw input directory not found: {RAW_IN}")
        return

    os.makedirs(OUTBOX, exist_ok=True)
    files = [f for f in os.listdir(RAW_IN) if not f.startswith(".")]

    if not files:
        log("[INGEST ROUTER] No files in raw/ — nothing to route.")
        return

    routed  = 0
    rejected = 0

    for filename in files:
        src = os.path.join(RAW_IN, filename)

        if is_rejected(src):
            log(f"[DOMAIN REJECT] @scout blocked cross-brand file: {filename}")
            rejected += 1
            continue

        # Stamp output with DRAFT prefix per DEC-005 Outbound Safety Gate
        ts_prefix = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        out_name  = f"DRAFT — DO NOT SEND — {ts_prefix}_{filename}"
        dst       = os.path.join(OUTBOX, out_name)

        shutil.copy2(src, dst)
        log(f"[INGEST ROUTER] Routed: {filename} → Outbox_Drafts/{out_name}")
        routed += 1

    log(f"[INGEST ROUTER] Complete — {routed} routed, {rejected} domain-rejected.")

if __name__ == "__main__":
    route_raw_to_outbox()
