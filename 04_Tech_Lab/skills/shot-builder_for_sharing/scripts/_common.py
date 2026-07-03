"""
Shared helpers for shot-builder generation scripts.

Provides:
  - load_config()        — read workspace/config.json
  - save_config()        — write workspace/config.json + touch INDEX timestamp
  - load_api_key()       — read FAL_KEY / KIE_API_KEY from configured .env
  - resolve_output_dir() — date-stamped, project-scoped folder under config'd output_dir
  - resolve_token_dir()  — project-scoped token dir with global fallback
  - get_active_project() / set_active_project() / list_projects() — project state
  - slugify_project()    — filesystem-safe project slug
  - log_render()         — append to workspace/shots/<date>/ + INDEX.md recent renders
  - download_to_local()  — fetch a remote URL and save locally with a unique filename
"""

from __future__ import annotations

import json
import os
import re
import shutil
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
WORKSPACE = SKILL_DIR / "workspace"
CONFIG_PATH = WORKSPACE / "config.json"
INDEX_PATH = WORKSPACE / "INDEX.md"
PROJECTS_DIR = WORKSPACE / "projects"
TOKEN_KINDS = ("cast", "locations", "styles")


class ShotBuilderError(RuntimeError):
    pass


def load_config() -> dict[str, Any]:
    if not CONFIG_PATH.exists():
        raise ShotBuilderError(
            f"No config at {CONFIG_PATH}. Run `python scripts/setup.py` first."
        )
    return json.loads(CONFIG_PATH.read_text())


def save_config(config: dict[str, Any]) -> None:
    """Persist config and bump its modified timestamp."""
    config["modified"] = datetime.now(timezone.utc).isoformat()
    WORKSPACE.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_text(json.dumps(config, indent=2))


def _read_env_file(path: Path) -> dict[str, str]:
    """Parse a simple KEY=value .env file. Skips blanks and comments."""
    if not path.exists():
        return {}
    out: dict[str, str] = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        out[k.strip()] = v.strip().strip('"').strip("'")
    return out


def load_api_key(provider: str, config: dict[str, Any] | None = None) -> str:
    """
    Find the API key for a provider. Order:
      1. process env (FAL_KEY / FAL_API_KEY for fal, KIE_API_KEY for kie)
      2. config'd key_path .env file
      3. ~/.shot-builder/.env
      4. workspace/.env
    """
    if config is None:
        config = load_config()

    if provider == "fal":
        env_names = ("FAL_KEY", "FAL_API_KEY")
        key_path_field = "fal_key_path"
    elif provider == "kie":
        env_names = ("KIE_API_KEY",)
        key_path_field = "kie_key_path"
    else:
        raise ShotBuilderError(f"unknown provider: {provider}")

    # 1. Process env
    for name in env_names:
        if name in os.environ and os.environ[name]:
            return os.environ[name]

    # 2-4. .env files in fallback order
    candidate_paths: list[Path] = []
    cfg_path = config["provider"].get(key_path_field)
    if cfg_path:
        candidate_paths.append(Path(cfg_path).expanduser())
    candidate_paths.append(Path.home() / ".shot-builder" / ".env")
    candidate_paths.append(WORKSPACE / ".env")

    for path in candidate_paths:
        env = _read_env_file(path)
        for name in env_names:
            if name in env and env[name]:
                return env[name]

    raise ShotBuilderError(
        f"No {provider.upper()} API key found. Checked: env vars ({', '.join(env_names)}) "
        f"and .env files: {[str(p) for p in candidate_paths]}. "
        f"Run `python scripts/setup.py --reset` to re-enter."
    )


def slugify_project(name: str) -> str:
    """
    Filesystem-safe project slug. Lowercase, hyphenated, no leading/trailing dashes.
    Examples:
        "OMV Post-It"     -> "omv-post-it"
        "Artlist / Noise" -> "artlist-noise"
        "  test  "        -> "test"
    """
    s = name.strip().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    return s[:60] or "untitled"


def get_active_project(config: dict[str, Any] | None = None) -> str | None:
    """Return the active project slug, or None if not set."""
    if config is None:
        try:
            config = load_config()
        except ShotBuilderError:
            return None
    project = config.get("active_project")
    return project or None


def set_active_project(slug: str | None, config: dict[str, Any] | None = None) -> dict[str, Any]:
    """
    Set (or clear) the active project. Pass slug=None to clear.
    Slug must already exist under workspace/projects/ unless None.
    Returns the updated config dict.
    """
    if config is None:
        config = load_config()
    if slug is not None:
        slug = slugify_project(slug)
        if not (PROJECTS_DIR / slug).exists():
            raise ShotBuilderError(
                f"project '{slug}' not found under {PROJECTS_DIR}. "
                f"Create it first with `python scripts/project.py new <name>`."
            )
    config["active_project"] = slug
    save_config(config)
    return config


