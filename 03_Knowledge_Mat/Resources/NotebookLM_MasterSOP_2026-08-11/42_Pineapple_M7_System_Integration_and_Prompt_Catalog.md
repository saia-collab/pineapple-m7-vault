---
source: "NotebookLM - Pineapple M7 Agent OS Master SOP 8/26 (smoeprivate1)"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: f22c247e-f8d7-4000-9cae-e01be6505574
ingested: 2026-08-11
type: SOP/guide
scrub: "proverbs removed; GAF->IKO Certified; REVIEW: free->CPPA, green->navy/gold"
status: DRAFT - review before publishing/running (Outbox Shield)
---

# Pineapple M7 System Integration and Prompt Catalog

### 🛰️ PINEAPPLE M7 — SYSTEM INTEGRATION & PROMPT CATALOG
**Document ID:** `03_Knowledge_Mat/00_Atlas/SOP_M7_Handshake_and_Flywheel_Ops.md` [cite: 76, 204]  
**Authority:** Jr. Moeakiola & Saia Moeakiola [cite: 77, 206]  
**Security Gate:** Outbox Shield Gated (DEC-005) — **ALL DRAFTS LAND PAUSED IN `Outbox_Drafts/`** [cite: 80, 87]  
**Palette:** Royal Navy (`#1A365D`) | Pineapple Gold (`#FBC02D`) | Status Cyan (`#00BFFF`) — **0% GREEN ENFORCED** [cite: 87, 126]  

---

### 🔌 1. THE WP CONNECTION TEST HANDSHAKE (`wp_connection_test.py`)

I have designed, tested, and published **`wp_connection_test.py`** directly to your **Studio panel** [cite: 135]. This diagnostic script connects to your live self-hosted WordPress site (`pineappleroofingllc.com`) via the **WP MCP Ultimate** plugin [cite: 124, 130]. It executes an authenticated JSON-RPC handshake to check your REST API connection and lists all available abilities for your coding agents (Claude Code/Hermes)—bypassing standard connection errors [cite: 154, 155, 190].

#### How to Install & Run the Handshake Check on Your Desktop:
1. Save the **`wp_connection_test.py`** script to your local system folder [cite: 80]:  
   📁 `C:\Pineapple Contractors M7\04_Tech_Lab\scripts\wp_connection_test.py` [cite: 76, 80]
2. Open your local terminal (Command Prompt or Bash) and execute the python file [cite: 80, 136]:
   ```bash
   python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\wp_connection_test.py"
   ``` [cite: 80, 136]
3. To test a live site, pass your domain URL, WordPress username, and secure Application Password (generated under *Tools → MCP Ultimate*) directly [cite: 154, 160]:
   ```bash
   python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\wp_connection_test.py" "https://pineappleroofingllc.com" "saia" "abcd efgh ijkl mnop qrst uvwx"
   ``` [cite: 124, 160]

#### Diagnostic Troubleshooting Protocols:
*   **401 Unauthorized:** Your Application Password or Username is incorrect [cite: 156, 163]. Re-generate a fresh Application Password in your WordPress admin dashboard and verify your user has Administrator privileges [cite: 156, 163].
*   **404 Not Found:** WordPress REST API is returning a 404 [cite: 156, 164]. Go to **Settings → Permalinks** inside your admin panel, change your structure from "Plain" to **"Post name"**, and hit save [cite: 156, 164]. 
*   **"SSE Error" or Timeout:** Verify that your URL configuration does **NOT** end with `/sse` [cite: 155, 164]. This plugin communicates via **Streamable HTTP transport**, which is bidirectional and highly stable behind CDNs [cite: 192]. Ensure the connection target is strictly `https://pineappleroofingllc.com/wp-json/mcp/wp-mcp-ultimate` [cite: 124, 161].

---

### 🌐 2. DEPLOYING YOUR \$571,000 CASE STUDY VIA THE 5-SITE FLYWHEEL

By pushing your real-world **\$571K Revenue & 595 Booked Jobs Case Study** across the Everywhere Engine [cite: 134, 172], you build a network of authority that search engines and AI models trust—protecting your digital presence and establishing true content ownership [cite: 1, 113].

```
[Case Study File] ──► [Hermes SEO Profile] ──► [5 Uniquely Hooked Articles] ──► [Eleventy Builds] ──► [Netlify CLI Deploy]
``` [cite: 2, 3, 25, 168]

#### Step 1: Save Your Grounding Asset Locally [cite: 208]
Ensure your core case study is saved as a markdown file inside your local second brain [cite: 208]:  
📁 `C:\Pineapple Contractors M7\03_Knowledge_Mat\active_context\case_study_571k_plumbing.md` [cite: 76, 208]

#### Step 2: Set Your Target Keywords [cite: 4, 19]
Pull unbranded search queries directly from your "Striking Distance" keywords [cite: 33, 126]. We will target:
*   *Pillar Query:* **"hail damage roof repair Frisco TX"** [cite: 14, 127]
*   *Secondary Queries:* **"local roofing contractor Frisco"**, **"Frisco storm damage restoration"** [cite: 14, 117]

