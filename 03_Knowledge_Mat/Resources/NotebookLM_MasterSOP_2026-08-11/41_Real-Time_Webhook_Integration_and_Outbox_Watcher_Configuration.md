---
source: "NotebookLM - Pineapple M7 Agent OS Master SOP 8/26 (smoeprivate1)"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: f0c82bac-7095-428b-8ca5-6433477afe34
ingested: 2026-08-11
type: SOP/guide
scrub: "proverbs removed; GAF->IKO Certified; REVIEW: free->CPPA, green->navy/gold"
status: DRAFT - review before publishing/running (Outbox Shield)
---

# Real-Time Webhook Integration and Outbox Watcher Configuration

I have built, verified, and published two vital assets to your Studio panel to add webhook alerts to your staging area:

1.  **`outbox_watcher-v2.py`** — The upgraded real-time watcher daemon that automatically connects to your chat channels.
2.  **`notifications.json`** — The simple configuration file to link your secure Discord, Slack, and Telegram webhooks.

---

### 📡 HOW THE REAL-TIME WEBHOOK INTEGRATION WORKS

The updated **`outbox_watcher-v2.py`** script acts as an active compliance gatekeeper. Every time you or your autonomous agents save a file into your `Outbox_Drafts` folder:

1.  **Trigger:** The script automatically detects the file modification and runs the `brand_firewall.py` check.
2.  **Evaluation:** It captures the firewall's output logs and checks if the file received a clean **PASS** or a **FAIL** (meaning a banned word like *"free"* or a green visual hex code leaked into your layout).
3.  **Dispatch:** It queries your `notifications.json` file. If Webhook links are active, it formats a rich Markdown payload and fires a live message directly to your team's Discord, Slack, or Telegram channel within seconds.

---

### ⚙️ STEP-BY-STEP WEBHOOK CONFIGURATION

To activate these alerts, you only need to configure the newly published JSON file on your machine:

#### Step A: Place the Configuration File
Save the **`notifications.json`** file from your Studio panel onto your computer at this exact location:  
📁 `C:\Pineapple Contractors M7\04_Tech_Lab\config\notifications.json`

#### Step B: Paste Your Chat Webhooks
Open the file in any text editor and replace the placeholder fields with your team's active channels:

```json
{
  "discord_webhook_url": "https://discord.com/api/webhooks/PASTE_YOUR_DISCORD_WEBHOOK_HERE",
  "slack_webhook_url": "https://hooks.slack.com/services/PASTE_YOUR_SLACK_WEBHOOK_HERE",
  "telegram_bot_token": "PASTE_YOUR_TELEGRAM_BOT_TOKEN_HERE",
  "telegram_chat_id": "PASTE_YOUR_TELEGRAM_CHAT_ID_HERE",
  "notify_on_pass": true,
  "notify_on_fail": true
}
```

*   *Want to silence successful draft passes and only receive alerts on failures?* Simply toggle `"notify_on_pass": false`.

---

### 🚀 RUNNING THE UPGRADED DAEMON

Open your local terminal window and run the upgraded daemon file:

```bash
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\outbox_watcher-v2.py"
```

Keep this window active in the background. Now, every time an article is optimized, an Elementor layout is built, or a campaign is staged, your team will receive real-time brand reports natively in your chat room!

---


📊 **Next Step Suggestion:**  
I can write a custom Windows startup file (**`LAUNCH_WATCHER.bat`**) to automatically boot your new `outbox_watcher-v2.py` script in the background every morning when you launch your local Agent OS dashboard. Would you like me to map out this automatic startup batch file?