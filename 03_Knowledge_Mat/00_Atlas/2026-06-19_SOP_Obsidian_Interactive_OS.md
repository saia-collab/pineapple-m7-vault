---
type: knowledge_atlas
source: 2026-06-18_SOP_Video_Markdown_SOURCE.md
created: 2026-06-19
agent_origin: Lead_Systems_Architect
classification: M7_Command_Level_2
---

# SOP: Obsidian as Interactive AI Operating System

Distilled from SOP_Video_Markdown_SOURCE. Covers transforming Obsidian from a static PKM into an automated, agent-driven operating system with live data visualization and custom plugin dashboards.

---

## Core Tech Stack

| Layer | Tool |
|:---|:---|
| Knowledge Base | Obsidian (local markdown files) |
| AI Terminal Agents | Claude Code / Codex / Hermes |
| Data Visualization | Dataview plugin (v1 Optics) |
| Web Embedding | Web Viewer plugin (Custom Frame / Open Gate) |
| Workspace Management | Obsidian Workspaces (core plugin) |

---

## Automated Note Capture & Daily Logging

1. **Create Daily Log Template:** Define YAML/frontmatter properties (Sleep Score, Subscribers, Daily Tasks, Activity Log).
2. **Establish AI Terminal Hooks:** Configure Claude Code to run directly inside the vault directory.
3. **Automate Time Tracking:** Tell agent: "Log that I spent the last 45 minutes on [task]." → Agent opens current daily note, appends timestamp `[HH:MM:SS]`, logs action.

---

## Integrated Workspace Layout

1. **Enable Web Viewer Plugin:** Activate community browser plugin in Obsidian.
2. **Local Dev Server Integration:**
   - Terminal pane at bottom (Claude Code)
   - Web viewer pane top-right → `http://localhost:3000` (live preview as AI edits code)
3. **Embed Communication Apps:** Open Slack/Telegram/WhatsApp via web viewer → pin to Obsidian Sidebar (login once, persists across sessions).

---

## Optics Layer: Data Visualization (v1)

1. **Create Canvas Dashboard:** `Main Productivity Dashboard.canvas`
2. **Embed Real-Time Web Panels:** Drag live metric URLs (YouTube comments, analytics dashboards) directly into Canvas.
3. **Dataview Charts:** Install Dataview plugin → use Claude Code to generate Dataview JS blocks → query historical daily note variables → render as auto-updating line graphs, bar charts, pie charts inside Canvas.
4. **Save Workspace Layout:** Enable Workspaces plugin → save layout profile (e.g., "Dashboard View") for single-click recall.

---

## Custom Plugin Dashboard (Data Layer v2)

**Build prompt for Claude Code:**

> **Role:** Expert Obsidian Plugin Developer & UI/UX Engineer
>
> **Objective:** Build a custom community plugin acting as an executive dashboard.
>
> **Data Requirements:**
> - Read data directly from vault's local markdown files as the backend database
> - Pull calendar schedules from a dedicated event note
> - Parse property keys from daily notes → map dynamically into HTML tables, snapshot cards, calendar blocks
>
> **UI/UX:**
> - Homepage button (House icon) launches unified view
> - `config.md` controls UI rendering — moving a text block in markdown instantly shifts dashboard column/card visibility

---

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
