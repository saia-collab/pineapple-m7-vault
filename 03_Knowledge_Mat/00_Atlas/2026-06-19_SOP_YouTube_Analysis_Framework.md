---
type: knowledge_atlas
source: 2026-06-17_YouTube_Analysis_B_SOURCE.md
created: 2026-06-19
agent_origin: Lead_Systems_Architect
classification: M7_Command_Level_2
---

# SOP: YouTube Video Analysis Framework — 8-Prompt Extraction Engine

Distilled from the B-batch YouTube analysis session (14 videos on agentic AI workflows). Use these prompts inside NotebookLM or Claude when ingesting any new YouTube video resource to extract maximum operational value.

---

## The 8 Analytical Prompt Frameworks

### 1. Deep Content Deconstruction
Identify: core problem the video solves → main frameworks introduced → logical teaching sequence → section-by-section objectives. Finish with: big-picture summary in plain English + top 5 highest-leverage insights + most actionable immediate lessons.

### 2. Complete Skill Tree & Dependency Mapping
Extract a hierarchical skill tree: **Foundations → Enabling Skills → Execution Skills → Advanced Optimization**. For each micro-skill: what it involves, why it matters, prerequisites, connections, common beginner mistakes, mastery indicators. Conclude with: top 20% of skills driving 80% of results + fastest competency path.

### 3. High-Leverage Insight Extraction (80/20)
Identify the smallest number of ideas producing the largest results. For each: what it is, why it creates disproportionate results, specific application situations, common misapplication mistakes. Output: ranked insight list + 80/20 action plan (learn first / ignore initially / practice repeatedly).

### 4. Step-by-Step Execution Playbook
Convert advice into a Phase 1–5 operating system: **Preparation → Setup → Execution → Optimization → Troubleshooting**. Per step: objective, exact actions, tools required, expected output, success indicators, decision variations. Finish with beginner quick-start checklist.

### 5. Mental Models & Expert Thinking Patterns
Surface implicit cognitive frameworks the creator uses. Organize into: Core Mental Models → Expert Decision Frameworks → Hidden Assumptions → Beginner vs. Expert Thinking. Deliverable: "think like an expert" cheat sheet + practical decision framework.

### 6. Real-World Implementation Scenarios
Build 4 scenarios: Beginner / Intermediate / Advanced / Failure. Per scenario: starting context, specific challenge, step-by-step process using video teachings, key decision points, expected outcome if executed correctly. Finish with lessons across all scenarios + implementation roadmap.

### 7. Failure Points & Beginner Pitfalls
Surface why people fail in practice. Organize: Beginner Mistakes → Execution Bottlenecks → Hidden Failure Points → Recovery Strategies. Per failure point: what it is, why beginners fall into it, early warning signs, correct approach, step-by-step fix. Deliverable: top 10 mistakes to avoid + quick troubleshooting checklist.

### 8. Structured Mastery Roadmap
Design a progression: **Beginner → Developing Practitioner → Advanced Practitioner → Expert**. Per stage: required knowledge, concepts to master, practice exercises, real-world projects, performance indicators. Create: 30-Day Fast Track Plan + Deliberate Practice System + Skill Gap Analysis Framework + Mastery Scorecard.

---

## Strategic Architecture Synthesis (from 14-video analysis)

**Key finding:** 2026 AI transition is from manual prompt engineering to **local-first, multi-agent automated execution**. Cloud-based middleware creates configuration drift, high API costs, and data leakage risk.

**Four-Agent Production Team:**
- Research Agent — scrapes local market data and competitor intelligence
- Copy Agent — writes compliant ad copy gated against the brand firewall
- Render Agent — compiles video variations via FFmpeg/video-multiplier.py
- Judge Agent — cross-examines and fuses agent outputs into master execution scripts

**Protocol 0 (Persistent State):** Before any long-running automation, initialize a state folder recording task progress, findings, and decisions in local files. Prevents context drift across multi-session workflows.

**Local Translation Proxy:** Route terminal requests through a local port (4000) to access local model APIs without paid external middleware. Deploy via Ollama + LiteLLM (`drop_params: true`).

**Modular Video Construction:** Separate videos into interchangeable hook / body / CTA parts for automated assembly → produces hundreds of compliant variations from limited source footage.

---

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
