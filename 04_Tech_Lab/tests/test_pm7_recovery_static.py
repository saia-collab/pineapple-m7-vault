#!/usr/bin/env python3
"""Dependency-free static acceptance tests for the PM7 recovery patch."""

from __future__ import annotations

import importlib.util
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class RecoveryStaticTests(unittest.TestCase):
    def read(self, relative: str) -> str:
        return (ROOT / relative).read_text(encoding="utf-8")

    def test_authority_chain_is_current(self) -> None:
        claude = self.read("CLAUDE.md")
        context = self.read("CONTEXT.md")
        core = self.read("m7_core_rules.config")
        self.assertIn("M7_START_HERE.md", claude)
        self.assertIn("M7_SYSTEM_RECOVERY_AND_ROUTING_SOP_2026-08-22.md", claude)
        self.assertIn("#003299", context)
        self.assertIn("founded         = 2021", core)
        self.assertIn("omniroute_port  = 20128", core)
        self.assertNotIn("Read `01_Command_Center/M7_MASTER_SOP.md`", claude)

    def test_launchers_do_not_embed_placeholder_credentials(self) -> None:
        free = self.read("LAUNCH_PM7_FREE.bat")
        paid = self.read("LAUNCH_PM7_PAID.bat")
        studio = self.read("LAUNCH_PM7_STUDIO.bat")
        all_text = free + paid + studio
        self.assertNotIn("sk-pm7-free-local-token", all_text)
        self.assertIn("omniroute launch", free)
        self.assertIn("ANTHROPIC_AUTH_TOKEN=", paid)
        self.assertIn("START-PINEAPPLE-AGENT-OS.ps1", studio)
        gemini = self.read("LAUNCH_PM7_GEMINI.bat")
        google = self.read("CONFIGURE_PM7_GOOGLE_AI.bat")
        self.assertIn("omniroute run gemini --model auto/best-chat", gemini)
        self.assertIn('ANTIGRAVITY_CREDITS=off', google)
        self.assertNotIn("MITM", google.split("Do not enable", 1)[0])

    def test_model_config_is_dynamic_and_valid(self) -> None:
        config = json.loads(self.read("04_Tech_Lab/config/models.json"))
        self.assertEqual(config["schema_version"], 2)
        self.assertEqual(config["routes"]["chat"], "auto/best-chat")
        self.assertEqual(config["routes"]["coding"], "auto/best-coding")
        self.assertFalse(config["ollama"]["automatic_pull"])
        serialized = json.dumps(config)
        for retired in ("gemma4-pineapple", "deepseek-v4", "qwen3.6"):
            self.assertNotIn(retired, serialized)

    def test_doctor_reads_obsidian_key_from_environment(self) -> None:
        doctor = self.read("04_Tech_Lab/m7_doctor.py")
        self.assertIn('os.environ.get("OBSIDIAN_REST_API_KEY"', doctor)
        self.assertNotRegex(doctor, r"\b[0-9a-fA-F]{64}\b")

    def test_known_live_key_shapes_removed_from_current_targets(self) -> None:
        targets = [
            "01_Command_Center/M7_COMMAND_CENTER.html",
            "01_Command_Center/M7_QUICK_CARD.md",
            "01_Command_Center/M7_STUDY_GUIDE.md",
            "03_Knowledge_Mat/raw/Copy of Prompt Compression",
            "03_Knowledge_Mat/00_Atlas/templates/Gemini_File_Search_API_Kit/PDF and Text File Upload to Google Gemini File Search Store.json",
            "03_Knowledge_Mat/00_Atlas/templates/seo-pack/blog-post.md",
            "04_Tech_Lab/m7_doctor.py",
        ]
        text = "\n".join(self.read(path) for path in targets)
        self.assertNotRegex(text, r"\bsk-proj-[A-Za-z0-9_-]{20,}")
        self.assertNotRegex(text, r"\bAIza[A-Za-z0-9_-]{20,}")
        credential_targets = "\n".join(
            self.read(path)
            for path in (
                "01_Command_Center/M7_COMMAND_CENTER.html",
                "01_Command_Center/M7_QUICK_CARD.md",
                "01_Command_Center/M7_STUDY_GUIDE.md",
                "04_Tech_Lab/m7_doctor.py",
            )
        )
        self.assertNotRegex(credential_targets, r"\b[0-9a-fA-F]{64}\b")
        blog_template = self.read("03_Knowledge_Mat/00_Atlas/templates/seo-pack/blog-post.md")
        self.assertNotRegex(blog_template, r'(?m)^KEY="[A-Za-z0-9_-]{40,}"$')

    def test_current_approved_copy_passes_firewall(self) -> None:
        path = ROOT / "04_Tech_Lab/scripts/brand_firewall.py"
        spec = importlib.util.spec_from_file_location("brand_firewall", path)
        self.assertIsNotNone(spec)
        module = importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(module)
        violations, _ = module.scan_text(
            "IKO Certified. Schedule a free roof inspection.",
            Path("<test>"),
        )
        self.assertEqual(violations, [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
