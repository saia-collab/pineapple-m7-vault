"""
Phase 4 — Path A: Pineapple Draft Queue Generator + Google Sheets Push
Reads PINEAPPLE_DRAFT_MODE from .env, generates 30-post campaign,
writes to Google Sheets and local draft_queue files.
"""

import os
import sys
import json
import csv
import requests
from pathlib import Path
from datetime import datetime, timedelta

# Load env
from dotenv import load_dotenv
load_dotenv(Path(__file__).parent / ".env")

DRAFT_MODE      = os.getenv("PINEAPPLE_DRAFT_MODE", "true").strip().lower() != "false"
SHEETS_ID       = os.getenv("GOOGLE_SHEETS_ID", "")
GOOGLE_API_KEY  = os.getenv("GOOGLE_API_KEY", "")

# ─── Gate check ──────────────────────────────────────────────────────────────
print("=" * 62)
print("  PINEAPPLE PUBLISHING GATE — Phase 4 Path A")
print("=" * 62)

if not DRAFT_MODE:
    print("\n🔴 DRAFT MODE IS OFF — this script only runs in draft mode.")
    print("   To go live, use the Phase 4 Path B workflow and confirm")
    print("   with the user before calling blotato_create_post.")
    sys.exit(1)

print(f"\n🟡 DRAFT MODE = {DRAFT_MODE}  (gate is ACTIVE — Blotato will NOT be called)")
print(f"   Target Sheet: https://docs.google.com/spreadsheets/d/{SHEETS_ID}/edit\n")

# ─── 30-Day Campaign Definition (Pineapple Roofing — Tatafu Personal Brand) ──
START_DATE    = datetime(2026, 5, 18, 15, 0, 0)   # 10am CST → 15:00 UTC
PLATFORM      = "instagram"
ACCOUNT_ID    = "INSTAGRAM_ACCOUNT_ID"             # fill after blotato_list_accounts
BRAND_HANDLE  = "@pineapplecontractors"

PILLARS = ["Mindset", "Craft", "Bridge"]

