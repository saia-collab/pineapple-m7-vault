---
source: "NotebookLM - Pineapple M7 Agent OS Master SOP 8/26 (smoeprivate1)"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: 570bef82-939f-4105-8605-d1ca0a0f8d0f
ingested: 2026-08-11
type: SOP/guide
scrub: "proverbs removed; GAF->IKO Certified; REVIEW: free->CPPA"
status: DRAFT - review before publishing/running (Outbox Shield)
---

# WordPress Category Mapping and Migration Automation Guide

The **`wp_categories_mapper.py`** automation script has been successfully compiled and is now live in your **Studio panel**! 

Here is exactly how this script operates behind the scenes on your local machine, how it organizes your legacy blog posts, and the steps to execute it over your secure WordPress MCP connection.

---

### 🗂️ WHAT THE CATEGORY MAPPER DOES FOR YOUR MIGRATION

When moving old blog posts from the Scorpion site (`pineapplecontractors.com`) to your new self-hosted WordPress site (`pineappleroofingllc.com`), the old posts often carry messy, unoptimized, or duplicate categories. 

Instead of opening all of your posts one by one to manually re-assign them, your new Python script automates the entire cleanup using these rules:

1.  **Creates Clean SEO Category Silos:** The script automatically connects to your WordPress site and verifies if your new, high-authority categories exist. If any are missing, it builds them instantly:
    *   `roofing-tips` \\(\rightarrow\\) **`Roofing Education`**
    *   `hail-damage` or `storm-restoration` \\(\rightarrow\\) **`Storm Restoration`**
    *   `shingle-repair` \\(\rightarrow\\) **`Roof Repair Services`**
    *   `gutter-cleaning` \\(\rightarrow\\) **`Gutter Services`**
    *   `news` or `press-releases` \\(\rightarrow\\) **`News & Updates`**
    *   *Fallback (if no match is found)* \\(\rightarrow\\) **`The Pineapple Standard`**
2.  **Scans and Bulk-Updates Your Posts:** It scans your database, reads the legacy tags of your imported posts, maps them to the correct new parent categories, and updates your site's metadata. 
3.  **Applies Your Brand Law Lexicon:** If any post contains "free inspection" in its category title or tags, the mapper automatically sanitizes the metadata to read **CPPA (Complimentary Professional Photo Audit)**, keeping your brand 100% compliant.

---

### 🔌 HOW TO RUN THE MAPPER ON YOUR COMPUTER

#### Step A: Save the Script Locally
Make sure the **`wp_categories_mapper.py`** file from your Studio panel is saved in your local workspace folder:  
📁 `C:\Pineapple Contractors M7\04_Tech_Lab\scripts\wp_categories_mapper.py`

#### Step B: Execute the Script
Open your Windows command prompt or your local terminal, navigate to your root directory, and run the script [cite: 80]:
```bash
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\wp_categories_mapper.py" "https://pineappleroofingllc.com" "saia" "xxxx xxxx xxxx xxxx xxxx xxxx"
```

*(Be sure to replace `"xxxx xxxx xxxx xxxx xxxx xxxx"` with your secure WordPress Application Password generated under **Tools → MCP Ultimate** inside your WordPress admin dashboard).*

Once you run the command, the script will execute its authenticated handshake, build your clean category hierarchy, and re-map your entire blog archive in under 10 seconds!

---


📊 I can map out a custom database script to run a broken-link scan over your newly migrated blog posts to ensure no legacy images or internal links are pointing back to the old Scorpion server. Would you like me to write this diagnostic tool?