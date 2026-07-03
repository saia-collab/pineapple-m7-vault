---
type: cross_agent_communication_protocol
status: active
last_updated: 2026-06-16
classification: M7_Command_Level_1
color_primary: "#1A365D"
color_secondary: "#FBC02D"
color_status: "#00BFFF"
---

# M7 — CROSS-AGENT FRONTIER COMMUNICATION PROTOCOL

Universal JSON telemetry contract passed between **Claude Code**, **Hermes**, **OpenClaw**, and **NotebookLM** workflows through the `CONTEXT.md` input/output gates of the `05_Campaign_Factory` Stage-Contract line. One envelope format, strict state synchronization, zero data drift.

---

## 1. THE UNIVERSAL ENVELOPE

Every artifact crossing a stage gate is wrapped in this envelope. Required fields are non-negotiable; a missing required field rejects the artifact upstream.

```json
{
  "m7_protocol_version": "1.0",
  "envelope_id": "uuid-v4",
  "trace_id": "uuid-v4",
  "timestamp_utc": "2026-06-16T18:00:00Z",
  "stage": "10_Research_Stage",
  "next_stage": "20_Copy_Drafting",
  "producer": {
    "agent": "claude_code",
    "role": "research",
    "model": "claude-opus-4-8"
  },
  "consumer": {
    "agent": "hermes",
    "role": "synthesis"
  },
  "state": "READY",
  "compliance": {
    "firewall_pass": true,
    "green_violations": 0,
    "lexicon_mutations": 0,
    "palette_ok": true,
    "audited_by": "brand_firewall.py",
    "audited_at": "2026-06-16T18:00:01Z"
  },
  "payload": { },
  "lineage": [
    {"stage": "10_Research_Stage", "agent": "claude_code", "ts": "2026-06-16T17:59:00Z"}
  ],
  "outbox_shield": {
    "delivery_state": "PAUSED",
    "human_authorization_required": true
  },
  "signature": "sha256:<hash-of-payload>",
  "closing": "Ko e hala 'o e fononga ko e faka'apa'apa."
}
```

### Field rules

- `m7_protocol_version` — pinned; agents reject mismatched majors.
- `trace_id` — constant across the full pipeline run; `envelope_id` is per-hop.
- `state` — one of `DRAFT | READY | REJECTED | APPROVED | BLOCKED`.
- `compliance.firewall_pass` — must be `true` for `state: APPROVED`. Any `green_violations > 0` forces `state: BLOCKED`.
- `signature` — SHA-256 of the canonical `payload` so the consumer can detect drift/tampering.
- `outbox_shield.delivery_state` — always `PAUSED` until an authorized human flips it.

---

## 2. AGENT ROLE REGISTRY

| Agent | Primary Stage | Role | Reads | Writes |
| :--- | :--- | :--- | :--- | :--- |
| **NotebookLM** | pre-10 | Source grounding | `03_Knowledge_Mat\` | `10_Research_Stage\input\` |
| **Claude Code** | 10 → 20 | Research + drafting | `input\`, `GROUNDING.md` | `intent.json`, `draft_copy.json` |
| **Hermes** | orchestration | Scheduler / router | all stage gates | `lineage`, state transitions |
| **OpenClaw** | 30 | Compliance audit gateway | `draft_copy.json` | `approved.json` |

---

## 3. STAGE-GATE PAYLOAD SCHEMAS

### 3.1 `10_Research_Stage` → output `intent.json`

```json
{
  "intent_profiles": [
    {
      "query": "frisco hail roof claim window",
      "avatar": "local_fan",
      "search_intent": "commercial",
      "content_gaps": ["30-day claim deadline math", "CPPA vs adjuster-first"],
      "lead_score_hint": 70,
      "zips": ["75033", "75034"]
    }
  ],
  "source_grounding": ["nws_hail_2026-06", "g2_voc_roofing"]
}
```

### 3.2 `20_Copy_Drafting` → output `draft_copy.json`

```json
{
  "drafts": [
    {
      "angle": "deadline",
      "avatar": "local_fan",
      "hook": "Frisco hail hit — your 30-day claim window is open.",
      "body": "We document everything with a Complimentary Professional Photo Audit (CPPA)...",
      "cta": "Reserve your CPPA — 20 minutes, drone + ground.",
      "video_spec": {"engine": "50/5/3", "runtime_s": 50, "hook_frames": "0-15", "end_card_frames": "1411-1500"},
      "compliance_prechecked": true
    }
  ]
}
```

### 3.3 `30_Compliance_Audit` → output `approved.json`

```json
{
  "approved": [
    {
      "ref": "draft#1",
      "final_copy": "Frisco hail hit — your 30-day claim window is open...",
      "firewall_pass": true,
      "green_violations": 0,
      "lexicon_mutations": 0,
      "palette_ok": true,
      "score": 100
    }
  ],
  "rejected": [],
  "delivery_state": "PAUSED"
}
```

---

## 4. STATE-SYNCHRONIZATION RULES (NO DRIFT)

1. **Single trace, append-only lineage.** Every hop appends to `lineage`; no agent rewrites prior entries.
2. **Compliance is a gate, not a suggestion.** An envelope cannot advance to `next_stage` unless `compliance.firewall_pass === true` and `green_violations === 0`.
3. **Signature verification on read.** The consumer recomputes `sha256(payload)`; mismatch → `state: REJECTED`, returned upstream.
4. **Idempotent hops.** Re-delivering the same `envelope_id` is a no-op (consumers dedupe on `envelope_id`).
5. **Outbox Shield is terminal.** No agent may set `delivery_state` to anything but `PAUSED`; only an authorized human flips it at the Outbox.
6. **Schema-version pinning.** Mismatched `m7_protocol_version` major → `state: BLOCKED` with a human alert.
7. **Heartbeat.** Hermes writes a `lineage` heartbeat every 15 minutes for long-running goals so stalled stages are detectable.

---

## 5. CONTEXT.md GATE BINDING

Each `05_Campaign_Factory` stage folder's `CONTEXT.md` declares which envelope `state` it accepts and emits:

```text
10_Research_Stage  : accepts state DRAFT   -> emits state READY
20_Copy_Drafting   : accepts state READY   -> emits state READY (compliance_prechecked)
30_Compliance_Audit: accepts state READY   -> emits state APPROVED | REJECTED
```

---

Ko e hala 'o e fononga ko e faka'apa'apa.

<!-- M7-FIREWALL-EXEMPT: governance-reference -->
