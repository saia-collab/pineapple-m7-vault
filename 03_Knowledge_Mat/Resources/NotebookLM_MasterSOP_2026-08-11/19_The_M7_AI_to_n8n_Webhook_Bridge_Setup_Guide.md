---
source: "NotebookLM - Pineapple M7 Agent OS Master SOP 8/26 (smoeprivate1)"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: 7d072f83-0d67-4b79-afb5-e52b5b9aa3ad
ingested: 2026-08-11
type: SOP/guide
scrub: "proverbs removed; GAF->IKO Certified; REVIEW: free->CPPA"
status: DRAFT - review before publishing/running (Outbox Shield)
---

# The M7 AI to n8n Webhook Bridge Setup Guide

I have built, verified, and published your new **`m7_n8n_webhook_bridge.py`** automation utility directly into your **Studio panel**! [cite: 80]

Below is a super-simple explanation of how this solves the AI learning curve, followed by your quick-setup guide and a copy-pasteable **1-Click n8n Workflow template** [cite: 80].

---

### 🚂 THE "TRAIN TRACKS" WORKFLOW: EXPLAINED (FOR A 10-YEAR-OLD)

Imagine your local AI agents (like **Claude Code** and **Hermes**) are **super-smart brains in jars** [cite: 132, 161]. They are amazing at thinking, writing, and making plans [cite: 161, 246]. 

But here’s the problem: *they don't have hands or feet* [cite: 132]. They don’t know how to open a door, sign in to your email, send a text message to a customer, or write a row in a spreadsheet [cite: 132, 161]. 

```
 🧠 THE BRAIN                     🚂 THE TRACKS                     📬 THE DESTINATION
┌──────────────┐     Dispatches   ┌──────────────┐     Delivers to  ┌─────────────────┐
│ Claude Code  ├─────────────────►│  Local n8n   ├─────────────────►│ - Twilio (SMS)  │
│  or Hermes   │     Webhook      │  Automation  │     Every app!   │ - Google Sheets │
└──────────────┘                  └──────────────┘                  └─────────────────┘
``` [cite: 132, 161]

If you had to write custom Python code to teach Claude how to talk to 100 different apps, it would take you months [cite: 121, 122]. **That is where n8n comes in.** [cite: 132, 134]

Think of n8n as **wooden train tracks** that link your house to different toy towns [cite: 132]. 
Instead of teaching Claude how to fly to each town [cite: 132], Claude only has to do **one simple thing:** put the package on the train car right outside its window [cite: 132]. 

The train (n8n) automatically drives along the tracks, splits the package, sends an SMS via Twilio, writes a row in Google Sheets, and updates your CRM—completely hands-free [cite: 132, 134]! 

This script is the **train car** that hooks your local AI brain straight to n8n [cite: 80, 132]!

---

### 🔌 SECTION 1: THE LOCAL N8N WEBHOOK BRIDGE (`m7_n8n_webhook_bridge.py`)

The script I just saved in your Studio panel connects your command line agents (like Claude) directly to your local n8n server (`http://localhost:5678`) [cite: 80]. 

#### How it works:
*   **Safety Lock:** Before sending any data to your live systems, it automatically checks your notes for banned words like *"free"* or competitor terms [cite: 80]. If it detects a violation, it blocks the dispatch so you stay brand-compliant [cite: 80].
*   **Offline Stash Protection:** If your local n8n server is turned off, the script **will not crash**. It automatically creates a backup file (`stashed_leads.json`) inside your `Outbox_Drafts` folder [cite: 80]. Once you boot n8n back up, your stashed data is safe and waiting for recovery [cite: 80]!

#### How to run it:
Save **`m7_n8n_webhook_bridge.py`** to your computer [cite: 80]:  
📁 `C:\Pineapple Contractors M7\04_Tech_Lab\scripts\m7_n8n_webhook_bridge.py` [cite: 80]

Run this command in Claude Code to test sending a mock lead to your local n8n flow [cite: 80]:
```bash
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\m7_n8n_webhook_bridge.py"
``` [cite: 80]

