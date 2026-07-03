---
type: knowledge_atlas
source: 2026-06-18_SOP_Local_Memory_Bridge_SOURCE.md
created: 2026-06-19
agent_origin: Lead_Systems_Architect
classification: M7_Command_Level_2
---

# SOP: Local Memory & Execution Bridge (Claude Code + Obsidian)

Distilled from SOP_Local_Memory_Bridge_SOURCE. Covers the Left Brain / Right Brain permission model and deployment initialization workflow.

---

## Left Brain / Right Brain Permission Model

| Human Side (Left Brain) | Machine Side (Right Brain) |
|:---|:---|
| Authentic, unedited user voice | AI-generated outputs, automation scripts, compliant marketing drafts |
| Daily notes, direct brain-dumps, manual tasks, relationship logs | Research results, SOPs, templates, code files |
| Read-only for AI agents unless explicitly commanded to append | AI is free to write, organize, and execute within this directory |

**Rule:** This strict split prevents AI "slop" from diluting brand voice. Agents never overwrite human notes; they append to the machine side only.

---

## Directory Mapping

```
01_Command_Center\   — MASTER_PLAYBOOK.md, CLAUDE.md, OS Dashboard HTML (governance, read-only)
02_Workspaces\       — Active staging: human brain-dumps, unedited daily logs
03_Knowledge_Mat\    — Machine brain: research results, SOPs, flattened RAG substrates
04_Tech_Lab\         — Terminal plugins, Python automation, MCP server configs
```

---

## Deployment Initialization Sequence

```shell
# Step 1: Initialize local directory scaffolding
./setup_m7.ps1

# Step 2: Bind Claude Code to the Obsidian memory vault
claude --mcp-vault "C:\Pineapple Contractors M7"

# Step 3: Trigger the today prep routine to scan active context
hermes run today_prep.yaml
```

---

## Ollama Fallback Configuration

When Anthropic rate limits are reached, the system falls back to local models via Ollama (DeepSeek, Qwen) routed through LiteLLM proxy with `drop_params: true`. File-based context is preserved across the fallback transition — no data loss.

**LiteLLM proxy config (04_Tech_Lab/config/):**
```yaml
model_list:
  - model_name: deepseek-local
    litellm_params:
      model: ollama/deepseek-coder
      api_base: http://localhost:11434
drop_params: true
```

---

## Elite Lexicon Compliance (Embedded)

All outputs from this bridge pass the brand firewall before write:
- "Inspection" / "Estimate" → "Complimentary Professional Photo Audit (CPPA)"
- "$0 Down" / "$0 Out of Pocket" → "Full Restoration Coverage"

---

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
