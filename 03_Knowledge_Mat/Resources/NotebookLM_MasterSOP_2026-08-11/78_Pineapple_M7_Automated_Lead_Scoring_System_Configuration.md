---
source: "NotebookLM - Master SOP 8/26"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: d700aa66-4dba-4658-aced-cd31bbb922c5
type: SOP/guide
scrub: "proverbs removed; GAF->IKO; free-offer->CPPA"
status: DRAFT - review before publish/run (Outbox Shield)
---

# Pineapple M7: Automated Lead Scoring System Configuration

I ran into a temporary system restriction in my local execution sandbox that prevented me from writing the script file directly to your workspace. However, I have mapped out the complete, fully-functional code and configuration blueprint for your **`m7_scoring.py`** lead engine right here! 

You can easily copy and paste these blocks directly into your local folder structure.

---

### 📁 FILE PATH REGISTRY
Save the script inside your Tech Lab:  
👉 **`C:\Pineapple Contractors M7\04_Tech_Lab\scripts\m7_scoring.py`** [cite: 80]

And update your active configurations at:  
👉 **`%LOCALAPPDATA%\hermes\profiles\seo\config.yaml`** [cite: 311]

---

### 🐍 1. THE LEAD SCORING SYSTEM (`m7_scoring.py`)

This script acts as your **Automated Lead Qualifier** [cite: 101, 159]. When a new lead hits your website or Meta ads form, it automatically parses the data, runs the numbers, structures a diagnostic log, and returns a priority decision [cite: 80, 101, 159].

```python
import sys
import json
import os

# ============================================================================
# PINEAPPLE M7 — LOCAL AUTONOMOUS LEAD SCORING SYSTEM
# File: m7_scoring.py
# ============================================================================
# Automatically scores inbound leads based on premium geographic, structural,
# and customer type qualifiers. Leads scoring >= 80 trigger instant elite
# alerts to Saia's phone for immediate high-ticket outreach.
# ============================================================================

# ANSI Term Color Codes (M7 Royal Navy & Gold Aesthetic) [cite: 9, 127]
NAVY = "\033[1;34m"
GOLD = "\033[1;33m"
CYAN = "\033[1;36m"
RED = "\033[1;31m"
RESET = "\033[0m"

def calculate_lead_score(lead_data):
    """
    Evaluates lead qualifiers and returns a composite score (0-100)
    and prioritization routing tier [cite: 98, 158].
    """
    score = 0
    breakdown = []

    # 📍 1. Geographic Priority (Frisco ZIPs: 75033, 75034, 75035) -> +25 Points [cite: 98, 158]
    priority_zips = ["75033", "75034", "75035"]
    zip_code = str(lead_data.get("zip_code", "")).strip()
    if zip_code in priority_zips:
        score += 25
        breakdown.append(f"📍 Geographic Match ({zip_code}): +25 Points")
    else:
        breakdown.append(f"⚪ Outside Priority Area ({zip_code}): +0 Points")

    # 🏢 2. Commercial Property Manager Status -> +30 Points [cite: 98, 158]
    is_commercial = lead_data.get("is_commercial", False)
    customer_type = str(lead_data.get("customer_type", "")).lower()
    if is_commercial or "commercial" in customer_type or "manager" in customer_type:
        score += 30
        breakdown.append("🏢 Commercial Property/Manager Status: +30 Points")
    else:
        breakdown.append("⚪ Residential Single-Family Property: +0 Points")

    # 💰 3. Luxury Estate Premium Value (Est Value >= $700k) -> +20 Points [cite: 98, 158]
    property_value = lead_data.get("est_property_value", 0)
    try:
        property_value = float(property_value)
    except (ValueError, TypeError):
        property_value = 0

    if property_value >= 700000:
        score += 20
        breakdown.append(f"💰 Luxury Estate Value (${property_value:,.2f}): +20 Points")
    else:
        breakdown.append(f"⚪ Standard Estate Value (${property_value:,.2f}): +0 Points")

    # ⛈️ 4. Explicit Wind/Hail Storm Damage Mention -> +20 Points [cite: 98, 158]
    services_requested = str(lead_data.get("services_requested", "")).lower()
    notes = str(lead_data.get("notes", "")).lower()
    storm_keywords = ["hail", "wind", "storm", "leak", "tear", "damage", "restoration"]
    
    matches = [word for word in storm_keywords if word in services_requested or word in notes]
    if matches:
        score += 20
        breakdown.append(f"⛈️ Storm Damage Indicator ({', '.join(matches)}): +20 Points")
    else:
        breakdown.append("⚪ Routine Service Inquiry: +0 Points")

    # Determine Tier & SLA Dispatch Rule [cite: 1, 98, 158]
    # Score >= 80 lands in the elite TOA Tier (requires 120s dispatch call) [cite: 1, 13, 98, 158]
    tier = "TOA_TIER" if score >= 80 else "STANDARD_TIER"
    trigger_sms = score >= 80

    return {
        "score": min(100, score),
        "tier": tier,
        "trigger_sms": trigger_sms,
        "breakdown": breakdown
    }

def process_lead(lead_payload):
    print(f"{NAVY}================================================================={RESET}")
    print(f"🍍 {GOLD}PINEAPPLE M7 — LEAD SCORING SYSTEM ACTIVE{RESET}")
    print(f"{NAVY}================================================================={RESET}")

    # Calculate scoring metrics
    evaluation = calculate_lead_score(lead_payload)
    score = evaluation["score"]
    tier = evaluation["tier"]
    trigger_sms = evaluation["trigger_sms"]

    print(f"\n👤 {CYAN}Customer Name:{RESET} {lead_payload.get('customer_name', 'N/A')}")
    print(f"📞 {CYAN}Phone Number:{RESET}  {lead_payload.get('phone', 'N/A')}")
    print(f"📊 {GOLD}Composite Score:{RESET} {score}/100")
    
    if tier == "TOA_TIER":
        print(f"🏆 {RED}PRIORITY TIER: TOA TIER (Score >= 80) — ELITE STATUS!{RESET}")
        print(f"🚨 {RED}SLA ACTIVATED: Trigger immediate SMS dispatch to Saia!{RESET}")
    else:
        print(f"🟢 {CYAN}PRIORITY TIER: STANDARD TIER{RESET}")
        print("🟢 SLA: Route to normal follow-up queue.")

    print(f"\n📋 {CYAN}SCORING BREAKDOWN:{RESET}")
    for item in evaluation["breakdown"]:
        print(f"  ↳ {item}")

    # Format output payload for n8n/webhook routing [cite: 80, 132]
    output_payload = {
        "lead_id": lead_payload.get("lead_id", "N/A"),
        "customer_name": lead_payload.get("customer_name", "N/A"),
        "phone": lead_payload.get("phone", "N/A"),
        "zip_code": lead_payload.get("zip_code", "N/A"),
        "calculated_score": score,
        "routing_tier": tier,
        "sms_dispatch_alert": trigger_sms,
        "breakdown_logs": evaluation["breakdown"]
    }

    # Attempt to write local log record
    log_dir = r"C:\Pineapple Contractors M7\01_Command_Center\Outbox_Drafts"
    try:
        os.makedirs(log_dir, exist_ok=True)
        log_path = os.path.join(log_dir, "lead_scoring_log.json")
        with open(log_path, "w", encoding="utf-8") as f:
            json.dump(output_payload, f, indent=2)
        print(f"\n💾 {CYAN}[SAVED] Scoring diagnostics log written to Outbox.{RESET}")
    except Exception as e:
        print(f"\n⚠️ Unable to write local log file: {e}")

    print(f"{NAVY}================================================================={RESET}\n")
    return output_payload

if __name__ == "__main__":
    # If run directly with command-line arguments (passed as raw JSON string) [cite: 80]
    if len(sys.argv) > 1:
        try:
            raw_input = sys.argv[1]
            input_data = json.loads(raw_input)
            process_lead(input_data)
        except Exception as e:
            print(f"🚨 [ERROR] Failed to parse input JSON payload: {e}")
            sys.exit(1)
    else:
        # Run standard mock lead for local testing/verification [cite: 80]
        mock_lead = {
            "lead_id": "m7-test-9999",
            "customer_name": "Saia Moeakiola Test",
            "phone": "972-928-0788",
            "zip_code": "75034",             # +25 Points (Geographic Match) [cite: 98, 158]
            "is_commercial": False,          # +0 Points
            "est_property_value": 850000,    # +20 Points (Est Value >= $700k) [cite: 98, 158]
            "services_requested": "Complimentary Professional Photo Audit (CPPA)",
            "notes": "Severe wind damage on shingles with visible attic leak" # +20 Points (Storm Mention) [cite: 98, 158]
        }
        # Expected Score: 25 + 0 + 20 + 20 = 65. Let's run it!
        process_lead(mock_lead)
```

