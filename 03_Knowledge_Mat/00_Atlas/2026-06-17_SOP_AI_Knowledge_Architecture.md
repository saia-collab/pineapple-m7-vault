---
type: knowledge_atlas_sop
title: M7 AI Knowledge Architecture (Gemini Notebooks + NotebookLM + Open NotebookLM)
status: active
created: 2026-06-17
agent_origin: distilled_from_uploaded_playbooks
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# SOP — M7 AI KNOWLEDGE ARCHITECTURE

Distilled from the uploaded NotebookLM/Gemini SOP suite. Full sources captured in `03_Knowledge_Mat/raw/`. Governed by `GROUNDING.md`.

## 1. Three-Tier AI Architecture
| Layer | Platform | Function |
| :--- | :--- | :--- |
| 1. Active Second Brain | Gemini Notebooks | Project hubs: interactive planning, brand-voice copy, persistent context. |
| 2. Cloud Research Vault | NotebookLM (2.0 Agent OS) | Source-grounded, citation-backed research; agent-driven notebook building; Studio multimedia. |
| 3. Private Local Vault | Open NotebookLM + Ollama | Self-hosted, zero-cost, fully private vector lookups for sensitive data. |

**Rule:** NotebookLM holds your *facts* (ground truth). Gemini Gems hold your *style* (persona + execution). One Project = One Notebook.

## 2. Gemini Gems — PACT Framework
- **P — Persona:** explicit identity/voice.
- **A — Assignment:** exactly one repeatable objective per Gem.
- **C — Context:** constraints, guardrails, compliance laws (GROUNDING.md).
- **T — Template:** exact output layout.

## 3. M7 Custom System Instruction (paste into Gemini Notebook / Open NotebookLM)
```text
You are the elite AI Project Architect inside the Pineapple Contractor M7 Agentic OS.
Project Goal: [outcome]   Target Audience: [profile]
Brand Tone: clear, high-intent, practical, zero fluff. No corporate buzzwords / AI clichés.
Guardrails:
1. Prioritize sources loaded in this notebook above all else.
2. Ground every deliverable in verified business data, case studies, internal protocols.
3. Output direct, scannable Markdown ready for workspace integration.
```

## 4. Core Workflows
- **Content & SEO:** NotebookLM Deep Research → brief to Drive → Gemini Content Gem (Drive Search) → asset.
- **High-ticket proposal:** master capability doc in Drive → Proposal Gem → review pricing/timeline manually.
- **Support/compliance:** Support Knowledge Base in NotebookLM → Support Gem checks it before replying.
- **NotebookLM 2.0 Agent OS:** agent auto-creates notebook, ingests sources, indexes, then citation-backed interrogation ("Based ONLY on the sources…").
- **Studio multimedia:** audio overviews (2-host podcasts), video explainer outlines, infographic wireframes, slide decks.

## 5. GEO / AIO (AI Search Optimization)
- Optimize so AI engines (Google AI Overviews, Perplexity, ChatGPT) cite the brand.
- Extreme factual density, nested H1/H2/H3, clean tables, "Citation Bait" (original stats/case studies), answer in first 40 words, inject RCAT #03-0637 + IKO Certified + target ZIPs.

## 6. Quality Control Checklist (before any asset ships)
- [ ] Built inside the isolated project notebook (not a public chat).
- [ ] Zero-hallucination: every metric/name/number pulled from source files.
- [ ] AI-slang scrubbed (no "delve, testament, moreover, in conclusion, landscape").
- [ ] Exactly one clear CTA.
- [ ] Winning templates saved back to the Master Project Notebook (context loop).


<!-- M7-FIREWALL-EXEMPT: governance-reference -->
