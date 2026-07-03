---
type: architecture_and_mcp_hooks
status: active
last_updated: 2026-06-16
classification: M7_Command_Level_1
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
firewall: "M7-FIREWALL-EXEMPT: green-detection-tooling"
---

# M7 — IMMUTABLE DIRECTORY ARCHITECTURE & MCP HOOKS

Companion to `MASTER_PLAYBOOK.md`. Defines the line-by-line 4-Fala layout, the local ↔ Google Drive mirror, and the `.obsidian` vault index that patches the `obsidian-mcp` connection.

---

## 1. LINE-BY-LINE 4-FALA FILE SPECIFICATION MAP

> Role labels: `02_Workspaces` is the canonical on-disk folder; its operational role is **Tactical Ops** (the active staging mat). The folder name stays `02_Workspaces` to preserve zero directory drift against the existing vault.

```text
C:\Pineapple Contractors M7\
│
├── 01_Command_Center\                  # FALA 1 — Strategic Brain (DNA core)
│   ├── MASTER_PLAYBOOK.md              # Single source of truth
│   ├── ARCHITECTURE_MCP_MAP.md         # This file
│   ├── CROSS_AGENT_PROTOCOL.md         # Universal JSON telemetry contract
│   ├── tatafu.md                       # Brand core metrics & identity
│   ├── GROUNDING.md                    # Brand constitution (mirror in 03)
│   ├── ANTIGRAVITY_OS.md               # Master execution prompt config
│   ├── soul.md                         # Tonal persona bible
│   ├── OS_Dashboard.html               # Local Mission Control
│   ├── avatar_telemetry.json           # Live avatar feed (written by 04 scripts)
│   └── Outbox_Drafts\                  # Locked PAUSED publishing staging
│       └── YYYY-MM-DD_Outbox_Asset.md
│
├── 02_Workspaces\                      # FALA 2 — Tactical Ops (active mat)
│   └── Active_Campaigns\
│       └── YYYY-MM-DD_Campaign_Brief.md
│
├── 02_Media_Vault\                     # Raw + compiled brand-compliant media
│   └── YEAR_MONTH_CAMPAIGN_ASSET-TYPE.{png,mp4,webp}
│
├── 03_Knowledge_Mat\                   # FALA 3 — Neural Substrate (RAG)
│   ├── GROUNDING.md                    # Redundant constitution copy
│   ├── raw\                            # Temporary ingestion bin
│   │   └── YYYY-MM-DD_Raw_Transcript.md
│   └── 00_Atlas\                       # Index of peripheral SOPs
│       ├── YYYY-MM-DD_SOP_Onboarding.md
│       └── YYYY-MM-DD_FAQ_Community.md
│
├── 04_Tech_Lab\                        # FALA 4 — Execution Engine
│   └── Scripts\
│       ├── brand_firewall.py           # Compliance scanner + FS listener
│       ├── m7_scoring.py               # Lead + 1-3-12 campaign scoring
│       ├── m7_fetch.py                 # Clean competitor scrape
│       ├── m7_cleanup.py               # Housekeeping / dedupe
│       ├── m7_aggregate.py             # Knowledge_Mat flattening
│       ├── firewall_report.json        # Output of --report
│       └── scoring_report.json         # Output of scoring runs
│
└── 05_Campaign_Factory\                # Assembly Line (Stage Contracts)
    ├── 10_Research_Stage\
    │   ├── CONTEXT.md
    │   ├── input\                       # Raw Meta webhooks / search data
    │   └── output\  -> intent.json      # Scored intent profiles
    ├── 20_Copy_Drafting\
    │   ├── CONTEXT.md
    │   └── output\  -> draft_copy.json  # Unverified markdown copy blocks
    └── 30_Compliance_Audit\
        ├── CONTEXT.md
        └── output\  -> approved.json    # 100% brand-compliant, ready
```

---

## 2. LOCAL ↔ GOOGLE DRIVE MIRROR MAP

