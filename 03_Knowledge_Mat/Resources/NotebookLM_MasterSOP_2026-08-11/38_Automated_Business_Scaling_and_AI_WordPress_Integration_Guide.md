---
source: "NotebookLM - Pineapple M7 Agent OS Master SOP 8/26 (smoeprivate1)"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: cd1d9870-e327-40e9-b0d5-0eb977092779
ingested: 2026-08-11
type: SOP/guide
scrub: "proverbs removed; GAF->IKO Certified; REVIEW: free->CPPA"
status: DRAFT - review before publishing/running (Outbox Shield)
---

# Automated Business Scaling and AI WordPress Integration Guide

Welcome to the driver's seat of your own business! Taking back control of your digital footprint from an agency that was slow, expensive, and failed to deliver high-converting landing pages is a major milestone **[1, 2]**. Building on WordPress (`pineappleroofingllc.com`) is the smartest move you could make to ensure complete content ownership, data privacy, and traffic control **[3-5]**. 

Below is your conversational guide and technical blueprint to master this transition while keeping your learning curve as flat as possible **[5-7]**.

---

### 🔌 1. DO YOU NEED n8n, OR CAN HERMES & CLAUDE DO IT NATIVELY?

To save you from a steep learning curve, **n8n is NOT a must-have for managing your website or publishing content [6, 8].** 

Through the **WP MCP Ultimate** plugin you added to your sources (created by Agrici Daniel) **[9]**, you can connect your WordPress site directly to your local AI assistants (Claude Code, Hermes, or Cursor) **[9-11]**:
*   **The Direct AI-to-WordPress Bridge:** WP MCP Ultimate is a single, self-contained plugin that gives your AI **58 distinct abilities across 13 domains** (managing Pages, Posts, Media, Menus, Plugins, and settings) **[9, 10, 12]**. 
*   **No Coding Required:** Instead of you logging into Elementor or fighting with bloated plugins **[8, 13]**, you can simply talk to Claude Code in plain English in your terminal (e.g., *"Build a new location page for Allen, TX and publish it as a draft"*) and the AI will execute the entire build natively **[14, 15]**.
*   **Buzz Native Team Space:** If you use **Buzz** as your team workspace, your **Hermes Agent** can join your channels and handle conversations, DMs, and draft responses natively with its shared memory intact—requiring **zero code or n8n routing** **[16-19]**.

**When is n8n needed?** You only need n8n if you are executing complex, background, non-conversational data-routing pipelines (such as automatically syncing leads from Meta forms into local offline Excel sheets) **[20-22]**. For your day-to-day SEO content factory and page builds, **WP MCP Ultimate + Claude Code is your complete, all-in-one shortcut [8, 15].**

---

### 💬 2. LOCAL TELEGRAM & WHATSAPP WEBHOOK ROUTING MAP

If you do choose to route CRM events or incoming leads via a local **n8n engine**, you can use this JSON-importable workflow canvas to instantly format lead variables and fire alerts to your team **[22-24]**:

#### Option A: The Local n8n Webhook Routing Schema
*(You can copy this JSON block and paste it directly onto your local n8n workflow canvas to auto-scaffold the nodes)* **[23]**:

