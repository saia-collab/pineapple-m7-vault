#!/usr/bin/env python3
"""
M7 SEO MACHINE LOOP (opt-in, one-shot CLI)
==========================================
Per 05_Campaign_Factory/10_Research_Stage/CONTEXT.md + MASTER_PLAYBOOK.md:

  * Inputs:
      --target-zip <ZIP>            North Texas target ZIP (verified Frisco
                                     core = 75033/75034/75035; wider service
                                     = 75067/75068; everything else = flag
                                     <<OUT-OF-REGION — VERIFY>>)
      --competitor-url <URL>        Optional competitor URL to scrape for
                                     intent cues
      --keywords <csv>              Optional seed keyword list (else: defaults
                                     loaded from a small ground-truth bank
                                     anchored in MASTER_PLAYBOOK.md §Digital
                                     Marketing Engine)
  * Outputs (written into 05_Campaign_Factory/10_Research_Stage/):
      output/<YYYY-MM-DD>_Research_Intent_<slug>.md
      output/<YYYY-MM-DD>_Research_Intent_<slug>.intent.json
  * Scoring rubric fields are explicitly tagged <<VERIFY>> where the rubric
    is not grounded in a named source document. This is the same honesty
    rule the 2026-06-22 FriscoStorm brief followed for external figures.
  * Outbox Shield: this CLI writes research-stage artifacts only, never
    publishes. Stage-contract gate per CONTEXT.md is a `brand_firewall.py`
    PASS (no banned lexicon, no banned colors). The script runs the
    ComplianceOfficer from m7_scoring.py over its own output and aborts
    the write on FAIL.

Usage:
    python m7_seo_intent.py --target-zip 75034
    python m7_seo_intent.py --target-zip 75034 --keywords "hail damage,roof inspection,insurance claim"
    python m7_seo_intent.py --target-zip 75034 --competitor-url https://example.com
    python m7_seo_intent.py --target-zip 75034 --dry-run

Ko e hala 'o e fononga ko e faka'apa'apa.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.parse
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

# Local imports: reuse the Compliance Officer built earlier.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from m7_scoring import ComplianceOfficer  # noqa: E402

# ---------------------------------------------------------------------------- #
# Verified ZIP set
# ---------------------------------------------------------------------------- #

FRISCO_CORE_ZIPS = ("75033", "75034", "75035")
FRISCO_WIDER_ZIPS = ("75067", "75068")
FRISCO_ALL_ZIPS = FRISCO_CORE_ZIPS + FRISCO_WIDER_ZIPS

# ---------------------------------------------------------------------------- #
# Default seed keywords — anchored in MASTER_PLAYBOOK.md / M7_INTEGRATED_CAMPAIGN.md
# (These are the queries Frisco homeowners + property managers actually run
#  after a hail event, drawn verbatim from §Digital Marketing Engine and
#  §Audience Segments in the existing campaign docs.)
# ---------------------------------------------------------------------------- #

DEFAULT_KEYWORDS = [
    "frisco storm roofer",
    "frisco hail damage repair",
    "frisco roof inspection",
    "hail damage insurance claim frisco",
    "rcat licensed roofer frisco",
    "iko certified contractor frisco",
    "frisco property manager roofing",
    "starwood roof replacement",
    "newman village hail damage",
    "frisco tx hail claim window",
    "complimentary professional photo audit",   # brand-mandated phrasing
    "full restoration coverage evaluation",     # brand-mandated phrasing
]


# ---------------------------------------------------------------------------- #
# Scoring rubric — every field carries an explicit source-or-VERIFY marker.
# ---------------------------------------------------------------------------- #

# Each rubric dimension has:
#   id, label, weight, ground (source-or-verify), scoring_rules (text).
RUBRIC = [
    {
        "id": "geo_anchor",
        "label": "Geographic anchor (Frisco core ZIP)",
        "weight": 25,
        "ground": "GROUNDING.md §4 + MASTER_PLAYBOOK.md (Regional Expansion Vectors)",
        "scoring_rules": (
            "Award 25 if ZIP is in {75033, 75034, 75035}. Award 15 if ZIP is "
            "in {75067, 75068}. Award 0 with <<OUT-OF-REGION — VERIFY>> tag otherwise."
        ),
    },
    {
        "id": "storm_recency",
        "label": "Storm / hail recency in the window",
        "weight": 20,
        "ground": "MASTER_PLAYBOOK.md Lead Matrix: +20 storm mention",
        "scoring_rules": (
            "Award 20 if any seed keyword implies active or recent hail/wind event "
            "in the service region. Award 10 if historical. Award 0 otherwise."
        ),
    },
    {
        "id": "credential_match",
        "label": "Credential match (RCAT + IKO surface)",
        "weight": 15,
        "ground": "CLAUDE.md §2.4 + MASTER_PLAYBOOK.md (required credentials)",
        "scoring_rules": (
            "Award 15 if both 'RCAT #03-0637' and 'IKO Certified' can be cited in the "
            "answer without violating the Elite Compliance Filter. Award 8 if only one. "
            "Award 0 if neither."
        ),
    },
    {
        "id": "intent_class",
        "label": "Search intent class (informational / commercial / transactional)",
        "weight": 15,
        "ground": "<<VERIFY — Saia to confirm rubric vs. M7_INTEGRATED_CAMPAIGN.md §2>>",
        "scoring_rules": (
            "Award 15 if transactional (claim / quote / schedule). Award 10 if commercial "
            "(PM portfolio). Award 5 if informational. This rubric field is unverified — "
            "calibrate against the §2 audience segments before treating the score as final."
        ),
    },
    {
        "id": "lexicon_safety",
        "label": "Lexicon safety (CPPA / FRC substitution fit)",
        "weight": 15,
        "ground": "CLAUDE.md §2.1 + GROUNDING.md banned lexicon",
        "scoring_rules": (
            "Award 15 if the answer can be authored using only brand-safe phrases "
            "(CPPA, Full Restoration Coverage Evaluation, IKO Certified, The Pineapple "
            "Standard). Award 5 if any banned token would naturally appear and require "
            "substitution to a brand-safe phrase. Award 0 if the query is itself about "
            "a banned concept (e.g. bargain roofers). The banned-token list itself "
            "lives in m7_scoring.FORBIDDEN_COMPLIANCE_PATTERNS — this rubric never "
            "spells the banned tokens out."
        ),
    },
    {
        "id": "competitor_gap",
        "label": "Competitor / SERP gap (citation bait surface)",
        "weight": 10,
        "ground": "<<VERIFY — competitor scrape step not yet run on live SERP>>",
        "scoring_rules": (
            "Award 10 if the top-3 competitor pages do not surface RCAT + IKO together. "
            "Award 5 if only one. Award 0 if both. This depends on a live SERP pull "
            "the script can scaffold but not run autonomously."
        ),
    },
]


def score_intent(target_zip: str, keywords: list, competitor_url: str | None) -> dict:
    """Score a target ZIP + keyword set against the rubric.

    Returns a dict with per-dimension scores and a total (0-100).
    """
    dimension_results = []

    # 1. geo_anchor
    if target_zip in FRISCO_CORE_ZIPS:
        geo_score = 25
        geo_zone = "frisco_core"
    elif target_zip in FRISCO_WIDER_ZIPS:
        geo_score = 15
        geo_zone = "frisco_wider"
    else:
        geo_score = 0
        geo_zone = "out_of_region"
    dimension_results.append({
        **RUBRIC[0],
        "score": geo_score,
        "rationale": f"ZIP {target_zip} → zone '{geo_zone}'.",
    })

    # 2. storm_recency (keyword heuristic — no live weather ingestion)
    storm_terms = ("hail", "storm", "wind", "tornado", "damage")
    has_storm = any(any(t in kw.lower() for t in storm_terms) for kw in keywords)
    storm_score = 20 if has_storm else 0
    dimension_results.append({
        **RUBRIC[1],
        "score": storm_score,
        "rationale": "Storm-recency term found in seed keywords." if has_storm
                     else "No storm-recency term in seed keywords.",
    })

    # 3. credential_match (always grounded — we cite RCAT + IKO on every page)
    credential_score = 15  # by design
    dimension_results.append({
        **RUBRIC[2],
        "score": credential_score,
        "rationale": "RCAT #03-0637 + IKO Certified surface is the default credential bar.",
    })

    # 4. intent_class (heuristic; <<VERIFY>>)
    transactional = ("claim", "quote", "schedule", "book", "cppa")
    commercial = ("property manager", "hoa", "portfolio", "multi-unit")
    if any(any(t in kw.lower() for t in transactional) for kw in keywords):
        intent_score, intent_class = 15, "transactional"
    elif any(any(t in kw.lower() for t in commercial) for kw in keywords):
        intent_score, intent_class = 10, "commercial"
    else:
        intent_score, intent_class = 5, "informational"
    dimension_results.append({
        **RUBRIC[3],
        "score": intent_score,
        "rationale": f"Keyword intent classified as {intent_class}. <<VERIFY — calibrate vs §2>>",
    })

    # 5. lexicon_safety
    banned_anywhere = ("free", "cheap", "gaf certified", "warrior standard",
                       "toa standard", "six brothers")
    banned_hit = any(any(b in kw.lower() for b in banned_anywhere) for kw in keywords)
    lex_score = 0 if banned_hit else 15
    dimension_results.append({
        **RUBRIC[4],
        "score": lex_score,
        "rationale": ("Banned term found in seed keywords — substitution required."
                      if banned_hit else "No banned term in seed keywords — CPPA/FRC fit clean."),
    })

    # 6. competitor_gap
    if competitor_url:
        comp_score = 0  # cannot evaluate without a live SERP pull
        comp_rationale = (
            "Competitor URL provided but live SERP scrape is OUT OF SCOPE for "
            "this v0.1. <<VERIFY — Saia to run the SERP pull or wire in m7_fetch.py>>. "
            f"URL: {competitor_url}"
        )
    else:
        comp_score = 0
        comp_rationale = "No competitor URL provided. <<VERIFY — SERP pull not run>>."
    dimension_results.append({
        **RUBRIC[5],
        "score": comp_score,
        "rationale": comp_rationale,
    })

    total = sum(d["score"] for d in dimension_results)
    return {
        "target_zip": target_zip,
        "zone": geo_zone,
        "total_score": total,
        "max_score": 100,
        "dimensions": dimension_results,
    }


# ---------------------------------------------------------------------------- #
# Markdown brief rendering
# ---------------------------------------------------------------------------- #

def _slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_") or "intent"


def render_intent_markdown(target_zip: str, keywords: list, competitor_url: str | None,
                           score: dict, competitor_signal: str | None) -> str:
    today = date.today().isoformat()
    slug = _slugify(f"zip_{target_zip}")
    zone = score["zone"]
    out_of_region = (zone == "out_of_region")

    frontmatter = (
        "---\n"
        "type: research_brief\n"
        f"title: \"SEO Intent Profile — ZIP {target_zip} ({zone}) (DRAFT)\"\n"
        f"status: paused\n"
        f"created: {today}\n"
        f"agent: m7_seo_intent\n"
        f"brand: Pineapple Contractors M7\n"
        f"target_zip: \"{target_zip}\"\n"
        f"zone: \"{zone}\"\n"
        f"score: {score['total_score']}\n"
        f"competitor_url: \"{competitor_url or ''}\"\n"
        f"frisco_core_zips: [\"75033\", \"75034\", \"75035\"]\n"
        f"color_primary: \"#1A365D\"\n"
        f"color_secondary: \"#FBC02D\"\n"
        f"color_status: \"#00BFFF\"\n"
        "---\n\n"
    )

    banner = (
        f"# SEO Intent Profile — ZIP `{target_zip}`\n\n"
        f"> **PAUSED — awaiting Saia.** No campaign or ad activation from this brief.\n"
        f"> Stage envelope: DRAFT (per `05_Campaign_Factory/10_Research_Stage/CONTEXT.md`).\n"
    )
    if out_of_region:
        banner += (
            f"> **<<OUT-OF-REGION — VERIFY>>** ZIP `{target_zip}` is not in the verified\n"
            f"> Frisco core ({', '.join(FRISCO_CORE_ZIPS)}) or wider-service ({', '.join(FRISCO_WIDER_ZIPS)})\n"
            f"> set. Confirm via `MASTER_PLAYBOOK.md` before any deployment.\n"
        )
    banner += "\n"

    cred = (
        "## Brand rails (applied to every output)\n\n"
        "- Royal Navy (#1A365D) credential bar: **RCAT #03-0637 · IKO Certified**.\n"
        "- CTA hook: **Complimentary Professional Photo Audit (CPPA)**.\n"
        "- Lexicon: Full Restoration Coverage Evaluation (per CLAUDE.md §2.1 — "
        "the brand substitution for promotional pricing phrasing).\n"
        "- IKO Certified (never shortened). No banned terms. No green.\n\n"
    )

    kw_section = "## Seed keywords analyzed\n\n"
    if keywords:
        kw_section += "| # | Keyword | Storm term? | Banned term? |\n|---|---|---|---|\n"
        storm_terms = ("hail", "storm", "wind", "tornado", "damage")
        banned = ("free", "cheap", "gaf certified", "six brothers",
                  "warrior standard", "toa standard")
        for i, kw in enumerate(keywords, 1):
            has_storm = any(t in kw.lower() for t in storm_terms)
            has_banned = any(b in kw.lower() for b in banned)
            kw_section += (
                f"| {i} | `{kw}` | {'yes' if has_storm else 'no'} "
                f"| {'YES — substitute' if has_banned else 'no'} |\n"
            )
    else:
        kw_section += "_No keywords provided — using default bank (see `--keywords` to override)._\n"
    kw_section += "\n"

    rubric_section = "## Scoring rubric (per-dimension)\n\n"
    rubric_section += (
        "| Dimension | Weight | Score | Rationale | Ground |\n"
        "|---|---|---|---|---|\n"
    )
    for d in score["dimensions"]:
        rubric_section += (
            f"| {d['label']} | {d['weight']} | **{d['score']}** | "
            f"{d['rationale']} | {d['ground']} |\n"
        )
    rubric_section += (
        f"\n**Total intent score: {score['total_score']} / 100**\n\n"
    )

    hook_section = "## Factual density hooks (candidate AEO answers)\n\n"
    hook_section += (
        "These hooks are derived from the seed keywords + the verified credential bar.\n"
        "All hooks pass the Elite Compliance Filter (CPPA, FRC, IKO Certified only).\n\n"
    )
    if "hail" in " ".join(keywords).lower() or "storm" in " ".join(keywords).lower():
        hook_section += (
            "1. **Hail-damage intent** — answer in the first 40 words with: ZIP, "
            "credential, CPPA hook. Example: \"In Frisco ZIPs 75033 / 75034 / 75035, "
            "Pineapple Contractors (RCAT #03-0637, IKO Certified) runs a Complimentary "
            "Professional Photo Audit within 48 hours of any hail event.\"\n"
        )
    if any("property manager" in kw.lower() or "hoa" in kw.lower() or "portfolio" in kw.lower()
           for kw in keywords):
        hook_section += (
            "2. **Property-manager intent** — surface the 72-hour storm-response SLA "
            "and the priority-tier portfolio agreement in the first paragraph.\n"
        )
    if any("insurance" in kw.lower() or "claim" in kw.lower() for kw in keywords):
        hook_section += (
            "3. **Claim-window intent** — cite the typical 12-month Texas hail-claim "
            "window and the 30-day documentation discipline recommendation. Use Full "
            "Restoration Coverage Evaluation as the substitution phrase.\n"
        )
    if len(hook_section.splitlines()) <= 5:
        hook_section += "_No high-confidence hook generated from the seed keywords — widen the seed list._\n"
    hook_section += "\n"

    bait_section = "## Citation bait surface (FAQPage / HowTo / LocalBusiness schema candidates)\n\n"
    bait_section += (
        "- `FAQPage` schema: 5–7 questions per ZIP-targeted page. Sample Q: \"How do I know "
        "  if my Frisco roof actually needs replacement or just repair?\" (gap from the "
        "  2026-06-22 brief §D).\n"
        "- `LocalBusiness` schema: NAP = 1 Cowboys Way, Suite 270W, Frisco, TX 75034 · "
        "  972-928-0788 · RCAT #03-0637.\n"
        "- `HowTo` candidate: \"How to file a hail-damage claim in Frisco, TX in 4 steps.\"\n\n"
    )

    comp_section = "## Competitor URL (optional)\n\n"
    if competitor_url:
        parsed = urllib.parse.urlparse(competitor_url)
        comp_section += (
            f"- URL: `{competitor_url}`\n"
            f"- Host: `{parsed.netloc}`\n"
            f"- Path: `{parsed.path}`\n"
        )
        if competitor_signal:
            comp_section += f"- Extracted signal (verbatim, raw): `{competitor_signal}`\n"
        else:
            comp_section += (
                "- No live scrape executed in v0.1. <<VERIFY — wire m7_fetch.py to "
                "pull the page, then re-run with the captured <h1>/<title> signal.>>\n"
            )
    else:
        comp_section += "_No competitor URL provided. Re-run with `--competitor-url` to add._\n"
    comp_section += "\n"

    firewall_section = "## Compliance + firewall trail\n\n"
    firewall_section += (
        "- Lexicon: CPPA, IKO Certified (RCAT #03-0637), The Pineapple Standard, Full "
        "Restoration Coverage Evaluation. No banned terms.\n"
        "- Visual: Royal Navy #1A365D, Pineapple Gold #FBC02D, Process Status Cyan #00BFFF. "
        "No green.\n"
        "- Outbox Shield: this file is PAUSED in `05_Campaign_Factory/10_Research_Stage/`. "
        "No outbound publish from this stage.\n\n"
        "Ko e hala 'o e fononga ko e faka'apa'apa.\n"
    )

    return frontmatter + banner + cred + kw_section + rubric_section + hook_section + bait_section + comp_section + firewall_section


def render_intent_json(target_zip: str, keywords: list, competitor_url: str | None,
                       score: dict) -> str:
    today = date.today().isoformat()
    payload = {
        "stage": "10_Research_Stage",
        "envelope_state": "DRAFT",
        "next_state_on_completion": "READY",
        "generated": today,
        "target_zip": target_zip,
        "zone": score["zone"],
        "score": score["total_score"],
        "service_region": {
            "zips_core": list(FRISCO_CORE_ZIPS),
            "zips_wider": list(FRISCO_WIDER_ZIPS),
        },
        "keywords": keywords,
        "competitor_url": competitor_url,
        "rubric_dimensions": [
            {"id": d["id"], "label": d["label"], "weight": d["weight"],
             "score": d["score"], "ground": d["ground"]}
            for d in score["dimensions"]
        ],
        "firewall_status": "PASS",
        "outbox_shield": "PAUSED",
    }
    return json.dumps(payload, indent=2)


# ---------------------------------------------------------------------------- #
# CLI
# ---------------------------------------------------------------------------- #

def _out_paths(target_zip: str) -> tuple:
    today = date.today().isoformat()
    slug = _slugify(f"zip_{target_zip}")
    out_dir = Path("05_Campaign_Factory/10_Research_Stage/output")
    return (
        out_dir / f"{today}_Research_Intent_{slug}.md",
        out_dir / f"{today}_Research_Intent_{slug}.intent.json",
    )


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="M7 SEO Machine Loop (opt-in)")
    ap.add_argument("--target-zip", required=True, help="North Texas target ZIP code")
    ap.add_argument("--keywords", help="comma-separated seed keyword list")
    ap.add_argument("--competitor-url", help="optional competitor URL for intent signal")
    ap.add_argument("--competitor-signal", help="verbatim text extracted from competitor URL")
    ap.add_argument("--dry-run", action="store_true", help="do not write outputs")
    args = ap.parse_args(argv)

    keywords = [k.strip() for k in (args.keywords or "").split(",") if k.strip()] or DEFAULT_KEYWORDS
    score = score_intent(args.target_zip, keywords, args.competitor_url)

    md = render_intent_markdown(args.target_zip, keywords, args.competitor_url,
                                score, args.competitor_signal)
    js = render_intent_json(args.target_zip, keywords, args.competitor_url, score)

    # Compliance gate — fail the write if the brief itself violates the lexicon.
    officer = ComplianceOfficer()
    md_report = officer.scan(md)
    if md_report.verdict != "PASS":
        print(json.dumps({
            "status": "BLOCKED",
            "reason": "M7 Elite Compliance Filter FAIL on generated brief",
            "compliance_score": md_report.compliance_score,
            "violations": [{"pattern": v.pattern, "banned_label": v.banned_label,
                            "substitute": v.substitute} for v in md_report.violations],
        }, indent=2))
        return 3

    md_path, json_path = _out_paths(args.target_zip)
    summary = {
        "target_zip": args.target_zip,
        "zone": score["zone"],
        "score": score["total_score"],
        "keyword_count": len(keywords),
        "compliance_score": md_report.compliance_score,
        "compliance_verdict": md_report.verdict,
    }
    if args.dry_run:
        summary["md_path"] = "(dry-run, not written)"
        summary["intent_json_path"] = "(dry-run, not written)"
    else:
        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.write_text(md, encoding="utf-8")
        json_path.write_text(js, encoding="utf-8")
        summary["md_path"] = md_path.as_posix()
        summary["intent_json_path"] = json_path.as_posix()
    summary["outbox_shield"] = "PAUSED"
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
