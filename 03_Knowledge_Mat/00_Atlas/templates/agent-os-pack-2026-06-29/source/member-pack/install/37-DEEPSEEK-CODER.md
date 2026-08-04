# 37 · DeepSeek Coder — V4 Flash, Official API (Optional)

> 🛑 **Already built.** This tab ships working in your Agent OS — don't ask an AI to build it. If you don't see it, your pack is out of date: run `Update Agent OS.command`.

The **DeepSeek Coder** tab chats with **DeepSeek V4 Flash** (the 31-July-2026 public beta) on DeepSeek's **official API** — a very cheap, very fast reasoning coder. You get a chat panel plus a workspace for the files it writes.

Why the official API and not a router? Third-party routes list "v4-flash" undated and may still serve the older preview — the official endpoint is the real 0731 model.

## Setup (2 minutes)
1. **Get a DeepSeek API key** — create one at <https://platform.deepseek.com> (API keys section). New accounts get free trial credit; after that it's pay-as-you-go (V4 Flash is among the cheapest frontier-class models).
2. **Give the key to Agent OS** — add this line to `~/.fcc/.env` (or set it as an environment variable):
   ```
   DEEPSEEK_API_KEY=sk-your-key-here
   ```
3. Open the **DeepSeek Coder** tab. When the status dot goes green, chat away.

> 🟢 Easiest: open any AI agent in the folder and say *"add my DeepSeek API key so the DeepSeek Coder tab works"* and paste the key when it asks.

## Good to know
- **It's a reasoning model** — V4 "thinks" before it answers; the panel shows a thinking indicator first. That's normal.
- **Models:** `deepseek-v4-flash` (default, fast + cheap) and `deepseek-v4-pro` (stronger, pricier) — pick in the panel.
- **Costs are yours** — DeepSeek bills your key directly; nothing is charged by Agent OS.
- **Pick the right brain:** DeepSeek V4 Flash for fast cheap iterations; GPT 5.6 Code / real Claude for the heaviest builds.
