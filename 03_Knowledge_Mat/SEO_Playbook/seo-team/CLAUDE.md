# SEO Team: Team Charter

This folder is a complete specialist SEO team that runs inside Claude Code. Eight
specialist agents, one shared brain, one coordinator that runs everything from a
single prompt.

## The Team

| # | Role | Agent | What they produce |
|---|------|-------|-------------------|
| 1 | Keyword & Market Research Manager | `keyword-research-manager` | `01-keyword-map.md` |
| 2 | Technical Auditor | `technical-auditor` | `02-technical-audit.md` |
| 3 | Analytics & Reporting Manager | `analytics-reporting-manager` | `03-performance-snapshot.md` |
| 4 | AI Search / GEO Specialist | `ai-search-geo-specialist` | `04-geo-audit.md` |
| 5 | On-Page Copywriter | `on-page-copywriter` | `05-onpage-fixes.md` |
| 6 | Blog / Content Writer | `blog-content-writer` | `06-content-plan.md` + draft post |
| 7 | Local SEO Manager | `local-seo-manager` | `07-local-seo.md` |
| 8 | Client Report Builder | `client-report-builder` | `client-report.html` |
| 9 | Workflow Coordinator | `/seo-team` skill | Runs roles 1–8 in order |

## How the team works

**Shared context.** Every agent starts by reading `context/client.md` (who the client
is) and, for writing roles, `context/brand-voice.md` (how the client sounds). This is
what keeps eight separate agents behaving like one team instead of eight strangers.

**File handoffs.** Each agent writes exactly one numbered output file to
`outputs/<client-slug>/`. Downstream agents read upstream files as their inputs:

- Wave 1 (parallel, needs only client.md): roles 1, 2, 3, 4
- Wave 2 (parallel, needs wave 1 files): roles 5, 6, 7
- Wave 3 (needs everything): role 8

The `<client-slug>` is the client's domain with dots replaced by dashes
(`myinclusion.com.au` → `myinclusion-com-au`).

**One prompt runs it all.** The `/seo-team` skill is the coordinator. It reads the
client context, dispatches wave 1 in parallel, waits for their files, dispatches
wave 2, then the report builder. See `.claude/skills/seo-team/SKILL.md`.

## Rules every agent follows

1. **Read `context/client.md` first.** If it's still the unfilled template, stop and
   say so instead of inventing a client.
2. **Never publish anything.** No review replies go live, no GBP posts go live, no
   content gets posted. Everything external is drafted and queued for human approval.
   This team augments the SEO specialist; it does not replace their judgment.
3. **Real data only.** If a data source (DataForSEO, Windsor.ai) is unavailable, say
   what's missing and produce what you can from public data. Never fabricate metrics.
4. **Write your output file even if partial.** Downstream agents depend on it existing.
   Mark gaps clearly with `> NEEDS DATA:` blocks.
5. **Client-safe language in outputs.** Anything you write may end up in front of the
   client, so no internal snark, no jargon without a plain-English gloss.

## Data connections

- **DataForSEO MCP**: keywords, SERPs, rankings, on-page crawl data. Configured in
  `.mcp.json`, credentials from `DATAFORSEO_USERNAME` / `DATAFORSEO_PASSWORD` env vars.
- **Windsor.ai**: the Google-data connector layer (Google Business Profile, and the same
  path used for GSC + GA4). Read-only. The Local SEO Manager pulls the
  `google_my_business` connector (reviews, insights, profile) via the Windsor.ai MCP or
  its REST API with a `WINDSOR_API_KEY`. Optional: only the Local SEO Manager uses it.

## Onboarding a new client

1. Run `/seo-intake <domain>`. It researches the site, GBP, and competitors and drafts
   `context/client.md` + `context/brand-voice.md`, flagging every assumption as a
   `> CONFIRM:` line. (Or fill both files by hand.)
2. Open both files, fix the CONFIRM lines and add the owner-only facts it can't know
   (customer value, whether the GBP is connected in Windsor.ai, who prepares the report).
3. Run `/seo-team <domain>`.
