#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""M7 — publish the 33 migration Elementor-block pages into WordPress as DRAFTS
with the Elementor Canvas template (clean render, no double header). Outbox Shield:
everything lands status='draft' for Saia to review + Publish in wp-admin.
Idempotent: matches by slug, UPDATES in place on re-run instead of duplicating."""
import os, re, csv, base64, json, urllib.request, urllib.error

HERE = "C:/Pineapple Contractors M7/04_Tech_Lab/scripts"
BUILD = "C:/Pineapple Contractors M7/02_Workspaces/2026-07-23_SEO_Site_Migration/pineapple-migration-build"
BLOCKS = BUILD + "/elementor-blocks"

c = {}
for line in open(os.path.join(HERE, ".wp_secrets.env"), encoding="utf-8"):
    line = line.strip()
    if line and not line.startswith("#") and "=" in line:
        k, v = line.split("=", 1); c[k.strip()] = v.strip()
BASE = c["WP_URL"].rstrip("/")
TOK = base64.b64encode(f'{c["WP_USER"]}:{c["WP_APP_PASSWORD"]}'.encode()).decode()
H = {"Authorization": f"Basic {TOK}", "Content-Type": "application/json"}

def api(path, data=None, method="GET"):
    req = urllib.request.Request(BASE + path,
        data=json.dumps(data).encode() if data is not None else None,
        headers=H, method=method)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)

# manifest: block filename (x.html) -> canonical URL
man = {}
with open(BUILD + "/page-manifest.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        man[row["File"]] = row["Canonical URL"]

def canonical_parts(url):
    """return (parent_slug or None, leaf_slug)"""
    path = re.sub(r"^https?://[^/]+/", "", url).strip("/")
    if not path:
        return None, "home"
    segs = path.split("/")
    return (segs[0], segs[-1]) if len(segs) > 1 else (None, segs[0])

def find_page_by_slug(slug):
    res = api(f"/wp-json/wp/v2/pages?slug={urllib.request.quote(slug)}&status=any&per_page=1")
    return res[0] if res else None

def ensure_parent(slug, title):
    p = find_page_by_slug(slug)
    if p: return p["id"]
    p = api("/wp-json/wp/v2/pages", {"title": title, "slug": slug, "status": "draft"}, "POST")
    print(f"  + created parent '{slug}' (id {p['id']})")
    return p["id"]

def title_from(html, fallback):
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S | re.I)
    if m:
        t = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        if t: return t + " | Pineapple Roofing"
    return fallback

# collect all block files
files = []
for sub in ("core", "services", "city-pages"):
    d = os.path.join(BLOCKS, sub)
    if os.path.isdir(d):
        for fn in sorted(os.listdir(d)):
            if fn.endswith("-elementor.html"):
                files.append((sub, os.path.join(d, fn), fn.replace("-elementor.html", ".html")))

print(f"found {len(files)} Elementor blocks to publish\n")
parents = {}
created = updated = failed = 0
rows = []
for sub, path, manfile in files:
    try:
        url = man.get(manfile) or man.get(manfile.replace(".html", ""))
        parent_slug, leaf = canonical_parts(url) if url else (None, manfile.replace(".html",""))
        html = open(path, encoding="utf-8").read()
        title = title_from(html, leaf.replace("-", " ").title() + " | Pineapple Roofing")
        parent_id = 0
        if parent_slug:
            if parent_slug not in parents:
                nice = "Roofing Services" if parent_slug == "services" else ("Service Areas" if parent_slug == "locations" else parent_slug.title())
                parents[parent_slug] = ensure_parent(parent_slug, nice)
            parent_id = parents[parent_slug]
        payload = {"title": title, "slug": leaf, "status": "draft",
                   "content": html, "template": "elementor_canvas", "parent": parent_id}
        existing = find_page_by_slug(leaf)
        if existing:
            api(f"/wp-json/wp/v2/pages/{existing['id']}", payload, "POST")
            updated += 1; act = "updated"; pid = existing["id"]
        else:
            d = api("/wp-json/wp/v2/pages", payload, "POST")
            created += 1; act = "created"; pid = d["id"]
        rows.append((act, sub, leaf, pid))
        print(f"  {act:8} [{sub:10}] {leaf:40} id {pid}")
    except Exception as e:
        failed += 1
        print(f"  FAILED   [{sub}] {manfile}: {type(e).__name__} {str(e)[:120]}")

print(f"\n=== DONE: {created} created, {updated} updated, {failed} failed (all status=DRAFT) ===")
print("Review + Publish in wp-admin -> Pages (filter: Drafts).")
