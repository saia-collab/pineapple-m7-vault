# m7_pipeline.py – Orchestrates the M7 workflow
# ---------------------------------------------------
# This script provides a clean, local‑only orchestration of the two core M7 tools:
#   * m7_fetch.py – fetches a URL and returns markdown content
#   * m7_scoring.py – consumes markdown and produces a brand‑compliance score report
#
# Usage:
#   python m7_pipeline.py <url>
#
# The script will:
#   1. Create a "scraped_content" directory next to this file (if it does not exist).
#   2. Run m7_fetch.py via subprocess, capture its stdout (the markdown).
#   3. Write the markdown to a timestamped file inside the scraped_content folder.
#   4. Run m7_scoring.py on that markdown file via subprocess and print the report.
#
# The implementation uses only the Python standard library (subprocess, pathlib,
# datetime, sys) to keep the dependency footprint minimal and to ensure the script
# works on any Windows machine with Python installed.

import sys
import subprocess
from pathlib import Path
from datetime import datetime

def run_subprocess(command: list[str]) -> subprocess.CompletedProcess:
    """Run a subprocess and raise on failure.

    Args:
        command: List of command arguments (program + args).
    Returns:
        CompletedProcess with captured stdout.
    """
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Command {' '.join(command)} failed with exit code {result.returncode}\n"
            f"stderr: {result.stderr.strip()}"
        )
    return result

def main(url: str) -> None:
    # Resolve paths relative to this script
    base_dir = Path(__file__).parent
    scraped_dir = base_dir / "scraped_content"
    scraped_dir.mkdir(exist_ok=True)

    # 1️⃣ Run m7_fetch.py
    fetch_cmd = [sys.executable, str(base_dir / "m7_fetch.py"), url]
    print(f"[▶] Fetching content from {url} ...")
    fetch_result = run_subprocess(fetch_cmd)
    markdown = fetch_result.stdout.strip()
    if not markdown:
        raise RuntimeError("m7_fetch.py produced no output.")

    # 2️⃣ Save markdown with a timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    markdown_path = scraped_dir / f"scraped_{timestamp}.md"
    markdown_path.write_text(markdown, encoding="utf-8")
    print(f"[💾] Saved markdown to {markdown_path}")

    # 3️⃣ Run m7_scoring.py on the saved file
    score_cmd = [sys.executable, str(base_dir / "agents" / "m7_scoring.py"), str(markdown_path)]
    print(f"[▶] Scoring scraped content ...")
    score_result = run_subprocess(score_cmd)
    report = score_result.stdout.strip()
    print("\n=== Brand Compliance Score Report ===\n")
    print(report)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python m7_pipeline.py <url>")
        sys.exit(1)
    main(sys.argv[1])