def list_projects() -> list[str]:
    """Return sorted list of existing project slugs."""
    if not PROJECTS_DIR.exists():
        return []
    return sorted(
        p.name for p in PROJECTS_DIR.iterdir()
        if p.is_dir() and not p.name.startswith(".")
    )


def ensure_project_scaffold(slug: str) -> Path:
    """
    Create workspace/projects/<slug>/{cast,locations,styles}/ if missing.
    Returns the project root path.
    """
    slug = slugify_project(slug)
    root = PROJECTS_DIR / slug
    for kind in TOKEN_KINDS:
        (root / kind).mkdir(parents=True, exist_ok=True)
    return root


def resolve_output_dir(
    kind: str,
    config: dict[str, Any] | None = None,
    project: str | None = None,
) -> Path:
    """
    Build the date-then-project output path:
      <output_dir>/<YYYY-MM-DD>/<project-or-_unsorted>/<kind>/

    `kind` is "shots" or "scenes".
    `project` overrides config.active_project. If neither is set, falls back
    to "_unsorted" so renders never get lost — the user can move them later.

    Also creates a workspace mirror at workspace/<kind>/<date>/<project>/.
    """
    if config is None:
        config = load_config()
    project_slug = slugify_project(project) if project else get_active_project(config) or "_unsorted"
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    output_dir = Path(config["paths"]["output_dir"]) / date / project_slug / kind
    output_dir.mkdir(parents=True, exist_ok=True)

    # Mirror in workspace for the skill's own log
    mirror = WORKSPACE / kind / date / project_slug
    mirror.mkdir(parents=True, exist_ok=True)
    return output_dir


def resolve_token_dir(kind: str, project: str | None = None) -> list[Path]:
    """
    Return search paths for a token kind, in lookup order:
      1. workspace/projects/<project>/<kind>/   (if project set and exists)
      2. workspace/<kind>/                       (global fallback)

    Caller iterates these to find a matching token file.
    """
    if kind not in TOKEN_KINDS:
        raise ShotBuilderError(f"unknown token kind: {kind}")

    paths: list[Path] = []
    if project:
        slug = slugify_project(project)
        project_path = PROJECTS_DIR / slug / kind
        if project_path.exists():
            paths.append(project_path)
    paths.append(WORKSPACE / kind)
    return paths


def slugify(s: str) -> str:
    """Filesystem-safe slug from arbitrary text (for filenames). Preserves case."""
    s = re.sub(r"[^A-Za-z0-9._-]+", "_", s.strip())
    return s[:60] or "untitled"


def unique_path(directory: Path, base: str, ext: str) -> Path:
    """Returns directory/base_001.ext, _002.ext, etc. — never overwrites."""
    n = 1
    while True:
        p = directory / f"{base}_{n:03d}.{ext.lstrip('.')}"
        if not p.exists():
            return p
        n += 1


def download_to_local(url: str, target: Path) -> Path:
    """Stream-download a URL to a local path. Returns the path. Mirrors to workspace if outside it."""
    target.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url) as response, target.open("wb") as f:  # noqa: S310 — trusted CDN
        shutil.copyfileobj(response, f)
    return target


