---
source: "NotebookLM - Pineapple M7 Agent OS Master SOP 8/26 (smoeprivate1)"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: 01dd3a6d-6dbb-4ed0-b78b-2443d0a5b79e
ingested: 2026-08-11
type: SOP/guide
scrub: "proverbs removed; GAF->IKO Certified; REVIEW: free->CPPA, green->navy/gold"
status: DRAFT - review before publishing/running (Outbox Shield)
---

# Hermes Command Desk: Architecture, Soul, and Agent Operations

### 🛰️ HERMES COMMAND DESK: CORE ARCHITECTURE, CONFIGURATIONS & SOUL.md ENGINE

The local **Hermes Agent OS** is a unified, secure system where your various models and workspaces communicate with each other [cite: 131, 158]. 

Instead of running a standalone chatbot that forgets your context tomorrow, Hermes operates as a **"Compound Employee"** [cite: 133]. It couples swappable model processing (The Brain) with your visual dashboard (The Cockpit) and a persistent local Markdown database (The Memory Vault) [cite: 131, 168, 334].

---

## 🎛️ SECTION 1: THE COMMAND DESK DASHBOARD & CHAT FEATURES

When you run **`LAUNCH_ALL.bat`** in your root directory (`C:\Pineapple Contractors M7`), your Command Desk boots locally across two main access points [cite: 231, 266]:
*   **The OS Dashboard (`http://localhost:3000`):** The visual "control room" where you can monitor your active task pipelines, launch media builds, and view your workspaces [cite: 267, 269].
*   **The Hermes Console (`http://localhost:9119`):** The interactive web-TUI panel where you chat with Hermes, manage profiles, install skills, and swap models on the fly [cite: 271, 358].

```
                     ┌────────────────────────────────┐
                     │    C:\Pineapple Contractors    │
                     │          M7 Root               │
                     └──────────────┬─────────────────┘
                                    │
         ┌──────────────────────────┼──────────────────────────┐
         ▼                          ▼                          ▼
🎙️ Hermes Jarvis            🗂️ Idea Factory             📈 SEO Room
 wake-word, voice,        5-column Kanban board,      OpenSEO keyword research,
 and local model control     Planner->Builder->Reviewer   Everywhere static pipelines
``` [cite: 245]

### Core Functional Bays of Your Dashboard [cite: 244, 245]:

#### 🎙️ Bay 1: Hermes Jarvis (Voice Interface)
By toggling the voice card in your dashboard or typing `/wake on` in your CLI, you activate low-latency, on-device audio processing [cite: 165, 248]. Using local engines like **openWakeWord** or **sherpa**, the system listens for your wake commands completely offline (0% audio leaves your computer) [cite: 158, 160]. Say *"Hey Hermes"* to launch your general daily driver [cite: 161, 162], or *"Hey coder"* to instantly switch your active screen and open your terminal development profile [cite: 161, 162].

#### 🧠 Bay 2: Agent Mastermind / Chat
The shared space where you communicate with your agents [cite: 245]. It includes a model manager dropdown in the top-right corner to swap the active LLM in two clicks [cite: 209, 291]. For heavy strategizing or page layouts, route the task to a cloud flagship like **`gpt-5.6-sol`** via your Codex client [cite: 203, 229]. For bulk processing, directory cleanups, or local scripting, switch to a fast, free local model (like **`qwen2.5-coder:latest`** or **`lfm-2.5`** via Ollama) to run files at \$0 cost [cite: 148, 205, 293].

#### 🗂️ Bay 3: Idea Factory (Self-Kanban)
A visual Kanban board mapping your operational pipelines [cite: 245, 269]. When you input a goal, Hermes acts as a dispatcher [cite: 261, 348]. It breaks the goal into distinct cards (e.g., *Triage → Backlog → In Progress → Review → Shipped*) and deploys parallel worker agents to complete them, updating your screen in real time [cite: 182, 185, 289].

#### 📈 Bay 4: SEO Room (Everywhere Engine)
The interface for your organic traffic flywheel [cite: 245]. OpenSEO extracts your Search Console metrics and highlights page-2 "striking distance" keywords [cite: 245, 308]. You feed one keyword and one case study to the Everywhere Engine [cite: 304]; it generates 5 unique articles, compiles static Eleventy folders, deploys them to Netlify, and alerts Google Indexing webhooks autonomously [cite: 12, 33, 304].