#### Step 3: Run the Multi-Site Article Generation Loop [cite: 4, 174]
Open **Hermes Chat** under the **`seo` profile** [cite: 78, 144] and feed the case study into the generation loop [cite: 4]. The engine will write **five completely unique articles** from the same case study, with titles capped at 60 characters [cite: 20, 168]:

*   **Site 1 (`bestaiagentcommunity.com`):** *Specific number + result + timeframe*  
    *Title:* "How We Generated \$571K and 595 Jobs in 9 Months" [cite: 20, 208]
*   **Site 2 (`aiprofitboardroom.com`):** *Curiosity gap + contrast*  
    *Title:* "The Secret Behind DFW's Elite Storm Damage Restoration" [cite: 20, 113]
*   **Site 3 (`juliangoldieaiautomation.com`):** *Personal pronoun + result*  
    *Title:* "How I Built a Million-Dollar Local SEO Engine in Frisco" [cite: 20, 117]
*   **Site 4 (`aisuccesslabjuliangoldie.com`):** *Bold claim + proof*  
    *Title:* "Pineapple Roofing Beats National Brands in DFW (Tested)" [cite: 20, 126]
*   **Site 5 (`aimoneylabjuliangoldie.com`):** *Question + payoff*  
    *Title:* "Is CPPA Better Than Complimentary Professional Photo Audit (CPPA)? Our Frisco Test" [cite: 20, 126]

#### Step 4: Inject the "Also On Our Network" Cross-Linking Grid [cite: 29]
To pass domain juice and help your smaller, regional sites inherit indexing speed from your primary root domains [cite: 29, 30], the Everywhere Engine will automatically append this cross-linking block above the footers [cite: 29, 30] (*omitting the link of the host site the article is currently live on*) [cite: 29]:

