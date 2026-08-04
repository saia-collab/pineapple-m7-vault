# 39 · jcode — Tiny Rust Coding Agent on Your Claude Login (Optional)

> 🛑 **Already built.** This tab ships working — don't ask an AI to build it. Missing? Update your pack (`Update Agent OS.command`).

The **jcode** tab runs [jcode](https://github.com/1jehuang/jcode) — an open-source **Rust** coding agent that's absurdly light (~28MB of RAM, instant startup) with a semantic memory graph and a swarm mode. Best part: it rides your **existing Claude subscription** — no new API key. It auto-discovers your Claude Code login (`~/.claude/.credentials.json`) with a one-time consent, and runs Claude Opus 5.

You get a build panel plus a **History** view of your jcode sessions (they get fun animal names).

## Setup (5 minutes)
1. **You need Claude Code logged in** (the `claude` CLI — `7-AGENT-CLIS.md`). jcode reuses that login.
2. **Install jcode** — follow the README at <https://github.com/1jehuang/jcode>, and make sure the binary ends up at `~/.local/bin/jcode` (that's where the tab looks).
3. **Run it once in a terminal** to approve the one-time credential consent:
   ```bash
   jcode
   ```
   Say yes when it asks to use your Claude login (recorded in `~/.jcode/auth.json`), then quit.
4. Open the **jcode** tab and build.

> 🟢 Easiest: open any AI agent in the folder and say *"install jcode from github.com/1jehuang/jcode, put the binary at ~/.local/bin/jcode, and run it once so I can approve the Claude-login consent."*

## Good to know
- **No new costs** — it uses your Claude plan, same as the Claude tab.
- **Sessions** live in `~/.jcode/sessions/` and show up in the tab's History panel.
- **Why bother?** It's the lightest harness around — great for quick builds without spinning up anything heavy.
