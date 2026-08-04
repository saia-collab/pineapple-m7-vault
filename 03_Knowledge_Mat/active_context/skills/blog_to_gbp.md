---
name: blog_to_gbp
description: Turn a blog post into a Google Business Profile update under 1400 chars
status: ready
usage: paste this file + the full blog body; get one GBP-ready post back
---

# BLOG → GBP POST — COPY-PASTE KIT

## PROMPT (paste this + the blog text)

You are writing a Google Business Profile post for Pineapple Roofing (Frisco, TX · RCAT #03-0637 · IKO Certified · 972-928-0788) based on the blog below.

HARD RULES:
- UNDER 1,400 characters total including any CTA.
- Match the blog's voice — don't flatten it into generic marketing.
- Brand law: never "free" (use CPPA), never "GAF" (use IKO Certified), never green.
- No hashtags. No emojis. No links in the body — GBP adds the link separately.
- No headings, no markdown, no bullet symbols. Plain prose with line breaks.

STRUCTURE:
1. Hook line mirroring the blog's angle — what would make a Frisco/DFW homeowner click.
2. 1-3 real takeaways from the post (rewritten, not "this article explains…").
3. Soft CTA in brand voice inviting them to read the full post.

BLOG TEXT:
"""
{{PASTE_BLOG_BODY}}
"""
