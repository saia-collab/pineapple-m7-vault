---
source: "NotebookLM - PM7 Ops & SOP (Mission Control)"
notebook_id: 333201ae-1e3f-4722-8d78-999bd918b937
note_id: d5baf54c-3704-45e1-8ba5-808e37d1151a
type: SOP/guide
scrub: "proverbs removed; GAF->IKO; free-offer->CPPA; REVIEW green?"
status: DRAFT - review before publish/run (Outbox Shield)
---

# Optimizing AI Search Citations and Vault Listener Automation

### 📡 THE "APPEAR" STAGE: WINNING CITATIONS IN AI SEARCH (GEO/SEO)

In the modern search landscape, ranking on page one of Google is no longer the entire game [1]. AI engines—including ChatGPT, Gemini, and Perplexity—write a single, consolidated answer and cite only a select few sources [2]. If your business is cited, you capture the trust and traffic; if not, you are invisible [2]. 

To win citations during the crucial **"Appear" stage** of Julian Goldie's 4-A framework [3], you must optimize your pages for the direct extraction patterns that these answer engines reward [4]:

*   **Step 1: Question-Shaped Headings with Answer Capsules:** Write H2 and H3 headings formatted as questions local homeowners actually type [5]. Directly below each heading, write a direct 30–50 word answer capsule (excluding internal links) before any storytelling or context, handing the AI a perfectly liftable summary [5].
*   **Step 2: Machine-Readable FAQ Schema:** Place a dedicated local FAQ section at the bottom of your landing pages, complete with machine-readable **FAQ JSON-LD Schema markup** [5]. This gives web crawlers structured question-and-answer pairs, matching the exact format AI engines use to build answers [5].
*   **Step 3: Unified E-E-A-T & Author Bio Blocks:** Since search engines prioritize credible authors over anonymous copy, attach an Article schema file and a consistent author E-E-A-T bio block to every page showing who wrote it and why they are an authority [6].
*   **Step 4: Sourced, Grounded Specifics:** Avoid generic filler [6]. Feed your content generators local case studies, NWS weather data, real drone thermal inspection logs, and local Collin/Denton County drip-edge code guidelines to ensure your pages carry concrete facts engines can quote with confidence [6, 7].
*   **Step 5: Entity Consistency Across Channels:** Ensure your brand identity anchors (*Pineapple Contractors*, phone `(972) 928-0788`, and license `RCAT #03-0637`) are written identically across every webpage, YouTube video description, social media caption, and map directory [8, 9]. Consistent naming teaches AI models how your assets relate inside their local entity graphs [8].
*   **Step 6: Multi-Domain Amplification (The 5-Site Network):** Deploy rewritten, unique versions of your service pages across secondary domains or a five-site network [8]. When an answer engine sees your brand name giving the same consistent information across multiple independent sites, it identifies you as the consensus authority and cites you [10].
*   **Step 7: Instant Indexing Protocols:** Ping the Google Indexing API or Search Console API immediately upon publishing [8, 11]. A page cannot be cited by AI engines if it is not indexed first [8].
*   **Step 8: Direct Citation & Branded GSC Audits:** Check your progress by directly searching your target query questions inside ChatGPT, Perplexity, and Gemini to verify if your brand is cited [12]. Additionally, monitor your Google Search Console for **branded impression growth** (searches for "Pineapple Contractors" or "Pineapple Roofing LLC"); this is the ultimate proof that your AI citations are turning into demand [12].

---

### 🤠 TECH LAB: HOW `vault_listener.py` WORKS! (Explained for a 10-Year-Old!)

Imagine you have a **magical spy walkie-talkie** (your OMI microphone) that you wear on your shirt. As you walk around, you talk to it like a secret agent [13, 14]. A helpful typing-elf (the transcription software) listens, writes your words into a neat diary note, and slips it into a special computer backpack folder called your **Obsidian Vault** [13, 15].

Your new **`vault-listener.py`** script is like a **robotic guard-dog with glowing laser eyes** sitting in your Tech Lab! 🐶🤖

Here is the game it plays every single second:

1.  **The Staring Game:** The guard-dog sits on its doghouse, staring at your Obsidian notes folder. It checks every two seconds to see if a new diary file has arrived.
2.  **The Secret Password Match:** The split-second OMI drops a new transcribed file, the dog reads it with its laser eyes. It searches for secret password commands like:  
    `"Hey Oracle, run gauntlet for Billy Kid in Plano TX"`