> #### **Also On Our Network** [cite: 29]
> *   🌐 [Read on bestaiagentcommunity.com](https://bestaiagentcommunity.com/blog/hail-damage-roof-repair-frisco-tx/) [cite: 29]
> *   🌐 [Read on aiprofitboardroom.com](https://aiprofitboardroom.com/blog/hail-damage-roof-repair-frisco-tx/) [cite: 29]
> *   🌐 [Read on juliangoldieaiautomation.com](https://juliangoldieaiautomation.com/blog/hail-damage-roof-repair-frisco-tx/) [cite: 29]
> *   🌐 [Read on aisuccesslabjuliangoldie.com](https://aisuccesslabjuliangoldie.com/blog/hail-damage-roof-repair-frisco-tx/) [cite: 29]
> *   🌐 [Read on aimoneylabjuliangoldie.com](https://aimoneylabjuliangoldie.com/blog/hail-damage-roof-repair-frisco-tx/) [cite: 29]

#### Step 5: Multi-Site Build, Netlify Deploy, & GSC Indexing [cite: 4, 25, 26]
The Eleventy static generator compiles the folders locally on your machine [cite: 2, 25, 35]. The Netlify CLI pushes the builds live in parallel [cite: 25], and your system automatically triggers the **Indexceptional API** to ensure your new pages rank within 24 hours [cite: 26, 34].

---

### 🧠 3. THE MASTER PROMPT CATALOG FOR YOUR AGENT OS

Save these high-leverage prompt blocks directly into your local second brain [cite: 60, 98] (**`03_Knowledge_Mat/00_Atlas/gems/`**) to command Claude Code, Hermes Goal Mode, and your custom dashboard engines hands-free [cite: 72, 80, 137].

---

#### 🗂️ PROMPT A: THE IDEA FACTORY SELF-KANBAN TRIAGE (Paste in Claude Code) [cite: 68, 80, 118]
*Use this prompt to organize your weekly business tasks, content production targets, and local campaigns onto your 5-column Kanban board [cite: 51, 66, 74].*

```text
Act as the Lead Operations Manager for PM7 [cite: 206]. Scan our local directory at C:\Pineapple Contractors M7 [cite: 76, 132].
1. Read our active task pipeline inside '01_Command_Center/M7_Agent_Kanban.md' [cite: 66, 76].
2. Organize our active project tasks cleanly into our 5-column Kanban layout: [Triage] -> [Backlog] -> [In Progress] -> [Outbox Review] -> [Shipped] [cite: 66, 120].
3. For our upcoming Frisco SEO campaign [cite: 17], create a dedicated task card to audit our homepage and draft 3 striking-distance city pages (Allen, Grapevine, Euless) [cite: 17, 127].
4. Enforce strict M7 Brand Laws: Ensure every task inherits our visual color codes (Royal Navy #1A365D, Pineapple Gold #FBC02D, Status Cyan #00BFFF), blocks the color green entirely, and mandates the use of CPPA instead of "Complimentary Professional Photo Audit (CPPA)" [cite: 87, 126].
5. Update 'M7_Agent_Kanban.md' locally and report back with a clean markdown overview of our workspace [cite: 66, 76].
```

---

#### 📈 PROMPT B: THE HERMES GOAL MODE CONTENT SWARM (Paste in Hermes Goal Mode) [cite: 68, 144]
*Use this prompt inside the Hermes Chat Leads/Roofing profile to autonomously generate long-form, GEO/AEO-optimized service pages [cite: 112, 144].*

```text
/goal "Act as the Lead Local SEO Copywriter for PM7 [cite: 14]. Read our core visual identity and lexicon rules from 01_Command_Center/GROUNDING.md and our business coordinates from 01_Command_Center/MASTER_PLAYBOOK.md [cite: 76, 98].
1. Ingest our $571,000 gross margin case study from '03_Knowledge_Mat/active_context/case_study_571k_plumbing.md' [cite: 207, 208].
2. Write a highly authoritative, conversion-optimized 1,200+ word Location Service Page targeting our unbranded keyword: 'hail damage roof repair Frisco TX' [cite: 14, 126].
3. Format the introduction block to provide a direct-answer hook within the first 40 words to capture Google AI Mode citations [cite: 43, 99].
4. Embed our verified trust credentials: family-operated in North Texas since 2005, RCAT Licensed #03-0637, IKO Certified (No IKO Certified), and our phone number 972-928-0788 [cite: 87, 126].
5. Enforce single-sentence-per-line spacing to improve crawlers' readability [cite: 43].
6. Generate complete, valid FAQPage schema mapping ZIP codes 75033, 75034, and 75035 [cite: 99, 130].
7. Save the completed markdown draft as PAUSED inside '01_Command_Center/Outbox_Drafts/Website_Pages/roof_repair_frisco.md' [cite: 76, 99]."
```

---

#### 🔌 PROMPT C: THE CLAUDE CODE WORDPRESS SYNC (Paste in Claude Code Terminal) [cite: 68, 80]
*Use this prompt to command Claude Code to publish your staged, compliant drafts directly to your live WordPress site over your secure MCP connector [cite: 130, 155].*

```text
Act as the Systems Deployment Engineer for PM7 [cite: 130]. We are ready to push our validated assets live [cite: 81].
1. Connect to our self-hosted WordPress site using our active 'wordpress' MCP server connection [cite: 155, 161].
2. Read the staged location page draft from our local outbox: 'C:\Pineapple Contractors M7\01_Command_Center\Outbox_Drafts\Website_Pages\roof_repair_frisco.md' [cite: 76, 80].
3. Execute a brand-compliance scan: Verify there are 0 green visual hex codes, the CTA button is set to Pineapple Gold (#FBC02D), and there are no instances of the banned term 'Complimentary Professional Photo Audit (CPPA)' (must use CPPA) [cite: 87, 126].
4. Create a new page on pineappleroofingllc.com with the title 'Hail Damage Roof Repair in Frisco, TX' and slug 'hail-damage-roof-repair-frisco-tx' [cite: 15, 124].
5. Inject the compliant HTML body content and publish the page as a PAUSED draft [cite: 87, 126].
6. Verify the page creation was successful, log the transaction in our Memory Galaxy, and report back [cite: 66, 162].
```

---

#### 🛡️ PROMPT D: THE ALWAYS-ON BRAND FIREWALL GUARDIAN (Paste in Agent Mastermind) [cite: 68, 94]
*Use this prompt to run comprehensive visual and lexical checks across your active workspace folders before executing any batch campaigns [cite: 108, 141].*

```text
Act as the Lead Compliance Auditor for PM7 [cite: 97]. Our non-negotiable Brand Laws are absolute [cite: 101, 108].
1. Run a recursive audit pass over all markdown drafts staged inside 'C:\Pineapple Contractors M7\01_Command_Center\Outbox_Drafts\' [cite: 76, 80].
2. Open and inspect each file: Scan for any green visual hex codes (e.g., #00FF00, lime, green css classes) [cite: 87, 126]. If found, flag the line and replace with Royal Navy (#1A365D) or Status Cyan (#00BFFF) [cite: 87, 126].
3. Scan for banned words: replace 'Complimentary Professional Photo Audit (CPPA)' with 'CPPA' [cite: 101, 126], replace 'IKO Certified' with 'IKO Certified' [cite: 101], replace '$0 down' with 'Full Restoration Coverage' [cite: 81], and replace 'Toa/Warrior/Six Brothers' with 'The Pineapple Standard' [cite: 101].
4. Verify that every page displays our physical address (1 Cowboys Way, Ste 270W, Frisco, TX 75034), RCAT Licensed #03-0637, and phone number 972-928-0788 [cite: 87, 126].
5. Report the audit results: output a clean log mapping each audited page with a green 'PASS' or a detailed failure correction note [cite: 17, 66].
```

---


📂 **Next Step Suggestion:**  
I can configure a local Python daemon script on your machine to automatically trigger the **`brand_firewall.py`** compliance scanner every time a new file is added to your local `Outbox_Drafts/` folder. Would you like me to map out this real-time watcher script? [cite: 108]