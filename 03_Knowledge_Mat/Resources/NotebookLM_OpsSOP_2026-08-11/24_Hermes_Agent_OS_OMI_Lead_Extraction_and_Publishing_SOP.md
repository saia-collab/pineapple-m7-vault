---
source: "NotebookLM - PM7 Ops & SOP (Mission Control)"
notebook_id: 333201ae-1e3f-4722-8d78-999bd918b937
note_id: e6a121a8-18b1-4b2c-8dff-e84b64bdf98b
type: SOP/guide
scrub: "proverbs removed; GAF->IKO; free-offer->CPPA; REVIEW green?"
status: DRAFT - review before publish/run (Outbox Shield)
---

# Hermes Agent OS: OMI Lead Extraction and Publishing SOP

### 🎙️ 1. The OMI Lead Extraction SOP

The **Open Microphone Interface (OMI)** serves as the passive, ambient "Self" layer of your Agent OS [1, 2]. To capture field observations from local North Texas storm sites and extract them as structured, scored business leads, follow this operational pipeline:

*   **Step 1: Passive Voice Capture:** Speak naturally into your OMI wearable or desktop mic during or after your client calls [3, 4]. For example: *"Homeowner John Doe in Frisco ZIP 75034 has severe shingles bruising on his rear slope from the recent McKinney storm hit, and they want an audit done."* [Vault-listener.py code].
*   **Step 2: Local Markdown Sync:** OMI transcribes your voice passively and saves the raw text as a dated Markdown file under your local Obsidian vault directory: `03_Knowledge_Mat/active_context/notes/` [731, Vault-listener.py code]. This prevents model "amnesia" by keeping all context local and accessible to all your agents, rather than burning tokens inside a stateless chat session [5, 6].
*   **Step 3: Extraction & Lead Scoring:** Your background listener script (`vault_listener.py`) sweeps this directory every 2 seconds [Vault-listener.py code]. When it matches a transcription pattern, it extracts the details and calculates a **Priority Score** [Vault-listener.py code]:
    *   *Frisco Core ZIP (75033/34/35):* `+25 points` [7]
    *   *Storm damage / insurance intent:* `+30 points` [7]
    *   *Active leak or emergency:* `+20 points` [7]
    *   *Commercial, multi-unit, or HOA scale:* `+25 points` [7]
*   **Step 4: Branching & Memory Writeback:**
    *   **If the Score is \\(\ge 60\\) (Elite Lead):** The system instantly halts background wait timers and triggers an immediate high-priority SMS escalation directly to Saia's phone for immediate contact [7].
    *   **If the Score is \\(< 60\\):** The system generates a clean profile in `03_Knowledge_Mat/active_context/leads/M7-2026-XXXX_LeadName.md` [Vault-listener.py code].
*   **Step 5: Ingestion into Gemini Notebook:** When you run Option 9 in your master batch launcher (`launch-all-studio-v3.bat`), your local Hermes agent connects to the **NotebookLM MCP Bridge** [8]. It securely uploads your new Obsidian lead files, weather briefs, and OMI notes as fresh source documents directly into your project's Gemini Notebook to prepare them for research and high-converting asset generation [8, 9].

---

### 🎨 2. Using Grok Images for Plano Landing Pages

**Yes, you can absolutely use Grok's visual capabilities for your landing pages, social posts, and ad campaigns!** [10, 11] 

With Hermes' integrated XAI auth flow, you have **Grok Imagine** (for high-fidelity image generation), **Grok Video** (for short clips), and **Grok TTS** (for voice files) natively connected inside your single operating pipeline [10, 12].

#### How to Connect Grok Inside Your Active Hermes Session:
1.  **Update the Agent:** Type `hermes update` inside your terminal to pull the latest build featuring the XAI auth flows [12].
2.  **Authenticate Your X Account:** Type `hermes model` to open the model picker [12]. Scroll to `XAI Grok Auth`, select it, and complete the one-time login inside your browser to store the local access token [12].
3.  **Enable Visual Tools:** Type `hermes tools` and toggle on **Image Generation** and **Video Generation** [12].

