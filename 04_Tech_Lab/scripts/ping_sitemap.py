#!/usr/bin/env python3
"""Nudge search engines to re-crawl the sitemap after publishing changes.
HONEST NOTES:
- Google DEPRECATED sitemap ping (June 2023). Google now discovers via GSC + robots.txt. So we DON'T ping Google.
- Yoast already auto-submits your sitemap to GSC on every publish — this is a belt-and-suspenders nudge for Bing.
- Bing still accepts a ping. That's the one we send.
Usage: python ping_sitemap.py"""
import urllib.request, urllib.error

SITEMAP = "https://pineappleroofingllc.com/sitemap_index.xml"  # Yoast default

def ping(name, url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "PM7-SitemapPing/1.0"})
        with urllib.request.urlopen(req, timeout=20) as r:
            print(f"OK   {name}: HTTP {r.status}")
    except urllib.error.HTTPError as e:
        print(f"WARN {name}: HTTP {e.code} (endpoint may be retired — harmless)")
    except Exception as e:
        print(f"WARN {name}: {e}")

def main():
    print(f"Sitemap: {SITEMAP}\n")
    # Confirm the sitemap itself is reachable
    ping("sitemap reachable", SITEMAP)
    # Bing ping (still supported)
    ping("Bing", f"https://www.bing.com/ping?sitemap={SITEMAP}")
    print("\nGoogle: no ping (deprecated). Yoast + Site Kit already feed GSC automatically.")
    print("To force Google now: GSC -> Sitemaps -> submit 'sitemap_index.xml' (one time).")

if __name__ == "__main__":
    main()
