#!/usr/bin/env python3
"""
M7 FACTORY — runs the 05_Campaign_Factory stage-contract pipeline end to end:
  10_Research_Stage  ->  20_Copy_Drafting  ->  30_Compliance_Audit  ->  Outbox_Drafts

Each artifact moves in the universal envelope (CROSS_AGENT_PROTOCOL.md). The
compliance stage runs the brand firewall; only files with zero green violations
and mutated lexicon are APPROVED and written to 01_Command_Center/Outbox_Drafts/
in a PAUSED state (Outbox Shield). Nothing is ever published live.

Usage
-----
    python m7_factory.py --demo          # run with sample intent
    python m7_factory.py                 # consume 10_Research_Stage/output/intent.json

Ko e hala 'o e fononga ko e faka'apa'apa.
"""
from __future__ import annotations
import argparse, hashlib, json, re, sys, uuid
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parents[2] if len(Path(__file__).resolve().parents) >= 3 else Path.cwd()

LEXICON = [
    (re.compile(r"free\s+inspection", re.I), "Complimentary Professional Photo Audit (CPPA)"),
    (re.compile(r"free\s+quote", re.I), "Complimentary Professional Photo Audit (CPPA)"),
    (re.compile(r"\$0\s*(down|out\s*of\s*pocket)", re.I), "Full Restoration Coverage"),
    (re.compile(r"save\s+money", re.I), "Protecting your family's investment"),
    (re.compile(r"gaf\s+certified", re.I), "IKO Certified (RCAT License #03-0637)"),
    (re.compile(r"six\s+brothers", re.I), "The Pineapple Standard"),
    (re.compile(r"\bwarrior\b", re.I), "The Pineapple Standard"),
    (re.compile(r"\btoa\b", re.I), "The Pineapple Standard"),
    (re.compile(r"\bconsultation\b", re.I), "Complimentary Professional Photo Audit (CPPA)"),
    (re.compile(r"\bfree\b", re.I), "Complimentary"),
]
GREEN = [re.compile(p, re.I) for p in
         [r"#00ff00\b", r"#2d7d46\b", r"#008000\b", r"\bgreen\b",
          r"\b(lime|forestgreen|seagreen|darkgreen|lightgreen)\b",
          r"\b(bg|text|border)-green-\d{2,3}\b"]]


def now():
    return datetime.now(timezone.utc).isoformat()


def sha(payload) -> str:
    return "sha256:" + hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()[:32]


def envelope(stage, nxt, producer, payload, state="READY"):
    return {
        "m7_protocol_version": "1.0", "envelope_id": str(uuid.uuid4()),
        "trace_id": str(uuid.uuid4()), "timestamp_utc": now(),
        "stage": stage, "next_stage": nxt,
        "producer": {"agent": producer}, "state": state,
        "payload": payload, "signature": sha(payload),
        "outbox_shield": {"delivery_state": "PAUSED", "human_authorization_required": True},
        "closing": "Ko e hala 'o e fononga ko e faka'apa'apa.",
    }


def mutate(text):
    n = 0
    for rx, repl in LEXICON:
        if rx.search(text):
            n += len(rx.findall(text))
            text = rx.sub(repl, text)
    return text, n


def green_hits(text):
    return sum(1 for rx in GREEN if rx.search(text))


SAMPLE_INTENT = {
    "intent_profiles": [
        {"query": "frisco hail roof claim", "avatar": "local_fan",
         "content_gaps": ["30-day deadline math", "photo-audit-first vs adjuster"],
         "zips": ["75033", "75034"]},
        {"query": "commercial TPO storm portfolio", "avatar": "founders_circle",
         "content_gaps": ["multi-property documentation"], "zips": ["75035"]},
    ]
}


