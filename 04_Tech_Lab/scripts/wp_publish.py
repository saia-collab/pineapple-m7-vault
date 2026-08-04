#!/usr/bin/env python3
"""
M7 WordPress auto-draft — pushes a Markdown SEO post into WordPress as a DRAFT.
Outbox Shield honored: posts land as status='draft' for human review in wp-admin.
Free. Reads creds from a git-ignored secrets file (never hardcode them).

Usage:  python wp_publish.py "<path-to-post.md>"
Creds:  04_Tech_Lab/.wp_secrets.env  (WP_URL, WP_USER, WP_APP_PASSWORD)
"""
import sys, os, re, json, base64, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
SECRETS = os.path.join(HERE, ".wp_secrets.env")

def load_secrets():
    creds = {}
    if not os.path.exists(SECRETS):
        sys.exit(f"Missing {SECRETS} — create it with WP_URL, WP_USER, WP_APP_PASSWORD.")
    for line in open(SECRETS, encoding="utf-8"):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            creds[k.strip()] = v.strip()
    for k in ("WP_URL", "WP_USER", "WP_APP_PASSWORD"):
        if not creds.get(k):
            sys.exit(f"{k} not set in {SECRETS}")
    return creds

def parse_md(path):
    text = open(path, encoding="utf-8").read()
    title, meta, body = os.path.basename(path).replace(".md", ""), "", text
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if m:
        fm, body = m.group(1), m.group(2)
        for line in fm.splitlines():
            if line.lower().startswith("title:"):
                title = line.split(":", 1)[1].strip().strip('"')
            if line.lower().startswith(("meta", "description")):
                meta = line.split(":", 1)[1].strip().strip('"')
    # very light markdown -> HTML (headings, bold, paragraphs)
    html = []
    for para in body.strip().split("\n\n"):
        p = para.strip()
        if not p: continue
        if p.startswith("### "):   html.append(f"<h3>{p[4:]}</h3>")
        elif p.startswith("## "):  html.append(f"<h2>{p[3:]}</h2>")
        elif p.startswith("# "):   html.append(f"<h1>{p[2:]}</h1>")
        else:
            p = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", p)
            html.append(f"<p>{p}</p>")
    return title, meta, "\n".join(html)

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python wp_publish.py <path-to-post.md>")
    c = load_secrets()
    ptype = sys.argv[2] if len(sys.argv) > 2 else "posts"   # "posts" or "pages"
    update_id = sys.argv[3] if len(sys.argv) > 3 else None   # existing id → update in place
    title, meta, content = parse_md(sys.argv[1])
    body = {"title": title, "content": content, "excerpt": meta}
    if not update_id:
        body["status"] = "draft"   # new items land as draft; updates keep current status
    payload = json.dumps(body).encode("utf-8")
    base = c["WP_URL"].rstrip("/") + "/wp-json/wp/v2/" + ptype
    url = base + ("/" + update_id if update_id else "")
    auth = base64.b64encode(f'{c["WP_USER"]}:{c["WP_APP_PASSWORD"]}'.encode()).decode()
    req = urllib.request.Request(url, data=payload, method="POST", headers={
        "Authorization": f"Basic {auth}", "Content-Type": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            j = json.load(r)
            print(f"OK draft #{j.get('id')} -> {j.get('link','(review in wp-admin)')}")
            print("Review it in wp-admin -> Posts -> Drafts, then Publish.")
    except urllib.error.HTTPError as e:
        sys.exit(f"WordPress rejected it ({e.code}): {e.read().decode()[:300]}")

if __name__ == "__main__":
    main()