The Google Drive desktop client mounts at `G:\My Drive\`. Only the RAG substrate (`03_Knowledge_Mat`) and outbound drafts are cloud-mirrored so NotebookLM exports flow down cleanly; execution scripts and secrets stay local-only.

| Local Path | Google Drive Client Path | Sync Direction | Purpose |
| :--- | :--- | :--- | :--- |
| `C:\Pineapple Contractors M7\03_Knowledge_Mat\` | `G:\My Drive\03_Knowledge_Mat\` | Cloud → Local (pull) | NotebookLM research exports stage into `raw\`, flatten into `00_Atlas\`. |
| `C:\Pineapple Contractors M7\03_Knowledge_Mat\00_Atlas\` | `G:\My Drive\03_Knowledge_Mat\00_Atlas\` | Bi-directional | Shared SOP/FAQ index. |
| `C:\Pineapple Contractors M7\01_Command_Center\Outbox_Drafts\` | `G:\My Drive\01_Outbox\` | Local → Cloud (push) | Review drafts from any device (still PAUSED). |
| `C:\Pineapple Contractors M7\02_Media_Vault\` | `G:\My Drive\02_Media_Vault\` | Bi-directional | Raw drone captures + compiled reels. |
| `C:\Pineapple Contractors M7\04_Tech_Lab\` | *(not mirrored)* | Local only | Scripts, secrets, `.env`, tokens never leave the machine. |
| `C:\Pineapple Contractors M7\01_Command_Center\*.md` | *(not mirrored)* | Local only | Constitution is local-authoritative; avoids sync-conflict drift. |

**Sync discipline (zero-drift rules):**

- `memory_sync.py` pulls newest `brand-voice.md` / `marketing-wisdom.md` from `G:\My Drive\03_Knowledge_Mat\` into local `03_Knowledge_Mat\` on a daily, zero-token job.
- The mirror is one folder deep at the room boundary — never mirror the vault root (`.obsidian`, `.git`, and `04_Tech_Lab` must never sync).
- Drive `.tmp.drivedownload` / `.tmp.driveupload` folders are excluded from all firewall and aggregation scans.

---

## 3. `.obsidian` VAULT STRUCTURE INDEX — obsidian-mcp PATCH

The `obsidian-mcp` connection breaks when the vault config is missing the Local REST API key, the community-plugin allow-list, or when the vault path contains an unescaped space. The index below patches all three.

```text
C:\Pineapple Contractors M7\.obsidian\
├── app.json                 # core editor config
├── appearance.json          # theme; accent forced to Pineapple Gold
├── core-plugins.json        # enables file-explorer, canvas, backlinks, sync
├── community-plugins.json    # ["obsidian-local-rest-api","mcp-tools"]
├── hotkeys.json
├── workspace.json           # last layout (auto-managed)
├── graph.json               # knowledge-graph view state
├── canvas\
│   └── M7_Memory_Galaxy.canvas   # 3D constellation blueprint
└── plugins\
    ├── obsidian-local-rest-api\
    │   ├── main.js
    │   ├── manifest.json
    │   └── data.json        # { "apiKey": "<LOCAL_KEY>", "port": 27123, "enableInsecure": false }
    └── mcp-tools\
        ├── main.js
        ├── manifest.json
        └── data.json        # { "restApiUrl": "https://127.0.0.1:27123", "vaultName": "Pineapple Contractors M7" }
```

### 3.1 `appearance.json` (brand-locked accent)

```json
{
  "accentColor": "#FBC02D",
  "theme": "obsidian",
  "cssTheme": "",
  "baseFontSize": 16
}
```

### 3.2 `community-plugins.json`

```json
["obsidian-local-rest-api", "mcp-tools"]
```

### 3.3 `plugins/obsidian-local-rest-api/data.json`

```json
{
  "apiKey": "REPLACE_WITH_GENERATED_KEY",
  "port": 27123,
  "enableInsecureHttp": false,
  "bindingHost": "127.0.0.1"
}
```

### 3.4 MCP client registration (`claude_desktop_config.json` / `antigravity\mcp.json`)

```json
{
  "mcpServers": {
    "obsidian": {
      "command": "npx",
      "args": ["-y", "obsidian-mcp", "C:\\Pineapple Contractors M7"],
      "env": {
        "OBSIDIAN_API_KEY": "REPLACE_WITH_GENERATED_KEY",
        "OBSIDIAN_HOST": "127.0.0.1",
        "OBSIDIAN_PORT": "27123"
      }
    },
    "notebooklm": {
      "command": "npx",
      "args": ["-y", "notebooklm-mcp-server", "start"]
    }
  }
}
```

### 3.5 Connection-breakdown checklist (run in order)

1. In Obsidian: enable **Community plugins**, install **Local REST API** + **MCP Tools**, then **Enable** both.
2. Copy the generated API key into `data.json` *and* every MCP client `env` block above.
3. Confirm the vault path is double-quoted / double-backslashed in the MCP args (the space in `Pineapple Contractors M7` breaks unquoted launches).
4. Verify the listener: `curl -k https://127.0.0.1:27123/` should return the vault handshake.
5. Restart Claude Desktop / Antigravity so the MCP server re-registers.
6. Test cross-agent read: `read_note 01_Command_Center/MASTER_PLAYBOOK.md` must return content, not a 401.

### 3.6 `canvas/M7_Memory_Galaxy.canvas` blueprint (skeleton)

```json
{
  "nodes": [
    {"id":"core","type":"text","text":"MASTER_PLAYBOOK","x":0,"y":0,"width":260,"height":80,"color":"3"},
    {"id":"fala1","type":"text","text":"01_Command_Center","x":-360,"y":-160,"width":220,"height":60,"color":"3"},
    {"id":"fala3","type":"text","text":"03_Knowledge_Mat","x":360,"y":-160,"width":220,"height":60,"color":"5"},
    {"id":"fala4","type":"text","text":"04_Tech_Lab","x":-360,"y":160,"width":220,"height":60,"color":"3"},
    {"id":"fala5","type":"text","text":"05_Campaign_Factory","x":360,"y":160,"width":220,"height":60,"color":"5"}
  ],
  "edges": [
    {"id":"e1","fromNode":"core","toNode":"fala1"},
    {"id":"e2","fromNode":"core","toNode":"fala3"},
    {"id":"e3","fromNode":"core","toNode":"fala4"},
    {"id":"e4","fromNode":"core","toNode":"fala5"}
  ]
}
```

> Obsidian canvas color tokens used: `3` (gold-family) and `5` (cyan-family). Color `4` (green) is intentionally never used.

---

Ko e hala 'o e fononga ko e faka'apa'apa.
