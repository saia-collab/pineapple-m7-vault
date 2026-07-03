"""
Headless cookie refresh for NotebookLM.

Uses the persistent browser profile (which retains Google's session)
to re-export fresh cookies WITHOUT requiring manual login.

The browser profile handles Google's token rotation automatically,
so as long as we periodically "visit" NotebookLM, cookies stay alive.

Usage:
    python refresh_auth.py          # Refresh cookies headlessly
    python refresh_auth.py --check  # Just check if refresh is needed
"""

import json
import os
import sys
import time
from pathlib import Path

# Resolve paths (same as notebooklm-py uses)
NOTEBOOKLM_HOME = Path(os.environ.get("NOTEBOOKLM_HOME", Path.home() / ".notebooklm"))
STORAGE_PATH = NOTEBOOKLM_HOME / "storage_state.json"
BROWSER_PROFILE = NOTEBOOKLM_HOME / "browser_profile"


def get_cookie_age_hours():
    """How old is the current storage_state.json?"""
    if not STORAGE_PATH.exists():
        return float("inf")
    return (time.time() - os.path.getmtime(STORAGE_PATH)) / 3600


def check_cookies_valid():
    """Quick check: do the cookies actually work (not just exist)?"""
    import asyncio
    from notebooklm.auth import load_auth_from_storage, fetch_tokens

    try:
        cookies = load_auth_from_storage()
        asyncio.run(fetch_tokens(cookies))
        return True
    except Exception:
        return False


def refresh_headless():
    """Launch headless browser with persistent profile, visit NotebookLM, save fresh cookies."""
    if not BROWSER_PROFILE.exists():
        print("ERROR: No browser profile found. Run 'notebooklm login' manually first.")
        return False

    # Windows fix: Playwright needs ProactorEventLoop
    if sys.platform == "win32":
        import asyncio
        asyncio.set_event_loop_policy(asyncio.DefaultEventLoopPolicy())

    from playwright.sync_api import sync_playwright

    print(f"Refreshing cookies using profile: {BROWSER_PROFILE}")

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(BROWSER_PROFILE),
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--password-store=basic",
            ],
            ignore_default_args=["--enable-automation"],
        )

        page = context.pages[0] if context.pages else context.new_page()

        try:
            page.goto("https://notebooklm.google.com/", wait_until="networkidle", timeout=30000)
        except Exception as e:
            print(f"WARNING: Page load timeout/error (may still work): {e}")

        current_url = page.url

        if "notebooklm.google.com" in current_url and "accounts.google.com" not in current_url:
            # We're on NotebookLM — session is still valid, save fresh cookies
            context.storage_state(path=str(STORAGE_PATH))
            context.close()
            print(f"Cookies refreshed successfully. Saved to: {STORAGE_PATH}")
            return True
        else:
            context.close()
            print(f"ERROR: Google session expired. Redirected to: {current_url}")
            print("You need to run 'notebooklm login' manually to re-authenticate.")
            return False


def main():
    if "--check" in sys.argv:
        age = get_cookie_age_hours()
        valid = check_cookies_valid()
        print(f"Cookie age: {age:.1f} hours")
        print(f"Cookies valid: {valid}")
        if not valid and age > 24:
            print("Recommendation: refresh needed")
        sys.exit(0 if valid else 1)

    # Always try refresh
    success = refresh_headless()

    if success:
        # Verify the refreshed cookies actually work
        valid = check_cookies_valid()
        if valid:
            print("Verified: cookies are working.")
        else:
            print("WARNING: Cookies saved but verification failed. May need manual login.")
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
