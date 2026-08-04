# SEO Team for Claude Code

A complete specialist SEO team that runs inside Claude Code: eight specialist agents,
one shared context brain, and a coordinator that runs the whole pipeline for a client
from a single prompt.

```
/seo-team myinclusion.com.au
```

...dispatches keyword research, a technical audit, a performance snapshot and an AI
search (GEO) audit **in parallel**, feeds their outputs to the on-page copywriter,
blog writer and local SEO manager, then assembles everything into a client-ready
HTML report you can send a prospect to win the retainer.

## The roster

| Role | What you get |
|------|--------------|
| Keyword & Market Research Manager | Keyword map: clusters, volumes, difficulty, competitor gaps |
| Technical Auditor | Prioritized technical fix-list with evidence |
| Analytics & Reporting Manager | Baseline: rankings, traffic estimate, competitor benchmark |
| AI Search / GEO Specialist | Citability audit + the fan-out queries to own |
| On-Page Copywriter | Rewritten titles, metas, H1s, money-page copy |
| Blog / Content Writer | One-month content plan + a publish-ready draft post |
| Local SEO Manager | GBP health, drafted review replies, post drafts, citations plan |
| Client Report Builder | Polished client-facing HTML report + cover email |
| Workflow Coordinator | The `/seo-team` skill that runs all of the above |

## Install (5 minutes)

1. **Unzip this folder** anywhere (e.g. `~/seo-team/`) and open a terminal in it.

2. **Connect DataForSEO** (the data source for keywords, rankings, SERPs).
   Get an account at dataforseo.com. New accounts get trial credit, and pay-as-you-go
   is cheap for this workload. Then set your credentials as environment variables
   (add to `~/.zshrc` or `~/.bashrc`):

   ```bash
   export DATAFORSEO_USERNAME="you@example.com"
   export DATAFORSEO_PASSWORD="your-api-password"
   ```

   The included `.mcp.json` already wires the DataForSEO MCP server to those
   variables. Nothing is hardcoded.

3. **Optional: connect Windsor.ai** (only needed for the Local SEO Manager's live
   Google Business Profile data: reviews, insights, profile). Windsor.ai is the same
   connector layer you use for Search Console and GA4, and it is read-only.

   - Connect the client's Google Business Profile in your Windsor.ai account.
   - Then either add the Windsor.ai MCP to this project, or set a REST API key:

   ```bash
   export WINDSOR_API_KEY="your-windsor-key"
   ```

   Without it, the Local SEO Manager still runs: it works from public data and tells you
   what connecting unlocks.

4. **Start Claude Code** in the folder and approve the MCP server when prompted:

   ```bash
   claude
   ```

## Run it

1. Onboard the client with one prompt:

   ```
   /seo-intake clientdomain.com
   ```

   This researches the live site, its Google Business Profile, and its competitors, then
   writes `context/client.md` + `context/brand-voice.md` for you. It flags every
   assumption as a numbered `> CONFIRM:` list.

2. Open both files, fix the CONFIRM lines (a couple of minutes), and add the owner-only
   facts it could not know (customer value, whether the GBP is connected in Windsor.ai).
   You can still fill both files fully by hand instead if you prefer.
3. One prompt runs the whole team:

   ```
   /seo-team clientdomain.com
   ```

Outputs land in `outputs/<client-slug>/`, numbered in pipeline order, with
`client-report.html` as the final deliverable. Open it in a browser, print to PDF,
send it.

You can also run any specialist solo:

```
Use the technical-auditor agent to audit clientdomain.com
```

## What this team will NOT do

By design, nothing here publishes anything. Review replies, GBP posts, and blog
drafts all land in an approval queue for a human. The team is executional muscle;
you stay the strategist. Anyone who tells you to auto-publish AI review replies for
a business you're responsible for is selling you a liability.

## Requirements

- Claude Code
- DataForSEO account (trial credit works for your first runs)
- Windsor.ai account (optional, only for the Local SEO Manager's live GBP data)
