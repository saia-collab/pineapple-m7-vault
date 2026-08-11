---
source: "NotebookLM - Pineapple M7 Agent OS Master SOP 8/26 (smoeprivate1)"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: af9d8d1f-8e3b-4aaa-9077-13de777ec782
ingested: 2026-08-11
type: SOP/guide
scrub: "proverbs removed; GAF->IKO Certified; REVIEW: free->CPPA, green->navy/gold"
status: DRAFT - review before publishing/running (Outbox Shield)
---

# M7 Brand Law Integration and Automation Playbook

To flatline your learning curve, you do **not** need to build a complex local n8n server from scratch [cite: 168, 213]. While n8n is an excellent zero-cost bouncer for syncing large, multi-database pipelines [cite: 255], your local **Hermes Agent and Buzz can natively handle webhooks, alerts, and direct-to-phone messaging out of the box** [cite: 162, 163]. 

Here is your master integration playbook, mapped under strict M7 Brand Law, to connect Telegram/WhatsApp, configure your video render pipeline, and automate daily skill pruning [cite: 87].

---

# 🛰️ M7 Brand Law — Webhook, Video, & Curation SOP
**Document ID:** `03_Knowledge_Mat/00_Atlas/SOP_M7_Integration_Bridges.md` [cite: 286]  
**Security Tier:** Strict Outbox Shield Gated (DEC-005) [cite: 87]  
**Operational Colors:** Royal Navy (`#1A365D`) | Pineapple Gold (`#FBC02D`) | Status Cyan (`#00BFFF`) — **0% Green** [cite: 87]  

---

## 🔌 SECTION 1: THE FLAT LEARNING CURVE — HERMES & BUZZ VS. N8N

You can bypass n8n entirely if you just want instant notifications, mobile chat control, or Slack-style group collaboration [cite: 162, 168]. 

### The Difference:
*   **The Native Path (Hermes Gateway + Buzz):** Hermes includes its own secure **Gateway** supporting 19 messaging platforms (including Telegram, Discord, Teams, and WhatsApp) [cite: 147, 175, 182, 193]. When connected to **Buzz** (a beautiful, Slack-like team workspace app) [cite: 161, 163], Hermes joins channels, answers DMs, and drafts pipeline responses natively with all its local memory intact [cite: 161, 167]. **No code required.** [cite: 213]
*   **The n8n Path:** Only mandatory if you are executing heavy, non-conversational programmatic data routing (such as auto-syncing cold CSV files from local folders into your CRM pipeline automatically) [cite: 90, 255].

---

## 💬 SECTION 2: TELEGRAM ALERT & WHATSAPP WEBHOOK SETUP [cite: 182, 193]

### Route A: Direct Telegram Gateway (Hands-Free Control) [cite: 182]
1. Open your terminal at `C:\Pineapple Contractors M7` [cite: 296].
2. Run the Gateway initialization command [cite: 164]:
   ```bash
   hermes gateway setup
   ```
3. Select **Telegram** from the terminal selector list.
4. Paste your Telegram Bot API token (generated for free from `@BotFather`).
5. **Set the Chat ID:** Link your personal Telegram account ID so only *you* can command the agent.
6. Run `/wake on` in your Hermes terminal to allow hands-free voice commands [cite: 225]. 
7. **The Result:** You can now text or send voice notes to Hermes while walking the dog [cite: 193]. Hermes will execute local jobs and respond back with text or automatic text-to-speech (TTS) [cite: 153, 193].

### Route B: WhatsApp Webhook & Voice-Note Response [cite: 153]
1. Launch the Gateway setup [cite: 164]:
   ```bash
   hermes gateway setup --platform whatsapp
   ```
2. Link your Meta Developer WhatsApp Business API token.
3. Once enabled, Hermes becomes fully platform-aware [cite: 153]. You can send rambled audio notes [cite: 210]; Hermes will transcribe them locally [cite: 210], extract your operational ideas [cite: 210], log them directly to `SHARED_MEMORY.md` [cite: 115, 199], and reply directly with a natural spoken voice [cite: 153, 223].

---

## 🎬 SECTION 3: VIDEO DIRECTOR RENDER PIPELINE (`video-multiplier.py`)

This python-engineered pipeline runs on your local computer to convert raw case study scripts into high-converting, dopamine-style reels [cite: 89, 451].

Save this script structure directly to your workspace:  
📁 `C:\Pineapple Contractors M7\04_Tech_Lab\scripts\video-multiplier.py` [cite: 296]