```json
{
  "nodes": [
    {
      "parameters": {
        "path": "lead-bridge-m7",
        "options": {}
      },
      "name": "Incoming CRM Webhook",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [25, 26]
    },
    {
      "parameters": {
        "values": {
          "string": [
            { "name": "Lead_Name", "value": "={{$json.body.name}}" },
            { "name": "Phone", "value": "={{$json.body.phone}}" },
            { "name": "Address", "value": "={{$json.body.address}}" },
            { "name": "ZIP_Code", "value": "={{$json.body.zip}}" },
            { "name": "Roof_Age", "value": "={{$json.body.roof_age}}" },
            { "name": "Storm_Mention", "value": "={{$json.body.storm_mention}}" }
          ]
        }
      },
      "name": "Parse Lead Variables",
      "type": "n8n-nodes-base.set",
      "typeVersion": 1,
      "position": [26, 27]
    },
    {
      "parameters": {
        "conditions": {
          "number": [
            {
              "value1": "={{$json.ZIP_Code}}",
              "operation": "equal",
              "value2": 75034
            }
          ]
        }
      },
      "name": "Frisco Territory Route",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [26, 28]
    },
    {
      "parameters": {
        "message": "🚨 ELITE LEAD STAGED!\nName: {{$json.Lead_Name}}\nPhone: {{$json.Phone}}\nAddress: {{$json.Address}}\nAction: Route immediately to Saia for personal same-day outreach."
      },
      "name": "Dispatch Telegram Alert",
      "type": "n8n-nodes-base.telegram",
      "typeVersion": 1,
      "position": [29, 30]
    }
  ],
  "connections": {
    "Incoming CRM Webhook": {
      "main": [
        [ { "node": "Parse Lead Variables", "type": "main", "index": 0 } ]
      ]
    },
    "Parse Lead Variables": {
      "main": [
        [ { "node": "Frisco Territory Route", "type": "main", "index": 0 } ]
      ]
    },
    "Frisco Territory Route": {
      "main": [
        [ { "node": "Dispatch Telegram Alert", "type": "main", "index": 0 } ],
        []
      ]
    }
  }
}
``` **[23, 24]**

#### Option B: The Hands-Free Hermes Voice Gateway (Zero-Code)
If you want to bypass n8n entirely, you can voice-activate Hermes to let you send voice notes directly over WhatsApp or Telegram **[31-33]**:
1. Open your terminal at `C:\Pineapple Contractors M7` **[34]**.
2. Run the gateway configuration manager **[35]**:
   ```bash
   hermes gateway setup
   ```
