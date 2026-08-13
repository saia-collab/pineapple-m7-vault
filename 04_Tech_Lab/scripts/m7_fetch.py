#!/usr/bin/env python3
"""
M7 FETCH — clean competitor / research layout fetcher.
Pulls a URL via stdlib urllib, strips scripts/styles, extracts readable text,
and saves a clean markdown capture into 05_Campaign_Factory/10_Research_Stage/input/.
No external dependencies.

Usage
-----
    python m7_fetch.py --url https://example.com
    python m7_fetch.py --url https://example.com --out custom.md

"""
from __future__ import annotations
import argparse, json, re, sys
from datetime import datetime
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

DEFAULT_ROOT = Path(__file__).resolve().parents[2] if len(Path(__file__).resolve().parents) >= 3 else Path.cwd()
UA = "Mozilla/5.0 (M7-Fetch; +local research)"


def strip_html(html: str) -> str:
    html = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", html)
    html = re.sub(r"(?is)<!--.*?-->", " ", html)
    # capture title
    m = re.search(r"(?is)<title[^>]*>(.*?)</title>", html)
    title = re.sub(r"\s+", " ", m.group(1)).strip() if m else ""
    # block tags -> newlines
    html = re.sub(r"(?i)</(p|div|h[1-6]|li|section|article|br|tr)>", "\n", html)
    text = re.sub(r"(?s)<[^>]+>", " ", html)
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s*\n\s*\n+", "\n\n", text)
    return title, text.strip()


def main(argv=None):
    ap = argparse.ArgumentParser(description="M7 clean research fetcher")
    ap.add_argument("--url", required=True)
    ap.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    ap.add_argument("--out", default=None)
    args = ap.parse_args(argv)
    root = args.root.resolve()

    out_dir = root / "05_Campaign_Factory" / "10_Research_Stage" / "input"
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        req = Request(args.url, headers={"User-Agent": UA})
        with urlopen(req, timeout=20) as r:
            raw = r.read().decode("utf-8", "ignore")
    except (URLError, HTTPError, ValueError) as e:
        print(json.dumps({"ok": False, "url": args.url, "error": str(e)}, indent=2))
        return 1

    title, text = strip_html(raw)
    today = f"{datetime.now():%Y-%m-%d}"
    slug = re.sub(r"[^a-z0-9]+", "_", (title or args.url).lower())[:40].strip("_") or "capture"
    name = args.out or f"{today}_Research_{slug}.md"
    dest = out_dir / name
    fm = (f"---\ntype: research_capture\nsource_url: {args.url}\n"
          f"title: \"{title}\"\ncreated: {today}\nagent_origin: m7_fetch\n---\n\n")
    dest.write_text(fm + f"# {title}\n\n{text[:200000]}\n", encoding="utf-8")

    print(json.dumps({
        "ok": True, "url": args.url, "title": title,
        "chars": len(text), "saved": str(dest.relative_to(root)),
        "next": "Run brand_firewall.py --fix then feed to 10_Research_Stage.",
        "closing": ".",
    }, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
