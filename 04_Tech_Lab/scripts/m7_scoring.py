#!/usr/bin/env python3
"""
PINEAPPLE CONTRACTORS M7 — LEAD & CAMPAIGN SCORING ENGINE
=========================================================
Implements:
  * The Elite Lead Scoring Matrix (1-100) with multi-avatar classification.
  * The 1-3-12 Meta Offensive rule engine (1% Kill Rule / 1.5% Scale Rule).
  * Avatar routing: The Local Fan, The Culture Seeker, The Founder's Circle.

Single source of truth: 01_Command_Center/MASTER_PLAYBOOK.md

Usage
-----
    python m7_scoring.py --lead lead.json          # score one lead
    python m7_scoring.py --leads leads.json        # score an array of leads
    python m7_scoring.py --campaign creatives.json # apply 1-3-12 kill/scale rules
    python m7_scoring.py --compliance-text "..."   # run M7 Elite Compliance Filter
    python m7_scoring.py --demo                     # run built-in sample

Ko e hala 'o e fononga ko e faka'apa'apa.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path

# --------------------------------------------------------------------------- #
# CONSTITUTION CONSTANTS (mirror MASTER_PLAYBOOK.md)
# --------------------------------------------------------------------------- #

MIN_PROJECT_VALUE = 18_000          # baseline entry; below = auto-reject
DISPATCH_THRESHOLD = 80             # score >= 80 -> same-day dispatch to Saia
SPEED_TO_LEAD_SECONDS = 300         # 5 minutes; older = dead

FRISCO_ZIPS = {"75033", "75034", "75035", "75067", "75068"}
LUXURY_ENCLAVES = {"starwood", "newman village"}

# Lead scoring weights (Elite Lead Scoring Matrix)
W_FRISCO_ZIP = 25
W_PROPERTY_MANAGER = 30
W_LUXURY_ESTATE = 20          # $700K+ estate
W_STORM_MENTION = 20
W_COMMERCIAL = 15
W_ENCLAVE_BONUS = 10

# 1-3-12 Meta Offensive rules
CTR_KILL = 1.0               # below 1.0% after window -> PAUSE
CTR_SCALE = 1.5              # above 1.5% with CPL ok -> scale 15%
CPL_TARGET = 50.0            # target cost per lead
CPL_MAX = 250.0             # absolute ceiling
STABILIZE_HOURS = 48
STABILIZE_IMPRESSIONS = 1000
SCALE_INTERVAL = 0.15        # +15% budget weighting

# --------------------------------------------------------------------------- #
# AVATARS
# --------------------------------------------------------------------------- #

AVATARS = {
    "local_fan": "The Local Fan",
    "culture_seeker": "The Culture Seeker",
    "founders_circle": "The Founder's Circle",
}


def classify_avatar(lead: dict) -> str:
    """Route a lead to one of the three 1-3-12 ad-set avatars."""
    title = (lead.get("title") or "").lower()
    prop_type = (lead.get("property_type") or "").lower()
    age = lead.get("age")
    zip_code = str(lead.get("zip") or "")

    # The Founder's Circle: B2B commercial owners, property managers, investors.
    if any(k in title for k in ("property manager", "owner", "operator",
                                "investor", "portfolio", "hotel")) \
       or prop_type in ("commercial", "warehouse", "retail", "multi-family"):
        return "founders_circle"

    # The Culture Seeker: heritage / community-driven flags.
    if lead.get("heritage_affinity") or lead.get("community_referral"):
        return "culture_seeker"

    # The Local Fan: Frisco homeowners 35-65 near The Star.
    if zip_code in FRISCO_ZIPS and (age is None or 35 <= int(age) <= 65):
        return "local_fan"

    # Default fallback -> Local Fan (geo-anchored).
    return "local_fan"


# --------------------------------------------------------------------------- #
# LEAD SCORING
# --------------------------------------------------------------------------- #

@dataclass
class ScoredLead:
    lead_id: str
    score: int = 0
    avatar: str = ""
    avatar_label: str = ""
    rejected: bool = False
    reject_reason: str = ""
    dispatch: bool = False
    breakdown: dict = field(default_factory=dict)
    notes: list = field(default_factory=list)


def score_lead(lead: dict) -> ScoredLead:
    lead_id = str(lead.get("id") or lead.get("phone") or "unknown")
    result = ScoredLead(lead_id=lead_id)

    # Hard gate: minimum project value.
    est_value = float(lead.get("estimated_value") or 0)
    if est_value and est_value < MIN_PROJECT_VALUE:
        result.rejected = True
        result.reject_reason = f"Below ${MIN_PROJECT_VALUE:,} baseline (est ${est_value:,.0f})"
        return result

    bd = {}
    zip_code = str(lead.get("zip") or "")
    title = (lead.get("title") or "").lower()
    home_value = float(lead.get("home_value") or 0)
    prop_type = (lead.get("property_type") or "").lower()
    enclave = (lead.get("enclave") or "").lower()
    notes_text = (lead.get("notes") or "").lower()

    if zip_code in FRISCO_ZIPS:
        bd["frisco_zip"] = W_FRISCO_ZIP
    if "property manager" in title or "manager" in title:
        bd["property_manager"] = W_PROPERTY_MANAGER
    if home_value >= 700_000:
        bd["luxury_estate_700k"] = W_LUXURY_ESTATE
    if lead.get("storm_damage") or "storm" in notes_text or "hail" in notes_text:
        bd["storm_mention"] = W_STORM_MENTION
    if prop_type in ("commercial", "warehouse", "retail", "multi-family"):
        bd["commercial"] = W_COMMERCIAL
    if enclave in LUXURY_ENCLAVES:
        bd["enclave_bonus"] = W_ENCLAVE_BONUS

    total = min(100, sum(bd.values()))
    result.score = total
    result.breakdown = bd
    result.avatar = classify_avatar(lead)
    result.avatar_label = AVATARS[result.avatar]
    result.dispatch = total >= DISPATCH_THRESHOLD

    if result.dispatch:
        result.notes.append(f"Score {total} >= {DISPATCH_THRESHOLD}: same-day dispatch alert -> Saia.")
    if est_value:
        result.notes.append(f"Estimated value ${est_value:,.0f} qualifies (>= ${MIN_PROJECT_VALUE:,}).")

    # Speed-to-lead check.
    created = lead.get("created_epoch")
    if created:
        age_sec = datetime.now(timezone.utc).timestamp() - float(created)
        if age_sec > SPEED_TO_LEAD_SECONDS:
            result.notes.append(
                f"WARNING: lead age {age_sec/60:.1f}m exceeds 5m speed-to-lead window (flagged dead)."
            )
    return result


# --------------------------------------------------------------------------- #
# 1-3-12 META OFFENSIVE — CREATIVE RULE ENGINE
# --------------------------------------------------------------------------- #

def evaluate_creative(creative: dict) -> dict:
    """Apply the 1% Kill Rule and 1.5% Scale Rule to a single creative."""
    ctr = float(creative.get("ctr", 0))            # percent
    cpl = float(creative.get("cpl", 0))            # dollars
    impressions = int(creative.get("impressions", 0))
    hours = float(creative.get("hours_live", 0))
    name = creative.get("name", "creative")

    stabilized = hours >= STABILIZE_HOURS or impressions >= STABILIZE_IMPRESSIONS
    action = "HOLD"
    reason = "Within stabilization window — monitoring."

    if stabilized and ctr < CTR_KILL:
        action = "PAUSE"
        reason = f"CTR {ctr:.2f}% < {CTR_KILL}% after stabilization (1% Kill Rule)."
    elif ctr > CTR_SCALE and cpl and cpl < CPL_TARGET:
        action = "SCALE"
        reason = f"CTR {ctr:.2f}% > {CTR_SCALE}% and CPL ${cpl:.0f} < ${CPL_TARGET:.0f} (+{int(SCALE_INTERVAL*100)}%)."
    elif cpl and cpl > CPL_MAX:
        action = "PAUSE"
        reason = f"CPL ${cpl:.0f} exceeds absolute max ${CPL_MAX:.0f}."

    return {
        "name": name, "avatar": creative.get("avatar", "unassigned"),
        "ctr": ctr, "cpl": cpl, "stabilized": stabilized,
        "action": action, "reason": reason,
        # Outbox Shield: any spend change is staged PAUSED for human authorization.
        "delivery_state": "PAUSED",
    }


def evaluate_campaign(payload: dict) -> dict:
    creatives = payload.get("creatives", [])
    results = [evaluate_creative(c) for c in creatives]
    return {
        "campaign": payload.get("campaign", "1-3-12 Meta Offensive"),
        "budget_weekly": payload.get("budget_weekly", 250),
        "evaluated": len(results),
        "to_pause": [r["name"] for r in results if r["action"] == "PAUSE"],
        "to_scale": [r["name"] for r in results if r["action"] == "SCALE"],
        "results": results,
        "note": "All delivery states hardcoded PAUSED (Outbox Shield). Human authorization required to activate.",
    }


# --------------------------------------------------------------------------- #
# M7 ELITE COMPLIANCE FILTER (CLAUDE.md §2.1 — banned lexicon)
# --------------------------------------------------------------------------- #

# Each entry: (banned_pattern, required_substitute, compiled_regex).
# Patterns are case-insensitive whole-phrase matches with word boundaries so
# legitimate copy ("affordable") is not falsely flagged.
FORBIDDEN_COMPLIANCE_PATTERNS = [
    ("FREE",                    "Complimentary Professional Photo Audit (CPPA)",
     re.compile(r"\bfree\b", re.IGNORECASE)),
    ("$0 Out of Pocket",        "Full restoration coverage evaluation",
     re.compile(r"\$\s*0\s*(out\s*of\s*pocket|down)\b", re.IGNORECASE)),
    ("$0 Down",                 "Full restoration coverage evaluation",
     re.compile(r"\$\s*0\s*down\b", re.IGNORECASE)),
    ("cheap",                   "CPPA / value-engineered",
     re.compile(r"\bcheap\b", re.IGNORECASE)),
    ("low cost",                "CPPA / value-engineered",
     re.compile(r"\blow\s*cost\b", re.IGNORECASE)),
    ("bargain",                 "CPPA / value-engineered",
     re.compile(r"\bbargain\b", re.IGNORECASE)),
    ("discount",                "CPPA / value-engineered",
     re.compile(r"\bdiscount\b", re.IGNORECASE)),
    ("FREE Inspection",         "Complimentary Professional Photo Audit (CPPA)",
     re.compile(r"\bfree\s+inspection\b", re.IGNORECASE)),
    ("we beat your insurance",  "Comprehensive documentation for a successful claim",
     re.compile(r"\bwe\s+beat\s+your\s+insurance\b", re.IGNORECASE)),
    ("denial-buster",           "Comprehensive documentation for a successful claim",
     re.compile(r"\bdenial[\s-]?buster\b", re.IGNORECASE)),
    ("GAF Certified",           "IKO Certified",
     re.compile(r"\bgaf\s+certified\b", re.IGNORECASE)),
    ("Warrior Standard",        "The Pineapple Standard",
     re.compile(r"\bwarrior\s+standard\b", re.IGNORECASE)),
    ("Toa Standard",            "The Pineapple Standard",
     re.compile(r"\btoa\s+standard\b", re.IGNORECASE)),
    ("Six Brothers Narrative",  "Family Owned, Operated & Minority Owned",
     re.compile(r"\bsix\s+brothers\b", re.IGNORECASE)),
    ("$18,000+ High-Value Jobs","Premium Estate & Commercial Portfolio Restoration",
     re.compile(r"\$18,?000\+?\s*high[\s-]?value\s+jobs\b", re.IGNORECASE)),
]


@dataclass
class ComplianceViolation:
    pattern: str        # banned term as it appeared (raw)
    banned_label: str   # canonical banned label from FORBIDDEN_COMPLIANCE_PATTERNS
    substitute: str     # required substitute per CLAUDE.md §2.1
    spans: list         # list of (start, end) char offsets in the input


@dataclass
class ComplianceReport:
    text: str
    violations: list = field(default_factory=list)
    compliance_score: int = 100
    verdict: str = "PASS"
    notes: list = field(default_factory=list)


class ComplianceOfficer:
    """M7 Elite Compliance Officer — enforces CLAUDE.md §2.1 banned lexicon."""

    # Each unique violation costs 25 points; 4+ violations = 0 score, FAIL.
    VIOLATION_PENALTY = 25
    MIN_SCORE = 0

    def __init__(self, patterns=FORBIDDEN_COMPLIANCE_PATTERNS):
        self.patterns = patterns

    def scan(self, text: str) -> ComplianceReport:
        report = ComplianceReport(text=text)
        for banned_label, substitute, regex in self.patterns:
            spans = [(m.start(), m.end()) for m in regex.finditer(text)]
            if not spans:
                continue
            # Record the actual surface forms for the evidence trail.
            surfaces = list({text[s:e] for s, e in spans})
            for surface in surfaces:
                report.violations.append(ComplianceViolation(
                    pattern=surface,
                    banned_label=banned_label,
                    substitute=substitute,
                    spans=[(s, e) for s, e in spans if text[s:e].lower() == surface.lower()],
                ))
        # Deduplicate by (banned_label, surface) so multi-occurrence surfaces
        # still count as one violation per banned term.
        seen = set()
        unique = []
        for v in report.violations:
            key = (v.banned_label, v.pattern.lower())
            if key in seen:
                continue
            seen.add(key)
            unique.append(v)
        report.violations = unique

        penalty = len(report.violations) * self.VIOLATION_PENALTY
        report.compliance_score = max(self.MIN_SCORE, 100 - penalty)
        report.verdict = "FAIL" if report.violations else "PASS"
        if report.violations:
            report.notes.append(
                f"{len(report.violations)} banned term(s) detected — FAIL. "
                "Outbox Shield: do not publish. Drafts only to "
                "01_Command_Center/Outbox_Drafts/."
            )
        else:
            report.notes.append("No banned lexicon detected — PASS.")
        return report


# --------------------------------------------------------------------------- #
# I/O HELPERS + DEMO
# --------------------------------------------------------------------------- #

def _load(path: str):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _emit(obj):
    print(json.dumps(obj, indent=2, default=str))


DEMO_LEADS = [
    {"id": "L-001", "zip": "75034", "age": 47, "title": "Homeowner",
     "home_value": 950_000, "estimated_value": 42_000, "storm_damage": True,
     "enclave": "Starwood", "property_type": "residential"},
    {"id": "L-002", "zip": "75035", "title": "Commercial Property Manager",
     "property_type": "commercial", "estimated_value": 88_000,
     "notes": "hail across the retail portfolio"},
    {"id": "L-003", "zip": "76210", "age": 39, "title": "Homeowner",
     "estimated_value": 9_500, "property_type": "residential"},
]

DEMO_CAMPAIGN = {
    "campaign": "The Pineapple Standard — Professional Photo Audit",
    "budget_weekly": 250,
    "creatives": [
        {"name": "LF_Deadline_01", "avatar": "local_fan", "ctr": 0.6, "cpl": 70, "impressions": 1400, "hours_live": 50},
        {"name": "CS_Heritage_04", "avatar": "culture_seeker", "ctr": 1.9, "cpl": 38, "impressions": 2200, "hours_live": 60},
        {"name": "FC_Portfolio_09", "avatar": "founders_circle", "ctr": 1.2, "cpl": 120, "impressions": 600, "hours_live": 20},
    ],
}


def main(argv=None):
    ap = argparse.ArgumentParser(description="M7 Lead & Campaign Scoring Engine")
    ap.add_argument("--lead", help="path to single lead JSON")
    ap.add_argument("--leads", help="path to JSON array of leads")
    ap.add_argument("--campaign", help="path to campaign creatives JSON")
    ap.add_argument("--compliance-text", help="run M7 Elite Compliance Filter on inline text")
    ap.add_argument("--demo", action="store_true", help="run built-in sample data")
    args = ap.parse_args(argv)

    if args.demo:
        _emit({
            "leads": [asdict(score_lead(l)) for l in DEMO_LEADS],
            "campaign": evaluate_campaign(DEMO_CAMPAIGN),
        })
        return 0
    if args.lead:
        _emit(asdict(score_lead(_load(args.lead))))
        return 0
    if args.leads:
        _emit([asdict(score_lead(l)) for l in _load(args.leads)])
        return 0
    if args.campaign:
        _emit(evaluate_campaign(_load(args.campaign)))
        return 0
    if args.compliance_text is not None:
        officer = ComplianceOfficer()
        report = officer.scan(args.compliance_text)
        _emit({
            "compliance_score": report.compliance_score,
            "verdict": report.verdict,
            "violation_count": len(report.violations),
            "violations": [asdict(v) for v in report.violations],
            "notes": report.notes,
            "scanned_text": report.text,
        })
        return 0

    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
