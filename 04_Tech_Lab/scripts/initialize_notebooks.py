# -*- coding: utf-8 -*-
"""
M7 Notebook Configuration Generator
Writes the 4 notebook-hub config JSONs to the vault's active_context layer.

HONEST NOTE: NotebookLM does NOT auto-read these as settings. They are (a) the
single source of truth for each hub's rules, and (b) loadable as a notebook SOURCE.
The gear/custom-summary + Gemini Gem still require a one-time UI paste
(see 01_Command_Center/M7_NOTEBOOK_HUBS_CONFIG.md).
"""
import os, json

SYNC_DIR = r"C:\Pineapple Contractors M7\03_Knowledge_Mat\active_context\notebook_configs"
SIGNATURE = "."
FIREWALL = {
    "colors_permitted": ["#1A365D", "#FBC02D", "#00BFFF"],
    "colors_blacklisted": ["green"],
    "text_mutations": {
        "free_inspection": "Complimentary Professional Photo Audit (CPPA)",
        "free_quote": "Complimentary Professional Photo Audit (CPPA)",
        "zero_down": "Full Restoration Coverage",
        "GAF": "IKO Certified",
    },
    "trust_anchors": ["RCAT License #03-0637", "IKO Certified", "(972) 928-0788", "since 2005"],
}