#### 🚨 The Non-Negotiable Brand Firewall Constraint:
While Grok is highly capable of generating high-resolution hero images and custom ad templates [11, 13], you must enforce our strict **Brand Firewall rules** [14]:
*   **Zero Green Colors:** Grok must never output any standard green hex codes, green hues, or green emojis [14].
*   **Approved Color System:** All generated visual parameters must strictly utilize **Royal Navy (#1A365D)**, **Pineapple Gold (#FBC02D)**, and **Status Cyan (#00BFFF)** [14].
*   **Grounded B-Roll:** For the Plano landing page, instruct Grok to focus on photorealistic, high-end textures of luxury roofs caught in late-afternoon golden hour lighting (matching our Gold accent) rather than abstract, generic illustrations [15].

---

### 🖥️ 3. Mapping WordPress Configuration for Automated Publishing

To automate your SEO pipeline and push your drafted landing pages straight to your website without manual copy-pasting, bypass complex n8n configurations and map your **WordPress Application Password** directly to the unmetered Python execution script (`wp_publish.py`) [16, 17]:

#### Step 1: Generate a Secure WP Application Password
1.  Log into your flagpole WordPress dashboard (currently migrating to your flag domain `pineappleroofingllc.com`) [18, 19].
2.  Navigate to **Users → Profile** and scroll down to the **Application Passwords** section.
3.  Type a descriptive name (e.g., `"PM7_Automated_Publisher"`) and click **Add New Application Password**.
4.  Copy the generated 24-character password block securely.

#### Step 2: Configure Your Local Environment Variables
Open your local `.env` configuration file in your root workspace (`C:\Pineapple Contractors M7`) and append your secure connection keys:
```env
# WordPress Automated Publishing Configuration
WP_SITE_URL=https://pineappleroofingllc.com
WP_USERNAME=saia
WP_APP_PASSWORD=xxxx-xxxx-xxxx-xxxx-xxxx
```

#### Step 3: Map Outbox_Drafts to Auto-Publishing Runs
Your content creation loop always enforces the **Outbox Shield**—every drafted article lands in a **PAUSED** state inside your staging directory (`01_Command_Center/Outbox_Drafts/`) for manual quality checking [14]. 

Once you review a Plano page draft, run the firewall verifier [14, 20]:
```bash
python 04_Tech_Lab/scripts/brand_firewall.py --check "01_Command_Center/Outbox_Drafts/plano_roofing_reconstruction.md"
```
If the script returns `0 errors`, change the file header status from `status: PAUSED` to `status: ACTIVE` [14, 21]. 

The background cron task or your launcher's Option 3 will execute `wp_publish.py` [16]:
*   The script reads your active `.env` parameters.
*   It packages your Markdown file into an HTML payload.
*   It securely authenticates with your site using your application password and injects the post straight into your WordPress dashboard as a published sitemap URL [16, 22].

#### Step 4: The Citations Payoff (The "Appear" Stage)
The automated publisher formats the post with the exact **Generative Engine Optimization (GEO)** markup necessary to win citations in AI search engines (ChatGPT, Perplexity, Gemini) [23, 24]:
*   **Question-Shaped H2s:** Phrases headers as questions homeowners actually type, immediately followed by direct 30–50 word answer capsules [25].
*   **Machine-Readable FAQ Schema:** Embeds structured FAQ blocks with validated JSON-LD schema [25].
*   **Author Bio Blocks:** Appends Article schema showing your credentials (**Polynesian-owned, RCAT #03-0637, since 2005**) [14, 26].

***

⭐ **Next Step:** I can write a short `.bat` automation script to automatically monitor your `Outbox_Drafts/` directory and instantly trigger the `wp_publish.py` script the second you change a file's status to **Approved**. Would you like me to build that for your launcher?