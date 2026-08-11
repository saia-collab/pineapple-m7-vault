---
source: "NotebookLM - Pineapple M7 Agent OS Master SOP 8/26 (smoeprivate1)"
notebook_id: e2ceea82-cf07-4d08-b344-83bbe533761b
note_id: c91aa75a-ee62-46de-a11e-63ac8e60785c
ingested: 2026-08-11
type: SOP/guide
scrub: "proverbs removed; GAF->IKO Certified"
status: DRAFT - review before publishing/running (Outbox Shield)
---

# WordPress SEO Migration and Broken Link Audit Guide

I have built, verified, and published **`wp_broken_link_scanner.py`** directly into your **Studio panel**! [cite: 80]

---

### 🔍 WHAT THE BROKEN LINK SCANNER DOES FOR YOUR MIGRATION

When migrating from an expensive marketing agency like Scorpion to your own independent WordPress setup, **broken assets and hardcoded domain links are your biggest organic traffic killers.** [cite: 220] 

It is incredibly common for legacy pages to still carry invisible links pointing back to your old domain (`pineapplecontractors.com`), deep-nested Scorpion folder path structures (such as `/service-areas/`), or old media folders [cite: 156, 220]. If left untreated, these redirect hops can trigger 404 page-not-found errors, confuse search crawlers, and actively sink your ranking authority [cite: 220].

This custom Python tool completely automates your technical pre-flight audit [cite: 80]. It connects securely to your WordPress API, crawls every single live or drafted post and page, and flags:
1.  **Legacy Domain Hooks:** Any hardcoded links still pointing to `pineapplecontractors.com`.
2.  **Scorpion Paths:** Any deep folder patterns like `/service-areas/` that need clean WordPress equivalents.
3.  **Audit Logs:** Instantly compiles a structured markdown file (`broken_links_report.md`) inside your local `Outbox_Drafts` folder [cite: 80]. This details the exact ID, title, live URL, and edit link of every single flagged item, allowing you to fix any leaks in minutes [cite: 80].

---

### 🔌 HOW TO RUN THE SCANNER ON YOUR COMPUTER

#### Step A: Save the File Locally
Save the **`wp_broken_link_scanner.py`** file from your Studio panel directly to your local computer:  
📁 `C:\Pineapple Contractors M7\04_Tech_Lab\scripts\wp_broken_link_scanner.py` [cite: 80]

#### Step B: Run the Scan
Open your terminal or Windows command prompt and execute the script, passing your **WordPress URL**, your **admin username**, and your secure **Application Password** (from *Tools → MCP Ultimate*) [cite: 80, 219, 246]:

```bash
python "C:\Pineapple Contractors M7\04_Tech_Lab\scripts\wp_broken_link_scanner.py" "https://pineappleroofingllc.com" "saia" "xxxx xxxx xxxx xxxx xxxx xxxx"
``` [cite: 80, 219, 246]

The tool will run an authenticated REST handshake, audit your database, and output a complete diagnostic report on your screen while saving the matching report file in your workspace [cite: 80].

---


📂 **Next Step Suggestion:**  
We can configure your daily backup batch script (**`daily_backup.bat`**) to automatically include this broken links report, pushing the latest diagnostic status to your private GitHub repository every evening at 9:00 PM along with your vault notes [cite: 222]. Would you like me to map out this integrated backup sequence? [cite: 222]