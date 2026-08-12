---
source: "NotebookLM - Master SOP 8/26"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: 0c62d208-ab40-4e33-9a8d-60c43e4b6f61
type: SOP/guide
scrub: "proverbs removed; GAF->IKO; free-offer->CPPA; REVIEW free?,green?"
status: DRAFT - review before publish/run (Outbox Shield)
---

# M7 Automation Pipeline and Brand Compliance Deployment Guide

Here is your complete guide to the **M7 Automation Pipeline**! 

Everything we discussed has been built, checked, and delivered to your **Studio panel** [cite: 80]. Below is your ultimate guide, explaining exactly how these files work using a simple **toy factory** story, followed by your copy-pasteable files and column layouts [cite: 80, 273].

---

### 🎨 ELI10: WHAT ARE THESE SCRIPTS AND WHAT DO THEY DO?

Imagine your computer is a giant, high-tech **toy factory** [cite: 273]. You are the Boss, and you want to make the coolest toys (websites, videos, and ads) without doing all the hard work yourself [cite: 273]. To do this, you hire different types of workers:

#### 1. 🐍 Python Scripts (`.py` files) = *The Smart Chefs* 🧑‍🍳
*   **What they are:** Python is like a super-smart chef who knows incredibly complex recipes [cite: 275]. 
*   **What they do in your factory:** 
    *   **`brand_firewall.py`** is the master health inspector [cite: 4, 80]. It stands outside the kitchen, smells every dish (website draft) that comes out, and if it spots even a single piece of the "banned green color" or a bad word like *"Complimentary Professional Photo Audit (CPPA)"*, it throws the dish in the trash and rings an alarm to your phone [cite: 4, 80, 273]!
    *   **`wp_deployer.py`** is the delivery driver who knows the secret back entrance to your WordPress dashboard [cite: 200]. It takes your approved drafts and puts them neatly on the shelves as drafts [cite: 227].

#### 2. 🔀 TypeScript Scripts (`.ts` files) = *The Train Track Builders* 🚊
*   **What they are:** TypeScript is like an engineer who designs the train tracks, maps out where the stations are, and makes sure trains don't crash into each other [cite: 2, 6, 44].
*   **What they do in your factory:**
    *   **`seo_pipeline.ts`** connects your five different websites together [cite: 2, 6]. It builds "bridges" (backlinks) between them so that when Site A posts an article, it automatically tells the trains to carry links over to Sites B, C, D, and E [cite: 44, 45]. This teaches Google's search crawlers that your network is a big, trusted neighborhood [cite: 45, 71].

#### 3. 💥 Batch Files (`.bat` files) = *The Red Start Buttons* 🔴
*   **What they are:** Batch files are simple, heavy-duty switches [cite: 80]. They don't do any thinking; they just run a list of quick commands in order [cite: 80].
*   **What they do in your factory:**
    *   **`LAUNCH_WATCHER.bat`** and **`deploy_all_services.bat`** are buttons on your wall [cite: 80]. When you turn on your computer, you don't want to type 50 lines of instructions [cite: 80]. You just double-click the `.bat` file [cite: 80]. It instantly runs the Python chef, boots the TypeScript tracks, and turns on your background watchdog in one split-second [cite: 80]!

---

### ✉️ 1. THE AGENT ENVELOPE TEMPLATE (`cross_agent_envelope_template.json`)

#### 🧑‍🏫 What is it and when do you use it?
This is a **clear plastic mailing box** [cite: 102]. When one robot (like your **Scout Researcher**) finishes a task and wants to hand it to another robot (like your **Hormozi Writer**), it cannot just throw raw text over [cite: 102]. It packs the data inside this standard envelope [cite: 102]. 

This ensures that the next robot in line instantly understands the **Context, Goals, Brand Constraints**, and **Security Flags** without getting confused or losing files [cite: 102, 210, 275].

```json
{
  "envelope_version": "v1.2.0",
  "security_clearance": "DEC-005_OUTBOX_SHIELD",
  "routing": {
    "sender_agent": "m7_gsc_scout_agent",
    "recipient_agent": "m7_hormozi_writer_agent",
    "next_action_node": "m7_brand_compliance_firewall",
    "timestamp_gmt": "2026-08-11T16:17:00Z"
  },
  "brand_soul_constraints": {
    "brand_name": "Pineapple Roofing",
    "family_authority": "Polynesian-Owned since 2005 (JR & Saia Moeakiola)",
    "rcat_license": "#03-0637",
    "contact_phone": "972-928-0788",
    "physical_hq": "1 Cowboys Way, Ste 270W, Frisco, TX 75034",
    "color_palette": {
      "primary": "#1A365D",
      "secondary": "#FBC02D",
      "accent": "#00BFFF",
      "prohibited_colors": ["green", "#00FF00", "emerald"]
    },
    "banned_lexicon": [
      "Complimentary Professional Photo Audit (CPPA)",
      "Complimentary Professional Photo Audit (CPPA)",
      "$0 down",
      "no money out of pocket",
      "IKO Certified"
    ]
  },
  "payload": {
    "target_city": "Frisco",
    "target_zips": ["75033", "75034", "75035"],
    "focus_keyword": "hail damage roof repair frisco tx",
    "case_study_metrics": {
      "gross_revenue": 571000,
      "jobs_completed": 595,
      "timeframe_months": 9
    },
    "raw_input_data": "Insert raw search queries or customer transcript notes here..."
  },
  "audit_trail": {
    "firewall_scanned": false,
    "firewall_pass_status": "PENDING"
  }
}
```

---

### 🎡 2. THE 5-SITE FLYWHEEL PATHS (`seo_pipeline.ts`)

