# -*- coding: utf-8 -*-
"""
M7 Lexicon Gate Parser — scrubs generated CONTENT before staging.
Destination: /04_Tech_Lab/scripts/

FIX (2026-07-17): the original draft contained a gate that replaced EVERY
occurrence of "roof"/"roofing"/"roofs" with a long phrase. That would mangle
all copy ("roofing company" -> nonsense). REMOVED. This parser only fixes real
brand violations, not the word "roof".

Use on generated marketing/content strings, NOT on the rulebook config files
(those legitimately contain the words "free"/"green" as governance references).
"""
import re

LEXICON_GATES = {
    r"(?i)\bfree\s+inspection\b": "Complimentary Professional Photo Audit (CPPA)",
    r"(?i)\bfree\s+quote\b": "Complimentary Professional Photo Audit (CPPA)",
    r"(?i)\$0\s+down\b": "Full Restoration Coverage",
    r"(?i)\$0\s+out\s+of\s+pocket\b": "Full Restoration Coverage",
    r"(?i)\bGAF\s+certified\b": "IKO Certified",
    r"(?i)\bGAF\b": "IKO Certified",
}
# Terms that should never appear in customer-facing output (flag, don't auto-fix — a
# human should rewrite the sentence rather than have a word silently deleted).
BANNED_FLAG = [r"(?i)\bwarrior\b", r"(?i)\btoa\b", r"(?i)\bsix brothers\b",
               r"(?i)\bcheap\b", r"(?i)\bbargain\b", r"(?i)\bdiscount\b", r"(?i)\bgreen\b"]
SIGNATURE = "Ko e hala 'o e fononga ko e faka'apa'apa."


def scrub(text: str) -> str:
    """Auto-fix the safe mutations. Returns cleaned text."""
    for pattern, replacement in LEXICON_GATES.items():
        text = re.sub(pattern, replacement, text)
    return text


def flags(text: str):
    """Return a list of banned terms still present (needs human rewrite)."""
    hits = []
    for pattern in BANNED_FLAG:
        m = re.search(pattern, text)
        if m:
            hits.append(m.group(0))
    return hits


if __name__ == "__main__":
    sample = "Get a Free Inspection today with a $0 down GAF Certified roof replacement!"
    cleaned = scrub(sample)
    print("BEFORE:", sample)
    print("AFTER :", cleaned)
    remaining = flags(cleaned)
    print("FLAGS :", remaining if remaining else "none — clean")
