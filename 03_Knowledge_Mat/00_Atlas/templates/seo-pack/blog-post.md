---
name: blog-post
description: Write 5 unique SEO-optimised blog posts and deploy to all 5 of your websites. Optimised for CTR, conversions, and multi-video engagement.
user_invocable: true
status: reference_only_security_review_required
---

> **PM7 SECURITY HOLD — 2026-08-22:** This third-party template is reference-only. Its prior committed API credential must be rotated, and its five-site mass-deploy/cross-link workflow is not approved for Pineapple. Adapt useful research and drafting ideas to the current PM7 SEO SOP; never run its publishing, indexing, or network-link steps without a separate review and Saia's explicit GO.

# 🎯 BEFORE YOU USE THIS — CUSTOMISE 4 THINGS

This is the working skill Julian Goldie uses inside AIPB to publish to 5 sites at once.

Search this file for `{{TODO}}` markers — there are 4 spots you must edit.

## 1. Your transcripts folder

Search for `{{TODO_TRANSCRIPTS_PATH}}` and replace with the absolute path to your main site's `.claude/transcripts/` folder.

Example: `/Users/yourname/my-main-site/.claude/transcripts/`

## 2. Your brand voice

Search for `{{TODO_BRAND_VOICE}}` and paste 3-4 paragraphs of your actual writing.

Pull from your best blog posts. Pull from your tweets. Pull from your YouTube descriptions.

Claude reads this and copies your style.

## 3. Your video library

Search for `{{TODO_VIDEO_LIBRARY}}` and list your existing YouTube videos.

Format each as: `slug-name → YOUTUBE_VIDEO_ID → "Exact YouTube Title"`.

When Claude writes about a topic, it picks 2-3 of your videos to embed.

## 4. Your 5 sites

Search for `{{TODO_SITES}}` and list your 5 site IDs + names + URLs.

These must match the IDs in `seoPipeline.ts.template`.

---

# Blog Post Creator — 5-Site Deployment

Every blog post gets published to **all 5 sites** with **unique content** on each. Optimised for click-through rate, dwell time, and conversion.

## Step 0: Brand voice — REQUIRED CONTEXT

Before writing anything, internalise this brand voice. Every post must read in this voice.

{{TODO_BRAND_VOICE}}

Example: short punchy sentences. UK English. Direct. 3rd-grade reading level. No filler. Confident tone. Every paragraph ends with a benefit, not a fact.

## Step 0.5: Your video library

When writing a post, look at this library and embed 2-3 relevant videos.

{{TODO_VIDEO_LIBRARY}}

Example format:
- hermes-desktop-app → dQw4w9WgXcQ → "Hermes Desktop App — Full Walkthrough"
- openclaw-mission-control → abc123xyz → "OpenClaw Mission Control Demo"

## Step 0.6: Your 5 sites

Each post gets published to all 5. Pick a different CTR formula for each site.

{{TODO_SITES}}

Example:
- site1 → bestaiagentcommunity.com → "Specific Number + Result" formula
- site2 → aiprofitboardroom.com → "vs Competitor" formula
- site3 → mybrand.com → "Year + Update" formula
- site4 → another.com → "How To + Outcome" formula
- site5 → fifth.com → "Why X Beats Y" formula

---


# Blog Post Creator — 5-Site Deployment

Every blog post gets published to **all 5 sites** with **unique content** on each. Optimised for click-through rate, dwell time, and conversion.

## Step 1: Get the keyword and video transcript

Ask the user: **"What keyword do you want me to target?"**

Wait for their answer before proceeding.

**CRITICAL: Transcripts are the source of truth.** Check `{{TODO_TRANSCRIPTS_PATH}}/<slug>.txt` for the video transcript. If one exists, base every article on that transcript — specific features, numbers, examples, and terminology must come from the transcript, not invented. If no transcript exists, ASK the user to paste it before writing anything.

## Step 2: Embed multiple videos per article (NEW)

**CRITICAL: Each article should have 2-3 video embeds where relevant** — not just one.

- **Primary video** near the top (after the lede, before the first H2) — the main video for THIS keyword.
- **1-2 supporting videos** woven into the body where they add value — older Julian videos that fit the topic. Place them inside relevant H2 sections, not all at the top.

