# SYSTEM CONSTRAINTS & MASTER EXECUTION MANDATE

You are an AI Agent operating natively within the Pineapple Contractors M7 Agentic OS. You must strictly adhere to the 4-Fala Directory Standard.

### CRITICAL RULES:
1. NO LOOSE FILES IN THE ROOT DIRECTORY (`C:\Pineapple Contractors M7\`) except for `claw.md` and system configuration folders (`.obsidian`, `.claude`).
2. All generated outputs, temporary logs, or script modifications MUST be targeted explicitly to their corresponding Fala directory (`01_Command_Center`, `02_Media_Vault`, `03_Knowledge_Mat`, `04_Tech_Lab`, or `05_Campaign_Factory`).
3. "LOOK BEFORE YOU LEAP" PROTOCOL: Prior to creating or modifying any file, perform a directory check to ensure compliance. If drift is detected, you are commanded to self-correct and sort the target artifacts instantly.

# Master AI Operating Manual & Directory Guardrail

**Tags:** #system/core #agent/directive #4fala/compliance
**Created:** 2026-06-12
**Updated:** 2026-06-12
**Agent Origin:** Lead Systems Architect
**Confidence:** 100% (Deterministic Autonomy)

## 1. Ground State Rule: The "Look Before You Leap" Protocol
To prevent directory drift, duplicated folders, and legacy file collisions, any AI agent initializing in this environment **MUST** run the following three steps before executing any write, edit, or migration command:

1. **Inspect Directory Tree:** List the top‑level folders to verify that only the three authorized primary Fala directories exist.
2. **Read the Anchor:** Load this file (`C:\\Pineapple Contractors M7\\claw.md`) and verify the active directory map.
3. **Check for Duplicate Names:** If about to write a master file (e.g., `MASTER_PLAYBOOK.md`), search the entire workspace first to ensure a version doesn't already exist in another folder.

## 2. The 4‑Fala Directory Standard
Every file generated, edited, or ingested by an AI agent must strictly reside within this layout. No exceptions are permitted.

```
C:\\Pineapple Contractors M7\
├── .obsidian/                      # Obsidian configuration data (System hidden)
├── claw.md                         # This file (The root‑level Agent Rulebook)
│
├── 01_Command_Center/              # THE SECOND Fala (Fine Mat: Brand Truth)
│   ├── MASTER_PLAYBOOK.md          # Unified marketing blueprint & branding laws
│   ├── soul.md                     # Tatafu Vēhala brand character bible
│   ├── ANTIGRAVITY_OS.md           # Master system execution prompt configuration
│   ├── OS_Dashboard.html           # Visual single‑page command dashboard
│   └── OBSIDIAN_SETUP.md           # Obsidian walkthrough guide
│
├── 03_Knowledge_Mat/               # THE FIRST Fala (Base Mat: Grounding Context)
│   ├── raw/                        # Raw source PDFs, transcripts, and voice dumps
│   └── 00_Atlas/                   # System indices, logs, and process registers
│       ├── index.md                # System‑wide index file
│       └── log.md                  # Detailed chronological run‑logs
│
└── 04_Tech_Lab/                    # THE THIRD Fala (Weaving Mat: CLI Scripts)
    ├── scripts/                    # PowerShell, Node.js, and Python automations
    └── Outputs/                    # THE FOURTH Fala (Ceremonial Mat: Final Assets)
```

## 3. Autonomous Self‑Correction Script (Agent Execution)
If an agent detects files out of place, duplicates, or folders named `M7_Core`, `M7_Sources`, or `M7_Vault`, it must instantly execute the following automated correction script in its shell environment to align the workspace:

```powershell
# Executed by Agent to auto‑clean workspace anomalies
$rootDir = "C:\\Pineapple Contractors M7"
$fCenter = "$rootDir\\01_Command_Center"
$fRaw    = "$rootDir\\03_Knowledge_Mat\\raw"

# Move orphaned files back to their respective Falas
if (Test-Path "$rootDir\\soul.md") { Move-Item "$rootDir\\soul.md" $fCenter -Force }
if (Test-Path "$rootDir\\MASTER_PLAYBOOK.md") { Move-Item "$rootDir\\MASTER_PLAYBOOK.md" $fCenter -Force }
if (Test-Path "$rootDir\\ANTIGRAVITY_OS.md") { Move-Item "$rootDir\\ANTIGRAVITY_OS.md" $fCenter -Force }
if (Test-Path "$rootDir\\OS_Dashboard.html") { Move-Item "$rootDir\\OS_Dashboard.html" $fCenter -Force }

# Remove legacy folder artifacts
@("M7_Core", "M7_Sources", "M7_Vault") | ForEach-Object {
    $legacyPath = Join-Path $rootDir $_
    if (Test-Path $legacyPath) {
        Remove-Item $legacyPath -Recurse -Force
    }
}
```

## 4. Elite Compliance Guards (Terminology & Design Filters)
Before saving any file, draft, script, or campaign asset, the agent must run this regex/text filter across its planned output. Any violation must trigger a self‑correction rewrite before the file hits your drive:

- **DO NOT** write the word **"FREE"** in connection with property evaluations.
  - **Correction:** Replace with **"Complimentary Professional Photo Audit"** (CPPA).
- **DO NOT** write **"$0 down"**, **"$0 out of pocket"**, or use the **$** symbol for promotional pricing.
  - **Correction:** Replace with **"Full restoration coverage evaluation"**.
- **DO NOT** write **"GAF Certified"**.
  - **Correction:** Replace with **"IKO Certified"**.
- **DO NOT** suggest, write, or generate any CSS, HTML, or asset design elements that include the color **Green**.
  - **Correction:** Restrict designs entirely to **Royal Navy (#1A365D), Pineapple Gold (#FBC02D), Slate, White, and Dark Gray**.

---

### Agent Initialization Instruction
#### Direct Instruction Block: Initializing Your Agent in the 4‑Fala System
Whenever you start a terminal session with an AI agent (such as Claude Code or Hermes), copy and paste the following command block directly into the console. This completely bypasses human operational error and forces the AI to fix any layout discrepancies immediately:

```bash
claude --commands "Read claw.md first, verify that no legacy M7 folders or loose root files exist, run the self‑correction cleanup block inside claw.md if any layout errors are found, and confirm alignment to the 4‑Fala system."
```

**How this works:**
1. Save `claw.md` to the root folder `C:\\Pineapple Contractors M7\\claw.md`.
2. Save the initialization command sheet to `01_Command_Center/AGENT_INIT_INSTRUCTION.md`.
3. Whenever your AI workspace gets disorganized, copy the initialization command in your terminal. The agent will read `claw.md` and autonomously rearrange the files back into their exact designated folders.

---

*End of Guardrail Document*


**Tags:** #system/core #agent/directive #4fala/compliance
**Created:** 2026-06-12
**Updated:** 2026-06-12
**Agent Origin:** Lead Systems Architect
**Confidence:** 100% (Deterministic Autonomy)

## 1. Ground State Rule: The "Look Before You Leap" Protocol
To prevent directory drift, duplicated folders, and legacy file collisions, any AI agent initializing in this environment **MUST** run the following three steps before executing any write, edit, or migration command:

1. **Inspect Directory Tree:** List the top‑level folders to verify that only the three authorized primary Fala directories exist.
2. **Read the Anchor:** Load this file (`C:\\Pineapple Contractors M7\\claw.md`) and verify the active directory map.
3. **Check for Duplicate Names:** If about to write a master file (e.g., `MASTER_PLAYBOOK.md`), search the entire workspace first to ensure a version doesn't already exist in another folder.

## 2. The 4‑Fala Directory Standard
Every file generated, edited, or ingested by an AI agent must strictly reside within this layout. No exceptions are permitted.

```
C:\\Pineapple Contractors M7\
├── .obsidian/                      # Obsidian configuration data (System hidden)
├── claw.md                         # This file (The root‑level Agent Rulebook)
│
├── 01_Command_Center/              # THE SECOND FALA (Fine Mat: Brand Truth)
│   ├── MASTER_PLAYBOOK.md          # Unified marketing blueprint & branding laws
│   ├── soul.md                     # Tatafu Vēhala brand character bible
│   ├── ANTIGRAVITY_OS.md           # Master system execution prompt configuration
│   ├── OS_Dashboard.html           # Visual single‑page command dashboard
│   └── OBSIDIAN_SETUP.md           # Obsidian walkthrough guide
│
├── 03_Knowledge_Mat/               # THE FIRST FALA (Base Mat: Grounding Context)
│   ├── raw/                        # Raw source PDFs, transcripts, and voice dumps
│   └── 00_Atlas/                   # System indices, logs, and process registers
│       ├── index.md                # System‑wide index file
│       └── log.md                  # Detailed chronological run‑logs
│
└── 04_Tech_Lab/                    # THE THIRD FALA (Weaving Mat: CLI Scripts)
    ├── scripts/                    # PowerShell, Node.js, and Python automations
    └── Outputs/                    # THE FOURTH FALA (Ceremonial Mat: Final Assets)
```

## 3. Autonomous Self‑Correction Script (Agent Execution)
If an agent detects files out of place, duplicates, or folders named `M7_Core`, `M7_Sources`, or `M7_Vault`, it must instantly execute the following automated correction script in its shell environment to align the workspace:

```powershell
# Executed by Agent to auto‑clean workspace anomalies
$rootDir = "C:\\Pineapple Contractors M7"
$fCenter = "$rootDir\\01_Command_Center"
$fRaw    = "$rootDir\\03_Knowledge_Mat\\raw"

# Move orphaned files back to their respective Falas
if (Test-Path "$rootDir\\soul.md") { Move-Item "$rootDir\\soul.md" $fCenter -Force }
if (Test-Path "$rootDir\\MASTER_PLAYBOOK.md") { Move-Item "$rootDir\\MASTER_PLAYBOOK.md" $fCenter -Force }
if (Test-Path "$rootDir\\ANTIGRAVITY_OS.md") { Move-Item "$rootDir\\ANTIGRAVITY_OS.md" $fCenter -Force }
if (Test-Path "$rootDir\\OS_Dashboard.html") { Move-Item "$rootDir\\OS_Dashboard.html" $fCenter -Force }

# Remove legacy folder artifacts
@("M7_Core", "M7_Sources", "M7_Vault") | ForEach-Object {
    $legacyPath = Join-Path $rootDir $_
    if (Test-Path $legacyPath) {
        Remove-Item $legacyPath -Recurse -Force
    }
}
```

## 4. Elite Compliance Guards (Terminology & Design Filters)
Before saving any file, draft, script, or campaign asset, the agent must run this regex/text filter across its planned output. Any violation must trigger a self‑correction rewrite before the file hits your drive:

- **DO NOT** write the word **"FREE"** in connection with property evaluations.
  - **Correction:** Replace with **"Complimentary Professional Photo Audit"** (CPPA).
- **DO NOT** write **"$0 down"**, **"$0 out of pocket"**, or use the **$** symbol for promotional pricing.
  - **Correction:** Replace with **"Full restoration coverage evaluation"**.
- **DO NOT** write **"GAF Certified"**.
  - **Correction:** Replace with **"IKO Certified"**.
- **DO NOT** suggest, write, or generate any CSS, HTML, or asset design elements that include the color **Green**.
  - **Correction:** Restrict designs entirely to **Royal Navy (#1A365D), Pineapple Gold (#FBC02D), Slate, White, and Dark Gray**.

---

### Agent Initialization Instruction
#### Direct Instruction Block: Initializing Your Agent in the 4‑Fala System
Whenever you start a terminal session with an AI agent (such as Claude Code or Hermes), copy and paste the following command block directly into the console. This completely bypasses human operational error and forces the AI to fix any layout discrepancies immediately:

```bash
claude --commands "Read claw.md first, verify that no legacy M7 folders or loose root files exist, run the self‑correction cleanup block inside claw.md if any layout errors are found, and confirm alignment to the 4‑Fala system."
```

**How this works:**
1. Save `claw.md` to the root folder `C:\\Pineapple Contractors M7\\claw.md`.
2. Save the initialization command sheet to `01_Command_Center/AGENT_INIT_INSTRUCTION.md`.
3. Whenever your AI workspace gets disorganized, copy the initialization command in your terminal. The agent will read `claw.md` and autonomously rearrange the files back into their exact designated folders.

---

*End of Guardrail Document*

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
