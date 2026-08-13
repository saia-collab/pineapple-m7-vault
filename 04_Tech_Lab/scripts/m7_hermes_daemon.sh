#!/usr/bin/env bash
# =============================================================================
# M7 HERMES DAEMON — persistent 24/7 orchestrator loop.
# Keeps the Hermes agent + M7 engine alive, re-arms the brand firewall watcher,
# and runs the telemetry refresh on a cron-like interval. Outbox Shield enforced:
# this daemon NEVER publishes live or moves money.
# =============================================================================
set -euo pipefail
ROOT="${M7_ROOT:-/c/Pineapple Contractors M7}"
SCRIPTS="$ROOT/04_Tech_Lab/Scripts"
INTERVAL="${M7_INTERVAL:-900}"   # 15 minutes

log(){ echo "[hermes-daemon $(date -u +%H:%M:%S)] $*"; }

log "starting — root: $ROOT"

# 1) Arm the brand firewall live listener (background)
python "$SCRIPTS/brand_firewall.py" --root "$ROOT" --watch --fix &
FW_PID=$!
log "brand firewall listener pid=$FW_PID"

# 2) Start the M7 engine (dashboard + APIs) if not already up
if ! curl -s -m2 http://localhost:3000/api/metrics >/dev/null 2>&1; then
  node "$ROOT/04_Tech_Lab/server.js" &
  log "engine started pid=$!"
fi

cleanup(){ log "stopping"; kill "$FW_PID" 2>/dev/null || true; exit 0; }
trap cleanup INT TERM

# 3) Recurring loop: refresh telemetry + ingest any dropped skill zips
while true; do
  python "$SCRIPTS/m7_scoring.py" --demo > "$ROOT/04_Tech_Lab/logs/last_scoring.json" 2>&1 || true
  python "$SCRIPTS/m7_skill_intake.py" --root "$ROOT" >/dev/null 2>&1 || true
  log "cycle complete — sleeping ${INTERVAL}s"
  sleep "$INTERVAL"
done
