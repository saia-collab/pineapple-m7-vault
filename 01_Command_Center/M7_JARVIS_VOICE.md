---
type: config_card
title: Jarvis/Apollo Voice — Free Setup (no OpenAI, no Whisper)
status: active
last_updated: 2026-07-13
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# 🎙️ Jarvis Voice — The Free Configuration

> **The "always go here" card.** Packs keep flipping Jarvis back to OpenAI's paid
> voice (that's the "OpenAI out of credits" error). This card is how you set it
> back to the FREE voice we use — and the paste-ready goal to auto-fix it.

## 🧠 The one thing to understand
The voice tab has 3 listening modes. Two are FREE, one is PAID:

| Mode / Toggle | What powers it | Cost |
|---|---|---|
| **Realtime** | OpenAI Realtime API | 💵 **PAID** ← the "out of credits" culprit |
| **Live** | Chrome's built-in speech recognition | ✅ **FREE** |
| **Wake word** | Chrome's built-in speech recognition | ✅ **FREE** |

**Chrome has speech recognition built in** — that's why we do NOT need Whisper.
Whisper is a heavy local install; the browser already does it for $0.

## ✅ Set it to free (click settings, every time it reverts)
On the Hermes/Apollo voice tab:
1. **Turn Realtime OFF** (this is the paid OpenAI one — keep it off).
2. **Turn Live ON** (or Wake word) — free browser listening.
3. Brain/model = a **free model** (Groq / OmniRoute), never an OpenAI key.

## ♻️ Auto-fix after a pack update (paste into Hermes → Goal Mode, FREE)
When an update flips Jarvis back to paid OpenAI voice, paste this:
```
caveman: In the dashboard source (03_Knowledge_Mat/00_Atlas/templates/agent-os-pack-2026-06-29/source),
edit src/components/ApolloView.tsx so the voice is FREE by default:
1) Default the `realtime` state to FALSE (do NOT auto-connect OpenAI Realtime).
2) For spoken replies, use the browser's built-in speechSynthesis instead of the
   OpenAI TTS endpoint (provider:"openai") — fall back to browser voice, no API key.
3) Keep Live + Wake word (browser SpeechRecognition) as the listening path.
Then add src/components/ApolloView.tsx to the CUSTOMS preserve-list in
04_Tech_Lab/update_agent_os.ps1 so future updates don't revert it.
Do not touch anything else. Report what changed. PAUSED — I'll rebuild.
```
After it runs: rebuild the dashboard (dashboard OpenSEO/updater) or run
`LAUNCH_ALL.bat` to pick up the change.

## 🚫 What NOT to do
- Do **not** top up OpenAI billing to fix the voice — that's paying for the paid
  path. The free path (browser + Groq) is right there.
- Do **not** install Whisper — the browser covers speech-to-text for free.

## For your brother (the short version)
"You don't need Whisper. Chrome already hears you for free. In the AI dashboard,
turn **Realtime OFF** and **Live ON** — that's the free voice. Realtime is the
paid OpenAI one; leave it off."

<!-- M7-FIREWALL-EXEMPT: config-card -->
