# 7 · The Agent Tabs (Optional — Pick What You Use)

Down the left side of the dashboard you'll see tabs for **Claude, OpenClaw, Gemini, Antigravity, Codex**. Each one lights up when you have that tool installed on your computer. You don't need all of them — **install only the ones you actually use.**

## The simple rule
A tab works when its program is installed and you're logged in. If a tab says it can't find the tool, that just means you haven't installed that one — and that's fine. Skip it.

## The tools and where to get them

| Tab | What it is | Where to get it |
|-----|-----------|-----------------|
| **Claude** | Anthropic's Claude Code | https://claude.com/claude-code |
| **Codex** | OpenAI's coding agent | OpenAI's Codex CLI |
| **Gemini** | Google's Gemini CLI ⚠️ *retired 18 Jun 2026* | — use **Antigravity** instead |
| **Antigravity** | Google's Antigravity (Gemini's successor) | Google Antigravity (`agy`) |
| **OpenClaw** | OpenClaw agent | The OpenClaw project |

After you install one, just log in to it once the normal way (each tool tells you how). Then its tab in the Agent OS works.

> ✅ **Claude needs `claude login`, not an API key.** The Claude tab uses Claude Code's normal sign-in — run **`claude login`** once (a browser login that works with your Claude **Pro/Max subscription**) and the tab works. You do **not** need an `ANTHROPIC_API_KEY`.
> - ⚠️ **Don't leave an *empty* `ANTHROPIC_API_KEY=` in a `.env.local`.** An empty key *overrides* your `claude login` and makes the Claude tab fail to authenticate. If a setup step created one, delete that line (or the whole `.env.local`) and just use `claude login`.
> - 💳 Prefer pay-per-token instead of a subscription? Put a **real** key (`ANTHROPIC_API_KEY=sk-ant-…` from <https://console.anthropic.com>) in `.env.local`, then restart.
> - 💵 No subscription and no key? Use the **Free Claude Code** tab instead — it routes to free models, no Anthropic key needed (`5-FREE-CLAUDE-CODE.md`).

> ⚠️ **Gemini CLI was retired on 18 June 2026** for free/Pro/Ultra users — Google replaced it with **Antigravity** (the `agy` CLI). So the **Gemini** tab won't connect anymore; install **Antigravity** instead — it's the direct successor (multi-agent harness, plugins). *(The optional Live-Translate **Gemini API key** below is separate — that's the Gemini API, not the CLI, and still works.)*

## 🌐 Optional: Live Translate (Gemini key)
A few places in the OS (the Jarvis voice, the phone agent, the video tools) can do **live translation** using Google's Gemini. It's optional. To switch it on, get a free **Gemini API key** from **https://aistudio.google.com/apikey**, then save it:
```bash
mkdir -p ~/.agentic-os
echo 'GEMINI_API_KEY=your_key_here' > ~/.agentic-os/gemini.env
chmod 600 ~/.agentic-os/gemini.env
```
Restart the dashboard. (Skip this if you don't need live translation.)

## How the dashboard finds them
It looks for each tool on your computer automatically. If you installed a tool somewhere unusual and the tab can't find it, you can point the dashboard straight at it using a setting (see `config.example.json`) — but for normal installs you won't need to.

## More on the Claude tab
Besides Chat, the Claude tab has two extra sub-tabs: **Artifacts** (publish any HTML your agent builds to a private shareable link) and **Ultracode** (kick off a multi-agent cloud review of your work). Both optional — use them when you want them.

## Which should I start with?
If you're new: just use **Claude** (you probably installed it already from the README) and the **Free Claude Code** / **Hermes** tabs. Add the others later if you start using them.

## ⭐ Choosing your Claude model (read this — it affects your usage)

The Claude tab (and the SEO engine) now come set to **Claude Opus 5** (`claude-opus-5`, launched 24 July 2026) — Anthropic's newest flagship, the strongest all-round Claude. There's **nothing to set up**: if your Claude CLI/plan has Opus 5, it just works. Most people should leave it.

**Prefer something else?** You can pin any Claude model with one tiny file change, no code:

1. Open (or create) the file `~/.agentic-os/config.json`
2. Add this line inside the curly braces (swap in whichever model you want):
   ```json
   "claudeModel": "claude-opus-5"
   ```
   So the file looks something like:
   ```json
   {
     "claudeModel": "claude-opus-4-8"
   }
   ```
3. Restart the dashboard. Done — every Claude feature now uses that model.

**Which should you pick?**
- **Opus 5** (`claude-opus-5`, the default) → newest flagship, best all-round results. Leave it here unless you have a reason not to.
- **Opus 4.8** (`claude-opus-4-8`) → the previous default; rock-solid and a little lighter on your plan's tokens. A good fallback if Opus 5 isn't on your plan yet.
- **Claude 5** (`claude-fable-5`, Mythos-class) → a heavier "thinks-more" model for the hardest reasoning; uses more tokens.

> If a Claude feature errors on the model you picked, that model probably isn't enabled on your Claude CLI/plan yet — set `claudeModel` to `claude-opus-4-8` and you're back in business.

You can switch any time by changing that one line. (Power users: the `AGENTIC_OS_CLAUDE_MODEL` environment variable does the same thing.)

## Done?
That's everything. If a piece is acting up, head to **`8-TROUBLESHOOTING.md`**.
