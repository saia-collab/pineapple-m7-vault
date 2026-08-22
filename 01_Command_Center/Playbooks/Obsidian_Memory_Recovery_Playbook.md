---
title: Obsidian Memory Recovery Playbook
status: active
date: 2026-08-22
owner: Saia
scope: Windows 11, PM7 Obsidian, Local Studio memory, agent access
---

# Obsidian memory recovery playbook

## Purpose

Use this playbook when Obsidian hangs, the graph never finishes loading, Local Studio shows a stuck memory graph, or an AI client cannot reach the PM7 knowledge vault. This procedure preserves every note. It resets only Obsidian's saved window/workspace state and narrows Local Studio's memory index to the knowledge folder.

## PM7 memory contract

| Layer | Authoritative location | Role |
|---|---|---|
| Project workspace | `C:\Pineapple Contractors M7` | Git repository, launchers, campaigns, media references, code |
| Shared AI memory | `C:\Pineapple Contractors M7\03_Knowledge_Mat` | focused graph/index scope for Local Studio and AI retrieval |
| Boot memory | `03_Knowledge_Mat\SHARED_MEMORY.md` | current rules every agent reads before work |
| Memory contract | `03_Knowledge_Mat\OBSIDIAN_MEMORY_CONTRACT.md` | focused Obsidian/Agent OS recovery authority |
| Live execution state | `_memory\` | active phase/router state; not a replacement for shared memory |
| Obsidian UI state | `.obsidian\workspace.json` | disposable layout state; not business knowledge |

The full project stays where it is. Do not bulk-move or reorganize notes during recovery. Local Studio's `vaultRoot` should target `03_Knowledge_Mat` so its graph does not index build output, media, vendor packages, Git metadata, or thousands of unrelated files.

## Hermes / Agent OS Memory Galaxy

The supplied Hermes/Agent OS guide confirms that the Memory Galaxy reads the folder named by `%USERPROFILE%\.agentic-os\config.json`. PM7 intentionally replaces the Mac examples with this Windows configuration:

```json
{
  "vaultRoot": "C:\\Pineapple Contractors M7\\03_Knowledge_Mat"
}
```

The recovery script preserves every other property in that JSON, makes a timestamped backup, and changes only `vaultRoot`. After the script finishes, restart Local Studio and verify that the Memory tab contains notes from `03_Knowledge_Mat`. Jarvis/Hermes answers must identify the notes used; a populated galaxy alone does not prove retrieval quality.

Privacy correction: graph building can be local, but any question sent to a cloud-hosted Claude, Gemini, DeepSeek, Kimi, GLM, MiniMax, or other provider can transmit selected note content to that provider. Only an intentionally local runtime such as Ollama keeps model inference on the computer. Features that save Pipeline, Journal, Jarvis, or Notebook output are write operations and remain subject to the Outbox Shield and project-folder rules.

## One-click recovery

From the project root, double-click:

`PM7_OBSIDIAN_RECOVER.bat`

The launcher performs these controlled actions:

1. Resolves the project root and stops if it is missing.
2. Closes every running Obsidian process gracefully, then terminates only remaining Obsidian processes.
3. Preserves an older backup if present, then renames `.obsidian\workspace.json` to `.obsidian\workspace.json.bak`.
4. Verifies `.obsidian\plugins\obsidian-local-rest-api` without reading or printing any configuration value.
5. Verifies whether the plugin id is enabled.
6. Backs up `%USERPROFILE%\.agentic-os\config.json` and changes only `vaultRoot` to `03_Knowledge_Mat`.
7. Restarts Obsidian and probes the loopback HTTPS service on `127.0.0.1:27124`.
8. Writes a secret-free, dated receipt to `01_Command_Center\Outbox_Drafts`.

If the launcher returns attention/failure, open the newest `PM7_OBSIDIAN_MEMORY_RECOVERY_*.md` receipt. Fix only the named failed row, then rerun the same launcher.

## Local REST API security and rotation

The supported plugin is `coddingtonbear/obsidian-local-rest-api`. Keep it on loopback HTTPS at `https://127.0.0.1:27124`. Do not expose it through router forwarding, tunnels, remote dashboards, or the public internet. Do not enable unencrypted port `27123` as a workaround.

Because an earlier credential appeared in the public repository, Saia must rotate it on the Windows desktop:

1. Open Obsidian after the workspace recovery.
2. Open **Settings → Community plugins → Local REST API → Settings**.
3. Select **Reset all cryptography** and confirm.
4. Treat the new value as a secret. Never paste it into GitHub, a Markdown file, BAT/PowerShell source, screenshots, chat, or a receipt.
5. Reconnect only approved local clients and revoke/remove their old Local REST configuration.

Important: **Re-generate certificates** alone changes certificates but does not rotate the API credential. Use **Reset all cryptography** for this incident.

## Agent access policy

Direct filesystem access is the primary PM7 memory path. Local REST/MCP is optional interactive access and must remain read-first.

