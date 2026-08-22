---
title: PM7 OmniRoute Recovery — Meeting Report
status: PAUSED
date: 2026-08-22
owner_action_required: yes
---

# PM7 OmniRoute recovery — meeting report

## Executive answer

The GitHub recovery configuration is prepared for Local Studio, OmniRoute, Claude Code, Codex, Cursor, OpenCode, Gemini CLI, Google AI Studio provider access, and Antigravity. It is not honest to call those tools installed or live-tested on the Windows computer yet. Claude Code confirmed that the recovery branch was absent locally and safely stopped. After this draft PR is reviewed and merged, the Windows launchers will configure the clients from the live OmniRoute catalog and generate a local verification receipt.

## Completed in the recovery branch

- Corrected the conflicting PM7 authority/brand boot chain.
- Repaired separate Studio, OmniRoute-routed Claude, and Claude subscription launchers.
- Added live-catalog setup for Claude Code, Codex, OpenCode, and Cursor.
- Added Gemini CLI launch through OmniRoute.
- Added a safe Google Gemini/Google AI Studio/Antigravity setup launcher that requires the owner's OAuth/key step, keeps Antigravity paid credits off, and rejects MITM/stealth modes.
- Replaced invented local model names with `auto/best-chat`, `auto/best-coding`, and `auto/best-reasoning` plus live catalog discovery.
- Kept Ollama optional for the 16 GB computer; no automatic large-model downloads.
- Removed exposed Obsidian, OpenAI, Google, and Omega Indexer credentials from current targets; all four still require rotation.
- Added a one-click Windows repair/verifier and dependency-free tests.

## Configuration status by tool

| Tool | GitHub configuration | Windows installed/authenticated | Live generation test |
|---|---|---|---|
| OmniRoute | prepared for `:20128` | NOT TESTED | NOT TESTED |
| Claude Code via OmniRoute | `setup-claude` + `omniroute launch` prepared | NOT TESTED | NOT TESTED |
| Claude subscription | isolated paid launcher prepared | NOT TESTED | NOT TESTED |
| Codex via OmniRoute | `setup-codex` + `launch-codex` prepared | NOT TESTED | NOT TESTED |
| Cursor | upstream setup plus required GUI steps prepared | NOT TESTED | NOT TESTED |
| OpenCode | `setup-opencode` prepared | NOT TESTED | NOT TESTED |
| Gemini CLI | `omniroute run gemini` launcher prepared | NOT TESTED | NOT TESTED |
| Google AI Studio key | safe OmniRoute provider-dashboard path prepared | OWNER LOGIN REQUIRED | NOT TESTED |
| Antigravity | safe OAuth path prepared; paid credits/MITM blocked | OWNER LOGIN REQUIRED | NOT TESTED |
| Ollama | optional runtime discovery only | NOT TESTED | NOT TESTED |
| DeepSeek/Kimi/GLM/MiniMax | use only live OmniRoute providers/models | PROVIDER LOGIN MAY BE REQUIRED | NOT TESTED |
| DeepSeek Harness | intentionally deferred as developer-preview experiment | NOT INSTALLED | NOT TESTED |

## Required completion order after PR review

1. Claude fetches and reviews the draft PR without touching its dirty local `main`.
2. Saia gives GO to merge.
3. Resolve Google Drive/Git file movement before pulling.
4. Pull the approved recovery.
5. Run `LAUNCH_PM7_STUDIO.bat`.
6. Run `CONFIGURE_PM7_AI_CLIENTS.bat`.
7. Run `CONFIGURE_PM7_GOOGLE_AI.bat` and complete the owner-only Google/Antigravity login.
8. Run `PM7_REPAIR_AND_VERIFY.bat`.
9. Accept completion only from the new Windows receipt showing ports and model outputs.

## Meeting bottom line

The wiring and safety controls are prepared. The physical Windows connections and free-provider availability are the final test—not a completed fact. No publishing, sending, advertising spend, secret disclosure, forced paid credits, Docker installation, or DeepSeek Harness installation was performed.

<!-- M7-FIREWALL-EXEMPT: audit-report -->