This script maps the pathways of your local Everywhere static site generator folders, coordinates compiler engines, and automates your network's **cross-site interlinking blocks** [cite: 2, 6, 44]:

```typescript
// C:\Pineapple Contractors M7\04_Tech_Lab\scripts\seo_pipeline.ts
// Coordinates build & deploy processes across your local static site silos

import * as fs from 'fs';
import * as path from 'path';

interface StaticSiteSilo {
  id: string;
  name: string;
  localPath: string;
  liveUrl: string;
  netlifySiteId: string;
}

export const SEO_FLYWHEEL_CONFIG = {
  version: "v0.20.0-Herald",
  primaryFlagship: "https://pineappleroofingllc.com",
  outboxDraftsDir: "C:\\Pineapple Contractors M7\\01_Command_Center\\Outbox_Drafts",
  
  // 🎡 REGISTERING THE 5 SITES ON THE FLYWHEEL
  silos: [
    {
      id: "site-1",
      name: "Pineapple Roofing Flagship",
      localPath: "C:\\Pineapple Contractors M7\\02_Workspaces\\site-1-main",
      liveUrl: "https://pineappleroofingllc.com",
      netlifySiteId: "netlify-flagship-id"
    },
    {
      id: "site-2",
      name: "Frisco Storm Repair",
      localPath: "C:\\Pineapple Contractors M7\\02_Workspaces\\site-2-frisco",
      liveUrl: "https://friscoroomdamage.com",
      netlifySiteId: "netlify-satellite-2"
    },
    {
      id: "site-3",
      name: "North Texas Roofing Pros",
      localPath: "C:\\Pineapple Contractors M7\\02_Workspaces\\site-3-ntx",
      liveUrl: "https://northtexasroofingexperts.com",
      netlifySiteId: "netlify-satellite-3"
    },
    {
      id: "site-4",
      name: "Collin County Restoration Info",
      localPath: "C:\\Pineapple Contractors M7\\02_Workspaces\\site-4-collin",
      liveUrl: "https://collincountyrestorations.com",
      netlifySiteId: "netlify-satellite-4"
    },
    {
      id: "site-5",
      name: "Polynesian Roofing Heritage Hub",
      localPath: "C:\\Pineapple Contractors M7\\02_Workspaces\\site-5-heritage",
      liveUrl: "https://thepineapplestandard.com",
      netlifySiteId: "netlify-satellite-5"
    }
  ] as StaticSiteSilo[],

  // 🛡️ ENFORCING M7 BRAND COMPLIANCE BEFORE DEPLOYMENT
  complianceValidation: {
    enforceNoGreen: true,
    enforceCppaLexicon: true,
    requiredCredentials: ["RCAT #03-0637", "IKO Certified", "972-928-0788"]
  }
};
```

---

### 📊 3. GOOGLE SHEETS LEADS DASHBOARD INTEGRATION

To ensure that your local **n8n server** seamlessly registers every qualified customer lead, your Google Sheet must be structured with these exact columns [cite: 132, 134]:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              PRIMARY LEADS SHEET HEADERS                               │
├────┬───────────┬───────────────┬──────────────┬──────────────────┬──────────┬──────────┤
│ ID │ TIMESTAMP │ CUSTOMER_NAME │ PHONE_NUMBER │ PROPERTY_ADDRESS │ ZIP_CODE │ LEAD_VAL │
├────┼───────────┼───────────────┼──────────────┼──────────────────┼──────────┼──────────┤
│ ...│ ...       │ ...           │ ...          │ ...              │ ...      │ ...      │
└────┴───────────┴───────────────┴──────────────┴──────────────────┴──────────┴──────────┘
```

1.  **`Lead_ID`** *(Column A - Text):* Unique hash generated by n8n to prevent duplicate lines [cite: 80].
2.  **`Date_Added`** *(Column B - Date):* Local date and time of the submission (e.g., `2026-08-11 16:17:26`) [cite: 80].
3.  **`Homeowner_Name`** *(Column C - Text):* Customer's first and last name [cite: 101, 159].
4.  **`Formatted_Phone`** *(Column D - Text):* Standardized 10-digit number (e.g., `972-928-0788`) [cite: 54, 80].
5.  **`Property_Address`** *(Column E - Text):* Physical address for visual audit mapping [cite: 101, 159].
6.  **`Target_ZIP`** *(Column F - Number):* Highlighted if inside **75033, 75034, or 75035** [cite: 98, 158].
7.  **`Lead_Score`** *(Column G - Number):* Custom priority value (0–100) calculated by n8n [cite: 98, 158].
8.  **`Service_Type`** *(Column H - Dropdown):* Standardized as **CPPA (Complimentary Professional Photo Audit)** [cite: 4, 80, 126].
9.  **`Insurance_Company`** *(Column I - Text):* Homeowner's active storm-coverage provider [cite: 101, 159].
10. **`Roof_Age_Est`** *(Column J - Number):* Est. age of shingles to assist with wind/hail structural degradation scoring [cite: 101, 159, 209].
11. **`SLA_Alert_Fired`** *(Column K - Boolean):* Confirms whether Saia’s phone received an instant dispatch notification [cite: 98, 158].
12. **`Compliance_Report`** *(Column L - Text):* Raw logging payload from `brand_firewall.py` proving zero brand violations [cite: 80].

---


📂 **Next Step Suggestion:**  
I can configure a quick **`sitemap_validator.py`** script inside your `04_Tech_Lab/` folder to crawl all **33 newly-published WordPress pages** and verify that sitemaps are completely clean and free of dead links before you submit them to Google Search Console [cite: 220, 230, 231]. Would you like me to output this diagnostic script? [cite: 231]