---
name: notebook-ingest
description: >-
  Pull notes from a Google NotebookLM notebook into the M7 vault as shared memory.
  Incremental (dedups by note_id, so re-pulling a growing notebook only adds new notes),
  brand-scrubs (removes Tongan proverbs, GAF->IKO Certified, customer-facing free->CPPA),
  routes code into a review-only DRAFTS folder, builds an index + prompt library, and
  commits to GitHub. Use when Saia says "ingest/pull the notebook", finishes a NotebookLM
  extraction, or names a NotebookLM notebook to bring into the vault. Nothing publishes or
  runs — everything lands as reviewable DRAFTS (Outbox Shield).
---

# notebook-ingest — NotebookLM → M7 vault (shared memory)

Bring a NotebookLM notebook's generated notes into `03_Knowledge_Mat/Resources/` as scrubbed,
structured, git-tracked shared memory. Safe to run repeatedly — it only adds notes it hasn't
seen before.

## When to use
- Saia says "ingest / pull the [notebook name]" or "bring that notebook into the vault."
- Saia just finished (or is still finishing) a NotebookLM extraction and wants it captured.
- A new batch of notes was generated in a notebook already ingested before (→ incremental top-up).

## Accounts (important)
Saia has two NotebookLM accounts. The `nlm` default profile is the business account. The
personal notebooks live under `smoeprivate1@gmail.com`. If a notebook returns
`PERMISSION_DENIED`, it's on the other account.

## Steps

1. **Identify the notebook.** Get its title or UUID. If unknown, call
   `mcp__notebooklm-mcp__notebook_list` and match by title.

2. **Make sure you're on the right account.** Try the pull; on `PERMISSION_DENIED`:
   - `nlm login switch smoeprivate1@gmail.com` (or `default`) in Bash, then
     call `mcp__notebooklm-mcp__refresh_auth`.
   - **Remember to switch back to `default` when finished** (business account runs the keep-alive).

3. **Pull the notes.** Call `mcp__notebooklm-mcp__note` with `action: "list"` and the notebook_id.
   - Large notebooks exceed the token limit and the tool **saves the JSON to a file** — use that path.
   - Small ones return inline; write the JSON to a temp file yourself.

4. **Run the engine** (does the scrub + structure + dedup):
   ```bash
   python ".claude/skills/notebook-ingest/ingest.py" \
     --src "<the note-list JSON file>" \
     --label "<notebook title>" \
     --notebook-id "<uuid>" \
     --out "NotebookLM_<ShortName>_<YYYY-MM-DD>"
   ```
   It prints `+N new, M skipped`. Re-runs skip everything already ingested (ledger:
   `03_Knowledge_Mat/Resources/.notebook_ingest_ledger.json`).

5. **Switch the account back to `default`** if you changed it in step 2.

6. **Commit + push** (this is what makes it shared memory between local + cloud):
   ```bash
   git add "03_Knowledge_Mat/Resources" && git commit -m "notebook-ingest: <notebook> (+N notes)" && git push origin main
   ```

7. **Report to Saia**: how many new notes, how many flagged for brand review, and where they landed
   (`Resources/NotebookLM_.../_INDEX.md`). Point out that any `_code_DRAFTS/` files are AI-generated
   and must be reviewed before running.

## What the scrub does (automatic, safe)
- Removes every Tongan-proverb line (decommissioned brand rule).
- `GAF` → `IKO Certified`.
- Customer-facing `free <inspection/estimate/quote/audit/…>` → `Complimentary Professional Photo Audit (CPPA)`.
- **Flags** (does NOT blind-replace) generic `free` / `green` for human review — these are internal SOPs.

## Guardrails
- **Outbox Shield:** everything lands as DRAFT. Nothing is published, sent, spent, or executed.
- **Code is never auto-run.** `.py/.bat/.sql/...` notes go to `_code_DRAFTS/` for review.
- Raw "download-only" Studio artifacts (standalone `.py`, `.bat`) are **not** returned by the note API —
  get those via NotebookLM **Batch export** → drop in `03_Knowledge_Mat/inbox/from_notebooklm/`.

## Brand lock (must survive in all output)
CPPA not "free" · IKO Certified not GAF · zero green · "Roofing Made Sweeter" / "The Pineapple Standard" ·
RCAT #03-0637 · (972) 928-0788.
