---
title: PM7 Cloud Recovery Audit
status: PAUSED
date: 2026-08-22
scope: GitHub repositories, uploaded handoff files, active PM7 configuration
live_windows_test: NOT TESTED
---

# PM7 cloud recovery audit

## Verdict

The repository contained a recoverable Studio/OmniRoute architecture, but the root launchers, active authority chain, model config, and secret handling were not safe or internally consistent. This recovery patch fixes those current-tree issues and adds a repeatable Windows verifier. It does not claim that the physical Windows desktop is live; that final gate requires the receipt produced by `PM7_REPAIR_AND_VERIFY.bat` on that computer.

## Sources reviewed

| Source | Audit result |
|---|---|
| `saia-collab/pineapple-m7-vault` | 3,291 indexed nodes / 2,457 files at scan time; active config plus historical material reviewed |
| `diegosouzapw/OmniRoute` | current default `release/v3.8.50`; setup, client, provider, auth, Windows, and memory guidance reviewed |
| `diegosouzapw/deepseek-harness` | separate large agent application; not required for DeepSeek routing and not recommended on the 16 GB machine now |
| Uploaded PM7 handoff DOCX | stale root, retired brand rules, malformed shell URLs, and unverified provider claims; not execution-safe |
| Uploaded troubleshooting guide | current opening rules but incomplete/truncated |
| Uploaded launchers | duplicate behavior; placeholder tokens; neither reliably starts the full Studio |
| Uploaded 2026-08-19 receipts | useful historical evidence only; not current machine proof |

The commit `a2ddc3ba443cc49e4e825fcf20495368f9957d91` has a broad restart/launcher description, but its actual committed change only removed a byte-order marker from `03_Knowledge_Mat/Areas/README.md`. Current `main` contained many later changes, so that commit cannot serve as the recovery receipt.

## Repaired

- Normalized `CLAUDE.md`, `CONTEXT.md`, `USER.md`, `m7_core_rules.config`, Command Center `AGENTS.md`, and `AGENT_READ_ME_FIRST.md` to the current 2026-08-14+ authority.
- Demoted the June master SOP and 2026-08-19 service matrix to historical evidence.
- Replaced root Studio, free-routed, and paid Claude launchers with distinct, fail-closed behavior.
- Added one-click client configuration and one-click start/retest launchers.
- Replaced invented Ollama defaults with automatic OmniRoute routes plus runtime discovery.
- Updated Hermes routing guidance to use the live catalog and current authentication state.
- Added a Windows PowerShell verifier that writes dated, secret-free PAUSED receipts.
- Added dependency-free static tests and a Windows GitHub workflow to parse the PowerShell scripts.
- Changed the dashboard's hardcoded Obsidian token to per-tab session input and updated its active prompts/palette.

## Security findings

Four plaintext credential types were found in the public current tree and removed/replaced:

1. Obsidian Local REST API token
2. OpenAI project key in an imported notebook
3. Google API key in a Gemini workflow template
4. Omega Indexer API key in a third-party SEO template

All four must be revoked/rotated. Current-tree cleanup cannot revoke a credential or remove it from existing Git history.

Post-repair targeted scans found zero live matches for those credential shapes in the corrected targets. Hashes used as file checksums, workflow instance IDs, and Gravatar identifiers were classified as non-secret evidence and retained.

## Verification completed in the cloud workspace

| Check | Result |
|---|---|
| Python compile: `m7_doctor.py` | PASS |
| JSON parse: `models.json` | PASS |
| Dependency-free recovery unit tests | PASS — 6/6 |
| Changed-file brand-firewall scan | PASS — 0 violations |
| Credential regression scan | PASS — 0 targeted live credentials |
| Git whitespace/error check | PASS |
| Windows PowerShell parse | PENDING GitHub Windows runner |
| Physical Windows services and model generation | NOT TESTED — requires desktop |

## Historical-content debt

A final full non-mutating brand-firewall scan found 1,224 flags across 368 files: 655 retired-lexicon warnings and 569 palette/critical references. Most are imported resources, old receipts, historical playbooks, and dated drafts. They were not bulk-mutated because doing so would corrupt evidence and third-party reference packs. The new authority chain explicitly demotes them. Any old draft selected for publication must be re-grounded and rechecked before Saia can approve it.

## Final Windows acceptance

After this patch is approved and pulled:

1. Rotate the four exposed credentials.
2. Install/update OmniRoute from its official package.
3. Run `LAUNCH_PM7_STUDIO.bat`.
4. Run `CONFIGURE_PM7_AI_CLIENTS.bat`.
5. Run `PM7_REPAIR_AND_VERIFY.bat`.
6. Review the newest local receipt. Studio, Hermes, OmniRoute, and the three automatic model routes must pass or show the exact authentication blocker.

No content was published, no message was sent, and no ad spend was changed.

<!-- M7-FIREWALL-EXEMPT: audit-evidence -->