Look at the transcripts folder + previously deployed posts to find related videos to reuse:
- For Hermes content → link related Hermes videos (hermes-desktop-app, hermes-webui, ollama-hermes, hermes-agent-swarm, hermes-workspace, hermes-second-brain, etc).
- For OpenClaw content → link openclaw-computer-use, clawx-openclaw, openclaw-aionui, openclaw-mission-control, etc.
- For SEO content → link claude-code-seo-agent, reddit-seo-ai-content, how-to-rank-in-google-ai-mode.
- For tool comparisons → link agent-zero-vs-openclaw, accomplish-vs-openclaw, kimi-2-6-benchmark.

Use this iframe block for every embed (no wrapper div — raw iframe renders correctly):

```html
<iframe width="848" height="485" src="https://www.youtube.com/embed/VIDEO_ID" title="EXACT YOUTUBE VIDEO TITLE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

Use the exact YouTube title string for the title attribute. After deploy, curl the live URL and grep for the video ID to verify each iframe rendered.

### Special: AI Profit Boardroom embeds

For articles ABOUT the AI Profit Boardroom (julian-goldie-ai-profit-boardroom-reviews, ai-profit-boardroom keywords), embed BOTH:

```html
<iframe title="vimeo-player" src="https://player.vimeo.com/video/1052659405?h=14cfc74d5a" width="848" height="485" frameborder="0" referrerpolicy="strict-origin-when-cross-origin" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media; web-share" allowfullscreen></iframe>
```

```html
<iframe width="848" height="485" src="https://www.youtube.com/embed/uNK6GKIiUpI" title="BREAKING: NEW AI News Announcement…" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
```

## Step 3: CTR-optimised meta titles + descriptions (NEW — CRITICAL)

Treat meta titles like YouTube headlines. The goal is CLICKS in the search results, not just SEO keyword fit. Each of the 5 articles per keyword must have a different CTR-style title.

### Direct response title formulas to use

Pick a different formula for each of the 5 sites:

1. **Specific number + result + timeframe** — "Hermes Just Got 10X Smarter (Complimentary Update)"
2. **Curiosity gap + contrast** — "Why I Quit OpenClaw For Accomplish (Honest)"
3. **Personal pronoun + result** — "How I Built A 50-Page SEO Site With Hermes"
4. **Bold claim + proof** — "Hermes Beats Claude In 2026 (Tested)"
5. **Question + payoff** — "Is Accomplish Better Than OpenClaw? My Test"

### Title rules

- 50-60 chars max for SERP visibility.
- Include the target keyword naturally.
- Use power words: Complimentary, New, Insane, Crazy, Real, Honest, Tested, Why, How, Best.
- Numbers and brackets work — "(2026)", "(Complimentary)", "(Tested)".
- AVOID generic descriptive titles like "Guide to X" or "How To Use X".
- UK grammar still applies (optimise, colour) — but keep punchy direct response feel.

### Meta description rules

- 140-155 chars max.
- Lead with the result/payoff, not the explanation.
- Include keyword early.
- End with curiosity hook or specific number.
- Example: "Hermes second brain setup makes your AI agent 10X smarter. Complimentary Obsidian + OMI integration. 5-minute setup, real memory, no token limits."

## Step 4: Write FIVE unique articles

Write 5 completely different long-form SEO blog posts for the same keyword.

**CRITICAL: All 5 articles must be unique.** Same keyword, but each has different title, opening, structure, examples, FAQs.

### Author Voice — Julian Goldie (FULL BIO BLOCK — use as source context)

Write as **Julian Goldie**, an SEO entrepreneur, author, and online educator. He's the founder of a successful 7-figure link building agency with a team of 50 people, which he built from the ground up. Julian is also a thought leader in the field of AI and SEO. He has released two best-selling books on Amazon, "SEO Link Building Mastery" and "Agency Marketing Mastery." His Udemy courses have attracted over 50,000 students and he has over 70,000 subscribers on YouTube.

When relevant, weave in references to:

- **Mastermind / SEO Elite Circle** — `https://go.juliangoldie.com/buy-mastermind`
- **Complimentary SEO Strategy Session** — `https://go.juliangoldie.com/strategy-session`

These are higher-tier upsells beyond the AI Profit Boardroom and Complimentary AI Money Lab community CTAs. Use them in articles where SEO mastery, agency growth, or 1:1 strategy makes sense — not in every post.

### Tone + Voice Rules (PREFERRED STYLE — use this on every post)

