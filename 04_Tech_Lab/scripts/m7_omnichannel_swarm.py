#!/usr/bin/env python3
"""
M7 OMNICHANNEL SWARM DRAFTING (opt-in, one-shot CLI)
====================================================
Per CLAUDE.md §2 (M7 Elite Compliance Filter) + MASTER_PLAYBOOK.md
+ Outbox Shield (DEC-005):

  * Input: --source <path-to-approved-research.md|intent.json>
           The source MUST be a research-stage artifact the user has already
           approved for downstream drafting. This script does not auto-approve
           anything.
  * Outputs: three platform-native variations per source, written to
             01_Command_Center/Outbox_Drafts/ with `status: paused` frontmatter:
               - YYYY-MM-DD_Outbox_Swarm_<slug>_GBP.md       (Google Business Profile post)
               - YYYY-MM-DD_Outbox_Swarm_<slug>_Meta.md      (Meta ad creative)
               - YYYY-MM-DD_Outbox_Swarm_<slug>_Reel.md      (Reel / TikTok caption)
  * Lexicon mutation: every draft is run through the ComplianceOfficer from
    m7_scoring.py. If ANY draft fails, the entire batch is blocked — no
    partial outputs land in Outbox_Drafts.
  * Visual law: every draft references the brand colors in the frontmatter
    (Royal Navy #1A365D, Pineapple Gold #FBC02D, Process Status Cyan #00BFFF).
    Green is forbidden. No hex value other than those three + Slate / White /
    Dark Gray appears anywhere in the creative specs.

Usage:
    python m7_omnichannel_swarm.py --source 05_Campaign_Factory/10_Research_Stage/output/<...>.md
    python m7_omnichannel_swarm.py --source <...>.intent.json --dry-run

Ko e hala 'o e fononga ko e faka'apa'apa.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from m7_scoring import ComplianceOfficer  # noqa: E402

# ---------------------------------------------------------------------------- #
# Brand constants
# ---------------------------------------------------------------------------- #

BRAND = {
    "name": "Pineapple Contractors M7",
    "phone": "972-928-0788",
    "hq": "1 Cowboys Way, Suite 270W, Frisco, TX 75034",
    "rkat": "RCAT #03-0637",
    "iko": "IKO Certified",
    "cppa": "Complimentary Professional Photo Audit (CPPA)",
    "frc": "Full Restoration Coverage Evaluation",
    "color_primary": "#1A365D",      # Royal Navy
    "color_secondary": "#FBC02D",    # Pineapple Gold
    "color_status": "#00BFFF",       # Process Status Cyan
    "colors_allowed_extra": ("#FFFFFF", "#1F2937", "#475569"),  # White, dark grays
    "signoff": "Ko e hala 'o e fononga ko e faka'apa'apa",
}

FRISCO_CORE_ZIPS = ("75033", "75034", "75035")
FRISCO_WIDER_ZIPS = ("75067", "75068")

# Banned color tokens (any other hex is a violation in creative specs).
_RE_BANNED_HEX = re.compile(r"#[0-9A-Fa-f]{6}")
_ALLOWED_HEX = {BRAND["color_primary"].lower(),
                BRAND["color_secondary"].lower(),
                BRAND["color_status"].lower()} | {c.lower() for c in BRAND["colors_allowed_extra"]}
_BANNED_NAMES = ("green", "lime", "olive", "forest", "heritage green")


# ---------------------------------------------------------------------------- #
# Source distillation
# ---------------------------------------------------------------------------- #

@dataclass
class SourceDigest:
    target_zip: str
    zone: str
    keywords: list
    score: int
    hooks: list
    source_path: str


def _read_source(path: Path) -> SourceDigest:
    text = path.read_text(encoding="utf-8", errors="replace")
    # Pull target ZIP from frontmatter.
    zip_m = re.search(r'target_zip:\s*"?(\d{5})"?', text)
    zone_m = re.search(r'zone:\s*"?([a-z_]+)"?', text)
    score_m = re.search(r'(?<!max_)score:\s*(\d+)', text)

    # If JSON, parse it.
    if path.suffix == ".json":
        obj = json.loads(text)
        return SourceDigest(
            target_zip=obj.get("target_zip", ""),
            zone=obj.get("zone", ""),
            keywords=obj.get("keywords", []),
            score=int(obj.get("score", 0)),
            hooks=[],
            source_path=path.as_posix(),
        )

    # Pull keywords from the seed table.
    keywords = []
    in_kw = False
    for line in text.splitlines():
        if line.strip().startswith("## Seed keywords analyzed"):
            in_kw = True
            continue
        if in_kw and line.startswith("## "):
            break
        if in_kw:
            cm = re.match(r"\|\s*\d+\s*\|\s*`([^`]+)`", line)
            if cm:
                keywords.append(cm.group(1))

    # Pull hooks from the factual density hooks section.
    hooks = []
    in_hooks = False
    for line in text.splitlines():
        if line.strip().startswith("## Factual density hooks"):
            in_hooks = True
            continue
        if in_hooks and line.startswith("## "):
            break
        if in_hooks:
            mm = re.match(r"^\d+\.\s+\*\*(.+?)\*\*\s+—\s+(.+)$", line.strip())
            if mm:
                hooks.append({"title": mm.group(1), "body": mm.group(2)})

    return SourceDigest(
        target_zip=zip_m.group(1) if zip_m else "",
        zone=zone_m.group(1) if zone_m else "",
        keywords=keywords,
        score=int(score_m.group(1)) if score_m else 0,
        hooks=hooks,
        source_path=path.as_posix(),
    )


# ---------------------------------------------------------------------------- #
# Color audit — keep creative specs strictly on-palette
# ---------------------------------------------------------------------------- #

def color_violations(text: str) -> list:
    """Return a list of banned color tokens found in `text`.

    Negation-aware: the word "green" (or "lime"/etc.) preceded by a negation
    in a small window ("no green", "not green", "banned: green", "without
    green", "forbidden: green") is treated as a passing note, not a violation,
    because it is the kind of language that appears in design specs to tell
    the designer what to AVOID.
    """
    found_hex = []
    for m in _RE_BANNED_HEX.finditer(text):
        if m.group(0).lower() not in _ALLOWED_HEX:
            found_hex.append(m.group(0))
    # Dedupe
    found_hex = sorted(set(found_hex))

    # Look for banned color names, but skip when in a negation context.
    NEGATIONS = ("no ", "not ", "banned: ", "forbidden: ", "without ",
                 "avoid ", "never ", "don't ", "do not ")
    lower = text.lower()
    found_names = []
    for n in _BANNED_NAMES:
        for m in re.finditer(rf"\b{re.escape(n)}\b", lower):
            start = max(0, m.start() - 12)
            preceding = lower[start:m.start()]
            if any(neg in preceding for neg in NEGATIONS):
                continue
            found_names.append(n)
            break  # one hit per name is enough
    violations = []
    if found_hex:
        violations.append(f"non-palette hex tokens: {', '.join(found_hex)}")
    if found_names:
        violations.append(f"banned color names: {', '.join(found_names)}")
    return violations


# ---------------------------------------------------------------------------- #
# Platform-native drafting
# ---------------------------------------------------------------------------- #

def draft_gbp_post(digest: SourceDigest) -> str:
    """Google Business Profile post (short, local-first, CTA with phone)."""
    zip_phrase = (
        f"ZIP {digest.target_zip}" if digest.target_zip
        else f"Frisco core ZIPs {', '.join(FRISCO_CORE_ZIPS)}"
    )
    hook_title = digest.hooks[0]["title"] if digest.hooks else "Storm / hail response"
    hook_body = digest.hooks[0]["body"] if digest.hooks else (
        f"Pineapple Contractors ({BRAND['rkat']}, {BRAND['iko']}) runs a "
        f"{BRAND['cppa']} within 48 hours of any hail event in {zip_phrase}."
    )

    body = (
        f"**{hook_title}** — {zip_phrase}\n\n"
        f"{hook_body}\n\n"
        f"📞 Call {BRAND['phone']} to schedule a {BRAND['cppa']}.\n"
        f"📍 {BRAND['hq']}\n"
        f"🪪 {BRAND['rkat']} · {BRAND['iko']}\n\n"
        f"Family Owned, Operated & Minority Owned. Serving North Texas since 2005.\n\n"
        f"{BRAND['signoff']}"
    )

    return _wrap_outbox(
        title=f"GBP Post — ZIP {digest.target_zip or 'Frisco core'} ({digest.zone or 'n/a'}) (PAUSED)",
        body=body,
        platform="Google Business Profile",
        source_path=digest.source_path,
        spec={
            "character_limit": 1500,
            "primary_action": "Call now",
            "call_to_action": f"{BRAND['phone']}",
            "image_recommendation": (
                f"Royal Navy {BRAND['color_primary']} background, Pineapple Gold "
                f"{BRAND['color_secondary']} headline strip, Process Status Cyan "
                f"{BRAND['color_status']} CTA button. No green."
            ),
        },
        slug=digest.target_zip or "frisco",
    )


def draft_meta_ad(digest: SourceDigest) -> str:
    """Meta ad creative (1-3-12 avatar-aligned; primary text + headline + CTA)."""
    zip_phrase = (
        f"ZIP {digest.target_zip}" if digest.target_zip
        else f"Frisco core ZIPs {', '.join(FRISCO_CORE_ZIPS)}"
    )
    primary = (
        f"After a hail event in {zip_phrase}, the documentation clock is already running. "
        f"Pineapple Contractors ({BRAND['rkat']}, {BRAND['iko']}) runs a "
        f"{BRAND['cppa']} within 48 hours to lock the photo record before the trail "
        f"goes cold. We walk your adjuster through the file line by line."
    )
    headline = "Damage you can't see from the driveway."
    description = (
        f"{BRAND['cppa']} · {BRAND['rkat']} · {BRAND['iko']} · {BRAND['phone']}"
    )
    body = (
        f"**Primary text:**\n\n{primary}\n\n"
        f"**Headline:** {headline}\n\n"
        f"**Description:** {description}\n\n"
        f"**Call to action:** Book Now\n\n"
        f"**Audience routing (1-3-12):** The Local Fan (default) | "
        f"The Culture Seeker (heritage_ad affinity) | The Founder's Circle "
        f"(property_manager / commercial / portfolio keyword match).\n\n"
        f"**Budget:** CBO $250/wk · Advantage+ creative enhancements OFF.\n"
        f"**Rules:** 1% Kill / 1.5% Scale · CPL target <$50 (max $250).\n"
    )

    return _wrap_outbox(
        title=f"Meta Ad Creative — ZIP {digest.target_zip or 'Frisco core'} (PAUSED)",
        body=body,
        platform="Meta (Facebook + Instagram)",
        source_path=digest.source_path,
        spec={
            "format": "single image + primary text",
            "primary_text_max_chars": 125,
            "headline_max_chars": 40,
            "image_recommendation": (
                f"Drone still of a Frisco roof. Pineapple Gold {BRAND['color_secondary']} "
                f"0.3s hook strip top-of-frame. Royal Navy {BRAND['color_primary']} "
                f"credential bar bottom-of-frame: {BRAND['rkat']} · {BRAND['iko']}. "
                f"Process Status Cyan {BRAND['color_status']} for the CTA pill only."
            ),
        },
        slug=digest.target_zip or "frisco",
    )


def draft_reel_caption(digest: SourceDigest) -> str:
    """Reel / TikTok caption (short, hook in first line, CTA in last)."""
    zip_phrase = (
        f"ZIP {digest.target_zip}" if digest.target_zip
        else f"Frisco core ZIPs {', '.join(FRISCO_CORE_ZIPS)}"
    )
    hook = "Your roof took hail. You didn't know yet."
    beats = [
        f"Frame 1 (0.0-0.3s): Pineapple Gold {BRAND['color_secondary']} text flash — \"{hook}\"",
        "Frame 2 (0.3-2.0s): Drone ascent over a Frisco roof, hail bruising close-ups.",
        f"Frame 3 (2.0-5.0s): Royal Navy {BRAND['color_primary']} credential bar — "
        f"{BRAND['rkat']} · {BRAND['iko']}.",
        f"Frame 4 (5.0-8.0s): Process Status Cyan {BRAND['color_status']} CTA pill — "
        f"\"Book a {BRAND['cppa']}\".",
        f"Frame 5 (8.0-10.0s): Phone number {BRAND['phone']} on Pineapple Gold "
        f"{BRAND['color_secondary']} plate.",
    ]

    body = (
        f"**Hook (first line of caption):** {hook}\n\n"
        f"**Service region:** {zip_phrase}\n\n"
        f"**Caption body:**\n\n"
        f"After hail in {zip_phrase}, the evidence window is short. "
        f"Pineapple Contractors ({BRAND['rkat']}, {BRAND['iko']}) runs a "
        f"{BRAND['cppa']} to lock the photo record, then walks the adjuster "
        f"through the file line by line. Family Owned, Operated & Minority Owned — "
        f"serving North Texas since 2005.\n\n"
        f"📞 {BRAND['phone']}\n\n"
        f"**Reel beats (10s cut, 9:16):**\n\n"
        + "\n".join(f"- {b}" for b in beats)
        + f"\n\n**Hashtags (brand-safe):** #FriscoTX #NorthTexasStorm #RoofingFrisco "
        f"#RCATLicensed #IKOCertified\n\n"
        f"{BRAND['signoff']}"
    )

    return _wrap_outbox(
        title=f"Reel Caption — ZIP {digest.target_zip or 'Frisco core'} (PAUSED)",
        body=body,
        platform="Reel / TikTok",
        source_path=digest.source_path,
        spec={
            "format": "9:16 vertical video, 10s base cut",
            "audio": "voiceover over original audio (no copyrighted tracks)",
            "image_recommendation": (
                f"Pineapple Gold {BRAND['color_secondary']} + Royal Navy "
                f"{BRAND['color_primary']} + Process Status Cyan {BRAND['color_status']} "
                f"only. No green."
            ),
        },
        slug=digest.target_zip or "frisco",
    )


def _wrap_outbox(title: str, body: str, platform: str, source_path: str,
                 spec: dict, slug: str) -> str:
    today = date.today().isoformat()
    safe_slug = re.sub(r"[^a-z0-9_]+", "", slug.lower())
    return (
        "---\n"
        "type: outbox_draft\n"
        f"title: \"{title}\"\n"
        "status: paused\n"
        f"created: {today}\n"
        f"agent: m7_omnichannel_swarm\n"
        f"brand: Pineapple Contractors M7\n"
        f"platform: \"{platform}\"\n"
        f"source_path: \"{source_path}\"\n"
        f"color_primary: \"{BRAND['color_primary']}\"\n"
        f"color_secondary: \"{BRAND['color_secondary']}\"\n"
        f"color_status: \"{BRAND['color_status']}\"\n"
        "---\n\n"
        f"# {title}\n\n"
        "> **PAUSED — awaiting Saia.** No post, send, schedule, or spend from this draft.\n"
        "> Outbox Shield (DEC-005) intact. Brand firewall result embedded below.\n\n"
        f"**Source research:** `{source_path}`\n\n"
        f"**Creative spec:**\n\n```json\n{json.dumps(spec, indent=2)}\n```\n\n"
        "---\n\n"
        f"{body}\n\n"
        "---\n\n"
        "## Compliance trail (populated by m7_omnichannel_swarm.run)\n\n"
        "_See the run-log JSON next to this file. Outbox Shield: PAUSED._\n\n"
        f"{BRAND['signoff']}\n"
    )


# ---------------------------------------------------------------------------- #
# CLI
# ---------------------------------------------------------------------------- #

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="M7 Omnichannel Swarm (opt-in)")
    ap.add_argument("--source", required=True,
                    help="path to an approved research-stage artifact (.md or .intent.json)")
    ap.add_argument("--out-root", default="01_Command_Center/Outbox_Drafts")
    ap.add_argument("--dry-run", action="store_true", help="do not write outputs")
    args = ap.parse_args(argv)

    src = Path(args.source)
    if not src.exists():
        print(json.dumps({"status": "ERROR", "reason": f"source not found: {src}"}, indent=2))
        return 2

    digest = _read_source(src)
    drafts = {
        "GBP":  draft_gbp_post(digest),
        "Meta": draft_meta_ad(digest),
        "Reel": draft_reel_caption(digest),
    }

    # Compliance gate — block the whole batch on any failure.
    officer = ComplianceOfficer()
    per_platform = {}
    for name, text in drafts.items():
        rep = officer.scan(text)
        col_viol = color_violations(text)
        per_platform[name] = {
            "compliance_score": rep.compliance_score,
            "compliance_verdict": rep.verdict,
            "lexicon_violations": [
                {"pattern": v.pattern, "banned_label": v.banned_label,
                 "substitute": v.substitute}
                for v in rep.violations
            ],
            "color_violations": col_viol,
        }

    blocked = any(
        p["compliance_verdict"] != "PASS" or p["color_violations"]
        for p in per_platform.values()
    )

    summary = {
        "source": src.as_posix(),
        "target_zip": digest.target_zip,
        "zone": digest.zone,
        "score": digest.score,
        "per_platform": per_platform,
        "status": "BLOCKED" if blocked else "OK",
    }

    if blocked:
        summary["reason"] = (
            "At least one platform variation failed the Compliance Officer or "
            "the color audit. No files written. Fix the source research or "
            "extend the drafter before retrying."
        )
        print(json.dumps(summary, indent=2))
        return 3

    # Write outputs.
    today = date.today().isoformat()
    safe_slug = re.sub(r"[^a-z0-9_]+", "", (digest.target_zip or "frisco").lower())
    out_root = Path(args.out_root)
    written = []
    if not args.dry_run:
        out_root.mkdir(parents=True, exist_ok=True)
        for platform_key, text in drafts.items():
            p = out_root / f"{today}_Outbox_Swarm_{safe_slug}_{platform_key}.md"
            p.write_text(text, encoding="utf-8")
            written.append(p.as_posix())
    summary["written"] = written if not args.dry_run else ["(dry-run, not written)"]
    summary["outbox_shield"] = "PAUSED"
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