def write_render_sidecar(
    artifact_path: Path,
    *,
    provider: str,
    model: str,
    render_type: str,
    project: str | None,
    prompt: str,
    cost_usd: float | None,
    tokens_used: list[str] | None = None,
    settings: dict[str, Any] | None = None,
    extra: dict[str, Any] | None = None,
) -> Path:
    """
    Write a sibling .md file next to a generated artifact. Lets users browse renders
    in any markdown viewer (Obsidian, VS Code, Chrome extension) and see exactly
    what prompt / tokens / cost produced each image or video.

    Output path: <artifact>.md (e.g., HERO_001.png → HERO_001.png.md)

    Returns the sidecar path.
    """
    sidecar = artifact_path.with_suffix(artifact_path.suffix + ".md")
    now_iso = datetime.now(timezone.utc).isoformat()
    tokens_used = tokens_used or []
    settings = settings or {}
    extra = extra or {}

    fm_lines = [
        "---",
        f"created: {now_iso}",
        f"type: render",
        f"artifact: {artifact_path.name}",
        f"provider: {provider}",
        f"model: {model}",
        f"render_type: {render_type}",
        f"project: {project or '_unsorted'}",
    ]
    if cost_usd is not None:
        fm_lines.append(f"cost_usd: {cost_usd:.4f}")
    if tokens_used:
        token_list = ", ".join(f'"{t}"' for t in tokens_used)
        fm_lines.append(f"tokens_used: [{token_list}]")
    for k, v in extra.items():
        # Skip empty / None values
        if v in (None, "", [], {}):
            continue
        if isinstance(v, str):
            fm_lines.append(f"{k}: {v}")
        else:
            fm_lines.append(f"{k}: {json.dumps(v)}")
    tag_list = ["render", render_type]
    if project:
        tag_list.append(project)
    fm_lines.append(f"tags: [{', '.join(tag_list)}]")
    fm_lines.append("---")
    fm = "\n".join(fm_lines) + "\n"

    # Body
    title = artifact_path.stem
    cost_line = f"${cost_usd:.4f} — {provider} {model}" if cost_usd is not None else f"{provider} {model}"
    body_lines = [
        "",
        f"# {title}",
        "",
        f"**Path:** `{artifact_path}`",
        f"**Cost:** {cost_line}",
    ]
    if project:
        body_lines.append(f"**Project:** `{project}`")
    # Pick an outer fence longer than any backtick run inside the prompt — prevents
    # an inner ``` fence from prematurely closing the outer wrapper and breaking
    # downstream markdown rendering.
    import re as _re
    _runs = _re.findall(r"`+", prompt)
    _max_inner = max((len(r) for r in _runs), default=0)
    _fence = "`" * max(3, _max_inner + 1)
    body_lines.extend(["", "## Prompt", "", _fence, prompt.strip(), _fence])

    if settings:
        body_lines.extend(["", "## Settings", ""])
        for k, v in settings.items():
            if v in (None, ""):
                continue
            body_lines.append(f"- **{k}:** `{v}`")

    if tokens_used:
        body_lines.extend(["", "## Tokens used", ""])
        for token in tokens_used:
            body_lines.append(f"- `{token}`")

    body_lines.extend(
        [
            "",
            "## Regenerate",
            "",
            "Drop the prompt above into a new shot-builder request, or copy this file's tokens "
            "into a fresh prompt. Settings show exactly what was used.",
            "",
        ]
    )

    sidecar.write_text(fm + "\n".join(body_lines))
    return sidecar


def append_index_render(row: dict[str, Any]) -> None:
    """Append one render row to INDEX.md's Recent renders block. Creates the table if missing."""
    if not INDEX_PATH.exists():
        return  # INDEX seeded by setup; if missing, skip silently

    text = INDEX_PATH.read_text()
    header = "## Recent renders"
    table_header = (
        "| Date | Provider | Model | Project | Format | Cost | Path |\n"
        "|---|---|---|---|---|---|---|"
    )
    new_row = (
        f"| {row['date']} | {row['provider']} | {row['model']} | "
        f"{row.get('project', '—')} | {row['format']} | {row.get('cost', '—')} | "
        f"`{row['path']}` |"
    )

    if header not in text:
        return  # Index has been hand-edited beyond recognition — don't clobber

    section_start = text.index(header)
    section_end = text.find("\n## ", section_start + len(header))
    if section_end == -1:
        section_end = len(text)
    block = text[section_start:section_end]

    if "*No renders yet.*" in block:
        # First-ever render — initialize the table
        new_block = f"{header}\n\n{table_header}\n{new_row}\n"
        # Drop the HTML hint comment too
        new_text = text.replace(block, new_block)
        # Strip any trailing hint comment that immediately follows
        new_text = re.sub(
            r"\n<!--\s*\nPer-render row format:.*?-->\n",
            "\n",
            new_text,
            count=1,
            flags=re.DOTALL,
        )
    else:
        # Append to existing table — find the last row
        lines = block.splitlines()
        last_table_line = max(
            (i for i, line in enumerate(lines) if line.startswith("|")),
            default=None,
        )
        if last_table_line is None:
            return
        lines.insert(last_table_line + 1, new_row)
        new_block = "\n".join(lines) + "\n"
        new_text = text.replace(block, new_block)

    INDEX_PATH.write_text(new_text)


def touch_index_modified() -> None:
    """Update the 'Last updated' line in INDEX.md."""
    if not INDEX_PATH.exists():
        return
    text = INDEX_PATH.read_text()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    text = re.sub(r"\*\*Last updated:\*\* .+", f"**Last updated:** {now}", text)
    INDEX_PATH.write_text(text)