- **Tone: Alex Hormozi style** — direct, no fluff, no formal language, every sentence earns its place.
- **1st person throughout** ("I", "my", "I've found that…").
- **UK grammar** (optimise, colour, favourite, organisation, etc.).
- **Conversational** — like sharing insights with a friend over coffee.
- **Keep it real, keep it fresh, keep it engaging.**
- **No fluff, nothing cringe, keep it neutral.**
- **Sprinkle in stories and examples** — like sharing insights over coffee with a pal.
- **Plain talk** — skip the tech jargon unless it's what everyone's already chatting about. Simplify language wherever possible.
- **Kick off with real questions and worries** the audience actually has.

### SEO Structure

- **Keyword in the very first line** of the article.
- **Keyword in the very last line** of the article.
- **Keyword in H2/H3 headings** naturally.
- Sprinkle **semantically relevant keywords + LSI terms** throughout.
- Include **FAQ section** with 4-6 questions using the keyword and related terms.
- Use clear **H2 and H3 headers** to break up sections.

### Formatting Rules — JULIAN'S PREFERRED STYLE (sentence-per-line, NOT fragment-per-line)

**The rule: every COMPLETE sentence on its own line. Never a fragment.**

This is Julian's preferred Hormozi-style rhythm — short visual breaks, punchy delivery, but every line must be a real sentence with subject + verb. Lines stack to form a coherent flowing argument. Visually broken up, but reads as real prose.

**❌ FORBIDDEN (the fragment-per-line poetry style):**

```
Three reasons.

1 — Multi-agent = parallel build
Solo founder = small team output.

2 — Browser integration = real test
No more "looks ok in dev."
```

That reads like a poem and the user explicitly hates it.

**✅ JULIAN'S PREFERRED STYLE — every sentence on a new line, but each line is a real sentence:**

```
There are three reasons Antigravity matters for solo founders.

First, multi-agent workflows give you parallel output that used to need a real dev team.

One agent builds the UI while another writes tests and a third fixes bugs — all concurrent.

That's team-level velocity from one person.

Second, the browser integration means agents actually test what they build.

They click through the app, take screenshots, and verify it works before handing back.

No more "looks fine in dev" surprises that bite you in production.

Third, the mission control view shows what every agent is doing in real time.

You manage like a team lead instead of micro-prompting one model at a time.
```

Notice every line is a complete sentence. Every line could stand on its own. They stack to form a flowing paragraph in spirit, but visually each sits on its own line for that Hormozi rhythm.

**Hard rules:**

1. **Every line must be a complete sentence with subject + verb.** NEVER a fragment like "Three." or "Five reasons." or "1 — X = Y" or "More stars = more contributors."
2. **Each sentence gets its own line** — that's Julian's preferred visual rhythm. Skip the dense-paragraph approach.
3. **For lists, write full bullet items as complete sentences.** "Solo founders go from 1 feature per week to 3-5" — not "1 feature/week → 3-5/week."
4. **Subheadings are full claims or questions.** "Why Antigravity matters for solo founders" — not "Three reasons."
5. **Numbered sections get real explanation sentences after the heading**, each on its own line. Not a 4-word fragment.
6. **Hormozi tone is DIRECT and PUNCHY** — but punchy ≠ fragment. "This is the highest-leverage tool I've used this year" is punchy. "Highest leverage tool." is broken.
7. **Bullet points, bold highlights, tables** for skim-ability — but each bullet/cell must be a complete thought, not a stub.
8. **UK grammar** (optimise, colour, organisation, favourite).
9. Aim for **2,000-3,000 words** of actual sentences (broken into single-line rhythm), not 800 words of fragments.

### Quick mental test before saving

Look at a randomly chosen line in your draft. Could it stand alone as a sentence in any context? If yes, ship it. If it's a stub like "Three." or "More leverage." or "Complimentary.", rewrite it into a full sentence. Even short sentences are fine ("That's the unlock.") — but they have to be sentences.

### Content Style

- Kick off with **real questions and worries** the audience faces.
- Sprinkle in **stories and examples** like sharing over coffee.
- No fluff — every sentence earns its place.
- Aim for **2,000-3,000 words** for SEO depth.

### Single-Article Mode (when user provides keyword + outline directly)

The user sometimes asks for a single SEO-optimised article (not the full 5-site batch) using this exact template format:

```
KEYWORD = <keyword>
Content Outline = <headings + outline>
```

When this template arrives, deliver ONE article (not five) following the SOURCE CONTEXT bio block above. Single-article mode skips the multi-site deploy + Omega Indexer + sheet TSV steps. Just write the article and present it for the user to copy. Mention upsell links when topically relevant:

- Mastermind / SEO Elite Circle: `https://go.juliangoldie.com/buy-mastermind`
- Complimentary SEO Strategy Session: `https://go.juliangoldie.com/strategy-session`

