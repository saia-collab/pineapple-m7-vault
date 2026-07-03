---
type: knowledge_atlas
source: 2026-06-18_SOP_Local_Memory_Bridge_SOURCE.md
created: 2026-06-29
hash: 197f5fcdd5a291d83e50554b7f1e512b
agent_origin: m7_aggregate
---

# **SOP: M7 Agentic OS \- Local Memory & Execution Bridge**

This protocol defines the integration of Anthropic's **Claude Code** and **Obsidian** to serve as the persistent local memory layer for the Pineapple M7 Operating System. By wiring terminal-based agents directly into a structured vault, we eliminate context amnesia and ensure all business data remains grounded in our local architecture.

## **1\. 4-Fala Topography Mapping**

To maintain system integrity, all assets from this workflow must be distributed across the following directories:

* **01\_Command\_Center\\**: Houses the *MASTER\_PLAYBOOK.md*, *CLAUDE.md* constitution, and the OS Dashboard HTML.  
* **02\_Workspaces\\**: Active staging environment for human-brain dumps and unedited daily logs.  
* **03\_Knowledge\_Mat\\**: The "Machine Brain" directory containing research results, SOPs, and flattened RAG substrates.  
* **04\_Tech\_Lab\\**: Contains the terminal plugins, Python automation scripts, and MCP server configurations required to run Claude Code.

## **2\. The "Left Brain / Right Brain" Logic**

A strict split between human thought and machine generation is enforced to prevent AI "slop" from diluting the brand voice.

| Human Workspace (Left Brain) | Machine Workspace (Right Brain) |
| ----- | ----- |
| Unedited, read-only voice. Daily notes and brain-dumps. | AI outputs, automation scripts, and compliant marketing drafts. |

## **3\. Elite Lexicon & Compliance**

The following linguistic mutations must be hardcoded into the terminal configuration:

* **Offer Standardization:** Replace all instances of "Complimentary Professional Photo Audit (CPPA)" or "Complimentary Professional Photo Audit (CPPA)" with **Complimentary Professional Photo Audit (CPPA)**.  
* **Financial Authority:** "Full Restoration Coverage" or "Full Restoration Coverage" must be rewritten as **Full Restoration Coverage**.

## **4\. Deployment Workflow (/04\_Tech\_Lab)**

To initialize the memory bridge, execute the following in the integrated terminal:

```shell
# Step 1: Initialize local directory scaffolding
./setup_m7.ps1
# Step 2: Bind Claude Code to the Obsidian memory vault
claude-code --mcp-vault "C:\Pineapple Contractors M7"
# Step 3: Trigger the /today prep routine to scan active context
hermes run today_prep.yaml
```

The architecture is now fully future-proof. Should Anthropic reach rate limits, the system seamlessly fallbacks to local models (DeepSeek/Qwen) via Ollama while retaining the same file-based context.

**‘Oua lau e kafo kae lau e lava.**

| The Human Side (Left Brain) | The Machine Side (Right Brain) |
| :---- | :---- |
| Contains the user's authentic, unedited voice [07:42 Opens in a new window](http://www.youtube.com/watch?v=eIXheJcxDIg&t=462) . | Contains AI-generated output, automation scripts, and workflows [08:51 Opens in a new window](http://www.youtube.com/watch?v=eIXheJcxDIg&t=531) . |
| **Contents:** Personal daily notes, direct brain-dumps, manual tasks, and relationships [08:40 Opens in a new window](http://www.youtube.com/watch?v=eIXheJcxDIg&t=520) . | **Contents:** Research results, Standard Operating Procedures (SOPs), templates, and code files [08:51 Opens in a new window](http://www.youtube.com/watch?v=eIXheJcxDIg&t=531) . |
| **Permissions:** Read-only for AI agents unless explicitly commanded to append something [08:13 Opens in a new window](http://www.youtube.com/watch?v=eIXheJcxDIg&t=493) . | **Permissions:** AI is Complimentary to write, organize, and execute code within this directory [08:23 Opens in a new window](http://www.youtube.com/watch?v=eIXheJcxDIg&t=503) . |