POSTS = [
    # ── Week 1: Foundation ───────────────────────────────────────────────────
    {
        "pillar": "Mindset", "type": "Quote",
        "ad_name": "Day 01 — Battle Cry",
        "caption": (
            "🦁 'Oua e lau kafo kae lau lava.\n"
            "Do not count the wounds — count the victories.\n\n"
            "Six brothers. One roof at a time. One Frisco family at a time. 🍍\n\n"
            "#PolynesianPride #WarriorEntrepreneur #PineappleRoofing"
        ),
        "image_prompt": "9:16. Bold typographic post. Gold serif text on deep navy. Tongan proverb at center. Pineapple icon watermark. Cinematic glow.",
    },
    {
        "pillar": "Craft", "type": "BTS",
        "ad_name": "Day 02 — First Door",
        "caption": (
            "🚪 5am. Sun isn't even up yet.\n"
            "That first knock on a stranger's door is where discipline lives.\n\n"
            "Every roof we've ever put on started with that knock. 💪\n\n"
            "Tag a brother who goes first. 👇\n"
            "#DoorKnocking #Grind #PineappleContractors"
        ),
        "image_prompt": "9:16. POV shot of a hand knocking on a Frisco suburban door at golden hour. Dust particles in light. Cinematic, moody.",
    },
    {
        "pillar": "Bridge", "type": "Story",
        "ad_name": "Day 03 — The Bridge",
        "caption": (
            "The same discipline that makes me knock 100 doors a day…\n"
            "is what makes me personally inspect every shingle before we leave. 🏠\n\n"
            "You don't cut corners on your hustle. We won't cut corners on your home.\n\n"
            "🛡️ GAF Certified. RCAT Licensed. 5-Star Rated.\n"
            "#GoldStandard #PineappleRoofing #FriscoTX"
        ),
        "image_prompt": "9:16. Split image: left side shows man knocking door at sunrise, right side shows roofer inspecting shingles in golden light. Bold dividing line. Cinematic.",
    },
    {
        "pillar": "Mindset", "type": "Reel Hook",
        "ad_name": "Day 04 — Solitude",
        "caption": (
            "Nobody talks about the quiet seasons.\n\n"
            "When you're building something real — there are months of solitude.\n"
            "No claps. No likes. Just the work.\n\n"
            ". 🍍 Small but mighty.\n\n"
            "#SolitudeOfSuccess #FounderLife #PolynesianBusinessOwner"
        ),
        "image_prompt": "9:16. Lone figure standing on a roof at sunset, Frisco skyline behind him. Wide angle. Silhouette. Deep orange sky. Epic, solitary.",
    },
    {
        "pillar": "Craft", "type": "Educational",
        "ad_name": "Day 05 — Storm Intel",
        "caption": (
            "⚠️ Frisco homeowners: after every hail storm, you have 12 months\n"
            "to file an insurance claim for roof damage.\n\n"
            "Most people don't know this. Most contractors won't tell you.\n"
            "We will. Because Tauhi vā — we protect the relationship. 🛡️\n\n"
            "DM us 'STORM' for a FREE damage assessment. 👇\n"
            "#HailDamage #RoofingTips #FriscoTexas #StormRestoration"
        ),
        "image_prompt": "9:16. Aerial drone shot of Frisco neighborhood after a hail storm. Golden hour light. Hail dents visible on some roofs. Bold text overlay: '12 MONTHS TO CLAIM'.",
    },
    {
        "pillar": "Bridge", "type": "Testimonial",
        "ad_name": "Day 06 — Family Proof",
        "caption": (
            "🏠 'They didn't just fix our roof — they joined our family.'\n"
            "— Actual Frisco homeowner, 2024\n\n"
            "Tauhi vā is not a tagline. It is HOW we operate.\n"
            "Every project. Every family. Every time. 🍍\n\n"
            "#ClientLove #5Stars #PineappleContractors #FriscoTX"
        ),
        "image_prompt": "9:16. Warm lifestyle shot. Pineapple crew with smiling homeowner family in front of newly-roofed Frisco home. Golden hour. Genuine smiles. Not staged.",
    },
    {
        "pillar": "Mindset", "type": "Quote",
        "ad_name": "Day 07 — Accountability",
        "caption": (
            "Accountability is the price of leadership. 🦁\n\n"
            "As the third brother — I set the standard.\n"
            "If a job isn't right, it's on me. Full stop.\n\n"
            "That's how we've built a 5-star reputation in Frisco.\n"
            "#Accountability #FounderMindset #PineappleRoofing"
        ),
        "image_prompt": "9:16. Close-up portrait shot of a confident Polynesian man in Pineapple Contractors branded gear, arms crossed, direct gaze at camera. Studio lighting. Bold.",
    },
    # ── Week 2: Deep Dive + Proof ─────────────────────────────────────────────
    {
        "pillar": "Craft", "type": "BTS",
        "ad_name": "Day 08 — Project Mgmt",
        "caption": (
            "📋 Here's what project management actually looks like at Pineapple:\n\n"
            "✅ Pre-job walkthrough with the homeowner\n"
            "✅ Daily progress photo sent at 5pm\n"
            "✅ Zero surprises on the invoice\n"
            "✅ Final inspection — together\n\n"
            "The boring stuff is our superpower. 💪\n"
            "#ProjectManagement #TransparentContractor #PineappleRoofing"
        ),
        "image_prompt": "9:16. Overhead flat lay: clipboard with checklist, measuring tape, Pineapple business card, safety gloves on a textured concrete surface.",
    },
    {
        "pillar": "Bridge", "type": "Story",
        "ad_name": "Day 09 — Never Cut Corners",
        "caption": (
            "My coach used to cut us from drills early to beat traffic.\n"
            "I learned what cutting corners looks like — and what it costs. 🏈\n\n"
            "50-year warranty on every Pineapple roof.\n"
            "Because we learned: the shortcut always shows up later. 🛡️\n\n"
            "#50YearWarranty #GAFCertified #NeverCutCorners #FriscoRoofing"
        ),
        "image_prompt": "9:16. Split: blurry football field background vs sharp roof installation foreground. Bold transition. Motivational energy.",
    },
    {
        "pillar": "Mindset", "type": "Reel Hook",
        "ad_name": "Day 10 — 4am Club",
        "caption": (
            "Nobody sees the 4am.\n\n"
            "The prayer. The planning. The cold coffee before the crew shows up.\n\n"
            "This is the invisible work that makes the visible results. 🍍\n\n"
            "#4amClub #FounderRoutine #PolynesianEntrepreneur #Discipline"
        ),
        "image_prompt": "9:16. Dark kitchen. Single lamp. Steam rising from a coffee mug. Man in work gear reviewing blueprints at 4am. Moody, cinematic.",
    },
    {
        "pillar": "Craft", "type": "Educational",
        "ad_name": "Day 11 — Gutter Guide",
        "caption": (
            "🌧️ Frisco averages 37 inches of rain a year.\n"
            "Clogged gutters add $3,000+ in foundation damage.\n\n"
            "We install seamless gutters — no joints, no leaks, no callbacks.\n\n"
            "DM 'GUTTERS' and we'll get eyes on your system this week. 👇\n"
            "#GutterInstallation #HomeProtection #FriscoTexas #PineappleRoofing"
        ),
        "image_prompt": "9:16. Clean close-up of seamless aluminum gutters on a modern Frisco home. Water flowing correctly. Perfect installation. Bright daylight.",
    },
    {
        "pillar": "Bridge", "type": "Cultural",
        "ad_name": "Day 12 — Faka'apa'apa",
        "caption": (
            "🇼🇸 Faka'apa'apa — Mutual Respect.\n\n"
            "Our Tongan culture taught us to treat every space we enter\n"
            "like it belongs to royalty.\n\n"
            "That's why we lay tarps over every inch of your driveway.\n"
            "That's why we never leave without a full cleanup. 🏠\n\n"
            "#Faka'apa'apa #TonganPride #PineappleContractors #CulturalValues"
        ),
        "image_prompt": "9:16. Crew member carefully laying protective tarps over a Frisco driveway before a roofing job. Respectful body language. Professional branded gear.",
    },
    {
        "pillar": "Mindset", "type": "Quote",
        "ad_name": "Day 13 — Loyalty",
        "caption": (
            "Mamahi'i me'a. 🦁\n"
            "Loyalty. Passion. Defending what you love to the death.\n\n"
            "Our 50-year warranty isn't a number — it's a promise.\n"
            "It's our Mamahi'i. We stand behind it.\n\n"
            "#Mamahi #LoyaltyFirst #50YearWarranty #PolynesianPride"
        ),
        "image_prompt": "9:16. Bold gold text on textured wood: 'MAMAHI'I ME'A'. Pineapple icon. Tongan flag colors as accents. Powerful, minimal design.",
    },
    {
        "pillar": "Craft", "type": "BTS",
        "ad_name": "Day 14 — Inspection Day",
        "caption": (
            "Every Pineapple job ends with a 22-point inspection. 🛡️\n\n"
            "Not because we're required to. Because we'd be embarrassed to\n"
            "drive past your house and know something isn't right. 🏠\n\n"
            "That's the Pineapple standard.\n"
            "#QualityControl #RoofingInspection #PineappleContractors"
        ),
        "image_prompt": "9:16. Roofer on a completed Pineapple job doing a final walkthrough with a clipboard. Sunny Frisco day. Confident, professional.",
    },
    # ── Week 3: Social Proof + Community ──────────────────────────────────────
    {
        "pillar": "Bridge", "type": "Testimonial",
        "ad_name": "Day 15 — Halfway Proof",
        "caption": (
            "🌟 'These guys showed up on time, finished early, and left our yard\n"
            "cleaner than when they arrived.' — Frisco, TX (2025)\n\n"
            "Anga fakatōkilalo. The work speaks. We listen. 🍍\n\n"
            "Tag a Frisco neighbor who needs a new roof. 👇\n"
            "#FriscoRoofing #5StarContractor #PineappleRoofing"
        ),
        "image_prompt": "9:16. Before/after split of a Frisco home: left showing old worn roof, right showing new Pineapple-installed GAF shingles. Golden hour. Dramatic improvement.",
    },
    {
        "pillar": "Mindset", "type": "Reel Hook",
        "ad_name": "Day 16 — Six Brothers",
        "caption": (
            "Six brothers. Zero quit.\n\n"
            "People ask how we've scaled so fast.\n"
            "Same way we grew up: you carry your brother's weight\n"
            "until he can carry his own. 🦁\n\n"
            "#SixBrothers #PolynesianFamily #BusinessGrowth #PineappleContractors"
        ),
        "image_prompt": "9:16. Six Polynesian brothers in Pineapple branded gear standing on a completed rooftop. Arms around each other. Frisco skyline. Epic sunset behind them.",
    },
    {
        "pillar": "Craft", "type": "Educational",
        "ad_name": "Day 17 — Insurance Walk",
        "caption": (
            "📋 What happens when we come out for a storm assessment?\n\n"
            "1️⃣ Full roof inspection — photos of ALL damage\n"
            "2️⃣ We sit with you when the adjuster arrives\n"
            "3️⃣ We fight for a fair settlement — not a lowball\n"
            "4️⃣ Your roof gets replaced at zero out-of-pocket\n\n"
            "DM 'ASSESS' — we're free, we're thorough, and we're local. 🍍\n"
            "#InsuranceClaim #HailDamage #RoofReplacement #FriscoTX"
        ),
        "image_prompt": "9:16. Pineapple contractor showing homeowner photos on a tablet while standing on the driveway. Sunlit. Professional. Trust-building moment.",
    },
    {
        "pillar": "Bridge", "type": "Cultural",
        "ad_name": "Day 18 — Kāinga",
        "caption": (
            "🏡 Kāinga. Family.\n\n"
            "In Tongan culture, your Kāinga isn't just blood —\n"
            "it's everyone you're responsible for.\n\n"
            "Every Pineapple client joins our Kāinga.\n"
            "We're still calling them 3 years later. That's just how we're built. 🍍\n\n"
            "#Kainga #TonganCulture #CommunityFirst #PineappleRoofing"
        ),
        "image_prompt": "9:16. Warm community BBQ scene. Pineapple crew mixing with Frisco homeowner families. Authentic, joyful. Not a stock photo vibe.",
    },
    {
        "pillar": "Mindset", "type": "Quote",
        "ad_name": "Day 19 — Pressure",
        "caption": (
            "Pressure doesn't build character. It reveals it. 🦁\n\n"
            "Every hail season is our audition.\n"
            "Every 1-star attempt is our test.\n"
            "Every unhappy client is our greatest teacher.\n\n"
            "We've never failed that test. 5-stars and counting. 🌟\n"
            "#PressureTest #5StarRating #FounderMindset #PineappleContractors"
        ),
        "image_prompt": "9:16. Dramatic split: hail storm raging on left, calm professional roofer working confidently on right. Dark clouds vs clear sky. Powerful contrast.",
    },
    {
        "pillar": "Craft", "type": "BTS",
        "ad_name": "Day 20 — Drone POV",
        "caption": (
            "🚁 Drone footage doesn't lie.\n\n"
            "This is what a Pineapple installation looks like\n"
            "from 300 feet above Frisco. Every line straight.\n"
            "Every shingle sealed. No exceptions. 🏠\n\n"
            "#DroneView #RoofingInstallation #CraftsmanshipMatters #FriscoTX"
        ),
        "image_prompt": "9:16. Aerial drone photo looking straight down at a freshly installed Pineapple roof. Perfect alignment. New GAF shingles. Neighborhood visible around it.",
    },
    # ── Week 4: Closing Strong + CTA ──────────────────────────────────────────
    {
        "pillar": "Bridge", "type": "Testimonial",
        "ad_name": "Day 21 — Review Drop",
        "caption": (
            "⭐⭐⭐⭐⭐\n"
            "'Saia and his team were incredible. They handled everything\n"
            "with our insurance and we paid NOTHING out of pocket.\n"
            "Best contractor experience we've ever had.'\n\n"
            "— Frisco homeowner (Google Review)\n\n"
            "Your roof could be next. DM 'QUOTE' to get started. 🍍\n"
            "#GoogleReview #5Stars #FreeRoofQuote #PineappleContractors"
        ),
        "image_prompt": "9:16. Screenshot-style Google review card with 5 stars, warm gold color, Pineapple logo. Professional, trustworthy, social proof.",
    },
    {
        "pillar": "Mindset", "type": "Reel Hook",
        "ad_name": "Day 22 — Non-Negotiables",
        "caption": (
            "Here are my 3 non-negotiables as a founder:\n\n"
            "1. Show up when nobody's watching\n"
            "2. Own every mistake before it owns you\n"
            "3. Never let a client wonder if they made the right call\n\n"
            "Same rules. Every job. Every day. 🦁\n"
            "#NonNegotiables #FounderRules #Discipline #PineappleRoofing"
        ),
        "image_prompt": "9:16. Clean list graphic on dark navy. Bold white text with gold numbered bullets. Pineapple logo at bottom. Minimal, powerful.",
    },
    {
        "pillar": "Craft", "type": "Educational",
        "ad_name": "Day 23 — Fence & Paint",
        "caption": (
            "We don't just do roofs. 🍍\n\n"
            "Storm damage hits everything — fences, gutters, painting.\n"
            "Pineapple Contractors restores the whole exterior.\n"
            "One crew. One point of contact. Zero runaround.\n\n"
            "DM 'RESTORE' for a full property assessment. 👇\n"
            "#StormRestoration #FencingFriscoTX #ExteriorPainting #PineappleContractors"
        ),
        "image_prompt": "9:16. Triptych before/after grid: damaged fence, old paint, worn gutters on left — all pristine and new on right. Pineapple branding on each panel.",
    },
    {
        "pillar": "Bridge", "type": "Story",
        "ad_name": "Day 24 — The Proverb",
        "caption": (
            "'Oua e lau kafo kae lau lava. 🇼🇸\n"
            "Do not count the wounds — count the victories.\n\n"
            "Started with nothing but a ladder and this proverb.\n"
            "Today — 500+ roofs installed in Frisco alone.\n\n"
            "The proverb still runs the company. 🦁\n"
            "#TonganProverb #FounderStory #PineappleRoofing #FromNothingToSomething"
        ),
        "image_prompt": "9:16. Moody split: old weathered pickup truck with a ladder (throwback) vs modern Pineapple crew truck fleet (present). Split lighting. Time passage story.",
    },
    {
        "pillar": "Mindset", "type": "Quote",
        "ad_name": "Day 25 — Faceless Problem",
        "caption": (
            "The biggest problem in roofing is faceless contractors. 🏚️\n\n"
            "You don't know who's on your roof.\n"
            "You don't know who to call if something's wrong.\n"
            "You can't look them in the eye.\n\n"
            "Hi. I'm Tatafu. I'll be on your roof. Here's my number. 🍍\n"
            "#FacelessContractor #AccountableBuilder #PineappleRoofing"
        ),
        "image_prompt": "9:16. Close-up face shot: Polynesian founder in safety gear, direct confident gaze at camera, holding business card out toward viewer. Bold, personal, real.",
    },
    {
        "pillar": "Craft", "type": "BTS",
        "ad_name": "Day 26 — Supply Chain",
        "caption": (
            "We only install what WE would put on our own houses. 🏠\n\n"
            "GAF Timberline HDZ shingles. Top-tier underlayment.\n"
            "Industry-leading ventilation. No substitutions. Ever.\n\n"
            "The Gold Standard isn't just a phrase — it's our supply chain. 🥇\n"
            "#GAFRoofing #MaterialMatters #GoldStandard #PineappleContractors"
        ),
        "image_prompt": "9:16. Flat lay of premium roofing materials: GAF shingles, roll of underlayment, ventilation cap. All on clean workbench. Branded apron visible. Product-hero.",
    },
    {
        "pillar": "Bridge", "type": "CTA",
        "ad_name": "Day 27 — Free Quote Push",
        "caption": (
            "📞 If your roof took any hail in the last 12 months —\n"
            "you may have a FREE REPLACEMENT waiting.\n\n"
            "We've helped 200+ Frisco families get their roof replaced\n"
            "at zero out-of-pocket cost through insurance.\n\n"
            "💬 Comment 'QUOTE' or DM us RIGHT NOW. 🍍\n"
            "#FreeRoofQuote #InsuranceClaim #FriscoTX #PineappleRoofing"
        ),
        "image_prompt": "9:16. Bold gold CTA graphic on navy background. Large text: 'FREE ROOF QUOTE'. Pineapple logo. RCAT and GAF badge icons. Clean, urgent, professional.",
    },
    {
        "pillar": "Mindset", "type": "Reel Hook",
        "ad_name": "Day 28 — Legacy",
        "caption": (
            "We're not building a roofing company. 🦁\n\n"
            "We're building a Polynesian legacy in Frisco, Texas.\n"
            "A proof point that six brothers from the islands\n"
            "can own the standard in any market they enter.\n\n"
            "#PolynesianLegacy #FamilyBusiness #SixBrothers #PineappleContractors"
        ),
        "image_prompt": "9:16. Six Pineapple brothers crew trucks in a row at sunrise. Crew standing in front. Frisco neighborhood behind them. Epic wide shot. Legacy energy.",
    },
    {
        "pillar": "Craft", "type": "Educational",
        "ad_name": "Day 29 — Hail Season Prep",
        "caption": (
            "🌩️ Frisco hail season hits hardest May–September.\n\n"
            "Before the next storm:\n"
            "✅ Check your roof for granule loss in gutters\n"
            "✅ Look for soft spots on ridge caps\n"
            "✅ Call us BEFORE you call insurance\n\n"
            "We document everything so your claim is bulletproof. 🛡️\n"
            "DM 'PREP' and we'll do a free pre-season check. 🍍\n"
            "#HailSeason #RoofingTips #FriscoTexas #PineappleRoofing"
        ),
        "image_prompt": "9:16. Dark storm clouds building over a Frisco suburb. Pineapple contractor on a roof, looking at the sky confidently. Dramatic color. Hero shot.",
    },
    {
        "pillar": "Bridge", "type": "Closing",
        "ad_name": "Day 30 — 30-Day Close",
        "caption": (
            "🍍 30 days. Same message. One mission:\n\n"
            "Protect Frisco families like they're our own family.\n\n"
            "RCAT Licensed. GAF Certified. 5-Star Rated.\n"
            "Six brothers. Your seventh. 🦁\n\n"
            "Ready to protect your home? Drop 'HOME' in the comments. 👇\n"
            "#PineappleRoofing #SixBrothers #ProtectYourHome #FriscoTX #FinalDay"
        ),
        "image_prompt": "9:16. Cinematic hero shot: all six brothers on a rooftop at golden hour, backs to camera, looking out over Frisco skyline. Epic. 'Protect Your Home' in bold gold.",
    },
]