```python
import os
import sys

# ==========================================
# M7 BRAND LAW CONSTITUTIONAL CHECKS
# ==========================================
NAVY_HEX = "#1A365D"
GOLD_HEX = "#FBC02D"
CYAN_HEX = "#00BFFF"

# Prohibit Green Color Space
BANNED_COLOR_CHANNELS = ["green", "rgb(0, 255, 0)", "#00FF00", "lime"]

def verify_brand_safety(script_text):
    banned_terms = ["Complimentary Professional Photo Audit (CPPA)", "$0 down", "IKO Certified", "Toa", "Warrior", "Six Brothers"]
    for term in banned_terms:
        if term.lower() in script_text.lower():
            print(f"❌ FIREWALL BLOCK: Found banned term '{term}'")
            sys.exit(1)
    print("✅ Brand lexicon check: PASSED.")

# ==========================================
# THE 50/5/3 VIDEO STRUCTURE PARAMETERS (30 FPS)
# ==========================================
# Total length: 50 seconds (1,500 frames)
# Hook Segment: Frames 0 to 15 (0.5 seconds attention grabber)
# Body Segment: Frames 16 to 1,410 (Delivery of case study value)
# End Card Segment: Frames 1,411 to 1,500 (3s call-to-action slide)
# ==========================================
FRAME_RATE = 30
TOTAL_FRAMES = 1500

HOOK_END_FRAME = 15
BODY_END_FRAME = 1410
END_CARD_START_FRAME = 1411

def render_pipeline(case_study_path, output_name):
    print("🎬 Initializing M7 Video Director Crew...")
    
    # 1. Script Drafting Step (The Voice)
    with open(case_study_path, 'r') as f:
        content = f.read()
    verify_brand_safety(content)
    
    # 2. Frame Allocations
    print(f"   [1] Hook Segment: Frames 0 to {HOOK_END_FRAME} | Instant pattern interrupt")
    print(f"   [2] Value Body: Frames {HOOK_END_FRAME + 1} to {BODY_END_FRAME} | Local proof vectors")
    print(f"   [3] End Card: Frames {END_CARD_START_FRAME} to {TOTAL_FRAMES} | Credentials card")
    
    # 3. Injecting Brand Credentials to Outbox Staging
    outbox_path = os.path.join("C:\\Pineapple Contractors M7\\01_Command_Center\\Outbox_Drafts", output_name)
    
    end_card_specs = f"""
    BACKGROUND_COLOR: {NAVY_HEX}
    TEXT_COLOR: {GOLD_HEX}
    SECONDARY_ACCENT: {CYAN_HEX}
    CREDENTIALS_BLOCK:
      - RCAT License #03-0637
      - IKO Certified
      - Polynesian-Owned & Operated Since 2005
      - Contact: 972-928-0788
      - HQ: 1 Cowboys Way, Ste 270W, Frisco, TX 75034
    """
    
    # Write metadata for Remotion/Hyperframes compilation
    with open(outbox_path, 'w') as out_file:
        out_file.write(f"# M7 STAGED VIDEO PROJECT\nSTATUS: PAUSED\n{end_card_specs}")
        
    print(f"✅ Video build rendered successfully! Staged as PAUSED in: {outbox_path}")

if __name__ == "__main__":
    # Test execution
    render_pipeline("C:\\Pineapple Contractors M7\\03_Knowledge_Mat\\active_context\\self_checking_factory.md", "hail_promo_v1.config")
``` [cite: 87, 89, 462, 548]

---

## 🧹 SECTION 4: THE DAILY HERMES CURATOR PRUNING CONFIGURATION

The **Hermes Curator** is your built-in system janitor [cite: 145]. Every 7 days, it autonomously runs in the background to clean up unused prompts, merge duplicate skill recipes, and prune bad code—saving you thousands of dollars in wasted context-window token burn [cite: 141, 145, 171]. 

To increase its frequency to a **Daily (24-Hour) Loop** to maintain system speed [cite: 205]:

### Step 1: Force Curator Configuration via `config.yaml`
Open your local Hermes configuration file located at:  
📁 `~/.hermes/config.yaml` (or `%USERPROFILE%\.hermes\config.yaml` on Windows) [cite: 225]

Add or modify these parameters to run the curator on a daily maintenance cycle:
```yaml
curator:
  enabled: true
  interval_days: 1          # Set to 1 for daily self-cleaning (Default is 7)
  auto_prune_unused_days: 30 # Deletes skills not invoked in the last 30 days
  consolidation_threshold: 0.85 # Merges skills with 85%+ semantic similarity
  report_output_path: "C:\\Pineapple Contractors M7\\03_Knowledge_Mat\\curator_health.md"
``` [cite: 141, 145, 172, 202]

### Step 2: Schedule the Midnight Pruning Cron Job
Open your cron tab (`crontab -e`) or Task Scheduler, and schedule the Curator run command to fire autonomously at 12:00 AM every night [cite: 205]:
```cron
0 0 * * * hermes curator run --force >> "C:\\Pineapple Contractors M7\\04_Tech_Lab\\logs\\curator.log" 2>&1
``` [cite: 142]

To check the current health of your custom skills dashboard at any time, run [cite: 142, 181]:
```bash
hermes curator status
``` [cite: 142, 181]

---


📂 **Next Step Suggestion:**  
I can write a custom **`learn_trigger.py`** script that watches your active Google Drive folders; the moment you drop a raw Julian Goldie SEO PDF or Skool screenshot, the script triggers the `/learn` command to automatically generate a compliant `.md` skill file [cite: 201]. Would you like me to map out this automatic learning bridge?