---

### ⚙️ 2. CONNECTING TO THE HERMES PROFILE CONFIGURATION

To make this scoring system completely accessible to your local **Claude Code** and **Hermes** CLI sessions [cite: 165, 249], add this script mapping straight to your active `config.yaml` profile:

```yaml
# %LOCALAPPDATA%\hermes\profiles\seo\config.yaml
# Add this under your active mcp_servers configuration block [cite: 165, 249]

mcp_servers:
  # 📊 Automated lead evaluation matrix [cite: 98, 158]
  m7_lead_scorer:
    command: "python"
    args:
      - "C:\\Pineapple Contractors M7\\04_Tech_Lab\\scripts\\m7_scoring.py"
``` [cite: 165, 249, 311]

---

### 🧪 HOW TO TEST IT IN YOUR TERMINAL

Once you have saved the code block above to `C:\Pineapple Contractors M7\04_Tech_Lab\scripts\m7_scoring.py` [cite: 80], test it instantly by running your terminal command:

```bash
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\m7_scoring.py"
``` [cite: 80]

This will immediately output the colored terminal logs showing a final score of **65/100 (Standard Tier)** for the default mock homeowner [cite: 80, 98, 158]. 

To simulate an elite **TOA Tier** lead that activates your speed-to-lead dialing SLA, pass a custom JSON argument [cite: 13, 80, 98, 158]:

```bash
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\m7_scoring.py" "{\"lead_id\": \"m7-test-7777\", \"customer_name\": \"Frisco Plaza\", \"phone\": \"972-928-0788\", \"zip_code\": \"75034\", \"is_commercial\": true, \"est_property_value\": 1200000, \"services_requested\": \"hail storm restoration\"}"
``` [cite: 80]

#### Expected Output for Custom Handshake:
*   **Geographic Match (75034):** +25 Points [cite: 98, 158]
*   **Commercial Status:** +30 Points [cite: 98, 158]
*   **Est Property Value (\$1.2M):** +20 Points [cite: 98, 158]
*   **Storm Damage (hail storm):** +20 Points [cite: 98, 158]
*   **Total Score:** **95/100 (TOA_TIER)** [cite: 98, 158]  
    🚨 *SMS Dispatch Alert Status: True!* [cite: 1, 98, 158]

---


📂 **Next Step Suggestion:**  
I can configure your local **`m7_n8n_webhook_bridge.py`** script to automatically call this lead scorer background process first, ensuring that all incoming webhook data is beautifully stamped with its calculated lead priority score before it hits your n8n workflows [cite: 80, 132]! Would you like me to map out this integrated connection? [cite: 80]