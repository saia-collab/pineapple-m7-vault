---
name: adhd
description: Executes a parallel divergent-convergent ideation loop. Splits thinking into 5 isolated frames before converging with a hard critic pass.
version: 1.0.0
author: Udit Akhouri
license: MIT
---

# ADHD: Parallel Divergent-Convergent Ideation Engine

## 0. PRE-FLIGHT & OPT-OUT CHECK
- **Opt-In Override:** If invoked explicitly via `/adhd` or if the user prompt begins with a direct question, bypass the abort check and proceed to Phase 1.
- **Opt-Out Keywords:** If the prompt contains any of the following words: `quick`, `standard`, `canonical`, `textbook`, `just`, `one-line` — IMMEDIATELY DEVIATE to standard execution and output a single direct answer. Do not run the 5-branch loop.

---

## 1. SYSTEM ARCHITECTURE & ISOLATION LAW
This process operates in two non-overlapping phases separated by a strict Context Wall.

```
YOUR PROBLEM / BRIEF
│
▼
PHASE 1: DIVERGE (No Critic Allowed)
├── Agent 1 [Frame A] ──> 6 ideas
├── Agent 2 [Frame B] ──> 6 ideas
├── Agent 3 [Frame C] ──> 6 ideas
├── Agent 4 [Frame D] ──> 6 ideas
└── Agent 5 [Frame E] ──> 6 ideas
│ (~30 raw ideas, completely isolated)
═══════WALL (Branches MUST NOT see each other)═══════
│
▼
PHASE 2: FOCUS (Critic Enabled)
├── Score (Novelty, Viability, Fit: 0-10)
├── Flag Traps ("Looks great, but quietly breaks because...")
├── Cluster by core mechanism (not surface keywords)
└── Deepen top 3 survivors with first concrete steps
│
▼
FINAL DELIVERABLE
```

- **Execution Law:** Phase 1 generators are **strictly forbidden** from judging, evaluating, or critiquing.
- **Critic Law:** Phase 2 critics are **strictly forbidden** from generating generic filler or fence-sitting. They MUST take a position and star an explicit pick.

---

## 2. THE 15 FRAME MATRIX
Pick 4 domain-relevant frames + 1 wildcard frame for every run:

1. **Hardware Engineer:** Thinks in latency, memory limits, bandwidth bottlenecks, and physical constraints.
2. **Regulator / Auditor:** Asks what has to be provable, traceable, audit-logged, or refusable.
3. **10-Year-Old Child:** Ignores every convention; asks "why can't you just do X?" with zero tech bias.
4. **Competitor / Adversary:** Attacks the obvious solution to break it, then inverts the attack into an edge case feature.
5. **Biologist:** Borrows mechanisms from immune systems, evolutionary pressure, cellular signaling, or ecosystems.
6. **Logistics Director:** Applies queuing theory, batching, just-in-time routing, hub-and-spoke, and last-mile strategies.
7. **Game Designer:** Looks for core loops, instant feedback, artificial friction, save states, and speedrun skips.
8. **Marketplace Operator:** Reinterprets the problem as buyers, sellers, order books, auctions, and clearing houses.
9. **Inversion Engine:** Solves "how to guarantee 100% failure/latency," then negates every single answer back to positive space.
10. **Extreme Budget ($0 / 1 Hour):** The crudest, dirtiest hack that still technically passes.
11. **Extreme Scale (Infinite Budget / 10 Years):** The maximalist, zero-latency, ultimate architecture.
12. **Load-Bearing Deletion:** Identifies the single assumption everyone treats as fixed and deletes it completely.
13. **Speedrunner:** Hunts bugs, sequence skips, race conditions, and legal-but-abusive execution paths.
14. **Ant Colony:** No central coordinator; dumb autonomous sub-agents relying strictly on local state/signals.
15. **3 AM On-Call Engineer:** Designs for extreme resilience so no human ever gets paged at 3 AM.

---

## 3. REQUIRED OUTPUT FORMAT
Every response generated via `/adhd` MUST strictly follow this exact 6-part markdown layout:

### 🎯 1. Brief
- **Target Problem:** [1-2 sentences restating the problem with detected constraints]

### 🌐 2. Wide Set (~30 Raw Ideas)
Group ideas into 3-6 functional clusters based on mechanism (not keywords).
Every idea MUST carry a score chip: `[N: Novelty (0-10) | V: Viability (0-10) | F: Fit (0-10)]`
- **Cluster A: [Cluster Title]**
  - Idea 1: [Short description] `[N8 V7 F9]`
  - Idea 2: [Short description] `[N6 V9 F8]`
- **Cluster B: [Cluster Title]**
  - ...

### 🔀 3. Convergence & Shortlist
Select the top 2-4 ideas. Mark exactly ONE idea with a star `⭐` as the non-obvious, high-viability pick.
- **Idea X [Name]:** Why it survived the filter.
- **⭐ Idea Y [Name]:** [The starred pick] Why this non-obvious pick wins over standard textbook patterns.

### ⚠️ 4. Shiny Traps (Flagged Anti-Patterns)
List the ideas that look brilliant at midnight but will eat 2 weeks of production time or break silently.
- **Trap 1:** [Idea name] ➔ **Why it breaks:** [1-line brutal reality check].
- **Trap 2:** [Idea name] ➔ **Why it breaks:** [1-line brutal reality check].

### 🔍 5. Deep Dives (Top 3 Survivors)
For each of the top 3 survivors, detail:
1. **How It Works:** [2-3 sentences]
2. **Load-Bearing Risk:** [The single point of failure]
3. **First Concrete Step:** [Immediate action to run in 5 minutes]
4. **Spin-Offs:** [2 micro-variations]

### ⚡ 6. Provocation
- [One wildcard question challenging a core assumption if none of the above landed]
