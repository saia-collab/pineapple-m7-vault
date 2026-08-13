---
type: knowledge_atlas
source: 2026-06-18_Master_SOP_SOURCE.md
created: 2026-06-19
agent_origin: Lead_Systems_Architect
classification: M7_Command_Level_2
---

# SOP: Ultimate Agentic OS Master Blueprint
## Claude Code + Hermes + Jarvis + Obsidian + Paperclip + WhatsApp + Gemini + NotebookLM

Distilled from Master_SOP_SOURCE. Weekly operating cadence and 1-3-12 meta strategy are governed by MASTER_PLAYBOOK.md. This SOP covers the integration and deployment procedures not documented elsewhere.

---

## Architecture Selection Matrix

| Framework | Best Used For | Analogy |
|:---|:---|:---|
| Claude Code CLI | Deep terminal work, multi-file refactoring, script dev | Senior Technical Architect |
| Hermes Agent | Rapid task routing, voice shortcuts, WhatsApp bridge | Executive Agile Assistant |
| Paperclip | Multi-agent role-play debates, editorial review, cross-functional projects | Full Corporate Boardroom |
| Gemini Stack | Live audio translation, physics mockups, local sandbox processing | Global R&D Lab |
| Agentic NotebookLM | Deep-dive research, structured file generation (PDFs, decks, spreadsheets) | Chief Research Officer |

---

## Guardrails & Workspace Permissions

- **Folder Isolation:** Full read across business workspace; automated writes anchored to designated sandbox folders only.
- **Blocked Zones (hardcoded):** `/billing/`, `/admin/`, `/credentials/`, `/private-data/` — no read, edit, move, delete, or summarize.
- **Data Pre-Scrubbing Rule:** Before uploading to NotebookLM or any external model, strip passwords, API keys, private customer financial/medical records, and unapproved client data.
- **High-Risk Sign-off Rule:** No agent may auto-deploy scripts, overwrite source files, or publish content live without human-in-the-loop authorization.

---

## Jarvis Voice + Obsidian Memory Galaxy Setup

1. Toggle Microphone Access and Voice Replies ON in Agent OS to activate Jarvis.
2. Link local Obsidian Vault to system config as the cross-agent **Memory Galaxy**.
3. Create `_AI_Memory/` folder to isolate conversation logs, decisions, and system logs.
4. Sub-directories: `_AI_Memory/SEO_Knowledge/` and `_AI_Memory/Research_Repo/` — populate with authentic business assets (case studies, testimonials, internal frameworks).

**Command Routing Shortcuts:**
- `"Brief me"` → Daily Briefing engine (scans Obsidian task files, broadcasts top 3 priorities)
- `"Build me [X]"` → Routes to local developer sandbox
- `"Remember that [X]"` → Commits snippet to `_AI_Memory/` Obsidian log
- `"Run search for [X]"` → Activates Claude Code + RipGrep for local file search

---

## WhatsApp Business Cloud API Integration

1. Register app on Meta Developers → hook to business portfolio → collect Phone Number ID, Permanent Access Token, App Secret.
2. Expose local port via Cloudflare Tunnel pointing to local Hermes instance.
3. Set webhook: paste tunnel URL + `/whatsapp/webhook`, set verify token, subscribe to `messages` field.
4. Initialize: `hermes whatsapp cloud` — provide credentials, restart service, verify with developer test number.

---

## Agentic NotebookLM Deployment (3 Phases)

### Phase A — Project Scoping
Run scoping prompt: define output type, topic, audience, goal → convert to formal Project Brief with: research questions, source tiers, excluded content farms, Definition of Done.

### Phase B — Source Inventory
- Create a dedicated notebook per project (no topic mixing).
- Run **Source Inventory Audit** before drafting: for each source list file/page name, main topic, date, key information, relevance. Flag outdated, duplicated, or unclear.
- Idea-to-Research loop: `Research this topic: [X]. Find strong sources, suggest for review before adding. Prioritize primary sources, exclude content farms and unverified social posts.`

### Phase C — Structured Asset Generation
- **Research Reports:** Cite exact source support, separate confirmed facts from interpretations, preserve contradictions.
- **Slide Decks:** 10-slide framework: title + 3-5 value points + visual motif + speaker notes per slide.
- **Spreadsheets/Data:** Strict field labels — `topic, finding, source, confidence_level, recommended_action` — one item per row.
- **HTML Layouts:** Semantic, responsive, high-contrast, mobile-friendly, zero external scripts.

---

## Gemini Functional Modules

**Module A — Gemini Live Translate:** Load target languages + industry glossary before session. Keep sentences short and declarative. Log written confirmation after every audio session.

**Module B — Project Genie & Diffusion Gemma:** Use Project Genie for visual concept walk-throughs (modify one variable at a time). Use Diffusion Gemma as offline sandbox for text formatting, regex generation, code error checks — no external API latency.

---

## AI SEO Rank Machine Loop

```
[Search Console] → Identify Quick-Wins → [Obsidian Context] → Dual Content Engine → Personalized Outreach
```

1. **Discovery:** Hermes scrapes GSC data → isolate top 20 keywords at positions 7–15 with high impressions.
2. **Dual-Engine Production:** Feed keywords to NotebookLM → generate blog article + YouTube video script simultaneously, grounded in case studies and SEO vault assets.
3. **Personalized Outreach:** Outreach subagents build hyper-tailored backlink pitches citing specific coverage of non-competing industry sites.

---

## Fusion Protocol (Multi-Agent Consensus)

1. Route objective to Agent OS Group Chat → assign distinct roles (Senior Engineer, SEO Specialist, Copywriter, Financial Auditor) to cross-examine and pressure-test the roadmap.
2. Feed output variations to a Judge Agent → strip model biases, extract top-performing structural elements, fuse into one master execution script.

---

## System Maintenance Checklist (Weekly)

1. **Audit Skills:** Uninstall any marketplace extensions or skills not delivering active daily utility.
2. **Prune Knowledge Paths:** Wipe dead chat sessions with lessons already committed to Obsidian Memory Galaxy.
3. **Verify Security Logs:** Audit Cloudflare Tunnel connections, terminal tool histories, WhatsApp webhook charts for anomalous execution runs or injection discrepancies.
4. **Token Allocation Cleanup:** Toggle off background scraping/training tasks not aligned with primary monthly objectives.

**QC Sweep Prompt (before any publish/export):**
> Audit all calculations, formulas, text strings, and formatting layouts in this project. Verify formula accuracy, percentage totals, rounding metrics, structural hierarchy, and link validity. List issues by severity with corrected wording or explicit actions for every critical item.

---


<!-- M7-FIREWALL-EXEMPT: governance-reference -->