configs = {
    "seo_playbook_config.json": {
        "notebook_id": "PM7_SEO_PLAYBOOK",
        "system_role": "Lead SEO Librarian and GSC Data Analyst",
        "grounding_rules": "Analyze Google Search Console query metrics; optimize striking-distance terms (positions 5.0-20.0).",
        "aeo_mandate": "Deliver the exact answer to the target search phrase in sentence 1 to secure Google AI Mode citations.",
        "chat_extraction_prompt": "Review the loaded GSC sheets. Identify the top 3 high-impression keywords stuck on page 2 (positions 11-20). Extract query strings, CTR, matching URLs. Output a Markdown table [Keyword | Intent | Position | Impressions | Action Plan]. Apply M7 compliance (CPPA, zero green).",
        "gemini_gem_instructions": "You are the PM7 GSC Revenue Engine. Parse messy search data and identify immediate traffic wins. Filter for bottom-of-funnel intent across Frisco, Plano, McKinney, Allen. Mutate legacy terms to CPPA. Navy #1A365D + Gold #FBC02D; never green. Production-ready copy matrices, zero pleasantries.",
        "studio_panel_prompts": {
            "audio_overview": "Act as a Technical SEO Instructor. Synthesize the loaded search-performance data into a hyper-focused training brief. Explain how targeting premium DFW zip codes lifts local visibility on Google AI Overviews. Urgent, data-dense.",
            "video_overview": "50-second 50/5/3 script: 5s hook on off-season search drops, 42s technical value citing IKO Certified + RCAT #03-0637, 3s CTA to (972) 928-0788 for a Complimentary Professional Photo Audit.",
            "slide_deck": "Blueprint map: how local programmatic landing pages capture high-intent traffic. Navy/Gold hex labels. Highlight the validation-gate loop.",
            "blotato_feed": {"task": "generate_seo_social_payload", "format": "JSON_ONLY", "parameters": {"target_areas": ["Frisco", "Plano", "Lewisville"], "cta_string": "Book your Complimentary Professional Photo Audit (CPPA) at (972) 928-0788", "output_status": "PAUSED"}},
        },
        "compliance_firewall": FIREWALL,
    },
    "brand_content_config.json": {
        "notebook_id": "PM7_BRAND_CONTENT",
        "system_role": "Guardian of the Pineapple Standard Brand Voice",
        "tone_profile": "Authoritative, hardworking, family-focused, Polynesian-proud, zero-fluff",
        "multiplier_protocol": "Split one field documentation asset into 3 angles: The Sale, The Story, The Recruitment.",
        "chat_extraction_prompt": "Analyze brand assets, customer reviews, and the Tatafu Constitution. Extract 3 high-converting DFW roof-replacement stories. Re-write via the Content Multiplier: Sale (hail tracking), Story (Tongan proverb hooks), Recruitment (field adjusters). Save as PAUSED.",
        "gemini_gem_instructions": "You are the fractional CMO of Pineapple Contractors. Protect brand integrity while scaling high-ticket assets. Intercept 'free' -> CPPA; '$0 down' -> Full Restoration Coverage. Navy #1A365D primary, Gold #FBC02D focal; green forbidden. Close decks with the signature seal.",
        "studio_panel_prompts": {
            "audio_overview": "Act as Lead Brand Strategist. Turn our multi-generational history, 5-star reviews, and Tongan values into an energetic orientation track. Explain why a premium, zero-discount brand secures large residential + commercial projects without racing to the bottom.",
            "video_overview": "50-second SOP-V: 0-5s Gold-on-Navy pattern-break hook, 5-47s real field footage + RCAT #03-0637, 47-50s CTA to (972) 928-0788 for a CPPA.",
            "slide_deck": "Visual breakdown of the Content Multiplier loop: one smartphone asset splits into Sales, Heritage Story, Recruitment nodes. Enforce brand colors.",
            "blotato_feed": {"task": "generate_blotato_text_captions", "format": "JSON_ONLY", "variables": {"primary_color": "#1A365D", "secondary_color": "#FBC02D", "banned_phrases": ["free", "toa", "warrior"], "delivery_state": "PAUSED"}},
        },
        "compliance_firewall": FIREWALL,
    },
    "ops_sop_config.json": {
        "notebook_id": "PM7_OPS_SOP_MANUAL",
        "system_role": "Systems Automation Engineer and Core Architect",
        "operational_cadence": "Enforce daily/weekly/monthly lifecycle routines per the Mission Control Operator Manual.",
        "safety_gate": "Enforce the Outbox Shield. Every generated asset/DB write/script deploy lands PAUSED in Outbox_Drafts/.",
        "silo_discipline": "Silo roofing (Brand A) from restoration (Brand B). Never cross-contaminate dependencies.",
        "chat_extraction_prompt": "Review the Operator's Manual and 2026 SOP update. Extract the Monday-Sunday weekly routine. Name the required dashboard tab + validation script for each day. Strict Markdown checklist, no wrapper text.",
        "gemini_gem_instructions": "You are the PM7 Agent OS Technical Architect. Convert loose operational updates into deterministic flat-markdown scripts. Append STATUS: PAUSED atop every generation. Destroy 'free inspection'/'$0 out of pocket' -> premium equivalents. Maintain the 4-Fala structure. No fluff.",
        "studio_panel_prompts": {
            "audio_overview": "Act as Senior Operations Director. Synthesize the 4-folder matrix, terminal settings, and the Sunday Snapshot Protocol into a high-density training guide. Detail how PAUSED-in-Outbox protects margins and data.",
            "video_overview": "50-second training script: what to do when an LSA lead fires. Highlight the 5-minute speed-to-lead window, tracking setup, and disputing junk leads.",
            "slide_deck": "Sequential diagram of the Sunday Snapshot Protocol: copy live files, rename M7_Snapshot_YYYY_MM_DD, archive, refresh active_context.",
            "blotato_feed": {"task": "generate_ops_cadence_manifest", "format": "JSON_ONLY", "schedule": {"monday": "OpenSEO analysis & content", "thursday": "Thumbnail batches & micro-builds", "sunday": "Sunday Snapshot cleanup"}, "system_gate": "OUTBOX_SHIELD_ACTIVE"}},
        "compliance_firewall": FIREWALL,
    },
    "codex_technical_seo_config.json": {
        "notebook_id": "PM7_CODEX_TECHNICAL_SEO",
        "system_role": "Lead Technical Schema Engineer and Programmatic SEO Architect",
        "methodology": "Nico Stack reverse-engineering: parse competitor heading trees, map entity arrays, cluster hidden fan-out queries.",
        "tonality_profile": "Alex Hormozi style: zero-fluff, high-impact, short punchy, line-by-line.",
        "chat_extraction_prompt": "Review the technical SEO assets, DataForSEO/Windsor logs, and competitor header data. Extract the Nico on-page copy formula: content capsule technique, contextual link density, fan-out clustering. Output a clean playbook doc.",
        "gemini_gem_instructions": "You are the PM7 Technical SEO Architect. Convert competitor outlines into brand-compliant local landing-page matrices. Put the target query solution in the first 40 words of sentence 1 (Google AI Overviews). Hormozi line-by-line. Enforce CPPA + Full Restoration Coverage. Save as PAUSED.",
        "studio_panel_prompts": {
            "audio_overview": "Act as Lead Search Infrastructure Engineer. Turn intent-architecture layouts, citation logs, and Nico's cross-platform matrix into a technical class. Explain how connecting live Search Console data outranks big brands in DFW.",
            "video_overview": "50-second 50/5/3 technical script for high-net-worth owners: 5s pattern-interrupt on hidden storm damage, 42s forensic documentation + IKO Certified, 3s CTA to (972) 928-0788 for a CPPA.",
            "slide_deck": "Flat flowchart of the 10-step SEO lifecycle: tracking -> copy passes -> firewall sweep -> API staging -> sitemap -> 5-minute lead routing.",
            "blotato_feed": {"task": "generate_programmatic_seo_schema", "format": "JSON_ONLY", "payload": {"target_keywords": ["Roof Replacement Frisco 75034", "Storm Restoration Lewisville"], "required_license": "RCAT #03-0637", "output_directory": "Outbox_Drafts/schema/", "status": "PAUSED"}}},
        "compliance_firewall": FIREWALL,
    },
}

def main():
    os.makedirs(SYNC_DIR, exist_ok=True)
    for filename, data in configs.items():
        data["system_signature"] = SIGNATURE
        with open(os.path.join(SYNC_DIR, filename), "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"[M7 OS] wrote {filename}")
    print("[M7 OS] All 4 notebook configuration matrices written.")

if __name__ == "__main__":
    main()