Use the same prose style rules (every line a complete sentence, no fragments, Hormozi-direct, UK grammar, 1st person, FAQs at the end, keyword in first AND last line, keyword in headings).

## Step 5: Conversion optimisation elements

Beyond keyword optimisation, every article must have:

### Above-the-fold conversion hooks

- Strong opening line that's a benefit-led claim, not a generic intro.
- Result-focused first paragraph (numbers, specific outcomes).
- First CTA visible within the first 30% of the article.

### Trust signals throughout

- Member counts: "2,800+ members already using this".
- Specific results: "12,700 clicks in 28 days".
- Testimonial-style snippets where authentic.
- Course mentions: "6-hour OpenClaw course", "2-hour Hermes course".

### Visual hierarchy for scannability

- Use callout blockquotes (>) for key CTAs.
- Bold key benefits in lists.
- Section breaks every 200-300 words.
- Tables for comparisons where they fit.

### CRITICAL: Every URL must be wrapped in markdown link syntax

Bare URLs are NOT auto-linked by Eleventy's default markdown renderer. They render as plain text and KILL conversion. ALWAYS wrap external links.

**Wrong (plain text):**
```
📺 Video notes + links to the tools 👉 https://www.skool.com/ai-profit-lab-7462/about
```

**Right (markdown link):**
```
📺 [Video notes + links to the tools 👉](https://www.skool.com/ai-profit-lab-7462/about)
```

This applies to:
- All Skool URLs.
- All aiprofitboardroom.com URLs.
- All goldie.agency URLs.
- ANY external URL in body text.
- Footer CTAs especially (these get the most clicks).

The standard footer block at the bottom of every post must use this exact wrapped format:

```markdown
📺 [Video notes + links to the tools 👉](https://www.skool.com/ai-profit-lab-7462/about)

🎥 [Learn how I make these videos 👉](https://aiprofitboardroom.com/)

🆓 [Get a Complimentary AI Course + Community + 1,000 AI Agents 👉](https://www.skool.com/ai-seo-with-julian-goldie-1553/about)
```

Internal blog links (relative URLs like `/blog/post-slug/`) already use markdown syntax and are fine.

### Required CTAs (4 minimum, personalised)

**1. Main CTA** (use 2-3 times, personalised to topic): → https://www.skool.com/ai-profit-lab-7462/about

Reference the SPECIFIC thing the reader learned about. Mention what's inside the Boardroom relevant to THIS topic. Mention: step-by-step tutorials, weekly coaching calls, 2,800+ members, the specific section/course relevant.

**2. Video notes + tools**: "Video notes + links to the tools 👉" → https://www.skool.com/ai-profit-lab-7462/about

**3. Learn how I make these videos**: "Learn how I make these videos 👉" → https://aiprofitboardroom.com/

**4. Complimentary AI Course CTA**: "Get a Complimentary AI Course + Community + 1,000 AI Agents 👉" → https://www.skool.com/ai-seo-with-julian-goldie-1553/about

**CTA formatting (use this styled box):**
```markdown
> **🔥 Want the exact setup I used to get these results?**
> Inside the [AI Profit Boardroom](https://www.skool.com/ai-profit-lab-7462/about), I've got a full [TOPIC] section with step-by-step video tutorials. Plus weekly coaching calls + 2,800+ members building real automations.
> **[→ Get access here](https://www.skool.com/ai-profit-lab-7462/about)**
```

### Front Matter Template

```yaml
---
title: "[Direct response, CTR-optimised — max 60 chars with keyword]"
description: "[Result-led, payoff-first — max 155 chars with keyword]"
category: "[Relevant category]"
date: [today's date YYYY-MM-DD]
keywords: "[target keyword, related terms, LSIs]"
author: "Julian Goldie"
---
```

## Step 5b: Schema markup (NEW)

Add JSON-LD schema to every post for rich snippets in Google + AI search results. Insert near the top of the markdown body (before the first H2 but after the iframe):

### Article schema

For all blog posts:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "[POST TITLE]",
  "description": "[POST META DESCRIPTION]",
  "author": {
    "@type": "Person",
    "name": "Julian Goldie",
    "url": "https://aiprofitboardroom.com/",
    "sameAs": [
      "https://www.youtube.com/@juliangoldieseo",
      "https://x.com/JulianGoldieSEO"
    ]
  },
  "publisher": {
    "@type": "Organization",
    "name": "[SITE NAME]",
    "url": "[SITE URL]"
  },
  "datePublished": "[YYYY-MM-DD]",
  "image": "[OG IMAGE URL or default]"
}
</script>
```

### FAQ schema

For posts with an FAQ section, also add:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[FAQ QUESTION 1]",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[FAQ ANSWER 1]"
      }
    }
    // ... include all 4-6 FAQs
  ]
}
</script>
```

