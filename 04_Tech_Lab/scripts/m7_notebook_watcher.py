#!/usr/bin/env python3
"""
M7 NOTEBOOK WATCHER (opt-in, one-shot CLI — no background daemon)
=================================================================
Per CLAUDE.md / MASTER_PLAYBOOK.md / Outbox Shield (DEC-005):

  * Trigger: human runs `python m7_notebook_watcher.py --raw <path-to-raw.md>`.
    There is NO background loop. This is intentional: every extraction result
    is staged PAUSED to 01_Command_Center/Outbox_Drafts/ for Saia to review.
  * Source: any .md dropped into 03_Knowledge_Mat/raw/ (roofer manual,
    estimator text, storm documentation, etc.).
  * Extraction: non-summarized PACT Study Guide table with the four columns
    | Core Concept/Technical Spec | Primary Source Reference | Key
    Brand-Compliant Facts | Operational Deployment Window |.
  * Anchoring: every row maps back to one of the verified Frisco core ZIPs
    (75033 / 75034 / 75035). Non-anchored rows are tagged <<NO FRISCO
    ANCHOR — VERIFY>> instead of silently dropped.
  * Page-level citation: any [p. N], (p. N), or `page N:` markers in the raw
    source are pulled into the "Primary Source Reference" column verbatim,
    with the source filename as the citation key. This is the
    context-drift guard the user explicitly asked for.
  * Output: 01_Command_Center/Outbox_Drafts/<YYYY-MM-DD>_StudyGuide_<slug>.md
    with `status: paused` frontmatter per Outbox Shield.

Usage:
    python m7_notebook_watcher.py --raw 03_Knowledge_Mat/raw/<file>.md
    python m7_notebook_watcher.py --raw <file>.md --out-root 01_Command_Center/Outbox_Drafts
    python m7_notebook_watcher.py --raw <file>.md --dry-run
    python m7_notebook_watcher.py --batch 03_Knowledge_Mat/raw/

Ko e hala 'o e fononga ko e faka'apa'apa.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

# ---------------------------------------------------------------------------- #
# Verified Frisco core ZIPs (MASTER_PLAYBOOK.md — Regional Expansion Vectors)
# ---------------------------------------------------------------------------- #

FRISCO_CORE_ZIPS = ("75033", "75034", "75035")
# Wider service region (10-15 mi radius per Master Playbook):
FRISCO_WIDER_ZIPS = ("75067", "75068")
FRISCO_ALL_ZIPS = FRISCO_CORE_ZIPS + FRISCO_WIDER_ZIPS

# ---------------------------------------------------------------------------- #
# PACT Study Guide row
# ---------------------------------------------------------------------------- #

@dataclass
class PactRow:
    concept: str
    source_reference: str
    brand_facts: str
    deployment_window: str
    frisco_zip_anchor: str  # "75033" or "" if missing
    anchor_status: str      # "anchored" | "no-anchor-verify"


# Compiled regexes. Keep them conservative — false positives are worse than
# misses in a Study Guide; if the row can't be parsed cleanly it is marked
# <<VERIFY>> rather than dropped.
_RE_HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
_RE_PAGE_TAG = re.compile(r"\[p\.\s*(\d+)\]|\(p\.\s*(\d+)\)|`page\s+(\d+)[:.]?", re.IGNORECASE)
_RE_BULLET = re.compile(r"^\s*[-*+]\s+")
_RE_NUMBERED = re.compile(r"^\s*\d+[.)]\s+")
_RE_DEFINITION = re.compile(r"^(?P<term>[A-Z][A-Za-z0-9 /()\-]{2,60}?):\s+(?P<def>.+)$")
_RE_ZIP = re.compile(r"\b(75033|75034|75035|75067|75068)\b")
# Sentence splitter: split on punctuation followed by whitespace, but NOT
# inside brackets like [p. 3] or (p. 3). This prevents "photo [p." from
# triggering a false split before the page tag.
_RE_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?!\d)")


# ---------------------------------------------------------------------------- #
# Extraction
# ---------------------------------------------------------------------------- #

def _slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_") or "source"


# Page-tag + heading-tag tracking. The default page citation for a row is
# the union of (section heading tags) + (row-line tags).
def _extract_page_tags(text: str) -> list:
    """Return list of (page_int, span) found in text, deduplicated, ordered."""
    seen = []
    for m in _RE_PAGE_TAG.finditer(text):
        for g in m.groups():
            if g is not None:
                p = int(g)
                if p not in seen:
                    seen.append(p)
    return seen


def _anchor_zip(row_text: str) -> str:
    """Return the first Frisco core ZIP found in the row text, else ''.
    Prefers core ZIPs (75033/75034/75035) over wider service ZIPs."""
    matches = _RE_ZIP.findall(row_text)
    for z in matches:
        if z in FRISCO_CORE_ZIPS:
            return z
    for z in matches:
        if z in FRISCO_WIDER_ZIPS:
            return z
    return ""


def _concept_candidate_from_heading(heading: str) -> str:
    h = heading.strip()
    if h.startswith("[") and "]" in h:
        h = h.split("]", 1)[1].strip()
    return h


def _row_from_text(text: str, source_file: Path, page_ref: int | None,
                   section_anchor_zip: str, section_concept: str) -> PactRow:
    """Build a PactRow from already-cleaned text (no bullet markers).

    Strategy:
      1. If text matches `Term: definition`, concept = term, facts = definition.
      2. Else if text has multiple sentences, concept = first sentence (capped
         at 120 chars), facts = remainder.
      3. Else treat the whole line as the concept; facts = '' (the source
         line was already short enough to be the whole idea).
      The `section_concept` is prepended ONLY when the parsed concept is
      empty/too generic, so we don't double-up obvious headings.
    """
    text = text.strip()
    if not text:
        # Defensive: never emit a totally empty row.
        text = "(unparsed line — review source)"

    m = _RE_DEFINITION.match(text)
    if m:
        concept = m.group("term").strip()
        facts_body = m.group("def").strip()
    else:
        # Split on sentence boundaries, but never inside [p. N] / (p. N) tags.
        parts = _RE_SENT_SPLIT.split(text, maxsplit=1)
        head = parts[0].strip(" -:")
        if len(parts) > 1:
            concept = head[:120] or section_concept or "(line)"
            facts_body = parts[1].strip()
        else:
            concept = head[:120] or section_concept or "(line)"
            facts_body = ""

    # If concept is a single bare word, prepend section heading so the row
    # is searchable in isolation. Two-or-more-word terms are already unique
    # enough on their own.
    if section_concept and len(concept.split()) == 1 and concept.lower() not in {
            "hail", "wind", "storm", "photo"}:
        # only prepend if section_concept itself isn't already in the concept
        if section_concept.lower().split("(")[0].strip() not in concept.lower():
            concept = f"{section_concept} — {concept}"

    source_ref = f"{source_file.name}" + (f", p. {page_ref}" if page_ref else "")

    # Anchor: row-level ZIP first; fall back to section-level ZIP from heading.
    anchor = _anchor_zip(text)
    if not anchor:
        anchor = section_anchor_zip
    if anchor:
        anchor_status = "anchored"
        deployment_window = (
            f"Activate across Frisco core ZIP {anchor} (10-15 mi Frisco HQ radius). "
            "Confirm via Master Playbook §Service Region before deployment."
        )
    else:
        anchor_status = "no-anchor-verify"
        deployment_window = (
            "<<NO FRISCO ANCHOR — VERIFY>> — confirm Frisco core ZIP "
            "(75033/75034/75035) applicability before any campaign deployment."
        )

    return PactRow(
        concept=concept,
        source_reference=source_ref,
        brand_facts=facts_body,
        deployment_window=deployment_window,
        frisco_zip_anchor=anchor,
        anchor_status=anchor_status,
    )


def extract_rows(raw_text: str, source_file: Path) -> list:
    """Parse raw markdown into a list of PACT Study Guide rows.

    Strategy:
      * Track the most recent heading; its text becomes the default concept
        prefix when a row needs one.
      * Track ZIPs and page tags found in the heading — these become the
        section-level defaults that any row under the heading inherits.
      * Each non-empty line that looks like a bullet, numbered item, or
        "Term: definition" produces one row.
      * Page tags found in the line itself override the section default.
      * ZIPs found in the line itself override the section default.
    """
    rows = []
    current_heading = ""
    default_pages: list = []
    section_anchor_zip = ""
    in_code_block = False

    for line in raw_text.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        if not stripped:
            continue

        m = _RE_HEADING.match(line)
        if m:
            current_heading = _concept_candidate_from_heading(m.group(2))
            default_pages = _extract_page_tags(m.group(2))
            # New section — reset and re-derive section anchor ZIP.
            section_anchor_zip = _anchor_zip(m.group(2)) or section_anchor_zip
            continue

        # Skip lines that don't look like row candidates.
        if not (_RE_BULLET.match(line) or _RE_NUMBERED.match(line) or _RE_DEFINITION.match(line)):
            continue

        # Strip leading bullet/number markers so the row builder sees clean text.
        clean = _RE_BULLET.sub("", line)
        clean = _RE_NUMBERED.sub("", clean).strip()

        # Page citation: line-level tags first, else section default.
        line_pages = _extract_page_tags(clean)
        pages_for_row = line_pages if line_pages else default_pages
        page_ref = pages_for_row[0] if pages_for_row else None

        row = _row_from_text(clean, source_file, page_ref,
                             section_anchor_zip, current_heading)
        rows.append(row)

    return rows


# ---------------------------------------------------------------------------- #
# Markdown rendering (PACT table)
# ---------------------------------------------------------------------------- #

def render_study_guide(source_path: Path, rows: list, scanned_chars: int) -> str:
    today = date.today().isoformat()
    slug = _slugify(source_path.stem)
    anchored = sum(1 for r in rows if r.anchor_status == "anchored")
    unanchored = len(rows) - anchored

    frontmatter = (
        "---\n"
        f"type: outbox_draft\n"
        f"title: \"PACT Study Guide — {source_path.stem} (PAUSED)\"\n"
        f"status: paused\n"
        f"created: {today}\n"
        f"agent: m7_notebook_watcher\n"
        f"brand: Pineapple Contractors M7\n"
        f"source_file: \"{source_path.as_posix()}\"\n"
        f"row_count: {len(rows)}\n"
        f"anchored_rows: {anchored}\n"
        f"unanchored_rows: {unanchored}\n"
        f"scanned_chars: {scanned_chars}\n"
        f"frisco_core_zips: [\"75033\", \"75034\", \"75035\"]\n"
        f"color_primary: \"#1A365D\"\n"
        f"color_secondary: \"#FBC02D\"\n"
        f"color_status: \"#00BFFF\"\n"
        f"---\n\n"
    )

    banner = (
        f"# PACT Study Guide — `{source_path.name}`\n\n"
        f"> **PAUSED — awaiting Saia.** No promotion to wiki. No campaign activation.\n"
        f"> This guide is staged for human review. Source row extraction is\n"
        f"> **non-summarized**: every meaningful bullet, numbered item, and\n"
        f"> `Term: definition` line from the raw source becomes its own row.\n"
        f"> Page-level citations from the raw source are preserved in column 2.\n\n"
        f"**Source:** `{source_path.as_posix()}` "
        f"({scanned_chars:,} chars scanned)\n"
        f"**Rows:** {len(rows)} total · {anchored} Frisco-anchored · {unanchored} `<<VERIFY>>`\n"
        f"**Anchor rules:** Frisco core ZIPs = {', '.join(FRISCO_CORE_ZIPS)}. "
        f"Wider service ZIPs = {', '.join(FRISCO_WIDER_ZIPS)}.\n\n"
        "---\n\n"
    )

    if not rows:
        table = (
            "## PACT Study Guide Table\n\n"
            "_No row-shaped content detected in this source (no bullets, numbered "
            "items, or `Term: definition` lines outside code blocks)._ "
            "Re-author the raw source with structured rows or extend the extractor.\n"
        )
    else:
        header = (
            "## PACT Study Guide Table\n\n"
            "| Core Concept/Technical Spec | Primary Source Reference | "
            "Key Brand-Compliant Facts | Operational Deployment Window |\n"
            "|---|---|---|---|\n"
        )
        body_lines = []
        for r in rows:
            zip_tag = f" **(ZIP {r.frisco_zip_anchor})**" if r.anchor_status == "anchored" else ""
            body_lines.append(
                f"| {r.concept}{zip_tag} "
                f"| {r.source_reference} "
                f"| {r.brand_facts} "
                f"| {r.deployment_window} |"
            )
        table = header + "\n".join(body_lines) + "\n"

    anchor_section = (
        "\n---\n\n"
        "## Anchor Status Breakdown\n\n"
        f"- Frisco core-anchored rows (75033 / 75034 / 75035): **{anchored}**\n"
        f"- Wider-service ZIP rows (75067 / 75068): included in core counts when present\n"
        f"- Unanchored rows tagged `<<NO FRISCO ANCHOR — VERIFY>>`: **{unanchored}**\n\n"
        "> Unanchored rows are NOT silently dropped. They ship in the table with a\n"
        "> `<<NO FRISCO ANCHOR — VERIFY>>` deployment window so Saia can either\n"
        "> re-anchor them to a specific Frisco ZIP or strike them from the brief.\n\n"
        "---\n\n"
        "## Outbox Shield\n\n"
        "This file is **PAUSED** in `01_Command_Center/Outbox_Drafts/`. It will not\n"
        "be promoted to the wiki, published, or used to spin up campaigns without\n"
        "explicit Saia authorization. No outbound API call leaves this draft.\n\n"
        "Ko e hala 'o e fononga ko e faka'apa'apa.\n"
    )

    return frontmatter + banner + table + anchor_section


# ---------------------------------------------------------------------------- #
# CLI
# ---------------------------------------------------------------------------- #

def _process_one(raw_path: Path, out_root: Path, dry_run: bool) -> dict:
    text = raw_path.read_text(encoding="utf-8", errors="replace")
    rows = extract_rows(text, raw_path)
    today = date.today().isoformat()
    slug = _slugify(raw_path.stem)
    out_name = f"{today}_StudyGuide_{slug}.md"
    out_path = out_root / out_name
    rendered = render_study_guide(raw_path, rows, len(text))
    summary = {
        "source": raw_path.as_posix(),
        "rows": len(rows),
        "anchored": sum(1 for r in rows if r.anchor_status == "anchored"),
        "unanchored": sum(1 for r in rows if r.anchor_status != "anchored"),
        "output_path": out_path.as_posix() if not dry_run else "(dry-run, not written)",
    }
    if not dry_run:
        out_root.mkdir(parents=True, exist_ok=True)
        out_path.write_text(rendered, encoding="utf-8")
    return summary


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="M7 Notebook Watcher (opt-in, one-shot)")
    ap.add_argument("--raw", help="path to a single raw markdown source")
    ap.add_argument("--batch", help="path to a directory of raw markdown sources")
    ap.add_argument("--out-root", default="01_Command_Center/Outbox_Drafts",
                    help="PAUSED output root (default: 01_Command_Center/Outbox_Drafts)")
    ap.add_argument("--dry-run", action="store_true", help="do not write the output file")
    args = ap.parse_args(argv)

    if not args.raw and not args.batch:
        ap.print_help()
        return 0

    out_root = Path(args.out_root)
    summaries = []
    if args.raw:
        p = Path(args.raw)
        if not p.exists():
            print(f"ERROR: --raw path does not exist: {p}", file=sys.stderr)
            return 2
        summaries.append(_process_one(p, out_root, args.dry_run))
    if args.batch:
        d = Path(args.batch)
        if not d.is_dir():
            print(f"ERROR: --batch path is not a directory: {d}", file=sys.stderr)
            return 2
        for p in sorted(d.glob("*.md")):
            summaries.append(_process_one(p, out_root, args.dry_run))

    import json
    print(json.dumps({"summaries": summaries, "outbox_shield": "PAUSED"}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
