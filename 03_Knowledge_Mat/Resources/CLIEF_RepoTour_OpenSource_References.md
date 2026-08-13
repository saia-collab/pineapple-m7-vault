---
type: reference
title: Clief Notes — 1.4 Repo Tour (Open-Source AI-UI references)
status: reference
date: 2026-08-13
source: Clief Notes classroom (skool.com/cliefnotes) — Van Clief. Research resource, not a tutorial.
note: Study these; borrow patterns. You do NOT need to clone all of them.
---

# 📚 REPO TOUR — Open-Source AI-UI References
Curated by Van Clief. For each: what it does · what's worth studying · what to borrow. Pick the ones relevant to what you're building.

## Claude Code interfaces (if you ever build a custom front-end)
| Repo | What it is | Borrow |
|---|---|---|
| [claude-code-web-ui](https://github.com/lennardv2/claude-code-web-ui) | Browser front-end for Claude Code | **Session persistence** (close browser, resume the same convo); the websocket + streaming pattern |
| [opcode (316293/opcode)](https://github.com/316293/opcode) | Claude Code wrapper, project management | Usage tracking, multi-project switching, settings/config structure (skip the UI bloat) |
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | The official Claude Code TUI | How they parse/display output, keyboard nav |

## Custom chat UIs
| Repo | What it is | Borrow |
|---|---|---|
| [Open WebUI](https://docs.openwebui.com/) | Self-hosted multi-LLM chat | **Multi-provider abstraction** (one layer over many AI backends) — relevant to your FCC/OmniRoute routing |
| [lobe-chat](https://github.com/lobehub/lobe-chat) | Polished chat UI w/ plugins + knowledge base | Plugin architecture, file-upload/knowledge-base UX |

## Workflow / agent tools (you decided to SKIP n8n — folders replace it)
| Repo | What it is | Note |
|---|---|---|
| [n8n](https://github.com/n8n-io/n8n) | Visual node workflow automation | Studied for the visual map idea — but M7 uses **ICM folders instead of n8n** (Van Clief's whole point) |
| [langflow](https://github.com/langflow-ai/langflow) | Visual LLM app builder | Same — reference for visual workflow, not adopted |

## Design skill
- **UIUX Pro Skill** — a Claude skill (prompts, not code) that improves Claude's front-end design sense. Pairs with your `icm-architect` + design skills.

## M7 verdict (what's actually relevant to us)
- **Now:** none required — your Studio already gives you the UIs. Keep this as a reference.
- **If we build a custom M7 dashboard later:** start with `claude-code-web-ui` (session persistence) + `Open WebUI` (multi-provider abstraction, matches your free-model routing).
- **The big lesson holds:** folders (ICM) replace n8n/Langflow. You don't need the visual node builders.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
