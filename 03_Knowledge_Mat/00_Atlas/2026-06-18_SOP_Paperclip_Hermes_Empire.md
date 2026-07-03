---
type: knowledge_atlas_sop
title: M7 — Paperclip + Hermes One-Person AI Empire + Local Memory Bridge
status: active
created: 2026-06-18
agent_origin: distilled_from_uploaded_SOPs
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# SOP — PAPERCLIP + HERMES + LOCAL MEMORY BRIDGE

Distilled from the uploaded Paperclip/Hermes/Memory-Bridge/Master SOPs. Full sources in `03_Knowledge_Mat/raw/`.

## 1. Paperclip — the content engine
- Paperclip turns a single idea/source into a batch of repurposed assets (posts, scripts, emails) on a schedule.
- M7 role: feeds the 1-3-12 creative batch. Outputs land as DRAFTS only; the Brand Firewall mutates banned lexicon and the Outbox Shield keeps everything PAUSED until you publish.
- Add to fleet: a `paperclip` entry in `04_Tech_Lab/config/models.json` so its status shows on the dashboard.

## 2. Hermes — the orchestrator
- 24/7 daemon (see `04_Tech_Lab/scripts/m7_hermes_daemon.sh`, launch via `HERMES_COMMAND_CENTER.bat`).
- Plans goals, routes sub-tasks, writes lineage/heartbeats, reads the Obsidian vault via MCP.
- 64k context required for big jobs (set in models.json / `hermes config set model.context_length 65536`).

## 3. Local Memory & Execution Bridge
- Obsidian vault = persistent memory. MCP (Local REST API, port 27124) = the bridge agents read/write through.
- "Remember that…" → structured markdown into the vault. Nightly consolidation parses the day's notes/OMI streams into client nodes.
- The bridge is what lets Claude Code / Hermes act with real business context instead of cold prompts.

## 4. One-Person AI Empire loop
Capture (OMI / Paperclip) → Vault (Obsidian memory) → Orchestrate (Hermes) →
Execute (Claude Code / scripts) → Compliance (Brand Firewall) → Outbox (PAUSED) →
Human publish → Track (scorer + dashboard) → Double down. Repeat daily via the auto-sync.

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