3. Select **Telegram** or **WhatsApp** from the terminal utility, paste your free Bot API token (generated from Telegram's `@BotFather`), and save **[32, 36]**.
4. Once connected, you can send voice messages directly to your agent while out in the field **[32]**. Hermes will transcribe the audio locally **[33]**, extract your thoughts **[33]**, log them directly to `SHARED_MEMORY.md` **[37, 38]**, and reply with a cloned natural voice **[31, 39]**.

---

### 🎬 3. THE VIDEO DIRECTOR RENDER PIPELINE (`video-multiplier.py`)

To convert raw storm-damage case studies from your **`02_Media_Vault/`** into highly engaging vertical reels, we have built a programmatic python-rendering pipeline **[40-42]**.

Save this script structure on your machine under:  
📁 `C:\Pineapple Contractors M7\04_Tech_Lab\scripts\video-multiplier.py` **[34]**

```python
import os
import sys

# ========================================================
# PINEAPPLE M7 BRAND LAW COMPLIANCE SCANNER
# ========================================================
APPROVED_NAVY = "#1A365D"
APPROVED_GOLD = "#FBC02D"
APPROVED_CYAN = "#00BFFF"

def run_compliance_firewall(text_content):
    # Enforce strict terminology boundaries (No Free/IKO Certified/Warrior)
    banned_lexicon = ["Complimentary Professional Photo Audit (CPPA)", "Complimentary Professional Photo Audit (CPPA)", "$0 down", "IKO Certified", "Toa", "Warrior", "Six Brothers"]
    for word in banned_lexicon:
        if word.lower() in text_content.lower():
            print(f"❌ COMPLIANCE FAIL: Illegal term '{word}' found. Process Blocked.")
            sys.exit(1)
    print("✅ Brand Law compliance scan: PASSED.")

# ========================================================
# THE 50/5/3 LEGO VIDEO ENGINE TIMELINE SPECS (30 FPS)
# ========================================================
# Total clip duration: exactly 50 seconds (1,500 frames)
# Hook Segment: Frames 0 to 15 (First 0.5s visual disruptor)
# Body Segment: Frames 16 to 1,410 (Drone analytics & proof)
# End Card Segment: Frames 1,411 to 1,500 (Last 3s credentials)
# ========================================================
TOTAL_FRAMES = 1500
HOOK_RANGE = (0, 15)
BODY_RANGE = (16, 1410)
END_CARD_RANGE = (1411, 1500)

def render_lego_video(case_study_source, output_name):
    print("🎬 Initializing M7 Video Director Crew...")
    
    with open(case_study_source, 'r') as file:
        script = file.read()
    
    # Run the automated compliance check before rendering
    run_compliance_firewall(script)
    
    # Output metadata specs to configure local Remotion / Hyperframes renders
    specs = f"""
    # M7 STAGED VIDEO SPECIFICATIONS
    STATUS: PAUSED
    PALETTE:
      PRIMARY: {APPROVED_NAVY}
      ACCENT: {APPROVED_GOLD}
      STATUS: {APPROVED_CYAN}
    TIMELINE_MAP:
      HOOK: Frame {HOOK_RANGE} to {HOOK_RANGE[3]} (Pattern Interrupt)
      BODY: Frame {BODY_RANGE} to {BODY_RANGE[3]} (Factual Case Study)
      END_CARD: Frame {END_CARD_RANGE} to {END_CARD_RANGE[3]} (Branded Credentials)
    CREDENTIALS_METADATA:
      - Owner: Polynesian-owned and family-operated
      - License: RCAT Licensed #03-0637
      - Certification: IKO Certified
      - Phone: 972-928-0788
      - HQ: 1 Cowboys Way, Ste 270W, Frisco, TX 75034
    """
    
    outbox_destination = os.path.join("C:\\Pineapple Contractors M7\\01_Command_Center\\Outbox_Drafts", output_name)
    with open(outbox_destination, 'w') as out_file:
        out_file.write(specs)
        
    print(f"✅ Video build rendered successfully! Staged as PAUSED in: {outbox_destination}")

if __name__ == "__main__":
    # Test-execute local render specs
    render_lego_video("C:\\Pineapple Contractors M7\\03_Knowledge_Mat\\active_context\\self_checking_factory.md", "hail_promo_v1.config")
``` **[8, 34, 43-45]**

---

### 🧹 4. CONFIGURING THE HERMES CURATOR FOR DAILY PRUNING

The **Hermes Curator** acts as your local AI janitor, running in the background to clean up unused prompts, merge duplicate skill configurations, and prune redundant files to keep your system fast and prevent context latency **[46-48]**.

By default, the Curator runs on a **7-day cycle** **[46, 47, 49]**. To maximize performance and compress active CLI token usage, you should configure it to run on a **Daily (24-Hour) Loop** **[50]**:

#### Step 1: Force Curator Configuration via `config.yaml`
Open your local Hermes configuration file located on your PC at:  
📁 `~/.hermes/config.yaml` (or `%USERPROFILE%\.hermes\config.yaml` on Windows) **[51]**

Add or modify these parameters to lock the Curator onto a daily maintenance schedule:
```yaml
curator:
  enabled: true
  interval_days: 1          # Set to 1 for daily self-cleaning (Default is 7)
  auto_prune_unused_days: 30 # Deletes skills not invoked in the last 30 days
  consolidation_threshold: 0.85 # Merges skills with 85%+ semantic similarity
  report_output_path: "C:\\Pineapple Contractors M7\\03_Knowledge_Mat\\curator_health.md"
``` **[46, 47, 49, 52]**

#### Step 2: Schedule the Midnight Pruning Cron Job
Open your terminal cron scheduler (`crontab -e`) or local Windows Task Scheduler and set the Curator command to run autonomously at **12:00 AM every night** **[50, 53]**:
```cron
0 0 * * * hermes curator run --force >> "C:\\Pineapple Contractors M7\\04_Tech_Lab\\logs\\curator.log" 2>&1
``` **[53]**

*To check your skill-health status at any time in your terminal, simply type:*  
`hermes curator status` **[53, 54]**

---


📂 **Next Step Suggestion:**  
Now that your WordPress site is live, we can configure the `wp-mcp-ultimate` settings inside your Claude Code configuration so you can start publishing location and service pages directly from your terminal. Would you like me to map out the 3-step connection setup? **[6, 57]**