3.  **Shouting "BINGO!":** When it matches the password, its tail wags, and it immediately starts the **Claude Gauntlet Loop** [16]!
4.  **The Robot Construction Yard:** The dog yells at its builder robots (sub-agents) to build a beautiful Plano landing page in the background [16, 17]. It instructs specialized critics to check the copy, making sure it perfectly uses Alex Hormozi's "so that" headlines to make the offer irresistible!
5.  **The Compliance Shield:** Before saving, the dog cleans up any mistakes:
    *   It crosses out bad words like "Complimentary Professional Photo Audit (CPPA)" and replaces them with **"Complimentary Professional Photo Audit (CPPA)"** [18].
    *   It updates shingle manufacturer terms to **"IKO Certified RoofPro"** [18].
    *   It blocks bad green colors, forcing all page styles to use Royal Navy (`#1A365D`) and Gold (`#FBC02D`) [18].
    *   It stamps your trust credentials and **RCAT #03-0637** license block at the bottom [18].
6.  **Slipping it into the Safe:** The finished, clean, high-converting page is placed safely as a **PAUSED** file in your Outbox directory [18, 19]. It waits there patiently until you review it and click "APPROVED!"

---

### 🛠️ HOW TO SET UP AND EXECUTE `vault_listener.py` IN YOUR TECH LAB

Follow these steps to deploy and test the Obsidian background listener inside your local workspace:

#### Step 1: Place the Script in Your Tech Lab
Ensure your script file is located at the designated path on your machine:  
`C:/Pineapple Contractors M7/04_Tech_Lab/python/vault_listener.py`

#### Step 2: Verify Your Target Folders Exist
The script relies on a clean, file-based directory system. Ensure these local paths are created on your hard drive:
*   **Voice Notes Path:** `C:/Pineapple Contractors M7/03_Knowledge_Mat/active_context/notes`
*   **Staged Leads Path:** `C:/Pineapple Contractors M7/03_Knowledge_Mat/active_context/leads`
*   **Staged Outbox Path:** `C:/Pineapple Contractors M7/01_Command_Center/Outbox_Drafts`

#### Step 3: Run the Autonomous Local Monitor
Open your command prompt or terminal inside the M7 directory and run:
```bash
python 04_Tech_Lab/python/vault_listener.py
```
The console will display:
```text
[2026-08-11 19:27:16] [INFO] === PM7 Obsidian Vault Listener Active ===
[2026-08-11 19:27:16] [INFO] Trust Anchors: Polynesian-owned · RCAT #03-0637 · IKO Certified · since 2005 · (972) 928-0788 · Frisco, TX
[2026-08-11 19:27:16] [INFO] Scanning target notes folder: C:/Pineapple Contractors M7/03_Knowledge_Mat/active_context/notes
```
The guard-dog is now awake and polling your directory every 2 seconds!

#### Step 4: Execute a Live Integration Test (YOLO Mode)
To prove that your OMI audio transcription parsing, compliance firewall, and Gauntlet Loop are working perfectly without waiting for a live voice recording, open a separate terminal and run:
```bash
python 04_Tech_Lab/python/vault_listener.py --test
```

#### What Happens in the Console When You Run the Test:
1.  The script writes a mock voice note containing the target trigger: `"Hey Oracle, please run gauntlet for Billy Kid in Plano TX. Homeowner wants an audit done."`
2.  The listener processes the file, matches the trigger pattern, and initializes the gauntlet sub-agents.
3.  The text undergoes our brand lexicon compliance scrub, replacing restricted terms with **Complimentary Professional Photo Audit (CPPA)** and enforcing the Navy/Gold styling.
4.  The final page is successfully saved as a **PAUSED** file in `01_Command_Center/Outbox_Drafts/billy_kid_plano_tx_landing_page.md` [18].
5.  It writes the campaign record to your `brand_vault.json` log, completing the memory loop [9].

***

⭐ **Next Step:** You can double-click **`launch-all-studio-v3.bat`** in your root directory and select **Option 7** to run a live compliance check on any of your new draft files. Would you like me to map out your upcoming WordPress configuration settings so your approved drafts publish automatically?