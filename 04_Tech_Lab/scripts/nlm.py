"""
NotebookLM CLI wrapper using notebooklm-py library.
Replaces browser automation with direct API calls.
"""

import asyncio
import argparse
import json
import sys
import os

# Library data stored alongside the skill
SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIBRARY_FILE = os.path.join(SKILL_DIR, "data", "library.json")


def ensure_data_dir():
    os.makedirs(os.path.join(SKILL_DIR, "data"), exist_ok=True)


def load_library():
    ensure_data_dir()
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as f:
            return json.load(f)
    return {"notebooks": {}, "active": None}


def save_library(lib):
    ensure_data_dir()
    with open(LIBRARY_FILE, "w") as f:
        json.dump(lib, f, indent=2)


async def get_client():
    from notebooklm import NotebookLMClient
    return await NotebookLMClient.from_storage()


# --- Auth commands ---

async def cmd_login(args):
    """Open browser for Google login."""
    import subprocess
    # Use the installed CLI entry point directly
    subprocess.run(["notebooklm", "login"], check=True)
    print("Login complete. Cookies saved to ~/.notebooklm/storage_state.json")


async def cmd_auth_status(args):
    """Check if auth is valid."""
    storage = os.path.expanduser("~/.notebooklm/storage_state.json")
    if os.path.exists(storage):
        import time
        age_hours = (time.time() - os.path.getmtime(storage)) / 3600
        print(f"Auth file exists (age: {age_hours:.1f} hours)")
        if age_hours > 168:
            print("WARNING: Auth is over 7 days old. May need re-login.")
        else:
            print("Auth looks fresh.")
    else:
        print("NOT AUTHENTICATED. Run: python scripts/nlm.py login")


# --- Notebook commands ---

async def cmd_list(args):
    """List all notebooks from NotebookLM."""
    async with await get_client() as client:
        notebooks = await client.notebooks.list()
        if not notebooks:
            print("No notebooks found.")
            return
        for nb in notebooks:
            title = getattr(nb, 'title', None) or getattr(nb, 'name', 'Untitled')
            nb_id = getattr(nb, 'id', None) or getattr(nb, 'notebook_id', 'unknown')
            print(f"  {nb_id}  |  {title}")
        print(f"\nTotal: {len(notebooks)} notebooks")


async def cmd_create(args):
    """Create a new notebook."""
    async with await get_client() as client:
        nb = await client.notebooks.create(args.title)
        nb_id = getattr(nb, 'id', None) or getattr(nb, 'notebook_id', 'unknown')
        print(f"Created notebook: {nb_id} — {args.title}")


async def cmd_describe(args):
    """Get AI description of a notebook."""
    async with await get_client() as client:
        desc = await client.notebooks.get_description(args.notebook_id)
        print(desc)


# --- Source commands ---

async def cmd_sources(args):
    """List sources in a notebook."""
    nb_id = args.notebook_id or _get_active()
    if not nb_id:
        print("ERROR: No notebook specified. Use --notebook-id or set active notebook.")
        return
    async with await get_client() as client:
        sources = await client.sources.list(nb_id)
        if not sources:
            print("No sources in this notebook.")
            return
        for s in sources:
            title = getattr(s, 'title', None) or getattr(s, 'name', 'Untitled')
            s_id = getattr(s, 'id', None) or getattr(s, 'source_id', 'unknown')
            print(f"  {s_id}  |  {title}")
        print(f"\nTotal: {len(sources)} sources")


async def cmd_add_source(args):
    """Add a source to a notebook (URL, file, or text)."""
    nb_id = args.notebook_id or _get_active()
    if not nb_id:
        print("ERROR: No notebook specified.")
        return
    async with await get_client() as client:
        if args.url:
            source = await client.sources.add_url(nb_id, args.url, wait=True)
            print(f"Added URL source: {args.url}")
        elif args.file:
            source = await client.sources.add_file(nb_id, args.file, wait=True)
            print(f"Added file source: {args.file}")
        elif args.text:
            source = await client.sources.add_text(nb_id, args.title or "Untitled", args.text, wait=True)
            print(f"Added text source: {args.title or 'Untitled'}")
        else:
            print("ERROR: Provide --url, --file, or --text")


# --- Chat commands ---

async def cmd_ask(args):
    """Ask a question to a notebook."""
    nb_id = args.notebook_id or _get_active()
    if not nb_id:
        print("ERROR: No notebook specified. Use --notebook-id or set active notebook.")
        return
    async with await get_client() as client:
        result = await client.chat.ask(nb_id, args.question)
        answer = getattr(result, 'answer', None) or getattr(result, 'text', str(result))
        print(answer)

        # Print citations if available
        citations = getattr(result, 'citations', None)
        if citations:
            print("\n--- Citations ---")
            for c in citations:
                print(f"  - {c}")


async def cmd_chat_history(args):
    """Get chat history for a notebook."""
    nb_id = args.notebook_id or _get_active()
    if not nb_id:
        print("ERROR: No notebook specified.")
        return
    async with await get_client() as client:
        history = await client.chat.get_history(nb_id, limit=args.limit or 10)
        for q, a in history:
            print(f"Q: {q}")
            print(f"A: {a[:200]}...")
            print()


