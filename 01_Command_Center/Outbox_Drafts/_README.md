# Outbox Calibration Shield — Draft Sink
All automated outbound copy (lead reactivations, review requests, WhatsApp follow-ups, Meta replies, email drips) MUST land in this folder as a DRAFT. No agent, script, or cron job may call any send/transmit/publish API directly. Humans own the send button.

## File naming convention
`<YYYY-MM-DD>_<channel>_<lead_or_job_id>_DRAFT.md`

## Required file header
```
STATUS: DRAFT — DO NOT SEND
INTENT: <one-sentence intent statement>
TARGET_PERSONA: <Multi-Unit PM | Luxury Homeowner | Hotel Mgmt | etc.>
GUARDRAILS_PASSED: [ ] Compliance [ ] Skeptic [ ] Brand Manager
```

See `../tatafu.md` Section 3 for the full Outbox Calibration Shield law.
