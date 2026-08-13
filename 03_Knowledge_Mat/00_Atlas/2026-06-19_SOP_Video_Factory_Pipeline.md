---
type: knowledge_atlas
source: 2026-06-18_SOP_Agent_OS_Rank1_Video_Factory_SOURCE.md
created: 2026-06-19
agent_origin: Lead_Systems_Architect
classification: M7_Command_Level_2
---

# SOP: AI Agent OS — Video Factory Pipeline (Google Flow + Claude Code)

Distilled from SOP_Agent_OS_Rank1_Video_Factory_SOURCE. Covers the Google Flow video production layer and multi-model crew routing not documented in MASTER_PLAYBOOK.md.

---

## Mission Control Dashboard Layout (3-Panel)

| Panel | Contents |
|:---|:---|
| **Left** | Active Agents/Sub-agents, Connected MCP Tools, AutoSync Cloud Folders, Brand Layout Configurations |
| **Center** | Main Claude Code Terminal, Live Google Flow Project Interface, Document Workspace |
| **Right** | Live Video Previews, Interactive Canvas Testing, Dynamic Workflow Trees, Memory Logs |

---

## Multi-Model Crew Routing Matrix

| Task Type | Recommended Model |
|:---|:---|
| Premium strategy, complex code, elite quality review, swarm orchestration | Claude Opus (latest) via terminal |
| Aesthetic prototyping, landing page wireframes, digital design | Claude Design layer |
| Multimedia production, scene generation, clip sequencing | Google Flow Agent |
| High-speed bulk text creation, draft iterations | Hermes / GLM / Kimi variants |
| File system ops, background scripts, repository tracking, local tool search | Local Hermes configurations |

---

## NotebookLM AutoSync Business Infrastructure

1. Connect NotebookLM terminal layout to core operational Google Drive directory.
2. Toggle **AutoSync ON** — document updates are dynamically processed without manual re-uploading.
3. **Source-Grounded Querying:** Enforce parameters requiring the AI to answer exclusively from the synced source pool to eliminate hallucination.

---

## Google Flow AI Video Factory Pipeline

```
[GDrive AutoSync Data] → [Plan & Script] → [Batch Scene Generation] → [Brand Style Edit] → [Organize & Review]
```

### Phase 1 — Initialize Agent
Open Google Flow module, explicitly engage:
> "Turn on Google Flow Agent inside this project so it can help me plan, create, edit, and organize my video."

### Phase 2 — Grounded Scripting
> "Help me plan a 30-second promotional video about the topic in our active research note. Give me a clear scene-by-scene outline, then write a conversational, human script for the host."

### Phase 3 — Batch Scene Generation
> "Create 5 different opening shot options for this script. Tell me which is strongest for our conversion goal, then build subsequent scenes with identical visual style and character consistency."

### Phase 4 — Asset & Character Continuity
Use strict `@mention` reference variables (character anchors) for visual avatar consistency across scene transitions. Never regenerate without the anchor reference.

### Phase 5 — Brand Style Edit & Review
Apply brand palette (Royal Navy `#1A365D` / Pineapple Gold `#FBC02D`) to all overlays. Run brand_firewall.py before export. Review final cuts against the 50/5/3 Lego Video Engine spec (MASTER_PLAYBOOK.md).

---

## Keyword Fueling (Before Any Automation Loop)

Before triggering automation loops, isolate high-intent long-tail keywords from:
- Google Autocomplete suggestions
- Google Search Console pages 2–5 with high impressions and low CTR

Feed these into the pipeline as the seed layer for all content and video generation.

---


<!-- M7-FIREWALL-EXEMPT: governance-reference -->
