---
source: "NotebookLM - Pineapple M7 Agent OS Master SOP 8/26 (smoeprivate1)"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: a6a6688c-5f2c-4d32-8bcd-3355b7076aef
ingested: 2026-08-11
type: SOP/guide
scrub: "proverbs removed; GAF->IKO Certified"
status: DRAFT - review before publishing/running (Outbox Shield)
---

# Bridging Python Scripts to n8n Webhook Listeners

To get your local **n8n workflow** to perfectly "hear" and capture the payloads sent by your new **`m7_n8n_webhook_bridge.py`** script, you need to understand one key concept that trips up almost everyone starting with n8n [cite: 132]: **The difference between the Test URL and the Production URL.** [cite: 132]

Here is the step-by-step setup guide to wire up the connection, clear the learning curve, and run a successful live test! [cite: 132]

---

### 📡 STEP 1: CONFIGURING THE WEBHOOK NODE IN n8n

If you pasted the JSON template from the previous step, your webhook node is already created! Double-click on the **M7 Webhook Listener** node to open its settings, and verify these parameters [cite: 132]:

1.  **HTTP Method:** Must be set to `POST` (since the Python bridge script is "pushing" data to n8n) [cite: 80].
2.  **Path:** Set this to `m7-leads` [cite: 80].
3.  **Response Mode:** Set this to `When Last Node Finishes` (or keep it as default `onReceived` for instant return) [cite: 80].

---

### ⚠️ STEP 2: UNDERSTANDING THE TEST VS. PRODUCTION URL (The Learning Curve)

When you look at the top of your Webhook node settings in n8n, you will see a toggle for **Test URL** and **Production URL** [cite: 132]. 

```
  When Editing:
  👉 http://localhost:5678/webhook-test/m7-leads  ◄── (Only listens when you click "Listen")
  
  When Active (Live):
  👉 http://localhost:5678/webhook/m7-leads       ◄── (Always listens in the background)
``` [cite: 80, 132]

*   **The Test URL (`/webhook-test/`):** This URL only wakes up when you manually click the **"Listen for test event"** button inside n8n [cite: 132]. If you send data here while n8n isn't actively listening, it will return a `404 Not Found` error [cite: 132].
*   **The Production URL (`/webhook/`):** This is the permanent, always-on URL [cite: 132]. It only works when you flip the workflow switch at the top right of your screen to **Active** [cite: 132]. 

---

### 🚀 STEP 3: RUNNING Your First Connection Test

Let’s run a live test to watch the data flow from your terminal, through your bridge script, and straight into your n8n canvas [cite: 80, 132]!

#### 1. Put n8n into Listening Mode
Inside your n8n editor, double-click your Webhook node, select the **Test URL** tab, and click the big orange button:  
👉 **"Listen for test event"** [cite: 132]  
*(The screen will blur and say "Waiting for Webhook call...")* [cite: 132]

#### 2. Fire the Test Script Natively
Because our Python bridge script is pre-programmed to look for a local n8n instance on `http://localhost:5678` [cite: 80], it will automatically try to hit the **Test URL** if it detects you are in active setup mode [cite: 80].

Open your terminal and execute the bridge script [cite: 80]:
```bash
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\m7_n8n_webhook_bridge.py"
``` [cite: 80]

#### 3. Watch the Magic Happen
*   In your terminal, you will instantly see:  
    `✅ [SUCCESS] Dispatch completed! Response Code: 200` [cite: 80]
*   In your n8n browser tab, the waiting screen will vanish, and you will see your mock customer payload (Saia Test Lead, 972-928-0788, CPPA requested) appear on your screen as structured JSON [cite: 80]!

---

### 🔓 STEP 4: GOING LIVE (Background Automation)

Once you see your test data flow through the nodes successfully [cite: 132]:

1.  Click **Save** in n8n [cite: 132].
2.  Flip the toggle in the top-right corner from **Inactive** to **Active** [cite: 132].
3.  Your local n8n server is now permanently listening on `http://localhost:5678/webhook/m7-leads` [cite: 80]. 
4.  Your **`outbox_watcher-v3.py`** script will now safely dispatch real-time lead and brand compliance updates to this live production webhook every single time you edit or save a draft page! [cite: 80]

---


📂 **Next Step Suggestion:**  
Now that n8n is wired up to hear the bridge, I can generate a **Local Leads Dashboard Google Sheet Template structure** so that your n8n workflow can automatically write every verified customer lead into a clean spreadsheet. Would you like me to map out this sheet columns integration? [cite: 132]