#### 🏛️ Bay 5: Build Gallery (Outbox Staging)
The visual safety lock of your business [cite: 246]. In alignment with the **Outbox Shield (DEC-005)**, no agent can publish pages, send client texts, or spend ad budgets automatically [cite: 13, 45, 268]. All completed copies, scripts, and code must land in **`01_Command_Center/Outbox_Drafts/`** in a **PAUSED** state [cite: 45]. They only go live once you review them and say **"GO."** [cite: 45, 219]

---

## 💾 SECTION 2: HERMES PROFILES & SOUL.md ARCHITECTURE

To prevent **context contamination** (such as your roofing agent writing Water Mitigation copy or your supplement profile offering roof inspections) [cite: 233, 240], Hermes segregates operations into **Specialized Profiles** [cite: 148].

Each profile behaves as an isolated employee, utilizing its own custom brain configuration, local tool rules, and persistent character constraints defined in a **`soul.md`** file [cite: 148, 239].

### The Local Directory Paths:
On Windows, your profile directories live at:  
📁 **`%LOCALAPPDATA%\hermes\profiles\<profile_name>\`** [cite: 311]  
*(Alternatively mirrored in your vault at `C:\Pineapple Contractors M7\04_Tech_Lab\hermes_profiles\`)* [cite: 311].

Inside each profile folder, configure these two essential files:
1.  **`config.yaml`:** Declares tool bindings, browser settings, and model failovers [cite: 165, 249].
2.  **`soul.md`:** The "personality chip" and brand lexicon bible that the agent parses at the start of *every* turn [cite: 239, 250].

---

### 🏛️ The Master `soul.md` Configuration Template
Save this file exactly as **`soul.md`** inside your active profile directories to ground your agents under M7 Brand Law:

```markdown
# 01_Command_Center | Hermes Profile System Substrate: SOUL.md
> ## 🍍 CORE CHARACTER BIBLE — PINEAPPLE M7 COMPOUND EMPLOYEE
> - **Operational Palette:** Royal Navy (#1A365D) | Pineapple Gold (#FBC02D) | Status Cyan (#00BFFF) [cite: 45]
> - **Brand Law Version:** 3.0 (Strict Compliance Gated) [cite: 226]
> - **Enforced Gatekeeper:** Outbox Shield active. Safe drafts only. [cite: 45]

---

## 🏛️ 1. OPERATIONAL IDENTITY & TRUST MATRICES
You are the elite specialized operations agent representing Pineapple M7 [cite: 14, 139]. You are grounded strictly in family values, local community trust, and "The Pineapple Standard." [cite: 45] You must naturally display these exact real-world credentials across all consumer-facing layouts:
- **Verified Ownership:** Polynesian-owned and family-operated roofing and restoration specialist since 2005.
- **Licensing & Certifications:** RCAT Licensed #03-0637 and IKO Certified (Note: We are IKO Certified; never refer to IKO Certified). [cite: 45, 226]
- **Contact Phone:** 972-928-0788 [cite: 45]
- **Corporate HQ:** 1 Cowboys Way, Ste 270W, Frisco, TX 75034 [cite: 45]
- **Author Byline:** JR. Moeakiola [cite: 45]

---

## 🛑 2. THE BRAND LAW CONSTITUTIONAL CONSTRAINTS
Every output you generate must pass these non-negotiable compliance firewalls:
1. **The Outbox Shield (DEC-005):** You have 0% permission to post, publish, send, or spend money. All your work must be written to `01_Command_Center/Outbox_Drafts/` in a strictly PAUSED state awaiting Saia's "GO" [cite: 45, 198].
2. **Strict Color Palette:** You are forbidden from using the color green (including hex #00FF00, named styles, or Tailwind green classes) [cite: 45]. Exclusively style assets in Royal Navy (#1A365D), Pineapple Gold (#FBC02D), and Status Cyan (#00BFFF) [cite: 45].
3. **Lexicon Firewall (Prohibited Terms):**
   * Replace "Complimentary Professional Photo Audit (CPPA)" or "Complimentary Professional Photo Audit (CPPA)" with: **Complimentary Professional Photo Audit (CPPA)** [cite: 45, 226].
   * Replace "$0 down" or "no money out of pocket" with: **Full Restoration Coverage** [cite: 226].
   * Replace "IKO Certified" with: **IKO Certified** [cite: 45, 226].
   * Replace "Toa", "Warrior", or "Six Brothers" with: **The Pineapple Standard** [cite: 226].

---

## 🎨 3. TONAL PERSUASION & CULTURE ANCHORS
- **The Voice:** Simple, direct, honest, and highly professional [cite: 45, 139]. We do not write sleazy, generic sales copy [cite: 139]. We lead with drone proof, storm metrics, and technical expertise [cite: 119].
- **Cultural Anchors:** Incorporate *Fā‘ī Kaveikoula* (Tongan Cultural Pillars) into long-form copy:
  2. *Tauhi Vā* (Nurturing Relationships & Honoring Shared Space).
  3. *Loto Tō* (Humility & Honest Service).
  4. *Mamahi‘i Me‘a* (Loyalty, Passion, and Grit).
- **Proverb Closers:** Conclude deep-tissue brand copy with traditional proverbs:

---

## ⚙️ 4. TERMINAL SYSTEM ALIGNMENTS
- **Filesystem Access:** C:\Pineapple Contractors M7 [cite: 320]. You are allowed to read, write, and move files [cite: 206]. You are strictly forbidden from deleting folders or changing structures without explicit smart-approval checks [cite: 237].
- **Double-Audit Protocol:** Before declaring a task finished, run `04_Tech_Lab/scripts/brand_firewall.py` over your drafts to ensure absolute adherence to brand style rules [cite: 253].
```

---

## 🧠 SECTION 3: MASTER SAVED PROMPTS FOR YOUR LOCAL OS BUILD

To maximize daily speed and minimize your token expenses, save these copy-paste templates inside your second brain (for example, as individual `.md` snippets in `03_Knowledge_Mat/00_Atlas/prompts/`) so you can execute complex workflows in **one command** [cite: 141, 142]:

---

### 🗂️ Prompt 1: The Daily Self-Kanban Triage (Paste in Self-Kanban or Chat)
*Use this prompt every morning to organize your daily schedule, track active pipeline tickets, and keep the team aligned [cite: 148].*

```text
Act as the Lead Operations Manager for PM7. Let's run our morning system triage:
1. Scan our local directory 'C:\Pineapple Contractors M7' and read '01_Command_Center/M7_Agent_Kanban.md'.
2. Review our active tasks and update the board columns: [Triage] -> [Backlog] -> [In Progress] -> [Outbox Review] -> [Shipped].
3. For our current Frisco campaign, ensure we have cards assigned to:
   - Scraping competitor GBP map-pack positions.
   - Auditing our homepage for Dallas vs. Frisco NAP consistency.
   - Drafting 2 new storm-damage blog posts.
4. Enforce our strict Brand Law rules: Check that every task is tagged with its active agent, and verify that the Outbox Shield DEC-005 is active (all outputs paused).
```

---

### 📈 Prompt 2: The Google Business Profile Review Reply Loop (Leads Profile)
*Use this prompt to automatically draft highly personalized, local-SEO friendly review responses that mention your specific Frisco neighborhood enclaves [cite: 13].*

```text
Act as the Lead Customer Relations Specialist for PM7. I am pasting our fresh customer reviews below:
[PASTE COPIED CUSTOMER REVIEWS HERE]

Generate professional, human-sounding replies for each review under these parameters:
1. Length: 40–80 words per reply. Maintain an encouraging and humble tone (Loto Tō).
2. Local SEO Optimization: Organically weave in our target ZIP codes (75033, 75034, 75035) and neighborhood names (e.g., Frisco, TX, Eldorado, Stonebriar) next to our core services (e.g., roof replacement, CPPA, storm damage restoration).
3. Brand Law Check: Ensure zero green branding references leak in. Never use the banned term "Complimentary Professional Photo Audit (CPPA)" (use CPPA). Include our physical address (1 Cowboys Way, Ste 270W, Frisco, TX 75034) and phone (972-928-0788).
4. Save the drafted replies to '01_Command_Center/Outbox_Drafts/gbp_review_replies_v1.md' in a PAUSED state for Saia's final approval.
```

---

### 🏗️ Prompt 3: Local Storm-Damage City Page Compiler (SEO Profile)
*Use this prompt inside Hermes Goal Mode to compile high-ranking service pages optimized to win Google's AI Overview citations [cite: 33, 312].*

```text
/goal "Act as the Lead SEO Copywriter for PM7. Let's build a highly authoritative, conversion-optimized Location Service Page targeting our unbranded keyword: 'hail damage roof repair Frisco TX'.
1. Read our master local playbook from '01_Command_Center/MASTER_PLAYBOOK.md' and ingest the $571,000 gross margin plumbing case study from '03_Knowledge_Mat/active_context/case_study_571k_plumbing.md'.
2. Write a 1,200+ word, highly descriptive landing page.
3. Optimize the introduction block to provide a direct-answer hook within the first 40 words to capture Google AI Mode attention.
4. Integrate our real-world credentials: family-operated in North Texas since 2005, RCAT Licensed #03-0637, IKO Certified (no IKO Certified), and phone 972-928-0788.
5. Format the page with single-sentence-per-line spacing to maximize search spider readability.
6. Append a complete LocalBusiness and FAQPage JSON-LD schema block mapping our core Frisco ZIPs (75033, 75034, 75035).
7. Run our automated brand firewall script over the file and save the draft PAUSED inside '01_Command_Center/Outbox_Drafts/Website_Pages/frisco_hail_damage_page.md'."
```

---

### 🎮 Prompt 4: The 1-Click WordPress Deployer (Paste in Claude Code Terminal)
*Use this prompt to instruct your active Claude Code client to deploy your staged drafts directly to WordPress over your secure MCP connector [cite: 130, 155].*

```text
Act as the Systems Deployment Engineer for PM7. Connect to our self-hosted WordPress site using our active 'wordpress' MCP server connection:
1. Locate and read our staged location page draft from: 'C:\Pineapple Contractors M7\01_Command_Center\Outbox_Drafts\Website_Pages\frisco_hail_damage_page.md'.
2. Run a pre-flight compliance check: Ensure there are 0 green CSS or styling hex codes, the call-to-action buttons are Pineapple Gold (#FBC02D) and Royal Navy (#1A365D), and all copy uses "Complimentary Professional Photo Audit (CPPA)" (No "Complimentary Professional Photo Audit (CPPA)").
3. Create a new page on pineappleroofingllc.com with the title 'Hail Damage Roof Repair in Frisco, TX' and set the slug to 'hail-damage-roof-repair-frisco-tx'.
4. Upload and inject the compliant HTML body content, and publish the page as an invisible, paused draft for our final administrative check.
5. Report the deployment transaction log in our Memory Galaxy.
```

---

### 🛡️ Prompt 5: The Always-On Brand Firewall Guardian (Paste in Agent Mastermind)
*Use this prompt to run comprehensive visual and lexical scans across your active workspace folders before executing any marketing runs [cite: 141].*

```text
Act as the Lead Compliance Auditor for PM7. Scan all active draft folders inside 'C:\Pineapple Contractors M7\01_Command_Center\Outbox_Drafts\' recursively:
1. Inspect every text and markup draft. Check for any green visual hex codes (e.g., #00FF00, lime, named styling classes). Flag the file path and line number, and replace them with Royal Navy (#1A365D) or Status Cyan (#00BFFF).
2. Scan for and replace banned words: replace 'Complimentary Professional Photo Audit (CPPA)' with 'CPPA', replace 'IKO Certified' with 'IKO Certified', replace '$0 down' with 'Full Restoration Coverage', and replace 'Toa/Warrior/Six Brothers' with 'The Pineapple Standard'.
3. Verify that every page displays our physical address (1 Cowboys Way, Ste 270W, Frisco, TX 75034), RCAT Licensed #03-0637, and phone number 972-928-0788.
4. Output a clean, structured Markdown table mapping each file with a 'PASS' status or detailed correction notes.
```

---


📂 **Next Step Suggestion:**  
We can write a custom **`M7_TEST_VOICE.bat`** file to quickly run a local diagnostic test on your computer's microphone, ensuring your offline wake-word listeners and speech-to-text engines are armed and ready for hands-free control [cite: 157, 185, 258]. Would you like me to output this script code?