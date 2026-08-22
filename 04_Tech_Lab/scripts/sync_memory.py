#!/usr/bin/env python3
"""Compatibility entry point for the root-relative M7 memory compiler.

The old implementation copied three guessed files between hard-coded OneDrive
and retired Pineapple-Mana paths, then claimed the memory was fully current.
That workflow is disabled. Keep this filename for existing shortcuts while
delegating to the authoritative, project-relative memory_sync.py implementation.
"""

from __future__ import annotations

from memory_sync import main


if __name__ == "__main__":
    raise SystemExit(main())
