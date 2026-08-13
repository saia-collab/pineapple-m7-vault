---
type: knowledge_atlas_sop
title: M7 Agent Tooling & Execution Environments
status: active
created: 2026-06-17
agent_origin: distilled_from_uploaded_playbooks
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# SOP — M7 AGENT TOOLING & EXECUTION ENVIRONMENTS

Distilled from the uploaded Claude Project Playbook + YouTube analyses. Full sources in `03_Knowledge_Mat/raw/`.

## 1. Which environment to execute in (zero copy-paste)
| Tool | Use it for | Note |
| :--- | :--- | :--- |
| **Claude Code (CLI)** | Autonomous file/folder/script execution in the vault | Lowest learning curve; `.claude/settings.json` already permissioned. Best fit. |
| **Cursor IDE (Agent/Composer)** | Visual multi-file editing with `@file` refs + built-in terminal | Great GUI; MCP-capable; separate agent from Claude Code. |
| **VS Code** | Plain editing / review | Use with Claude Code CLI in its terminal. |
| **Antigravity / Hermes / NotebookLM / Ollama** | Model/agent *endpoints* — NOT code editors | They are what the system runs, not where you edit. |
- Avoid web chat tabs for code ops (truncation, copy-paste corruption, Drive-sync lag).

## 2. Claude Code setup
```powershell
irm https://claude.ai/install.ps1 | iex
cd "C:\Pineapple Contractors M7"
claude            # or: claude --dangerously-skip-permissions
```
Add Obsidian as MCP:
```
claude mcp add --transport http obsidian http://127.0.0.1:27124/mcp/ --header "Authorization: Bearer YOUR_OBSIDIAN_API_KEY"
```
A root `CLAUDE.md` is auto-read each session (keep Outbox Shield + syntax-check rules there).

## 3. Aion UI — multi-agent cowork (24/7)
- Single GUI unifying Claude Code, OpenClaw, Hermes, local models via **ACP** over stdio/SSH.
- Auto-detects CLI runtimes on PATH; parallel session isolation (one context per tab).
- Leader/Teammate swarm: a reasoning leader (Claude Opus/Sonnet) plans, lightweight teammates (Qwen, Gemini Flash) execute concurrently.
- Cron scheduler: daily telemetry refresh `0 9 * * *`; hourly dedupe `0 * * * *`.

## 4. Hermes Agent + Jarvis memory
- Persistent planner daemon; voice via ElevenLabs; deep Obsidian vault index.
- "Remember that…" writes structured markdown into the vault; `curator` daemon snapshots active context.
- Daily/weekly briefings parse 01_Command_Center logs, 03_Knowledge_Mat, and Outbox_Drafts.
- **64k context fix (Qwen on Ollama):** `hermes config set model.context_length 65536` or `model.context_length: 65536` in `~/.hermes/config.yaml`, or run `deepseek-v4-flash`.

## 5. OpenClaw gateway
```powershell
iwr -useb https://openclaw.ai/install.ps1 | iex
openclaw onboard --install-daemon     # Multi-User Sandbox Lock: Yes; QuickStart; DeepSeek/Ollama
openclaw dashboard | openclaw terminal | openclaw tui
```

## 6. OMI wearable audio ingestion
- Ambient capture → diarized `.json`/`.md` transcripts → routed to root `Omi/` → Hermes parses regional intel + action items into client nodes nightly.

## 7. ANTIGRAVITY 5-Layer Orbit (see 01_Command_Center/ANTIGRAVITY_OS.md)
Capture (OMI) → Vault (Obsidian) → Intelligence (Antigravity/Gemini via MCP) → Command (Agent OS dashboard) → Loop (write back to vault to compound).


<!-- M7-FIREWALL-EXEMPT: governance-reference -->