def draft_from_intent(profiles):
    drafts = []
    for p in profiles:
        av = p.get("avatar", "local_fan")
        drafts.append({
            "angle": "deadline", "avatar": av,
            "hook": "Frisco hail hit — your 30-day claim window is open.",
            "body": ("We document everything with a Complimentary Professional Photo Audit "
                     "(CPPA) so you get comprehensive documentation for a successful claim."),
            "cta": "Reserve your CPPA — 20 minutes, drone + ground.",
            "video_spec": {"engine": "50/5/3", "runtime_s": 50,
                           "hook_frames": "0-15", "end_card_frames": "1411-1500"},
        })
    return drafts


def main(argv=None):
    ap = argparse.ArgumentParser(description="M7 Campaign Factory pipeline")
    ap.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    ap.add_argument("--demo", action="store_true")
    args = ap.parse_args(argv)
    root = args.root.resolve()
    factory = root / "05_Campaign_Factory"
    outbox = root / "01_Command_Center" / "Outbox_Drafts"
    outbox.mkdir(parents=True, exist_ok=True)

    # STAGE 10 -> intent
    intent_path = factory / "10_Research_Stage" / "output" / "intent.json"
    if args.demo or not intent_path.exists():
        intent = SAMPLE_INTENT
    else:
        intent = json.loads(intent_path.read_text(encoding="utf-8"))
    (factory / "10_Research_Stage" / "output").mkdir(parents=True, exist_ok=True)
    intent_path.write_text(json.dumps(intent, indent=2), encoding="utf-8")

    # STAGE 20 -> draft
    drafts = draft_from_intent(intent.get("intent_profiles", []))
    draft_env = envelope("20_Copy_Drafting", "30_Compliance_Audit", "claude_code", {"drafts": drafts})
    draft_dir = factory / "20_Copy_Drafting" / "output"
    draft_dir.mkdir(parents=True, exist_ok=True)
    (draft_dir / "draft_copy.json").write_text(json.dumps(draft_env, indent=2), encoding="utf-8")

    # STAGE 30 -> compliance audit + Outbox writeback
    approved, rejected = [], []
    today = f"{datetime.now():%Y-%m-%d}"
    for i, d in enumerate(drafts, 1):
        blob = "\n".join([d["hook"], d["body"], d["cta"]])
        mutated, n = mutate(blob)
        g = green_hits(mutated)
        if g == 0:
            rec = {"ref": f"draft#{i}", "avatar": d["avatar"], "final_copy": mutated,
                   "firewall_pass": True, "green_violations": 0, "lexicon_mutations": n, "score": 100}
            approved.append(rec)
            # Outbox writeback (PAUSED)
            md = (f"---\ntype: outbox_draft\nstatus: PAUSED\navatar: {d['avatar']}\n"
                  f"created: {today}\nfirewall_pass: true\n---\n\n"
                  f"# {d['avatar']} — {d['angle']}\n\n{mutated}\n\n"
                  f"> DELIVERY STATE: PAUSED. Human authorization required (Outbox Shield).\n\n"
                  f"Ko e hala 'o e fononga ko e faka'apa'apa.\n")
            (outbox / f"{today}_Outbox_{d['avatar']}_{i}.md").write_text(md, encoding="utf-8")
        else:
            rejected.append({"ref": f"draft#{i}", "green_violations": g})

    audit = envelope("30_Compliance_Audit", "Outbox_Drafts", "openclaw",
                     {"approved": approved, "rejected": rejected, "delivery_state": "PAUSED"},
                     state="APPROVED" if not rejected else "REJECTED")
    audit_dir = factory / "30_Compliance_Audit" / "output"
    audit_dir.mkdir(parents=True, exist_ok=True)
    (audit_dir / "approved.json").write_text(json.dumps(audit, indent=2), encoding="utf-8")

    print(json.dumps({
        "pipeline": "10 -> 20 -> 30 -> Outbox_Drafts",
        "drafted": len(drafts), "approved": len(approved), "rejected": len(rejected),
        "outbox_written": [p.name for p in outbox.glob(f"{today}_Outbox_*.md")],
        "delivery_state": "PAUSED (Outbox Shield)",
        "closing": "Ko e hala 'o e fononga ko e faka'apa'apa.",
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
