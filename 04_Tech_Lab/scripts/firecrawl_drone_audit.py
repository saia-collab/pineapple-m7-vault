import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib import error, parse, request

WORKSPACE_ROOT = Path("C:/Pineapple-Mana-Global")
ENV_PATH = WORKSPACE_ROOT / "01_Command_Center" / "PineappleHQ" / ".env"
OUTPUT_DIR = WORKSPACE_ROOT / "03_Knowledge_Mat" / "photo-audits"
FIRECRAWL_API_URL = "https://api.firecrawl.dev/v1/search"

CORPORATE_HEADER = "Complimentary Professional Photo Audit"
TRUST_LINE = "Pineapple Contractors | IKO Certified | RCAT Licensed #03-0637 | Full Restoration Coverage"


def load_dotenv(env_path: Path) -> dict[str, str]:
    env_vars: dict[str, str] = {}
    if not env_path.exists():
        return env_vars

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        env_vars[key.strip()] = value.strip().strip('"').strip("'")
    return env_vars


def get_firecrawl_api_key() -> str:
    if os.getenv("FIRECRAWL_API_KEY"):
        return os.getenv("FIRECRAWL_API_KEY", "")
    env_vars = load_dotenv(ENV_PATH)
    return env_vars.get("FIRECRAWL_API_KEY", "")


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-").lower()
    return slug or "property-audit"


def call_firecrawl_search(address: str, api_key: str) -> dict:
    query = (
        f'"{address}" property roof storm damage insurance home value site:zillow.com '
        f'OR site:redfin.com OR site:realtor.com'
    )
    payload = {
        "query": query,
        "limit": 5,
        "sources": [{"type": "web"}],
    }
    body = json.dumps(payload).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    req = request.Request(FIRECRAWL_API_URL, data=body, headers=headers, method="POST")
    with request.urlopen(req, timeout=60) as response:
        raw = response.read().decode("utf-8")
        return json.loads(raw)


def extract_result_fields(item: dict) -> dict[str, str]:
    return {
        "title": str(item.get("title") or item.get("metadata", {}).get("title") or "Unknown listing"),
        "url": str(item.get("url") or item.get("sourceURL") or item.get("sourceUrl") or ""),
        "description": str(item.get("description") or item.get("markdown") or item.get("content") or "").strip(),
    }


def build_brief(address: str, search_payload: dict | None, api_error: str | None) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        CORPORATE_HEADER,
        "=" * len(CORPORATE_HEADER),
        "",
        f"Generated: {timestamp}",
        f"Property: {address}",
        TRUST_LINE,
        "",
        "Executive Summary",
        "-----------------",
        "This pre-visit brief is designed to establish authority before an on-site inspection.",
        "Use it to frame the property conversation, explain likely roof-risk factors, and position the team as the documentation partner working alongside the insurance agent.",
        "",
        "Recommended Sales Angle",
        "-----------------------",
        "1. Lead with a complimentary professional photo audit.",
        "2. Explain that hidden storm damage often cannot be confirmed from the driveway.",
        "3. Position the inspection as documentation-first: photo evidence, claim-readiness, and full restoration coverage review.",
        "4. Reinforce trust signals: IKO Certified, RCAT Licensed #03-0637, 50-Year Warranty on qualifying installs.",
        "",
        "Insurance-Ready Talking Points",
        "------------------------------",
        "- Hidden storm damage can include bruising, granule displacement, seal-strip lift, flashing separation, and soft metal impacts.",
        "- The goal of the audit is to document findings clearly so the homeowner and insurance agent can evaluate covered damage together.",
        "- The team coordinates directly with the insurance company from inspection through completion when restoration is warranted.",
        "- If no storm damage is found, the homeowner still leaves with a documented roof condition snapshot.",
        "",
    ]

    if api_error:
        lines.extend([
            "Firecrawl Search Status",
            "-----------------------",
            f"Search did not complete: {api_error}",
            "No public property references were attached to this brief.",
            "",
        ])
    else:
        items = search_payload.get("data") or search_payload.get("results") or []
        lines.extend([
            "Public Property References",
            "--------------------------",
        ])
        if not items:
            lines.append("No public search results were returned for this address.")
        for index, item in enumerate(items, start=1):
            result = extract_result_fields(item)
            lines.append(f"{index}. {result['title']}")
            if result["url"]:
                lines.append(f"   URL: {result['url']}")
            if result["description"]:
                lines.append(f"   Note: {result['description'][:500]}")
        lines.append("")

    maps_query = parse.quote(address)
    lines.extend([
        "Field Prep",
        "----------",
        f"- Google Maps: https://www.google.com/maps/search/?api=1&query={maps_query}",
        f"- Google Earth: https://earth.google.com/web/search/{maps_query}",
        f"- Zillow Search: https://www.zillow.com/homes/{maps_query}_rb/",
        f"- Realtor Search: https://www.realtor.com/realestateandhomes-search/{maps_query}",
        "",
        "Crew Checklist",
        "--------------",
        "- Capture front elevation, all roof planes, ridge, hips, valleys, flashing, vents, gutters, soft metals, and interior leak indicators.",
        "- Document slope count, shingle condition, visible wind lift, granular loss, and any prior repair signatures.",
        "- Photograph carrier-relevant evidence with time-stamped closeups and wide shots.",
        "- Confirm homeowner goals: leak response, claim support, financing path, or full restoration review.",
        "",
        "Close",
        "-----",
        "Deliver this as a complimentary professional photo audit summary and position the on-site visit as the step that converts public data into claim-grade documentation.",
        "",
    ])
    return "\n".join(lines)


def save_outputs(address: str, brief_text: str, search_payload: dict | None) -> tuple[Path, Path | None]:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    slug = slugify(address)
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    brief_path = OUTPUT_DIR / f"{stamp}-{slug}-audit.txt"
    brief_path.write_text(brief_text, encoding="utf-8")

    json_path = None
    if search_payload is not None:
        json_path = OUTPUT_DIR / f"{stamp}-{slug}-firecrawl.json"
        json_path.write_text(json.dumps(search_payload, indent=2), encoding="utf-8")
    return brief_path, json_path


def main() -> int:
    if len(sys.argv) < 2:
        print('Usage: python 04_Tech_Lab\\firecrawl_drone_audit.py "[ADDRESS]"')
        return 1

    address = sys.argv[1].strip()
    if not address:
        print("Address cannot be empty.")
        return 1

    api_key = get_firecrawl_api_key()
    if not api_key:
        print("FIRECRAWL_API_KEY not found in environment or PineappleHQ/.env")
        return 1

    search_payload = None
    api_error = None
    try:
        search_payload = call_firecrawl_search(address, api_key)
    except error.HTTPError as exc:
        api_error = f"HTTP {exc.code}"
    except error.URLError as exc:
        api_error = f"Network error: {exc.reason}"
    except Exception as exc:  # noqa: BLE001
        api_error = str(exc)

    brief_text = build_brief(address, search_payload, api_error)
    brief_path, json_path = save_outputs(address, brief_text, search_payload)

    print("============================================================")
    print("PINEAPPLE CONTRACTORS - COMPLIMENTARY PROFESSIONAL PHOTO AUDIT")
    print("============================================================")
    print(f"Property   : {address}")
    print(f"Brief file : {brief_path}")
    if json_path:
        print(f"Raw data   : {json_path}")
    if api_error:
        print(f"Search     : partial output only ({api_error})")
    else:
        print("Search     : Firecrawl enrichment attached")
    print("============================================================")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
