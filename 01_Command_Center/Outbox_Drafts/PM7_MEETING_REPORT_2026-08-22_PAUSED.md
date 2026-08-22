---
title: PM7 OmniRoute Recovery — Meeting Report
status: PAUSED
date: 2026-08-22
owner_action_required: yes
---

# PM7 OmniRoute recovery — meeting report

## Executive answer

The recovery branch is now published in [draft PR #2](https://github.com/saia-collab/pineapple-m7-vault/pull/2), and its Windows GitHub Actions check passed. The configuration is prepared for Local Studio, OmniRoute, Claude Code, Codex, Cursor, OpenCode, Gemini CLI, Google AI Studio provider access, and Antigravity. It is not honest to call those tools installed, authenticated, or live-tested on the Windows computer yet. Claude Code confirmed that the recovery branch was absent locally and safely stopped. After PR review and owner approval, the Windows launchers will configure the clients from the live OmniRoute catalog and generate a local verification receipt.

## Publication and validation status

- Draft PR: [PM7 OmniRoute recovery: launchers, routing, security, and Windows verification](https://github.com/saia-collab/pineapple-m7-vault/pull/2)
- Branch: `codex/pm7-omniroute-recovery-20260822`
- Recovery implementation commit: `e60bf81a3fc370d3b3c6834ca0cfaeb93c80730d`
- Windows GitHub Actions: **PASSED** for the recovery and report update
- Main branch: unchanged
- Merge status: **PAUSED — Claude review, credential rotation, owner GO, and real Windows verification required**

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

1. Claude fetches and reviews draft PR #2 without touching its dirty local `main`.
2. Revoke and rotate the four previously exposed credentials.
3. Resolve Google Drive/Git file movement before pulling.
4. Saia gives GO to merge only after the review is accepted.
5. Pull the approved recovery.
6. Run `LAUNCH_PM7_STUDIO.bat`.
7. Run `CONFIGURE_PM7_AI_CLIENTS.bat`.
8. Run `CONFIGURE_PM7_GOOGLE_AI.bat` and complete the owner-only Google/Antigravity login.
9. Run `PM7_REPAIR_AND_VERIFY.bat`.
10. Accept completion only from the new Windows receipt showing ports and model outputs.

## Meeting bottom line

The wiring and safety controls are prepared. The physical Windows connections and free-provider availability are the final test—not a completed fact. No publishing, sending, advertising spend, secret disclosure, forced paid credits, Docker installation, or DeepSeek Harness installation was performed.

<!-- M7-FIREWALL-EXEMPT: audit-report -->