# --- Artifact commands ---

async def cmd_generate_audio(args):
    """Generate an audio overview."""
    nb_id = args.notebook_id or _get_active()
    if not nb_id:
        print("ERROR: No notebook specified.")
        return
    async with await get_client() as client:
        fmt = (args.format or "DEEP_DIVE").upper()
        length = (args.length or "DEFAULT").upper()
        instructions = args.instructions or None

        task = await client.artifacts.generate_audio(
            nb_id,
            source_ids=None,
            instructions=instructions,
            audio_format=fmt,
            audio_length=length
        )
        print(f"Audio generation started. Waiting for completion...")
        # Poll for completion
        task_id = getattr(task, 'task_id', None) or getattr(task, 'id', None)
        if task_id:
            await client.artifacts.wait_for_completion(nb_id, task_id)
            print("Audio generation complete.")
            if args.output:
                await client.artifacts.download_audio(nb_id, args.output)
                print(f"Downloaded to: {args.output}")
        else:
            print("Audio task submitted. Check artifacts list for result.")


async def cmd_generate_report(args):
    """Generate a report/study guide/blog post."""
    nb_id = args.notebook_id or _get_active()
    if not nb_id:
        print("ERROR: No notebook specified.")
        return
    async with await get_client() as client:
        from notebooklm.types import ReportFormat
        fmt_str = (args.format or "BRIEFING_DOC").upper()
        fmt = ReportFormat(fmt_str.lower())
        task = await client.artifacts.generate_report(
            nb_id,
            report_format=fmt,
            custom_prompt=args.prompt or None,
            extra_instructions=args.instructions or None
        )
        print(f"Report generation started ({fmt})...")
        task_id = getattr(task, 'task_id', None) or getattr(task, 'id', None)
        if task_id:
            await client.artifacts.wait_for_completion(nb_id, task_id)
            print("Report complete.")


async def cmd_generate_quiz(args):
    """Generate a quiz."""
    nb_id = args.notebook_id or _get_active()
    if not nb_id:
        print("ERROR: No notebook specified.")
        return
    async with await get_client() as client:
        task = await client.artifacts.generate_quiz(
            nb_id,
            instructions=args.instructions or None,
            quantity=args.quantity or "STANDARD",
            difficulty=args.difficulty or "MEDIUM"
        )
        print("Quiz generation started...")
        task_id = getattr(task, 'task_id', None) or getattr(task, 'id', None)
        if task_id:
            await client.artifacts.wait_for_completion(nb_id, task_id)
            print("Quiz complete.")


async def cmd_artifacts(args):
    """List all artifacts in a notebook."""
    nb_id = args.notebook_id or _get_active()
    if not nb_id:
        print("ERROR: No notebook specified.")
        return
    async with await get_client() as client:
        artifacts = await client.artifacts.list(nb_id)
        if not artifacts:
            print("No artifacts found.")
            return
        for a in artifacts:
            title = getattr(a, 'title', None) or getattr(a, 'name', 'Untitled')
            a_type = getattr(a, 'type', None) or getattr(a, 'artifact_type', '?')
            a_id = getattr(a, 'id', None) or getattr(a, 'artifact_id', 'unknown')
            print(f"  {a_id}  |  [{a_type}]  {title}")


# --- Research commands ---

async def cmd_research(args):
    """Start a research task (web or drive)."""
    nb_id = args.notebook_id or _get_active()
    if not nb_id:
        print("ERROR: No notebook specified.")
        return
    async with await get_client() as client:
        source = args.source or "web"
        mode = args.mode or "fast"
        print(f"Starting {source} research ({mode} mode): {args.query}")
        result = await client.research.start(nb_id, args.query, source=source, mode=mode)
        print("Research started. Polling for results...")

        # Poll until done
        while True:
            status = await client.research.poll(nb_id)
            state = getattr(status, 'status', None) or getattr(status, 'state', 'unknown')
            if state in ('DONE', 'COMPLETED', 'done', 'completed'):
                summary = getattr(status, 'summary', None)
                sources = getattr(status, 'sources', None)
                if summary:
                    print(f"\n--- Research Summary ---\n{summary}")
                if sources:
                    print(f"\n--- Sources Found: {len(sources)} ---")
                    for s in sources[:10]:
                        print(f"  - {s}")
                break
            elif state in ('FAILED', 'ERROR', 'failed', 'error'):
                print(f"Research failed: {status}")
                break
            await asyncio.sleep(3)


# --- Library commands (local metadata) ---

async def cmd_library_add(args):
    """Add a notebook to local library with metadata."""
    lib = load_library()
    slug = args.name.lower().replace(" ", "-")
    lib["notebooks"][slug] = {
        "id": args.notebook_id,
        "name": args.name,
        "description": args.description or "",
        "topics": args.topics or "",
        "uses": 0
    }
    save_library(lib)
    print(f"Added to library: {slug} → {args.notebook_id}")


