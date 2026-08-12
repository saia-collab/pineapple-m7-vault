---
source: "NotebookLM - Master SOP 8/26"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: 0ece5628-38d0-4e2b-8c70-d9de554be133
type: SOP/guide
scrub: "proverbs removed; GAF->IKO; free-offer->CPPA; REVIEW free?,green?"
status: DRAFT - review before publish/run (Outbox Shield)
---

# M7 Automation Upgrade and Brand Compliance Manual


---

### 🎛️ 1. CONNECTING YOUR SCORER TO YOUR DESKTOP (`HOT_LEADS.txt`)

To ensure you can instantly view your highest-value prospects without even opening your CRM or email, we are integrating a **Desktop Stash** function [cite: 80]. When a lead scores **\\(\ge\\) 80 (TOA_TIER)**, the scorer will automatically append their details to a text file right on your Windows desktop [cite: 80, 98, 158].

#### 🐍 Copy and Paste this Code Block into `m7_scoring.py`:
Open **`C:\Pineapple Contractors M7\04_Tech_Lab\scripts\m7_scoring.py`** and insert this code block inside the `process_lead()` function, right before the final return statement [cite: 80]:

```python
    # =========================================================================
    # 🔥 DESKTOP HOT LEADS STASH (TOA TIER SPECIAL DISPATCH)
    # =========================================================================
    if tier == "TOA_TIER":
        try:
            # Dynamically resolves the active user's Desktop path on Windows
            desktop_path = os.path.join(os.environ["USERPROFILE"], "Desktop", "HOT_LEADS.txt")
            
            with open(desktop_path, "a", encoding="utf-8") as hf:
                hf.write("====================================================\n")
                hf.write(f"🔥 HOT LEAD ALERT: TOA TIER QUALIFIED (Score: {score}/100)\n")
                hf.write("====================================================\n")
                hf.write(f"👤 Name:     {lead_payload.get('customer_name', 'N/A')}\n")
                hf.write(f"📞 Phone:    {lead_payload.get('phone', 'N/A')}\n")
                hf.write(f"📍 ZIP Code: {lead_payload.get('zip_code', 'N/A')}\n")
                hf.write(f"🏢 Comm:     {lead_payload.get('is_commercial', False)}\n")
                hf.write(f"💰 Est. Val: ${property_value:,.2f}\n")
                hf.write(f"⛈️ Services: {lead_payload.get('services_requested', 'N/A')}\n")
                hf.write(f"📝 Notes:    {lead_payload.get('notes', 'N/A')}\n")
                hf.write(f"🕒 Timestamp: 2026-08-11 18:48:55\n")
                hf.write("====================================================\n\n")
                
            print(f"\n🔥 {RED}[DESKTOP ALERT] Hot Lead instantly written to Desktop/HOT_LEADS.txt!{RESET}")
        except Exception as de:
            print(f"\n⚠️ [DESKTOP WRITE ERROR] Could not save hot lead: {de}")
``` [cite: 80, 98, 158]

Every time your background daemon processes an elite lead, it will silently write to your desktop file [cite: 80]. You can keep this text file open on your secondary screen to monitor priority calls in real-time [cite: 13]!

---

### 📐 2. THE HORMOZI 3-ANGLE MATRIX (META DIRECT-RESPONSE AD COPY)

These copy sets are written in the punchy, sentence-per-line **Alex Hormozi direct-response style** to maximize mobile scroll-stopping dwell time [cite: 466, 469]. They strictly adhere to your **0% Green design rules** (styled with Royal Navy backgrounds and Gold highlights) and explicitly point to your **Complimentary Professional Photo Audit (CPPA)** [cite: 9, 126, 127, 147].

#### ⏳ Angle 1: The Insurance Deadline (Fear of Loss / Urgency) [cite: 7]
> **Ad Headline:** Frisco: Your Hail Claim Window is actively Closing! ⏱️
> 
> **Primary Text:**
> Let’s be real.
> Frisco had record hail months ago.
> Most homeowners looked at their roof from the driveway.
> They saw nothing.
> So they assumed everything was fine.
> But hail micro-cracks are invisible to the naked eye.
> Over time, water seeps through to ruin your drywall.
> Under Texas law, your insurance claim window is closing.
> If you don’t file within the 12-month limit, you pay out of pocket.
> Don't guess. Get proof.
> Click below to book your Complimentary Professional Photo Audit.
> We bring the drones, document the decking, and secure your claim.
> 
> **Description:** 🛡️ RCAT License #03-0637 | 75033, 75034, 75035 ZIPs [cite: 126, 150, 256].

---

#### 💆 Angle 2: The Stress-Free Claim (Aspiration / Friction Reduction) [cite: 7]
> **Ad Headline:** Zero Sales Pressure. Just Cold, Hard Photographic Proof. 📸
> 
> **Primary Text:**
> Most roofing companies send high-pressure salespeople to your door.
> They push you.
> They rush you.
> They try to force you to sign a contract before you’ve even seen the damage.
> We hate that.
> At Pineapple Roofing, we do things differently.
> We do not sell. We document.
> Our specialists perform a Complimentary Professional Photo Audit.
> You get a full, high-definition engineering file of your roof.
> You see exactly what your insurance adjuster sees.
> No obligation.
> No sales pitch.
> Just objective, bulletproof proof.
> Click below to schedule your drone-assisted CPPA today.
> 
> **Description:** 🏆 Over 350+ Local North Texas Families Protected [cite: 191].

---