| Client | PM7 memory path | Model path | Status/policy |
|---|---|---|---|
| Claude Code | read `CLAUDE.md`, `CONTEXT.md`, then `SHARED_MEMORY.md`; optional local MCP | paid subscription or OmniRoute launcher | local writes require Saia approval and Outbox Shield |
| Codex CLI / ChatGPT desktop Codex | same boot files; optional Streamable HTTP MCP | native Codex or approved route | bearer value must come from a local environment variable, never tracked TOML |
| ChatGPT web/cloud | GitHub/attached files only | OpenAI cloud | cannot access Windows `localhost`; never claim a local test from the web |
| Hermes | direct focused vault/file access | OmniRoute or approved provider | orchestration only; no unsupervised publishing |
| Cursor / OpenCode | repository files and shared boot memory | OmniRoute OpenAI-compatible endpoint | app/client setup must be verified separately |
| Ollama | no memory authority | optional small local model runtime | optional on the 16 GB computer; never auto-pull a model |

For Codex CLI/desktop, the approved local configuration pattern is:

```toml
[mcp_servers.obsidian]
url = "https://127.0.0.1:27124/mcp/"
bearer_token_env_var = "OBSIDIAN_REST_API_KEY"
```

The value of `OBSIDIAN_REST_API_KEY` is set only in the local session or a protected OS credential mechanism. ChatGPT web does not read this local Codex configuration.

## Codex guide corrections for PM7

The supplied “How To Build And Automate Anything With ChatGPT Codex” guide is useful inspiration but is not an execution SOP. Apply these PM7 corrections:

- Use the existing PM7 project for PM7 recovery; do not create a second competing PM7 folder. Create separate folders only for genuinely separate apps.
- Keep approval prompts on for repository changes, credentials, WordPress, email, publishing, ads, or destructive actions. “Full Access” is not the PM7 default.
- Plugins/connectors remain permission-scoped and revocable; installing one does not make an agent permanently or universally capable.
- A scheduled cloud automation is different from a Windows-local task. Anything that must open Obsidian, use `localhost`, or change `C:\Pineapple Contractors M7` needs an available local/remote execution host.
- Never install a skill directly from a video or unknown GitHub link. Pin, inspect, test, and approve the artifact first.
- “Self-improving” means proposing version-controlled changes with tests and human review. No skill may rewrite itself or publish output autonomously.
- OmniRoute is an optional provider gateway, not an unlimited-token guarantee and not a replacement for native Codex access.

## What was reviewed but not installed

The following projects are reference material, not PM7 runtime authority:

- `AgriciDaniel/claude-obsidian`: useful non-destructive capture, transaction, retrieval, and audit patterns. Its Windows write workflow expects WSL, so a full install would add complexity while PM7 is unstable.
- `AgriciDaniel/fablesecondbrain`: advisory research-brain patterns; not a production memory service.
- `AgriciDaniel/secretary`: experimental governance/controller patterns; not approved for live PM7 mutation.
- `AgriciDaniel/deepseek-harness-brain`: advisory DeepSeek Harness snapshot; not required for OmniRoute or Obsidian.
- `awesome-deepseek-harness` and `awesome-deepseek-harness-plugins`: discovery lists, not packages to bulk-install.

Uploaded model/playbook notes are research leads. Mac-only commands, claimed future model names, provider counts, prices, privacy claims, and “nothing leaves the computer” claims must be reverified. A local gateway does not make cloud-model prompts local or private.

New research references received on 2026-08-22:

- Codex workflow video: `https://youtu.be/VVvDjwyjBlw`
- Hermes/Obsidian Memory Galaxy video: `https://youtu.be/kobM9Z1FQZM`
- supplied “How To Build And Automate Anything With ChatGPT Codex” notes
- supplied “The Memory Galaxy + Your Obsidian Vault” notes

The videos and supplied notes explain intended workflows; they are not proof of the installed PM7 build, current OpenAI behavior, privacy, provider availability, or successful Windows execution.

## Acceptance test

Recovery is complete only when a fresh Windows receipt records:

- Obsidian processes were stopped before the reset;
- `workspace.json` was backed up or was already absent;
- the official Local REST plugin folder exists and is enabled;
- Local Studio memory scope is `03_Knowledge_Mat`;
- after Local Studio restarts, the Memory Galaxy renders linked notes from `03_Knowledge_Mat` and a Jarvis/Hermes retrieval test identifies its source note;
- Obsidian restarts without the hour-long loading freeze;
- Local REST loopback HTTPS is listening on `27124` if the plugin is enabled;
- the replacement credential has been rotated by Saia and was not written to a file;
- `PM7_REPAIR_AND_VERIFY.bat` separately verifies Studio `:3737`, Hermes `:9119`, OmniRoute `:20128`, and live automatic routes.

No cloud agent may mark the Windows runtime complete. The dated desktop receipts are the proof.

## Rollback

If the clean Obsidian workspace is worse:

1. Close Obsidian.
2. Rename the newly created `.obsidian\workspace.json` to a timestamped diagnostic name.
3. Rename `.obsidian\workspace.json.bak` back to `.obsidian\workspace.json`.
4. Restart Obsidian.

This restores only the prior UI layout. Notes are never part of this rollback.

## Sources

- Official Local REST API repository and documentation: `https://github.com/coddingtonbear/obsidian-local-rest-api`
- Official Codex MCP configuration: `https://learn.chatgpt.com/docs/extend/mcp?surface=cli`
- PM7 routing recovery: `01_Command_Center/M7_SYSTEM_RECOVERY_AND_ROUTING_SOP_2026-08-22.md`
- Focused memory contract: `03_Knowledge_Mat/OBSIDIAN_MEMORY_CONTRACT.md`

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