### Review schema

For review-style posts (e.g. AI Profit Boardroom reviews, comparison posts):

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Review",
  "itemReviewed": {
    "@type": "[Product or SoftwareApplication or Service]",
    "name": "[ITEM NAME]"
  },
  "author": {
    "@type": "Person",
    "name": "Julian Goldie"
  },
  "reviewRating": {
    "@type": "Rating",
    "ratingValue": "[1-5]",
    "bestRating": "5"
  },
  "reviewBody": "[1-2 SENTENCE SUMMARY]"
}
</script>
```

These render correctly inline in Eleventy markdown — they're treated as raw HTML.

## Step 5c: Author bio block (NEW)

Add an author bio block near the end of every post (just before "Related reading" or after the FAQ). Builds E-E-A-T signals + reader trust + brand connection.

Standard bio block format:

```markdown
## About Julian

I'm Julian Goldie — AI entrepreneur, SEO expert, and founder of the [AI Profit Boardroom](https://www.skool.com/ai-profit-lab-7462/about) (2,800+ members). I help business owners scale with AI agents, automation, and SEO.

- 282K+ YouTube subscribers
- 7-figure AI agency (Goldie Agency)
- Daily training inside the Boardroom
- Author of multiple AI automation playbooks

[→ Get my best AI training inside the AI Profit Boardroom](https://www.skool.com/ai-profit-lab-7462/about)
```

Put this in EVERY new post. Treat it as a recurring trust block.

## Step 5d: Comparison tables (NEW)

For comparison-style posts (vs posts, "best of" lists, feature breakdowns), use HTML tables instead of markdown bullets where they fit.

### Why HTML tables over markdown bullets

- Tables show better in SERP rich results (sometimes pull as featured snippets).
- Better scannability for readers.
- Cleaner conversion when comparing pricing/features.

### Table format to use

```markdown
| Feature | Tool A | Tool B |
|---------|--------|--------|
| Setup time | 2 min | 30 min |
| Cost | Complimentary | Complimentary |
| Reliability | High | Medium |
| Best for | Beginners | Power users |
```

Eleventy renders markdown tables natively.

For richer tables (with images, links, or styling), use raw HTML:

```html
<table>
  <thead>
    <tr><th>Feature</th><th>Tool A</th><th>Tool B</th></tr>
  </thead>
  <tbody>
    <tr><td>Setup time</td><td>2 min</td><td>30 min</td></tr>
    <tr><td>Cost</td><td>Complimentary</td><td>Complimentary</td></tr>
  </tbody>
</table>
```

### When to add tables

- Always for "vs" posts.
- Always for "best of" lists.
- Always for pricing comparisons.
- Optional for feature-heavy posts.

If the article is purely a tutorial or guide, tables are optional.

## Step 6: Internal links to related previous articles

**CRITICAL: Every new article must naturally link to 2-4 related previous articles on the SAME site.**

### Before writing, glob existing posts on each site

- `/Users/juliangoldie/AIProfitBoardroom.com/src/blog/posts/`
- `/Users/juliangoldie/AIProfitBoardroom-main/src/blog/posts/`
- `/Users/juliangoldie/juliangoldieaiautomation/src/blog/posts/`
- `/Users/juliangoldie/aisuccesslab/src/blog/posts/`
- `/Users/juliangoldie/aimoneylab/src/blog/posts/`

### Interlink rules

- **Link to posts on the SAME site only**.
- **Use natural anchor text** — not "click here".
- **Weave links into the body naturally** — mid-sentence or end of paragraph.
- **Link format:** `[anchor text](/blog/post-slug/)` (relative URL, no domain).
- **Pick the 2-4 MOST relevant prior posts**.
- **Add a small "Related reading" section near the end** with 2-3 related links.

## Step 7: Save and deploy to ALL 5 sites

Save markdown to each site's posts folder, build with Eleventy, deploy to Netlify in parallel.

### Sites

| Site | Folder | Deploy |
|------|--------|--------|
| bestaiagentcommunity.com | /Users/juliangoldie/AIProfitBoardroom.com | `cd ... && npx @11ty/eleventy && netlify deploy --prod --dir=_site` |
| aiprofitboardroom.com | /Users/juliangoldie/AIProfitBoardroom-main | same pattern |
| juliangoldieaiautomation.com | /Users/juliangoldie/juliangoldieaiautomation | same pattern |
| aisuccesslabjuliangoldie.com | /Users/juliangoldie/aisuccesslab | same pattern |
| aimoneylabjuliangoldie.com | /Users/juliangoldie/aimoneylab | same pattern |

Run all 5 deploys in parallel using Bash `run_in_background`.

### Verify after deploy

- Curl each live URL and grep for video ID to confirm iframe rendered.
- For multi-video articles, grep for ALL embedded video IDs.

## Step 8: Submit URLs to Omega Indexer (API — always)

After all 5 sites are deployed, submit URLs to Omega Indexer via the API. NEVER use Chrome MCP — the API is faster, scriptable, and survives Chrome being disconnected.

### API key (do not commit to public repos)

```
OMEGA_INDEXER_API_KEY=${OMEGA_INDEXER_API_KEY}
```

Also stored at `/Users/juliangoldie/.omega-indexer.env` for shell sourcing.

### API endpoint

```
POST https://app.omegaindexer.com/api/omega-indexer-api
Content-Type: application/x-www-form-urlencoded
```

### Form-encoded body fields

| Field | Value |
|-------|-------|
| `apikey` | API key from Omega Indexer dashboard |
| `campaignname` | URL-encoded campaign name |
| `urls` | URL-encoded list of URLs separated by `\|` |
| `dripfeed` | Number of days (use `0` for No Drip Feed) |

### Submit a single campaign

```bash
KEY="${OMEGA_INDEXER_API_KEY}"
SLUG="example-keyword"
NAME="$SLUG - $(date +%B\ %Y)"

# Pipe-separated URL list
URLS=$(printf '%s|%s|%s|%s|%s' \
  "https://bestaiagentcommunity.com/blog/$SLUG/" \
  "https://aiprofitboardroom.com/blog/$SLUG/" \
  "https://juliangoldieaiautomation.com/blog/$SLUG/" \
  "https://aisuccesslabjuliangoldie.com/blog/$SLUG/" \
  "https://aimoneylabjuliangoldie.com/blog/$SLUG/")

curl -X POST "https://app.omegaindexer.com/api/omega-indexer-api" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "apikey=$KEY" \
  --data-urlencode "campaignname=$NAME" \
  --data-urlencode "dripfeed=0" \
  --data-urlencode "urls=$URLS"
```

### Bulk submit multiple keywords

```bash
KEY="${OMEGA_INDEXER_API_KEY}"
MONTH=$(date +%B\ %Y)

for slug in keyword-1 keyword-2 keyword-3; do
  NAME="$slug - $MONTH"
  URLS=$(printf '%s|%s|%s|%s|%s' \
    "https://bestaiagentcommunity.com/blog/$slug/" \
    "https://aiprofitboardroom.com/blog/$slug/" \
    "https://juliangoldieaiautomation.com/blog/$slug/" \
    "https://aisuccesslabjuliangoldie.com/blog/$slug/" \
    "https://aimoneylabjuliangoldie.com/blog/$slug/")

  echo "Submitting: $slug"
  curl -sX POST "https://app.omegaindexer.com/api/omega-indexer-api" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    --data-urlencode "apikey=$KEY" \
    --data-urlencode "campaignname=$NAME" \
    --data-urlencode "dripfeed=0" \
    --data-urlencode "urls=$URLS"
  echo
  sleep 1
done
```

Each campaign costs 5 credits (1 per URL). Top up before bulk submitting if low.

### Official Omega Indexer API documentation (verbatim)

This is the official documentation from `https://app.omegaindexer.com/api/omega-indexer-api` (only visible when logged in). Captured here so future runs don't need to re-verify.

```
OMEGA Indexer
API Documentation

HTTP POST
https://www.omegaindexer.com/amember/dashboard/api
(redirects 307 → https://app.omegaindexer.com/api/omega-indexer-api — call the new URL directly to skip the redirect)

HEADERS
Content-Type: application/x-www-form-urlencoded

POST BODY EXAMPLE
apikey=KOSIDkjsdjaoisO&campaignname=campaign%20name%20test&dripfeed=2&urls=http%3A%2F%2Fexample.com%7Chttp%3A%2F%2Ftest.com

PARAMETERS
| Parameter      | Value                                                                  |
|----------------|------------------------------------------------------------------------|
| apikey         | API KEY from Omega Indexer Dashboard                                   |
| campaignname   | URL-encoded campaign name for user to visually see in dashboard        |
| urls           | URLs separated with `|`. Final parameter should be URL-encoded         |
| dripfeed       | Days (integer; 0 = no drip feed)                                       |

RESPONSE
HTTP 200 with body `"done"` on success.
```

### Verified behaviour (from real submissions)

- Hitting the `www.omegaindexer.com/amember/dashboard/api` URL returns a 307 redirect with HTML body. `curl` does NOT follow the redirect with the POST body intact by default. Always call the canonical URL `https://app.omegaindexer.com/api/omega-indexer-api` directly.
- Successful submission returns the literal string `"done"` (with quotes) — not a JSON object.
- Sitemap.xml URLs cause errors — never include them.
- All URLs must be `https://` and must be live (Netlify deploy must complete first).

### Other services that integrate the Omega Indexer API

- SEO Neo (according to the official docs page).

## Step 9: Update the SEO Keywords tracker spreadsheet

After Omega Indexer submission, add the new post to the SEO Keywords Project tracker.

**Sheet URL:** https://docs.google.com/spreadsheets/d/1gowThbIxJ110SkSYPKRm8SIiET3kq2cqwgipbeSA4Gc/edit

**Columns:** A=KEYWORD, B=VIDEO, C=STATUS, D=bestaiagentcommunity.com, E=aiprofitboardroom.com, F=juliangoldieaiautomation.com, G=aisuccesslabjuliangoldie.com, H=aimoneylabjuliangoldie.com

### Paste method (fastest)

- Put TSV on clipboard via `navigator.clipboard.writeText`.
- Use Name box → click → type C<row> → Enter → Cmd+V.
- TSV format: `keyword\tvideoURL\tDONE\turl1\turl2\turl3\turl4\turl5`

If a row already exists for the keyword, update columns C-H on that row.
If no row exists, insert ABOVE "SITES ANALYTICS:" section.

## Step 10: Improvements log (track what works over time)

After each batch, log:

- Which CTR formulas got the most search clicks (check Google Search Console weekly).
- Which CTAs converted best (track via Boardroom signups).
- Which video embeds drove most YouTube traffic.
- Adjust the skill rules based on data.

## Step 11: Cross-site interlinking (CRITICAL for backlinks + indexing speed)

Every article must link to the same/related articles on the OTHER 4 sites in the network. This creates 4 backlinks per article (across the 5 sites = 20 backlinks per keyword) and dramatically speeds up indexing.

### The "Also On Our Network" block (add to every post above the related-reading section)

```markdown
## Also On Our Network

- 🌐 [Read on bestaiagentcommunity.com](https://bestaiagentcommunity.com/blog/<slug>/)
- 🌐 [Read on aiprofitboardroom.com](https://aiprofitboardroom.com/blog/<slug>/)
- 🌐 [Read on juliangoldieaiautomation.com](https://juliangoldieaiautomation.com/blog/<slug>/)
- 🌐 [Read on aisuccesslabjuliangoldie.com](https://aisuccesslabjuliangoldie.com/blog/<slug>/)
- 🌐 [Read on aimoneylabjuliangoldie.com](https://aimoneylabjuliangoldie.com/blog/<slug>/)
```

OMIT the link for the site the post is currently published on (so each post has 4 outbound network backlinks, not 5).

### Why this matters

- 4 backlinks per article × 5 articles per keyword = 20 backlinks per keyword instantly.
- Cross-site links pass juice between sites.
- Crawlers discover new posts faster when other sites link to them.
- Helps the smaller sites inherit indexing speed from aiprofitboardroom.com (the strongest of the 5).

### Why aiprofitboardroom.com indexes/ranks best

- Strongest brand-name domain (matches the actual product name).
- Older + more posts.
- Probably more inbound links from Skool/YouTube etc.
- The other 4 sites need cross-site backlinks from it to catch up — which is exactly what the network block delivers.

## Step 12: Inbound link ladder — internal + cross-site (CRITICAL)

For every new keyword K shipped, after the 5 articles are written + deployed, edit existing related posts on ALL 5 sites to add inbound links to the new posts. This creates two effects:

1. **Internal link ladder** (same-site) — boosts SEO authority for the new post.
2. **Cross-site backlinks** (network) — older posts on site A link to new post on site B, accelerating indexing of newer/smaller sites.

### How to execute (each new keyword)

For each new keyword K:

1. Identify 3-5 thematically related EXISTING posts (across all 5 sites — pick by topic relevance).
2. For each related post, add a "Latest Updates" block right before the standard footer (`📺 [Video notes`).
3. The block must include:
   - 1-2 SAME-SITE links to the new post (internal link ladder).
   - 1-2 CROSS-SITE links to the new post on a DIFFERENT site (network backlink).
4. Re-deploy all affected sites.

### Block template

```markdown
## Latest Updates

- [<New post title>](/blog/<new-slug>/) — fresh on this topic.
- 🌐 [Read on <other-site>](https://<other-site>/blog/<new-slug>/) — sister-site take.
- [<Related new post title>](/blog/<related-new-slug>/) — companion read.
```

OMIT the same-site link variant when editing the post on the SAME site as the new post (use cross-site only there). On the other 4 sites, mix same-site + cross-site links.

### Why this matters

- Each new post = ~5 related posts × 5 sites = up to 25 fresh inbound contextual links.
- Cross-site backlinks pass link equity from authority-strong site (aiprofitboardroom.com) to authority-weaker sites.
- Older posts staying fresh ("Latest Updates" block updated each batch) signals to Google the site is actively maintained.
- Internal link ladder strengthens topical clusters.

## Step 12.5: Indexing diagnostic + fix checklist

When a site indexes slower than aiprofitboardroom.com, run this diagnostic before chasing technical fixes:

### Diagnostic order

1. **Brand-domain authority** — strongest correlation. Domain that matches the brand name wins. Can't easily fix.
2. **Inbound links from authority sites** — Skool/YouTube/etc. links to aiprofitboardroom but maybe not to aimoneylabjuliangoldie. Check via Search Console > Links.
3. **Cross-site inbound links** — handled by Step 11 + Step 12 (this skill now bakes them in).
4. **Sitemap submission to GSC** — every site's sitemap.xml MUST be manually submitted in Google Search Console. Without GSC submission, Google may take weeks to discover.
5. **Google Indexing API** — for any time-sensitive launch, submit URLs via the official Google Indexing API (service account JSON key, POST to indexing.googleapis.com). Faster than waiting for Omega Indexer.
6. **Crawl budget waste** — use `site:domain.com` query to see what's indexed vs what's submitted. Missing pages → crawl budget issue or noindex tag.
7. **Speed + Core Web Vitals** — Netlify usually handles this. But verify in PageSpeed Insights.

### Fix priority

- HIGH: Cross-site inbound links (Step 11 + 12 — already baked in).
- HIGH: GSC sitemap submission (manual, do once per site).
- MEDIUM: Google Indexing API alongside Omega.
- LOW: Schema markup (already added).
- LOW: Content quality (already strong).

### Why aiprofitboardroom.com indexes/ranks best

- Brand-name domain match.
- More existing posts (83 vs 79 on the smaller sites).
- Probably more inbound links from Skool/YouTube/external.
- The link-equity gap closes fastest via cross-site inbound links from this strongest site to the smaller ones.

## Step 13: End-of-batch SEO improvement evaluation (always do this)

At the END of every batch run, before reporting back to the user, evaluate:

1. What worked well in this batch.
2. What could be improved next batch.
3. Generate 3-5 specific, actionable SEO improvement ideas.
4. Present them to the user in a numbered list.
5. Ask the user which (if any) to incorporate into the skill.
6. If the user accepts, write the changes into this skill file.
7. Confirm the skill file was updated.

### Example end-of-batch eval format

```
## SEO improvements observed this batch

What worked:
- [observation]
What could improve:
- [observation]

Proposed skill updates (pick any to add):
1. [Specific rule change]
2. [Specific rule change]
3. [Specific rule change]

Reply with the numbers you want to add to the skill.
```

This loop ensures the skill compounds over time based on real data.

## Optimisation principles (the "why" behind the rules)

1. **Multiple videos per page** = longer dwell time + better SEO + more video ad revenue + higher YouTube channel reach.
2. **Direct response titles** = higher CTR in SERPs + AI search results.
3. **Above-the-fold CTA** = first conversion opportunity before bounce.
4. **Trust signals + numbers** = social proof drives sign-ups.
5. **Internal linking network** = better SEO crawl + lower bounce rate.
6. **Same-day Omega Indexer submit** = fast Google indexing = faster ranking.
7. **5 unique articles per keyword** = capture multiple SERP positions per keyword.
8. **Cross-site interlinking** = 4 instant backlinks per post + faster indexing for smaller sites.
9. **End-of-batch SEO eval loop** = the skill compounds + improves based on actual results.
