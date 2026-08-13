---
type: local_model_playbook
title: M7 Local Model & Workload-Tier Playbook — never get stuck again
status: active
last_updated: 2026-06-22
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# 🧠 M7 LOCAL MODEL & WORKLOAD-TIER PLAYBOOK

Goal: your machine never freezes mid-task again. Every job gets matched to a model it can actually
run, and the agent **checks resources before it starts** — so it routes to a small local model, a
cloud model, or just defers, instead of locking up. This is your Codex Resource Safeguard, made real.

> Today's lesson (2026-06-22): the disk hit 99% full → models couldn't load → Hermes stalled. Root
> cause was disk, not the model. This playbook fixes both: free the disk, and tier the workload.

---

## 🚨 PART 1 — DISK TRIAGE (do this first, it's why things froze)
Your C: had ~215 MB free and Google Drive ~204 MB. AI models need **gigabytes** of free space to load.

**IMPORTANT — why "Stream files" did NOT free space (2026-06-22):**
The vault is set up under Google Drive **"My PC / Computers" backup** ("Pineapple Contractors M7 — 28.4 GB,
syncing to Computers"). The **Stream vs Mirror toggle only affects "My Drive"** — it does nothing for a
"backup-my-computer-folder," which is always stored fully on the local disk. So streaming can't shrink it.
The only fix is to physically move the heavy media OUT of the local vault folder.

**The real big win — relocate `02_Media_Vault` (≈28 GB) off the local disk:**
1. Plug in an **external SSD/USB drive** (or use a drive with space).
2. **Move** the folder `C:\Pineapple Contractors M7\02_Media_Vault` to the external drive
   (e.g. `E:\Pineapple_Media_Vault`). Cut + paste — this frees ~28 GB on C: immediately.
3. The agents don't need the raw video inside the vault — they work from file *paths* and the
   `m7_media_index`. Keep a lightweight `02_Media_Vault/INDEX.md` in the vault pointing to the external
   location, and pull only the clips you're editing.
4. Alternatively, move `02_Media_Vault` into **"My Drive"** (not the Computers backup) and set My Drive to
   **Stream** — then the 28 GB lives in the cloud and streams on demand.

**Two-Google-account note:** if the folder is backed up under your **personal** account while also shared to
the **business** account, it can double-store and sync-fight. Pick ONE account (business:
saia@pineappleroofingllc.com) to own the vault backup; sign the other out of Google Drive Desktop or remove
its duplicate backup of this folder.

**Quick wins (a few more GB):**
- Delete the stray installers: `01_Command_Center/CursorUserSetup-x64-3.7.42.exe` (178 MB) and the
  `CursorUserSetup-x64-3.8.11.exe` in Downloads (187 MB). They're setup files you've already used.
- Empty the Recycle Bin. Clear `%TEMP%`. (Windows: search "Disk Cleanup".)
- The 39 GB `02_Media_Vault` is your unfair advantage — don't delete it. With Drive on "Stream," it
  lives in the cloud and you pull only the clips you're editing. Or keep a copy on a cheap external SSD.

**Rule going forward:** keep **at least 15–20 GB free** on C: at all times so models + temp files have room.

---

## 📊 PART 2 — THE WORKLOAD TIER MATRIX
Every task gets a tier. The agent picks the lightest model that can do the job well.

| Tier | Task type (examples) | Run on | Local model (Ollama) | Needs free |
|------|----------------------|--------|----------------------|-----------|
| **T0 · Reflex** | classify a lead, tag a card, route, yes/no | local tiny | `qwen2.5:0.5b` · `gemma2:2b` | ~2 GB |
| **T1 · Light** | a caption, a short summary, a review text, simple rewrite | local small | `llama3.2:3b` · `phi3:mini` | ~4 GB |
| **T2 · Mid** | a blog draft, FAQ page, code edit, a research brief | local mid *or* cloud | `qwen2.5-coder:7b` · `llama3.1:8b` | ~6–8 GB |
| **T3 · Heavy** | multi-agent Mastermind loop, big build, Kimi `/goal`, video, full campaign | **cloud only** | — (Minimax M3 / GLM / Claude) | cloud |

**Plain version:** small stuff → tiny local model. Medium stuff → mid local model *if there's room*,
else cloud. Anything with multiple agents, long autopilot, or rendering → **always cloud.** Your laptop
should never try to run the whole Mastermind swarm locally — that's what froze it.

---

## 🛡️ PART 3 — THE RESOURCE PRE-FLIGHT (the agent checks before it starts)
Before any T2 or T3 job, the agent runs a 3-second check and decides. This is the safeguard that
stops the freeze.

```
PRE-FLIGHT (before heavy work):
1. Free disk on C: ?   < 5 GB  → STOP. Alert Saia to free space (Drive Stream mode). Do not start.
2. Free RAM ?          tight   → drop one tier (use a smaller model) or route to cloud.
3. Task tier ?         T3      → route to cloud model. Never run multi-agent loops locally.
4. Cloud model down ?          → fall back to the largest local model that fits, at a lower tier,
                                  and tell Saia the output is a lighter draft.
```

**The Fallback Ladder (free-first):**
Cloud flagship (Minimax M3 / GLM 5.2 / Claude) → mid local (`qwen2.5-coder:7b`) →
small local (`llama3.2:3b`) → tiny local (`gemma2:2b`) → **defer + alert Saia.**
Never crash; always step down a rung and say so.

---

## 🤖 PART 4 — TEACH HERMES TO DO THIS (copy-paste, once)
Paste into Hermes so it self-manages model selection forever:
```
Save this as a permanent operating rule. Before starting any task, classify its workload tier:
T0 Reflex, T1 Light, T2 Mid, or T3 Heavy (multi-agent / build / autopilot / video).

Then run a resource pre-flight:
- If free disk on C: is under 5 GB, STOP and tell me to free space (Google Drive → Stream mode). Do
  not start heavy work on a near-full disk.
- T0/T1 → a small local Ollama model (gemma2:2b / llama3.2:3b). T2 → a mid local model
  (qwen2.5-coder:7b / llama3.1:8b) only if RAM allows, else cloud. T3 → always a cloud model.
- If the chosen model can't load or the session is busy, step down the fallback ladder
  (cloud → mid local → small local → tiny local → defer) and tell me which rung you used.

Always tell me one line: the tier, the model you picked, and free disk. Never freeze silently.
```

---

## ⚡ PART 5 — RECOMMENDED LOCAL ROSTER TO INSTALL (when disk is healthy)
Once you've freed space (15 GB+), install these so you always have a free local option:
```
ollama pull gemma2:2b          # T0/T1 reflex + light — tiny, fast
ollama pull llama3.2:3b        # T1 light drafts
ollama pull qwen2.5-coder:7b   # T2 code + FAQ pages (only if you have ~8GB free)
```
Keep heavy reasoning on the cloud. Local models are your **free fallback so you're never blocked**,
not your main workhorse.

---

## 🆘 QUICK FIX — "Hermes won't let me switch models"
The error "session busy — /interrupt the current turn before switching models" means a task is
mid-run. Type **`/interrupt`** in Hermes, wait for it to stop, THEN switch the model. After switching
off a tiny model (gemma:e2b) back to a flagship, re-issue your command.


<!-- M7-FIREWALL-EXEMPT: governance-reference -->