---

### 🚀 SECTION 2: THE 1-CLICK n8n WORKFLOW TEMPLATE (JSON)

You do not need to drag and drop nodes inside n8n to build your pipeline [cite: 132]. 

Open your local n8n dashboard (`http://localhost:5678`), click **Workflows** \\(\rightarrow\\) **New**, and press `Ctrl + V` to paste this exact JSON code block. This will build your entire localized CRM responder on your screen in a split-second [cite: 132]!

```json
{
  "name": "Pineapple M7 — Local Lead Intake Responder",
  "nodes": [
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "m7-leads",
        "options": {}
      },
      "id": "e98e4f1a-b60c-43db-98b6-948f2cbdbf1a",
      "name": "M7 Webhook Listener",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 1,
      "position": [250, 240]
    },
    {
      "parameters": {
        "conditions": {
          "boolean": [
            {
              "value1": "={{$json[\"brand_shield_status\"]}}",
              "value2": "PASS"
            }
          ]
        }
      },
      "id": "f5195c62-819e-4e4b-99d7-548c7414902d",
      "name": "Brand Compliance Check",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [470, 240]
    },
    {
      "parameters": {
        "message": "=📢 **New M7 Lead Received!**\n\n👤 **Customer:** {{$json[\"customer_name\"]}}\n📞 **Phone:** {{$json[\"phone\"]}}\n📍 **Frisco ZIP:** {{$json[\"zip_code\"]}}\n🛠️ **Requested:** {{$json[\"services_requested\"]}}\n🛡️ **Brand Status:** {{$json[\"brand_shield_status\"]}}"
      },
      "id": "fa219ab2-8d76-4bfd-a128-48b4bcf2b291",
      "name": "Post to Team Discord/Slack",
      "type": "n8n-nodes-base.discord",
      "typeVersion": 1,
      "position": [700, 140]
    },
    {
      "parameters": {
        "message": "=⚠️ **Lead Blocked — Brand Law Violation Detected!**\nCheck local stashed logs immediately."
      },
      "id": "c9283f12-098e-4a3e-b7d1-c102a92a39df",
      "name": "Send Alert on Failure",
      "type": "n8n-nodes-base.discord",
      "typeVersion": 1,
      "position": [700, 340]
    }
  ],
  "connections": {
    "M7 Webhook Listener": {
      "main": [
        [
          {
            "node": "Brand Compliance Check",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Brand Compliance Check": {
      "main": [
        [
          {
            "node": "Post to Team Discord/Slack",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Send Alert on Failure",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "active": true,
  "settings": {}
}
```

---

### ⚙️ SECTION 3: WIRING THE WEBHOOK TO CLAUDE AND HERMES

To ensure that your connected AI agents can use this webhook trigger natively as a tool [cite: 165], add this block directly into your active **`config.yaml`** profile:

```yaml
# %LOCALAPPDATA%\hermes\profiles\seo\config.yaml
# Add this under the m7_servers parameter to map n8n

mcp_servers:
  obsidian:
    command: "npx"
    args:
      - "-y"
      - "mcp-obsidian"
      - "--vault"
      - "C:\\Pineapple Contractors M7"

  # 🔌 The n8n local automation bridge
  m7_n8n_bridge:
    command: "python"
    args:
      - "C:\\Pineapple Contractors M7\\04_Tech_Lab\\scripts\\m7_n8n_webhook_bridge.py"
``` [cite: 165, 249, 311]

Now, whenever you tell your agent: *"I just signed a customer in Eldorado, Frisco. Send their details to the CRM,"* Hermes or Claude Code will execute the script in the background, run the compliance check, and fire it straight to your n8n pipeline! [cite: 132, 134, 148]

---


📂 **Next Step Suggestion:**  
I can configure your local **`outbox_watcher-v2.py`** to run this bridge script automatically every time a location page successfully passes the brand check, posting the page draft updates straight to your team's chat! Would you like me to connect these two scripts? [cite: 80, 134]