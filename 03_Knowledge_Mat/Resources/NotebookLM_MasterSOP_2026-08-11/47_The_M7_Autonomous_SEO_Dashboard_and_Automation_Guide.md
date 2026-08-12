---
source: "NotebookLM - Master SOP 8/26"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: 0e6451c6-e29a-41a7-837b-82eb661ac8ac
type: SOP/guide
scrub: "proverbs removed; GAF->IKO; free-offer->CPPA; REVIEW green?"
status: DRAFT - review before publish/run (Outbox Shield)
---

# The M7 Autonomous SEO Dashboard and Automation Guide

### 🖥️ WHAT A VISUAL GRAPH DASHBOARD LOOKS LIKE

A visual graph dashboard (like your interactive **`m7_graph_map.html`**) is a browser-based control center. It replaces long, confusing text logs with an elegant, interactive flowchart of your entire digital factory. 

#### 🎨 The Visual Interface
When you open the dashboard in your web browser, you are presented with a clean, high-contrast control screen styled strictly within your brand guidelines (**0% Green**):
*   **The Background:** A deep slate canvas (`#0F172A`) that makes your active elements stand out.
*   **The Nodes (Stations):** Sleek, rounded boxes styled in **Royal Navy (`#1A365D`)** with **Pineapple Gold (`#FBC02D`)** borders representing your active worker stations (such as GSC Scout, Copywriter, Brand Firewall, and WordPress Deployer).
*   **The Edges (Handoff paths):** Glowing **Status Cyan (`#00BFFF`)** arrows showing exactly how data packets (your standardized JSON envelopes) are flowing from one machine to the next.

#### 🧒 ELI10: What is its Job?
Imagine you are the Commander of a futuristic space station. You have fifty tiny robot helpers running around doing chores, painting walls, and fixing doors. 

If you had to follow each robot around to make sure they were doing their job, you would get tired and dizzy!

The Visual Graph Dashboard is like a **giant glowing wall map** in your Commander’s Cabin. 
*   Instead of walking around, you look at the screen. 
*   If your **Scout Robot** is currently finding keywords, its box on the map glows with a **glowing Cyan light**. 
*   When it finishes and hands the data to your **Writer Robot**, a golden line zips across the screen to show the delivery. 
*   If a robot accidentally uses a banned word on a draft page, its box turns **flashing Red** to show you exactly where the mistake is so you can fix it.

It turns your entire business into a simple, beautiful video game map. It lets you verify that everything is running perfectly under **The Pineapple Standard** with a single glance!

---

### 🚀 HOW TO TRIGGER THE 24/7 BACKGROUND SEO AGENT LOOP

The 24/7 Background SEO loop runs completely on autopilot, executing content generation, strict brand auditing, and search indexing every 6 hours while you sleep—making **Roofing Made Sweeter** for your business.

Here are the two ways to trigger it:

#### Option A: The Manual Launch (For Active Work Sessions)
If you are sitting at your desk and want to watch the loop run in real-time, launch it directly in your terminal:

1.  Open your command console (Command Prompt or PowerShell).
2.  Run your background batch file:
    ```bash
    "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\run_background_seo.bat"
    ```
3.  **What you will see:** A persistent console window will open with a Gold header. It will write out step-by-step logs as it runs your GSC scans, drafts pages with jcode, runs the compliance firewall, and pings sitemaps. 
4.  Once the cycle is complete, the screen will display: `💤 CYCLE COMPLETE. Sleeping for 6 hours before next check...` and begin its countdown. Keep this window minimized on your taskbar to let it run during your work session.

---

#### Option B: The Invisible Trigger (Set-and-Forget 24/7 Mode)
To make this loop run quietly in the background without keeping any black command windows open on your screen, configure it to run as a **Windows Background Service**:

1.  Press the **Windows Key** on your keyboard, type **Task Scheduler**, and press Enter.
2.  In the right-hand *Actions* sidebar, click **Create Basic Task...**
3.  **Name the Task:** `M7_247_SEO_Engine` (Description: *Autonomous Everywhere SEO Loop*). Click *Next*.
4.  **Set the Trigger:** Select **When the computer starts** (this ensures the loop boots up automatically every time your PC turns on). Click *Next*.
5.  **Set the Action:** Select **Start a program**. Click *Next*.
6.  **Point to your Script:** Click *Browse* and navigate directly to your batch file:  
    `C:\Pineapple Contractors M7\04_Tech_Lab\scripts\run_background_seo.bat`
7.  Click *Next*, then check the box that says **Open the Properties dialog for this task when I click Finish**, and click **Finish**.
8.  **The Golden Security Step:** In the Properties window that pops up:
    *   Under the *General* tab, select the option: **Run whether user is logged on or not**.
    *   Check the box: **Run with highest privileges** (this prevents Windows from blocking your sitemap pings or local file writes).
    *   Click **OK** and enter your Windows password when prompted.

#### 🏆 The Result:
Your background SEO agent loop is now locked into your computer's system core. It runs silently in the background, checking keyword metrics, creating pages, scanning drafts, and publishing to your WordPress site on a continuous 6-hour clock—requiring absolutely zero daily maintenance from your team!

📂 **Next Step Suggestion:**  
I can prepare a custom local **`m7_graph_map.html`** file inside your `01_Command_Center/` directory that uses Mermaid.js to display your clickable, live flowchart of your Active Lead and SEO pipelines. Would you like me to compile this visual graph dashboard?