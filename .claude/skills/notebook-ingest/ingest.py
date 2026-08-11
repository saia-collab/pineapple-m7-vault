#!/usr/bin/env python3
"""
M7 notebook-ingest engine
--------------------------
Turns a NotebookLM note-list JSON dump into scrubbed, structured vault notes.

- INCREMENTAL: dedups by note_id (via a ledger + by scanning existing files),
  so re-pulling a still-growing notebook only adds the NEW notes.
- BRAND-LOCK scrub: strips Tongan proverbs, GAF -> IKO Certified,
  customer-facing "free <offer>" -> Complimentary Professional Photo Audit (CPPA).
- ROUTES code notes (.py/.bat/.sql/...) into _code_DRAFTS/ (never run automatically).
- Writes _INDEX.md (all files) and appends new prompt/code blocks to _PROMPTS_LIBRARY.md.

Usage:
  python ingest.py --src "<note-json-file>" --label "PM7 SEO Mastery" \
                   --notebook-id <uuid> --out NotebookLM_SEO_Mastery_2026-08-11

The --src file is what the notebooklm MCP `note(action=list)` returns (or the
file path it saves to when the result is large).
"""
import os, re, json, glob, argparse

VAULT = r"C:\Pineapple Contractors M7"
RES   = os.path.join(VAULT, "03_Knowledge_Mat", "Resources")
LEDGER = os.path.join(RES, ".notebook_ingest_ledger.json")

PROV   = re.compile(r'.*(faka.?apa.?apa|Ko e hala.*fononga|Tongan proverb|Si.i pe kae).*', re.I)
OFFER  = re.compile(r'\bfree\s+(roof\s+|roofing\s+)?(inspection|estimate|quote|consultation|assessment|audit|evaluation|inspections|estimates|quotes)\b', re.I)
CODEEXT = re.compile(r'\.(py|bat|sql|js|ts|jsx|tsx|sh|ps1|ya?ml)\b', re.I)
NOTEID  = re.compile(r'^note_id:\s*(\S+)', re.M)

def slug(t):
    t = re.sub(r'[^\w\.\- ]', '', t).strip().replace(' ', '_')
    return (t[:70] or 'untitled')

def scrub(c):
    c = '\n'.join(l for l in c.split('\n') if not PROV.match(l))   # drop proverb lines
    c = re.sub(r'\bGAF\b', 'IKO Certified', c)                     # GAF -> IKO Certified
    c = OFFER.sub('Complimentary Professional Photo Audit (CPPA)', c)  # free-offer -> CPPA
    return c

def load_ledger():
    try:
        return json.load(open(LEDGER, encoding='utf-8'))
    except Exception:
        return {}

def existing_ids(base):
    ids = set()
    for fp in glob.glob(os.path.join(base, '**', '*.md'), recursive=True):
        try:
            m = NOTEID.search(open(fp, encoding='utf-8').read(4000))
            if m: ids.add(m.group(1))
        except Exception:
            pass
    return ids

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', required=True)
    ap.add_argument('--label', required=True)
    ap.add_argument('--notebook-id', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    notes = json.load(open(a.src, encoding='utf-8')).get('notes', [])
    base = os.path.join(RES, a.out)
    code = os.path.join(base, "_code_DRAFTS")
    os.makedirs(code, exist_ok=True)

    led = load_ledger()
    seen = set(led.get(a.notebook_id, [])) | existing_ids(base)  # idempotent: ledger + on-disk
    start = len([f for f in glob.glob(os.path.join(base, '**', '*.md'), recursive=True)
                 if not os.path.basename(f).startswith('_')])

    proms = []; new = 0; skip = 0; flagN = 0; codeN = 0
    for i, n in enumerate(notes):
        nid = n.get('id') or f'idx{i}'
        if nid in seen:
            skip += 1; continue
        title = n.get('title') or f'note_{i}'
        content = scrub(n.get('content') or '')
        flags = []
        if re.search(r'\bfree\b', content, re.I):  flags.append('free?')
        if re.search(r'\bgreen\b', content, re.I): flags.append('green?')
        if flags: flagN += 1
        for m in re.finditer(r'```[\s\S]*?```', content):
            if len(m.group(0)) > 60: proms.append((title, m.group(0)))
        first = next((l for l in content.split('\n') if l.strip()), '')
        is_code = bool(CODEEXT.search(title)) or first.strip().startswith(
            ('```', 'import ', 'def ', '#!', '<?php', 'SELECT', 'CREATE'))
        if is_code: codeN += 1
        dest = code if is_code else base
        seq = start + new + 1
        hdr = (f"---\nsource: \"NotebookLM - {a.label}\"\nnotebook_id: {a.notebook_id}\n"
               f"note_id: {nid}\ntype: {'CODE-DRAFT (review before running)' if is_code else 'SOP/guide'}\n"
               f"scrub: \"proverbs removed; GAF->IKO; free-offer->CPPA"
               f"{'; REVIEW ' + ','.join(flags) if flags else ''}\"\n"
               f"status: DRAFT - review before publish/run (Outbox Shield)\n---\n\n# {title}\n\n")
        open(os.path.join(dest, f"{seq:02d}_{slug(title)}.md"), 'w', encoding='utf-8').write(hdr + content)
        seen.add(nid); new += 1

    if proms:
        with open(os.path.join(base, "_PROMPTS_LIBRARY.md"), 'a', encoding='utf-8') as f:
            f.write(f"\n\n# +{len(proms)} prompt/code blocks ({a.label})\n")
            for t, b in proms:
                f.write(f"\n## from: {t}\n{b}\n")

    # rebuild _INDEX.md from everything currently on disk
    idx = [f"# {a.label} - ingested notes", "",
           "Scrubbed: proverbs removed, GAF->IKO, free-offer->CPPA. CODE -> _code_DRAFTS/ (do NOT run until reviewed).",
           "", "| File | Kind |", "|--|--|"]
    for fp in sorted(glob.glob(os.path.join(base, '**', '*.md'), recursive=True)):
        b = os.path.basename(fp)
        if b.startswith('_'): continue
        kind = 'CODE' if os.sep + '_code_DRAFTS' + os.sep in fp else 'SOP'
        idx.append(f"| {b} | {kind} |")
    idx.append(f"\n**Last run:** +{new} new, {skip} skipped (already ingested), {codeN} code, {flagN} flagged for brand review.")
    open(os.path.join(base, "_INDEX.md"), 'w', encoding='utf-8').write('\n'.join(idx))

    led[a.notebook_id] = sorted(seen)
    json.dump(led, open(LEDGER, 'w', encoding='utf-8'), indent=1)
    print(f"notebook-ingest: +{new} new, {skip} skipped, {codeN} code, {flagN} flagged  ->  {base}")

if __name__ == '__main__':
    main()