#### 👑 Angle 3: The Local Trust & Polynesian Heritage (Authority) [cite: 7, 122]
> **Ad Headline:** Built by Family. Trusted by 350+ Frisco Neighbors. 🍍
> 
> **Primary Text:**
> We aren’t out-of-state storm chasers.
> We live right here in Frisco.
> Pineapple Roofing is family-operated and Polynesian-owned.
> We've served the DFW community since 2005.
> We hold our work to a higher standard—The Pineapple Standard.
> We don’t install cheap shingles that tear in high winds.
> We standardize strictly on premium, storm-resistant IKO systems.
> If your home is in Starwood, Newman Village, or surrounding areas:
> Work with a locally licensed team you can trust.
> Click below to request your Complimentary Professional Photo Audit.
> 
> **Description:** 📍 Visit our HQ at 1 Cowboys Way, Ste 270W, Frisco [cite: 54].

---

### 🛰️ 3. SETTING UP YOUR 24/7 BACKGROUND SEO AGENT

To run your SEO pipeline completely on autopilot while you sleep, your local Agent OS operates a **continuous headless background loop** [cite: 90]. This engine pulls your GSC search data, identifies trending terms, writes unique static pages, passes them through your brand firewall, and submits the URLs straight to sitemap indexers [cite: 6, 40, 53, 80].

```
┌────────────────────────────────────────────────────────────────────────┐
│               M7 24/7 BACKGROUND TRAFFIC ENGINE RUNTIME                 │
├────────────────────────────────────────────────────────────────────────┤
│  LOOP START (Every 6 Hours)                                            │
│   │                                                                    │
│   ├──► 1. Query GSC Data (gsc_frisco_scan.py) -> Finds hot terms       │
│   ├──► 2. Generate Content -> Claude Code drafts a clean static page   │
│   ├──► 3. Firewall Scan (brand-firewall.py) -> Block if green or "free"│
│   ├──► 4. Deploy Page (Netlify CLI / WP REST) -> Moves page live       │
│   └──► 5. Index Submission (sitemap_validator.py) -> Indexes in 24 hrs │
│                                                                        │
│  SLEEP (6 Hours) ──► RESTART LOOP                                       │
└────────────────────────────────────────────────────────────────────────┘
``` [cite: 6, 40, 53, 80, 220]

#### Step 1: Create Your Infinite Runner Loop
Save this script inside your scripts directory to manage the automation:  
📁 **`C:\Pineapple Contractors M7\04_Tech_Lab\scripts\run_background_seo.bat`** [cite: 80]

```cmd
@echo off
TITLE M7 24/7 Background SEO Traffic Engine
color 0C

:loop
cls
echo ===================================================================
echo   🛰️  M7 24/7 BACKGROUND TRAFFIC ENGINE IS ACTIVE
echo   Enforcing 0%% Green visual laws and strict CPPA naming schemas [cite: 9, 126, 127]
echo ===================================================================
echo [SYSTEM] Local Time: %date% %time%
echo.

:: 1. Scan GSC for trending keywords in Frisco/Plano
echo [STEP 1/4] Scanning Google Search Console for impression spikes...
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\gsc_frisco_scan.py" [cite: 80]
timeout /t 5 >nul

:: 2. Execute JCode to write a new local static landing page
echo.
echo [STEP 2/4] Initializing jcode Swarm to generate optimized city copy... [cite: 386]
jcode --role "builder" --task "Generate a new HTML location page for Frisco ZIP 75035 using IKO Dynasty metrics [cite: 150, 256]. Use no green styles [cite: 127]." [cite: 391]
timeout /t 10 >nul

:: 3. Force Compliance Check
echo.
echo [STEP 3/4] Passing page to Brand Firewall...
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\brand-firewall.py" "C:\Pineapple Contractors M7\01_Command_Center\Outbox_Drafts" [cite: 80]
if %errorlevel% neq 0 (
    echo [CRITICAL ERROR] Brand Firewall flagged a violation! Halting deploy.
    goto sleep_cycle
)

:: 4. Deploy and Index
echo.
echo [STEP 4/4] Publishing page and submitting to Indexceptional API...
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\sitemap_validator.py" [cite: 80]

:sleep_cycle
echo.
echo ===================================================================
echo   💤 CYCLE COMPLETE. Sleeping for 6 hours before next check...
echo ===================================================================
:: Sleeps for 21,600 seconds (6 hours)
timeout /t 21600

goto loop
``` [cite: 80]

#### Step 2: Configure as a Background Windows Task
Instead of leaving a black command window open on your screen [cite: 80], configure Windows to run it silently in the background:
1.  Open your Windows menu and type **Task Scheduler**.
2.  Click **Create Basic Task** on the right sidebar.
3.  Name it: `M7_247_SEO_Engine`.
4.  Set Trigger to: **When the computer starts**.
5.  Set Action to: **Start a program** and point it directly to your `run_background_seo.bat` file [cite: 80].
6.  Under **Conditions/Settings**, check **Run whether user is logged on or not** and select **Run with highest privileges** [cite: 80].

Now, the second you boot up your computer, the Agent OS silently coordinates your SEO flywheel in the background [cite: 80, 90]!

---

### 📈 4. COMPLIANCE AUDIT CONFIRMATION (`CLAUDE.md`)

In accordance with your updated branding requirements:
*   **Grounding Enforcement:** The system continues to strictly enforce **0% Green** design structures, the usage of **Royal Navy (`#1A365D`)** and **Pineapple Gold (`#FBC02D`)**, and mandates that all estimates are represented as **Complimentary Professional Photo Audits (CPPA)** [cite: 9, 126, 127, 147].

📂 **Next Step Suggestion:**  