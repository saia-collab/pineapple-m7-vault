import os

# Define the absolute root path for the M7 Engine
ROOT_DIR = r"C:\\Pineapple Contractors M7"

# 1. Build the strict 4-Fala Topography
structure = [
    r"01_Command_Center",
    r"02_Workspaces",
    r"03_Knowledge_Mat\\00_Atlas",
    r"04_Tech_Lab\\Scripts"
]

print("[-] Initializing Pineapple Mana Agentic OS Directory Structure...")
for folder in structure:
    path = os.path.join(ROOT_DIR, folder)
    os.makedirs(path, exist_ok=True)
    print(f"    Created: {path}")

# 2. Write the Immutable Master Playbook
playbook_path = os.path.join(ROOT_DIR, r"01_Command_Center\\MASTER_PLAYBOOK.md")
playbook_content = """---
type: systems_architecture_and_marketing_playbook
status: active
last_updated: 2026-06
classification: M7_Command_Level_1
---

# PINEAPPLE CONTRACTORS M7: AGENTIC OS MASTER PLAYBOOK

## 1. THE 4-FALA FILE TOPOGRAPHY (DIRECTORY ARCHITECTURE)
* **01_Command_Center\\** *(The Strategic Brain):* Houses brand constitution, master playbooks, and immutable laws.
* **02_Workspaces\\** *(The Active Mat):* Staging environment for active project execution and ad rendering.
* **03_Knowledge_Mat\\** *(The Content Substrate):* Data warehouse for historical data and standard operating procedures.
* **04_Tech_Lab\\** *(The Execution Engine):* Automation scripts, AI agent profiles, and MCP configurations.

## 2. THE BRAND FIREWALL & ELITE COMPLIANCE
### 2.1 The Visual Law
* **Royal Navy:** #001122 (Primary Brand Anchor & Text)
* **Pineapple Gold:** #FFD700 (Action, Highlights, & CTAs)
* *Under no circumstances is the color green permitted to be suggested, generated, or utilized.*

### 2.2 The Elite Lexicon (Mandatory Language Mutation)
* BANNED: "Free" / "Free Inspection" ➔ REQUIRED: "Complimentary Professional Photo Audit (CPPA)"
* BANNED: "$0 Out of Pocket" / "$0 Down" ➔ REQUIRED: "Full restoration coverage"
* BANNED: "GAF Certified" ➔ REQUIRED: "IKO Certified (RCAT License #03-0637)"

## 3. HIGH-VALUE METRICS & TOA STANDARDS
* **Minimum Baseline Entry:** $18,000+ project minimum.
* **Speed-to-Lead Directive:** Terminal-velocity response (< 5 minutes).

"""

with open(playbook_path, "w", encoding="utf-8") as f:
    f.write(playbook_content)
print(f"[+] Master Playbook Written cleanly to: {playbook_path}")

# 3. Write the AI Ingestion Cheat Sheet (The Execution Target)
cheatsheet_path = os.path.join(ROOT_DIR, r"01_Command_Center\\AI_INGESTION_TARGET.md")
cheatsheet_content = """# AI AGENT EXECUTION TARGET: COMMAND CENTER INGESTION

## MANDATE FOR CO-WORK AGENTS (CLAUDE & HERMES)
You are an active sub-module of the Pineapple Contractors M7 Agentic OS. Before running any operation, editing code, drafting copy, or manipulating file hierarchies, you must strictly ingest these rules.

### STEP 1: CONTEXT ANCHORING
- Read `01_Command_Center\\MASTER_PLAYBOOK.md` before processing any prompt.
- Never output cold-start assumptions. If information is missing, query `03_Knowledge_Mat\\`.

### STEP 2: MANDATORY COMPLIANCE AUDIT
- **Sanitize Language:** If the user or a data file passes the term "Free Inspection", you must programmatically rewrite it to "Complimentary Professional Photo Audit (CPPA)" before processing.
- **Sanitize Visuals:** All frontend web elements, landing pages, or CSS profiles generated must anchor exclusively to Royal Navy (#001122) and Pineapple Gold (#FFD700). Completely reject green configurations.

### STEP 3: HIGH-TICKET DISPATCH RULE
- Any incoming web lead routed via n8n with a property valuation over $700k or localized in Frisco ZIP codes (75033, 75034, 75035) must immediately bypass standard workflows and trigger an elevated Priority Alert to Saia.

"""

with open(cheatsheet_path, "w", encoding="utf-8") as f:
    f.write(cheatsheet_content)
print(f"[+] AI Ingestion Cheat Sheet Written cleanly to: {cheatsheet_path}")

print("[=>] SYSTEM BOOTSTRAP COMPLETE. READY FOR CLAUDE CODE EXECUTION.")
