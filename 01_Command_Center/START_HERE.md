---
type: operator_runbook
status: active
last_updated: 2026-06-16
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# START HERE — Run the M7 OS Agentic Dashboard Command Center

## One-click launch
Double-click **`RUN_M7_DASHBOARD.bat`** in the vault root. It will:

1. Scaffold/verify the 4-Fala topography (`setup_m7.ps1`).
2. Refresh live avatar telemetry from `m7_scoring.py`.
3. Arm the Brand Firewall live listener (`brand_firewall.py --watch --fix`).
4. Serve and open the dashboard at `http://127.0.0.1:8787/OS_Dashboard.html`.

## Obsidian MCP wiring (one-time)
1. Open Obsidian on the `Pineapple Contractors M7` vault.
2. Settings → Community plugins → enable **Local REST API** and **MCP Tools**.
3. The API key is already wired in `.obsidian/plugins/obsidian-local-rest-api/data.json`.
4. Confirm the non-encrypted server is on: `http://127.0.0.1:27124`.
5. Test from a terminal:

   ```bash
   curl -H "Authorization: Bearer 5af24fd3...d4dc86a0f7511fa" http://127.0.0.1:27124/vault/
   ```

   (Use port 27123 with `https://` once you install the certificate for encrypted mode.)

## Connect the agents
Copy the MCP client configs into place, then restart the app:

- Claude Desktop → `%APPDATA%\Claude\claude_desktop_config.json`
  (source: `04_Tech_Lab\config\claude_desktop_config.json`)
- Antigravity → `%APPDATA%\antigravity\mcp.json`
  (source: `04_Tech_Lab\config\antigravity_mcp.json`)

## Claude Code non-interactive execution
`.claude/settings.json` is configured to auto-allow file, folder, python, and git
operations inside the vault so the agent can build without permission prompts.
For a fully headless run:

```bash
claude --dangerously-skip-permissions
```

## Ports
| Port | Mode | URL | Use |
| :--- | :--- | :--- | :--- |
| 27124 | HTTP | `http://127.0.0.1:27124` | Initial MCP wiring (no cert) |
| 27123 | HTTPS | `https://127.0.0.1:27123` | Secure mode (requires cert install) |
| 8787 | HTTP | `http://127.0.0.1:8787` | Local dashboard server |

## Security
The API key lives only in local config files (gitignored, never cloud-mirrored).
Rotate it from the Local REST API plugin settings if it is ever exposed.

Ko e hala 'o e fononga ko e faka'apa'apa.
