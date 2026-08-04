---
type: sop
title: M7 Social SOP — Google Drive → Blotato → All Platforms
status: active
last_updated: 2026-07-17
rule: Nothing auto-posts. Everything schedules PAUSED/DRAFT until Saia hits GO (Outbox Shield).
---

# 🔁 The Social Machine — Drive → Caption → Blotato → Post

**One sentence:** *Media lives in Drive → captions live in the vault (firewall-clean) → Blotato pairs them and schedules → you approve → it posts to every platform at once.*

## 📂 Step 1 — Google Drive: organize the media (do once, then maintain)
Structure the 39GB so any post is a 30-second grab:
```
/PINEAPPLE_MEDIA/
  /01_READY_TO_POST/      ← trimmed clips + edited photos, post-ready
  /02_RAW_FOOTAGE/        ← unedited from the field
  /03_BEFORE_AFTER/       ← paired shots (your best converter)
  /04_TEAM_FAMILY/        ← crew, culture, recruitment
  /05_BY_CITY/            ← Frisco / Lewisville / Plano… (for local posts)
```
**Rule:** only pull from `01_READY_TO_POST`. If it's not trimmed + cleared, it doesn't post.
**Field-to-Drive:** crew uploads phone clips to `02_RAW` same day → you (or the editor) move keepers to `01_READY`.

## ✍️ Step 2 — Caption (already done for you)
Captions live in: `Outbox_Drafts/Content/Social_CaptionPack_Week_AllPlatforms.md`
Every post = HOOK → VALUE → ONE CTA, firewall-clean. **Fill any [BRACKETS]** (city/neighborhood) before scheduling.

## 📤 Step 3 — Blotato: pair media + caption, schedule to ALL platforms
Blotato posts to IG, FB, TikTok, LinkedIn, X, Pinterest, YouTube in one shot.
1. **Upload media** — drag from Drive `01_READY_TO_POST`, or import the Drive share-link.
2. **Paste the caption** from the pack (use the platform-specific variant — IG copy ≠ LinkedIn copy).
3. **Pick platforms** — select all connected accounts.
4. **Schedule, don't publish** — set the time; leave it queued. (Cadence below.)
5. **You review the queue → hit GO.** Never let it fire unreviewed.

## 🗓️ Weekly cadence (5 posts = full week, no new filming)
| Day | Post type (from the pack) | Best platforms |
|---|---|---|
| Mon | Post 3 — Education/authority | FB, LinkedIn, Pinterest |
| Tue | Post 1 — Storm hook | IG, FB, TikTok |
| Wed | Post 4 — Local/neighborhood | IG, FB, city-tagged |
| Thu | Post 5 — Recruitment | TikTok, IG, LinkedIn |
| Fri | Post 2 — Story/trust | all |
**Storm override:** if hail hits, that day's post is bumped for the Storm Playbook post — same day, both GBP profiles too.

## ✅ Pre-post checklist (30 seconds)
- [ ] Media from `01_READY_TO_POST` only
- [ ] Caption is the correct platform variant
- [ ] No banned words · phone + CPPA present · zero green
- [ ] Brackets filled
- [ ] Scheduled (not live) → queued for Saia's GO

## 🤖 Who does what
- **Captions / voice copy** → Claude (this session). No cap, knows the firewall.
- **Bulk / overflow** → GLM (OmniRoute) or Hermes-MoA.
- **Scheduling + cross-post** → Blotato.
- **The handshake** → the family. Never automate that.

<!-- M7-FIREWALL-EXEMPT: sop -->
