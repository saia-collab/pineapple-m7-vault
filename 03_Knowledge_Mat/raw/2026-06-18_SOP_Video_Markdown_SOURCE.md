Here is a comprehensive Standard Operating Procedure (SOP) written in scannable Markdown. You can paste this directly into Claude to help you architect and build this exact automated system.

# ---

**SOP: Building an AI-Driven Workspace & Automation System inside Obsidian**

## **1\. System Philosophy & Architecture**

The objective of this setup is to transition Obsidian from a static personal knowledge management (PKM) tool into an interactive, automated operating system. Instead of manual data entry, the system uses local AI agents as the "hands" to manipulate files, while Obsidian acts as a structured, local "memory layer" that provides the agent with persistent long-term context.

### **Core Tech Stack**

* **Knowledge Base:** [Obsidian](https://www.youtube.com/watch?v=VaGpWWiHXm8) (Local Markdown files)  
* **AI Terminal Agents:** Claude Code / Codex / PiAgent  
* **Data Visualization Plugins:** Dataview (v1 Optics)  
* **Core Plugins:** Web Viewer (Custom Frame / Open Gate), Workspaces

## ---

**2\. Automated Note Capture & Daily Logging Workflow**

Eliminate the friction of manual diary logs and property data-entry by routing all data through terminal automation.

### **Implementation Steps**

1. **Create a Daily Log Template:** Define standard YAML/Frontmatter properties in your daily note template (e.g., Sleep Score, Subscribers, Daily Tasks, Activity Log).  
2. **Establish AI Terminal Hooks:** Configure your CLI agent (like Claude Code) to run directly inside your vault directory.  
3. **Automate Time Tracking:** Use automation hooks to timestamp activities as you complete them during the day.  
   * *Example:* Tell your agent: "Log that I spent the last 45 minutes fixing the database script."  
   * The agent opens your current daily note, appends a line with the exact timestamp \[HH:MM:SS\], and logs the action [02:46 Opens in a new window](http://www.youtube.com/watch?v=VaGpWWiHXm8&t=166) .

## ---

**3\. Integrated Workspace Layout & Sidebar Embeds**

Consolidate web tools and communication channels into Obsidian to minimize window-switching and context distraction.

### **Implementation Steps**

1. **Enable the Internal Web Viewer:** Activate the community web browser/viewer plugin within Obsidian [03:33 Opens in a new window](http://www.youtube.com/watch?v=VaGpWWiHXm8&t=213) .  
2. **Set Up Localhost Development:** \* Open a pane with your terminal agent running at the bottom.  
   * Open the internal web viewer pane on the top right pointing to your local development server (e.g., http://localhost:3000) [04:02 Opens in a new window](http://www.youtube.com/watch?v=VaGpWWiHXm8&t=242) .  
   * This gives you real-time visual feedback directly within the vault as the AI writes and edits code files.  
3. **Embed Workspace Communication Apps:**  
   * Open web instances of communication tools (Slack, Telegram, WhatsApp, Spotify) via the web viewer [04:35 Opens in a new window](http://www.youtube.com/watch?v=VaGpWWiHXm8&t=275) .  
   * Log in once securely and pin these views directly to your **Obsidian Sidebar** [05:13 Opens in a new window](http://www.youtube.com/watch?v=VaGpWWiHXm8&t=313) .

## ---

**4\. Constructing the Optics Layer (Data Visualization v1)**

Use Obsidian Canvas and Dataview to dynamically aggregate and track your progress metrics visually.

### **Implementation Steps**

1. **Create an Obsidian Canvas Dashboard:** Name it Main Productivity Dashboard.canvas [06:13 Opens in a new window](http://www.youtube.com/watch?v=VaGpWWiHXm8&t=373) .  
2. **Embed Real-Time Web Panels:** Drag web pages directly into your Canvas layout (e.g., the YouTube comments page or a live metrics URL) [06:38 Opens in a new window](http://www.youtube.com/watch?v=VaGpWWiHXm8&t=398) .  
3. **Inject Dataview Charts:**  
   * Ensure the **Dataview** community plugin is installed [06:49 Opens in a new window](http://www.youtube.com/watch?v=VaGpWWiHXm8&t=409) .  
   * Use natural language with Claude Code to generate custom Dataview JS code blocks that query variables from your historical daily notes.  
   * Render these code blocks directly within Canvas notes to create auto-updating line graphs, bar charts, and pie charts [07:09 Opens in a new window](http://www.youtube.com/watch?v=VaGpWWiHXm8&t=429) .  
4. **Save Your Layout Workspace:**  
   * Enable the core **Workspaces** plugin [08:01 Opens in a new window](http://www.youtube.com/watch?v=VaGpWWiHXm8&t=481) .  
   * Once your dashboard canvas, sidebar apps, and terminal panes are positioned perfectly, save the workspace layout layout under a profile name (e.g., Dashboard View) to recall it with a single click [08:16 Opens in a new window](http://www.youtube.com/watch?v=VaGpWWiHXm8&t=496) .

## ---

**5\. Coding a Custom Plugin Dashboard (Data Layer v2)**

For a fully tailored application experience, build an interface inside Obsidian that acts as a visual frontend for your plain text Markdown databases.

### **Prompt Framework for Claude Code to Build the Plugin**

**Role:** Expert Obsidian Plugin Developer & UI/UX Engineer

**Objective:** Build a custom community plugin that acts as an executive dashboard.

**Data Structure Requirements:**

* The dashboard must read data directly from the vault's local Markdown files as its "backend database" [09:46 Opens in a new window](http://www.youtube.com/watch?v=VaGpWWiHXm8&t=586) .  
* It should pull calendar schedules from a dedicated configuration or event note [09:52 Opens in a new window](http://www.youtube.com/watch?v=VaGpWWiHXm8&t=592) .  
* It must parse property keys (e.g., metrics from daily notes) and map them dynamically into structured HTML tables, snapshot cards, and calendar blocks [10:02 Opens in a new window](http://www.youtube.com/watch?v=VaGpWWiHXm8&t=602) .

**UI/UX & Customization Design:**

* Include an main homepage button (e.g., a "House" icon) that launches the unified view [09:25 Opens in a new window](http://www.youtube.com/watch?v=VaGpWWiHXm8&t=565) .  
* Create a user-configurable file (config.md) that controls the UI rendering. Moving a text block or key in the markdown note should instantly shift the columns or visibility of a card tracking widget on the dashboard interface [10:07 Opens in a new window](http://www.youtube.com/watch?v=VaGpWWiHXm8&t=607) .

## ---

**Free Resources & Reference Links**

* **Starter System Templates & Scripts:** Check out the [Easy Machine AI Links Page](https://easymachineai.com/links) for free vault setups.  
* **Video Source Walkthrough:** Review the full architecture on [YouTube](https://www.youtube.com/watch?v=VaGpWWiHXm8).