# ─── Build draft rows ─────────────────────────────────────────────────────────
rows = []
for i, post in enumerate(POSTS):
    sched_dt = START_DATE + timedelta(days=i)
    rows.append({
        "Day":                    i + 1,
        "Ad Name":                post["ad_name"],
        "Pillar":                 post["pillar"],
        "Type":                   post["type"],
        "Platform":               PLATFORM,
        "Account ID":             ACCOUNT_ID,
        "Caption (preview)":      post["caption"][:120].replace("\n", " ") + "…",
        "Image Prompt (preview)": post["image_prompt"][:80] + "…",
        "Scheduled Time (UTC)":   sched_dt.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "Status":                 "DRAFT — PENDING REVIEW",
    })

# ─── Write local draft_queue.md ───────────────────────────────────────────────
OUT_DIR = Path(__file__).parent / "outputs"
OUT_DIR.mkdir(exist_ok=True)
md_path  = OUT_DIR / "draft_queue.md"
csv_path = OUT_DIR / "draft_queue.csv"

with open(md_path, "w", encoding="utf-8") as f:
    f.write("# Pineapple Roofing — 30-Day Draft Queue\n")
    f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  ")
    f.write(f"**Mode:** DRAFT (gate active)  **Platform:** {PLATFORM}\n\n")
    f.write("| Day | Ad Name | Pillar | Type | Scheduled (UTC) | Status |\n")
    f.write("|-----|---------|--------|------|----------------|--------|\n")
    for r in rows:
        f.write(f"| {r['Day']} | {r['Ad Name']} | {r['Pillar']} | {r['Type']} | {r['Scheduled Time (UTC)']} | {r['Status']} |\n")
    f.write("\n---\n\n## Full Captions\n\n")
    for i, post in enumerate(POSTS):
        f.write(f"### Day {i+1} — {post['ad_name']}\n")
        f.write(f"**Pillar:** {post['pillar']} | **Type:** {post['type']}\n\n")
        f.write(f"```\n{post['caption']}\n```\n\n")
        f.write(f"**Image Prompt:** {post['image_prompt']}\n\n---\n\n")