async def cmd_library_list(args):
    """List local library."""
    lib = load_library()
    if not lib["notebooks"]:
        print("Library empty. Add notebooks with: library-add")
        return
    active = lib.get("active")
    for slug, nb in lib["notebooks"].items():
        marker = " ★" if slug == active else ""
        print(f"  {slug}{marker}")
        print(f"    ID: {nb['id']}")
        print(f"    {nb.get('description', 'No description')}")
        print(f"    Topics: {nb.get('topics', 'none')}")
        print(f"    Uses: {nb.get('uses', 0)}")
        print()


async def cmd_library_activate(args):
    """Set active notebook in library."""
    lib = load_library()
    if args.slug not in lib["notebooks"]:
        print(f"ERROR: '{args.slug}' not in library. Use library-list to see available.")
        return
    lib["active"] = args.slug
    save_library(lib)
    nb_id = lib["notebooks"][args.slug]["id"]
    print(f"Active notebook: {args.slug} ({nb_id})")


def _get_active():
    """Get active notebook ID from library."""
    lib = load_library()
    active = lib.get("active")
    if active and active in lib.get("notebooks", {}):
        return lib["notebooks"][active]["id"]
    return None


# --- Main ---

def main():
    parser = argparse.ArgumentParser(description="NotebookLM CLI (notebooklm-py)")
    sub = parser.add_subparsers(dest="command")

    # Auth
    sub.add_parser("login", help="Open browser for Google login")
    sub.add_parser("auth-status", help="Check auth status")

    # Notebooks
    sub.add_parser("list", help="List all notebooks")
    p = sub.add_parser("create", help="Create a notebook")
    p.add_argument("title")
    p = sub.add_parser("describe", help="Get notebook description")
    p.add_argument("notebook_id")

    # Sources
    p = sub.add_parser("sources", help="List sources in a notebook")
    p.add_argument("--notebook-id", default=None)
    p = sub.add_parser("add-source", help="Add source to notebook")
    p.add_argument("--notebook-id", default=None)
    p.add_argument("--url", default=None)
    p.add_argument("--file", default=None)
    p.add_argument("--text", default=None)
    p.add_argument("--title", default=None)

    # Chat
    p = sub.add_parser("ask", help="Ask a question")
    p.add_argument("question")
    p.add_argument("--notebook-id", default=None)
    p = sub.add_parser("chat-history", help="Get chat history")
    p.add_argument("--notebook-id", default=None)
    p.add_argument("--limit", type=int, default=10)

    # Artifacts
    p = sub.add_parser("generate-audio", help="Generate audio overview")
    p.add_argument("--notebook-id", default=None)
    p.add_argument("--format", default="DEEP_DIVE", help="DEEP_DIVE|BRIEF|CRITIQUE|DEBATE")
    p.add_argument("--length", default="DEFAULT", help="SHORT|DEFAULT|LONG")
    p.add_argument("--instructions", default=None)
    p.add_argument("--output", default=None, help="Download path")
    p = sub.add_parser("generate-report", help="Generate report")
    p.add_argument("--notebook-id", default=None)
    p.add_argument("--format", default="BRIEFING_DOC", help="BRIEFING_DOC|STUDY_GUIDE|BLOG_POST|CUSTOM")
    p.add_argument("--prompt", default=None)
    p.add_argument("--instructions", default=None)
    p = sub.add_parser("generate-quiz", help="Generate quiz")
    p.add_argument("--notebook-id", default=None)
    p.add_argument("--instructions", default=None)
    p.add_argument("--quantity", default="STANDARD", help="FEWER|STANDARD|MORE")
    p.add_argument("--difficulty", default="MEDIUM", help="EASY|MEDIUM|HARD")
    p = sub.add_parser("artifacts", help="List artifacts")
    p.add_argument("--notebook-id", default=None)

    # Research
    p = sub.add_parser("research", help="Start research task")
    p.add_argument("query")
    p.add_argument("--notebook-id", default=None)
    p.add_argument("--source", default="web", help="web|drive")
    p.add_argument("--mode", default="fast", help="fast|deep")

    # Library (local metadata)
    p = sub.add_parser("library-add", help="Add notebook to local library")
    p.add_argument("--notebook-id", required=True)
    p.add_argument("--name", required=True)
    p.add_argument("--description", default="")
    p.add_argument("--topics", default="")
    p = sub.add_parser("library-list", help="List local library")
    p = sub.add_parser("library-activate", help="Set active notebook")
    p.add_argument("slug")

    args = parser.parse_args()

    commands = {
        "login": cmd_login,
        "auth-status": cmd_auth_status,
        "list": cmd_list,
        "create": cmd_create,
        "describe": cmd_describe,
        "sources": cmd_sources,
        "add-source": cmd_add_source,
        "ask": cmd_ask,
        "chat-history": cmd_chat_history,
        "generate-audio": cmd_generate_audio,
        "generate-report": cmd_generate_report,
        "generate-quiz": cmd_generate_quiz,
        "artifacts": cmd_artifacts,
        "research": cmd_research,
        "library-add": cmd_library_add,
        "library-list": cmd_library_list,
        "library-activate": cmd_library_activate,
    }

    if not args.command:
        parser.print_help()
        return

    fn = commands.get(args.command)
    if fn:
        asyncio.run(fn(args))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
