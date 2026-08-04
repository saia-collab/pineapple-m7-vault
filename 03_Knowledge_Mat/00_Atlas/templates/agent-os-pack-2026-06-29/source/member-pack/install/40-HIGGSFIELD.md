# 40 · Higgsfield — AI Images + Video via Hermes (Optional)

> 🛑 **Already built.** This tab ships working — don't ask an AI to build it. Missing? Update your pack (`Update Agent OS.command`).

The **Higgsfield** tab generates **images and video** with [Higgsfield](https://higgsfield.ai) — driven **through Hermes** using Higgsfield's official MCP server. You type what you want; Hermes picks the right Higgsfield tool, generates, and saves every asset into a gallery inside the tab. No manual downloads, no tab-hopping.

## What you need
1. **Hermes working** (`4-HERMES.md`).
2. **A Higgsfield account** — sign up at <https://higgsfield.ai> (generation uses your account's credits/plan).

## Setup (5 minutes)
1. **Register the MCP server** in your Hermes config — add this under `mcp_servers:` in `~/.hermes/config.yaml` (or your active profile's `config.yaml`):
   ```yaml
   mcp_servers:
     higgsfield:
       url: https://mcp.higgsfield.ai/mcp
   ```
2. **Sign in once** (opens a browser, your Higgsfield account):
   ```bash
   hermes mcp login higgsfield
   ```
3. Open the **Higgsfield** tab. The status line tells you exactly which half is missing (registered vs signed in) if something's off. When it's green — describe an image or video and go.

> 🟢 Easiest: open any AI agent in the folder and say *"register the Higgsfield MCP (https://mcp.higgsfield.ai/mcp) in my Hermes config and run hermes mcp login higgsfield with me."*

## Good to know
- **Everything lands in the gallery** — generated images/videos are saved into the tab's gallery automatically (`~/.agentic-os/higgsfield/gallery`).
- **Costs are yours** — generation spends your Higgsfield account's credits; nothing is charged by Agent OS.
- **Uses your active Hermes profile** by default; power users can pin one with the `HIGGS_PROFILE` env var.