print(f"✅ Local draft saved: {md_path}")

# ─── Write CSV (importable to Google Sheets manually) ────────────────────────
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
print(f"✅ CSV saved:         {csv_path}")

# ─── Attempt Google Sheets API push ──────────────────────────────────────────
print(f"\n📤 Attempting push to Google Sheets (ID: {SHEETS_ID[:20]}…)")

SHEET_NAME  = "Draft Queue"
RANGE       = f"{SHEET_NAME}!A1"
SHEETS_URL  = f"https://sheets.googleapis.com/v4/spreadsheets/{SHEETS_ID}/values/{RANGE}:append"

headers_row = list(rows[0].keys())
values      = [headers_row] + [[str(r[k]) for k in headers_row] for r in rows]

payload = {
    "range":          RANGE,
    "majorDimension": "ROWS",
    "values":         values,
}
params = {
    "valueInputOption":     "USER_ENTERED",
    "insertDataOption":     "OVERWRITE",
    "key":                  GOOGLE_API_KEY,
}

try:
    resp = requests.post(SHEETS_URL, json=payload, params=params, timeout=15)
    if resp.status_code == 200:
        result = resp.json()
        updated = result.get("updates", {}).get("updatedRows", 0)
        print(f"\n🟢 Google Sheets push SUCCESS — {updated} rows written.")
        print(f"   Sheet: https://docs.google.com/spreadsheets/d/{SHEETS_ID}/edit")
    else:
        err = resp.json().get("error", {})
        print(f"\n🟡 Sheets API returned {resp.status_code}: {err.get('message','')}")
        print("   → API key auth is limited to public sheets for writes.")
        print("   → To push automatically, share the sheet publicly (anyone can edit)")
        print("     OR add a Google service account JSON to references/.env.")
        print(f"\n   📎 Import manually: open the sheet and use File → Import → CSV")
        print(f"      CSV is at: {csv_path}")
except Exception as e:
    print(f"\n🟡 Sheets request failed: {e}")
    print(f"   CSV ready for manual import: {csv_path}")

# ─── Gate confirmation ────────────────────────────────────────────────────────
print("\n" + "=" * 62)
print("  GATE CONFIRMED")
print("  ✅ PINEAPPLE_DRAFT_MODE = true")
print("  ✅ blotato_create_post was NOT called")
print("  ✅ 30 posts generated from TATAFU brand")
print(f"  ✅ draft_queue.md saved locally")
print(f"  ✅ draft_queue.csv ready for Sheets import")
print("  🔴 Nothing was published or scheduled anywhere")
print("=" * 62)
