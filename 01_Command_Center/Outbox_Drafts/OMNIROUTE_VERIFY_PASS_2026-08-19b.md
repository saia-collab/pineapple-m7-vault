---
title: OmniRoute Verify + App Rewire — PASS receipt
status: PASS — verification + code change. Outbox Shield intact (app is PAUSED).
date: 2026-08-19
goal: "Read OMNIROUTE_BACKOFFICE_CONFIG_CHEATSHEET, verify OmniRoute :20128, test auto/best-chat, run brand_firewall, PASS receipt + wire the app's 4 buttons to free OmniRoute ($0)"
---

# 🍍 OmniRoute Verify + Gemini-App Rewire — PASS

## Part 1 — Verification
| Check | Result |
|---|---|
| Cheatsheet | ⚠️ not on disk → saved from your paste to `Playbooks/OMNIROUTE_BACKOFFICE_CONFIG_CHEATSHEET.md` (brand-fixed: combo `pm7-toa-free`→`pm7-free`; GLM/Z.ai flagged paid; Hermes model corrected to `oc/deepseek-v4-flash-free`) |
| OmniRoute `:20128/v1/models` | ✅ 200, 177 models |
| `auto/best-chat` routing (`stream:false`) | ✅ **live, $0** — routed to `big-pickle`, returned exact test string |
| CORS for local pages | ✅ `access-control-allow-origin` echoes page origin (POST allowed) |
| `brand_firewall.py` | ✅ PASS |

## Part 2 — App rewired to free OmniRoute
File: `Outbox_Drafts/Tools/2026-08-19_PM7_Google_Ecosystem_Map_Gemini_Studio_PAUSED.html`
| Button | Before (paid) | After (free, $0) |
|---|---|---|
| 1. Brand Scrubber | Gemini API | **OmniRoute** `auto/best-chat` |
| 2. Storm/AEO Lead | Gemini + Search Grounding | **OmniRoute** (grounding removed — paid-only) |
| 3. Voice Briefing | Gemini TTS (paid) | **Browser Web Speech API** (free, offline) |
| 4. 50/5/3 Video Spec | Gemini API | **OmniRoute** `auto/best-chat` |

**Verified:** 0 Gemini calls remain · `callOmniRoute` used 4× · `speechSynthesis` wired · no API key needed · brand_firewall scan_text = **0 violations**.

**Live-test note:** the in-preview click is blocked by the preview sandbox (`data:`/mixed-content can't reach `http://localhost`). Routing itself is proven by curl. **To test for real:** open the HTML in Chrome/Edge on this PC with the Studio running → tab "Gemini AI Interactive Studio" → click a preset → **Scrub & Brand-Check**. Output = $0.

**STATUS: PASS — PAUSED.** No publish, no spend.

<!-- M7-FIREWALL-EXEMPT: verification receipt -->
