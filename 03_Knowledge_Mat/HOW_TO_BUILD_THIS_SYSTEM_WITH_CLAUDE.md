---
INTENT: Beginner-friendly guide to build the whole Pineapple M7 Agentic OS system using Claude, in plain language.
type: guide
audience: anyone (non-technical friendly)
generated: 2026-07-02
---

# 🍍 How to Build Your Own AI Command Center (with Claude) 🤖

> **No coding degree needed.** If you can copy, paste, and click "Next," you can build this. Claude does the hard parts. 💪

---

## 🌟 What You're Building

A personal **AI headquarters** that runs on your own computer. Think of it like an office building 🏢 where every room has a smart AI helper:

- 🖥️ **A Dashboard** — your home screen. One place to see everything.
- 📎 **Paperclip** — a whole *company* of AI agents with a boss, managers, and workers (an org chart!).
- 🧠 **A Memory Vault** — your notes, so the AI remembers everything about you.
- 🦾 **Hermes** — an AI that actually *does* multi-step jobs (not just chat).
- 🎙️ **A voice** — talk to it, it talks back.

All of it lives **on your machine**. Private. Yours. 🔒

---

## 🧰 Before You Start (5 minutes)

You only need **two** things installed:

1. **Node.js** 🟢 → go to [nodejs.org](https://nodejs.org) → click the big **LTS** button → install. (This is the engine everything runs on.)
2. **Claude Code** 🤖 → your AI builder. It reads instructions and does the work for you.

> 💡 **Tip:** Node.js is the ONLY "techy" install. Everything else, Claude sets up.

---

## 🚀 The Magic Trick: Let Claude Do It

The system comes as a **ZIP folder** (the "Agent OS pack"). Inside is a file called `SETUP-WITH-AI.md`. That file is a *set of instructions written for an AI*. 🪄

**So you just say this to Claude:**

> *"Read SETUP-WITH-AI.md and set up the whole Agent OS for me on Windows, step by step. Ask me whenever you need a key or a decision."*

That's it. Claude reads the playbook and builds it. When it needs a password or a Complimentary account, it stops and asks you. 🙋

---

## 🪜 The Steps (what Claude does for you)

### 1️⃣ The Dashboard (the must-have) 🖥️
Claude runs three little commands inside the pack's `source` folder:
```
npm install        📦 (downloads the parts — takes a few minutes, that's normal)
npm run build      🔨 (assembles it)
npm start          ▶️ (turns it on)
```
Then your dashboard is live at **http://localhost:3000** (or 3737). Open it in **Chrome**. 🎉

> ⚠️ **Big tip:** always use `build` then `start` (not "dev mode"). It's way more stable. 🛡️

### 2️⃣ Connect Your Memory 🧠
Claude points the dashboard at your notes folder (your "vault") so the AI remembers your world. One line in a settings file — Claude handles it.

> 🪟 **Windows gotcha we learned the hard way:** the folder path must use **backslashes** (`C:\Your\Folder`), not forward slashes, or notes won't open. Claude knows this now. ✅

### 3️⃣ Add Hermes 🦾 (the do-er)
The agent that runs real tasks. It needs **one** cheap key from [openrouter.ai](https://openrouter.ai) (pennies). Claude wires it in.

> 🚫 **Golden rule:** never make the tiny on-device model (Gemma2) the "boss." It's only for quick offline builds. Big jobs → strong models. Claude follows this rule.

### 4️⃣ Add Paperclip 📎 (your AI company)
One command: `npx paperclipai onboard --yes`. Then Claude builds you an **org chart** — a CEO agent, managers (Marketing, Tech, Operations), and worker agents — each with a job. It shows up right inside your dashboard. 🏢

### 5️⃣ Turn On the Extras (optional) ✨
- 🎙️ **Voice (Jarvis)** — needs a Complimentary ElevenLabs account.
- 🆓 **Complimentary Claude Code** — code without a subscription.
- 🎬 **Video / Thumbnail / Music studios** — creative tools.

Claude asks which ones you want. Only add what you'll use. 🧩

---

## 🛟 If Something Breaks

Just tell Claude what you see. Seriously. 🗣️ Example:
> *"My Memory tab is empty and notes won't open — fix it."*

Because the setup guides live **inside your vault**, Claude can read them and fix things against the *real* steps — not guesswork. 🔧

---

## 🎯 The One Rule That Prevents 90% of Problems

🧠 **Different jobs use different AI brains. Don't force one small brain to do everything.**
- Coding → a strong model (Claude / N2)
- Hermes & voice → an OpenRouter model
- Quick offline builds → the tiny local model (Gemma2) — *only* here!

---

## ✅ You're Done When…

- 🖥️ Dashboard opens in Chrome
- 🧠 Your notes show up in the **Memory** tab (and open when clicked!)
- 📎 Paperclip shows your AI company org chart
- 🦾 Hermes answers when you give it a task

**Welcome to your AI command center.** 🍍🚀

---
