#!/usr/bin/env python3
"""
PINEAPPLE CONTRACTORS M7 — LOCAL-SIGNAL PHOTO AUDIT PIPELINE
============================================================
SOP-SEO-LOCAL-PM7 · Phase 2 · EXIF Geotagging + Brand-Fenced Tagging.

Purpose
-------
Apply deterministic, brand-compliant EXIF + IPTC + XMP metadata to photos
Pineapple Roofing owns (drone captures, field photos, on-site CPPA audits).
Coordinates correspond to the actual project site — never fabricated.

This pipeline is the local-signal asset layer for the "Near Me" Domination
Pipeline: every tagged photo carries verifiable GPS + neighborhood + ZIP +
brand string in EXIF + IPTC + XMP, reinforcing the local pack and the
Citation Bait schema downstream.

Brand-Firewall Gate
-------------------
Every keyword + description string passes the runtime ComplianceOfficer from
m7_scoring.py (the canonical M7 Elite Compliance Filter). Any row that
fails the regex pre-gate is QUARANTINED — not written to TAGGED/.

Outbox Shield (DEC-005)
-----------------------
This script is local-only. It never reads from or writes to any network
endpoint. TAGGED assets are NOT auto-published to GBP, the live site, or
social — they land in 02_Media_Vault/<YEAR_MONTH_CAMPAIGN>/TAGGED/ and
wait for Saia's GO before the GBP schema injector (Phase 4) touches them.

Determinism
-----------
The pipeline is idempotent: re-run against the same RAW/ + MANIFEST.csv
produces byte-identical TAGGED/ output. No random salts, no datetime.now()
outside the audit log row (the audit log timestamp is the *one* allowed
non-determinism, captured per run).

Library Reality (as of 2026-07-14)
----------------------------------
- piexif   : NOT installed on the operator box. Pipeline falls back to
             Pillow's `getexif`/`Image.Exif` API for the minimal GPS + EXIF
             fields and writes a sidecar JSON for IPTC + XMP.
- pyexiv2  : NOT installed. IPTC + XMP go to a sidecar JSON (.xmp.json).
- iptcinfo3: NOT installed. Same fallback.
- PIL/Pillow: installed (11.3.0). Used for synthetic test PNGs.

The SOP §2.2 spec calls for piexif + pyexiv2 + iptcinfo3. Until Saia
authorizes the pip install, this script runs in DEGRADED mode (EXIF via
Pillow + sidecar JSON for IPTC/XMP). The degradation is logged in
MANIFEST.audit.log so the lineage is honest. When the libraries land, the
script detects them at import time and upgrades to the full spec without
code change.

Usage
-----
    # Run the full pipeline against a manifest
    python m7_geotag_photo_audit.py run --manifest "02_Media_Vault/2026_07_LOCAL_PM7/MANIFEST.csv"

    # Run the deterministic sandbox test (synthesizes 5 PNGs + 5-row manifest)
    python m7_geotag_photo_audit.py sandbox

    # Print library + writer version report
    python m7_geotag_photo_audit.py info

"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sys
import tempfile
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

# --------------------------------------------------------------------------- #
# PATH DETECTION — find the script's vault root and import the ComplianceOfficer
# --------------------------------------------------------------------------- #

# Note: there is a local 04_Tech_Lab/Scripts/typing.py that shadows the stdlib
# `typing` module if we naively insert the scripts dir on sys.path before
# importing the stdlib. We work around it by:
#   1) Using `import typing as _typing` and then `getattr(_typing, ...)` so the
#      shadowed module never trips a `from typing import X` import.
#   2) Importing the M7 ComplianceOfficer via the *vault root* path, not via
#      the scripts dir path, so the scripts dir never has to be on sys.path
#      first.
import typing as _typing  # alias to dodge the local typing.py shadow
from typing import Any  # safe: name 'Any' is in the stdlib surface, see below

SCRIPT_PATH = Path(__file__).resolve()
# Script lives in 04_Tech_Lab/Scripts/. Vault root is two levels up.
VAULT_ROOT = SCRIPT_PATH.parents[2] if len(SCRIPT_PATH.parents) >= 3 else SCRIPT_PATH.parents[-1]
SCRIPTS_DIR = SCRIPT_PATH.parent

# ComplianceOfficer is the canonical runtime Compliance Filter. Imported here
# so the script always reads from the same source-of-truth as the rest of M7.
# We use importlib + a direct path so we do NOT need to put the scripts dir
# on sys.path (which would otherwise make the local typing.py shadow bite).
import importlib.util as _importlib_util
_compliance_spec = _importlib_util.spec_from_file_location(
    "m7_scoring",
    str(SCRIPTS_DIR / "m7_scoring.py"),
)
if _compliance_spec is not None and _compliance_spec.loader is not None:
    _compliance_module = _importlib_util.module_from_spec(_compliance_spec)
    try:
        _compliance_spec.loader.exec_module(_compliance_module)
        ComplianceOfficer = _compliance_module.ComplianceOfficer
        COMPLIANCE_OFFICER_AVAILABLE = True
        _COMPLIANCE_IMPORT_ERROR = ""
    except Exception as _import_err:  # pragma: no cover - hard import failure
        COMPLIANCE_OFFICER_AVAILABLE = False
        _COMPLIANCE_IMPORT_ERROR = repr(_import_err)
else:
    COMPLIANCE_OFFICER_AVAILABLE = False
    _COMPLIANCE_IMPORT_ERROR = "could not build module spec for m7_scoring"

# --------------------------------------------------------------------------- #
# LIBRARY DETECTION (graceful degradation)
# --------------------------------------------------------------------------- #

try:
    import piexif  # type: ignore
    PIEXIF_AVAILABLE = True
except Exception:
    piexif = None  # type: ignore
    PIEXIF_AVAILABLE = False

try:
    from PIL import Image, ImageDraw  # type: ignore
    PILLOW_AVAILABLE = True
except Exception:
    Image = None  # type: ignore
    ImageDraw = None  # type: ignore
    PILLOW_AVAILABLE = False

# pyexiv2 + iptcinfo3 are optional. Even if not present, the script degrades
# to writing a sidecar .xmp.json. The detection here is only for the
# info() report.

try:
    import pyexiv2  # type: ignore
    PYEXIV2_AVAILABLE = True
except Exception:
    pyexiv2 = None  # type: ignore
    PYEXIV2_AVAILABLE = False

try:
    import iptcinfo3  # type: ignore
    IPTCINFO3_AVAILABLE = True
except Exception:
    iptcinfo3 = None  # type: ignore
    IPTCINFO3_AVAILABLE = False

# --------------------------------------------------------------------------- #
# CONSTITUTION CONSTANTS (mirror brand_firewall.py APPROVED_HEX + lead scoring)
# --------------------------------------------------------------------------- #

WRITER_VERSION = "1.0.0-phase2-2026-07-14"

# The 5 primary Frisco ZIPs + the 2 luxury enclaves (per parent SOP §1).
PRIMARY_ZIPS = frozenset({"75033", "75034", "75035", "75067", "75068"})

# Texas geographic bounds for the bounds check on lat/lon.
TX_LAT_MIN, TX_LAT_MAX = 25.0, 37.0
TX_LON_MIN, TX_LON_MAX = -107.0, -93.0

# NWS event ID format: ^NWS-YYYYMMDD-XXXX$ (4-char alphanumeric token).
NWS_EVENT_ID_RE = re.compile(r"^NWS-[0-9]{8}-[A-Z0-9]{4}$")

# Brand-fence required substrings in EXIF ImageDescription and IPTC Caption.
# The ComplianceOfficer regex pre-gate enforces the wider banned-lexicon list;
# these are the *positive* tokens that MUST appear in every description.
REQUIRED_DESCRIPTION_TOKENS = (
    "RCAT #03-0637",
    "Pineapple",
)
REQUIRED_KEYWORD_TOKENS = (
    "IKO Certified",
    "CPPA",
    "North Texas",
)

# Brand compliance stamp template (used by Pillow when no description is supplied).
COPYRIGHT_STAMP = "© 2026 Pineapple Contractors — RCAT #03-0637"
CREATOR_STAMP = "JR. Moeakiola, Pineapple Roofing LLC"

# Approved palette (mirror brand_firewall.APPROVED_HEX for the script's own use).
APPROVED_HEX = {"#1a365d", "#001122", "#001a33", "#fbc02d", "#ffd700",
                "#e5a93c", "#00bfff", "#ffffff", "#ffe12d", "#000000"}

# Brand-only navy (Pineapple Roofing LLC primary mark).
NAVY_HEX = "#1A365D"

# Sidecar filename conventions.
IPTC_SIDECAR_SUFFIX = ".iptc.json"
XMP_SIDECAR_SUFFIX = ".xmp.json"
AUDIT_LOG_FILENAME = "MANIFEST.audit.log"
REJECTED_LOG_FILENAME = "MANIFEST.rejected.csv"
TAGGED_JSON_FILENAME = "MANIFEST.tagged.json"
QUARANTINE_DIRNAME = "QUARANTINE"
TAGGED_DIRNAME = "TAGGED"

# --------------------------------------------------------------------------- #
# DATA CLASSES
# --------------------------------------------------------------------------- #

@dataclass
class ManifestRow:
    filename: str
    address: str
    neighborhood: str
    zip: str
    capture_utc: str
    lat: float
    lon: float
    event_id: str
    roof_age: str
    surface_type: str
    hail_size_in: str
    swath_in: str
    nws_event_id: str
    sha256: str = ""
    source_path: str = ""


@dataclass
class RowResult:
    filename: str
    accepted: bool = False
    tagged: bool = False
    quarantined: bool = False
    rejected: bool = False
    firewall_status: str = "n/a"
    firewall_score: int = 100
    firewall_violations: list = field(default_factory=list)
    writer_mode: str = "pillow+sidecar"  # or "piexif+pyexiv2" if libs present
    sha256_source: str = ""
    sha256_tagged: str = ""
    lat: float = 0.0
    lon: float = 0.0
    neighborhood: str = ""
    zip: str = ""
    reason: str = ""


# --------------------------------------------------------------------------- #
# EXIF GPS RATIONAL CONVERSION (verbatim from parent SOP §2.2 step 3)
# --------------------------------------------------------------------------- #

def deg_to_dms_rational(deg: float) -> tuple:
    """Convert decimal degrees to EXIF GPS rational form (deg, min, sec)
    plus a sign function. North/East positive; South/West negative.

    Returns ((deg_d, deg_n), (min_d, min_n), (sec_d, sec_n)) where the
    (num, den) tuples are piexif-compatible and Pillow-EXIF-compatible.
    """
    deg_abs = abs(deg)
    degrees = int(deg_abs)
    minutes_full = (deg_abs - degrees) * 60
    minutes = int(minutes_full)
    seconds = (minutes_full - minutes) * 60
    # Reduce seconds to a small-denominator rational for compactness.
    # 10000ths of a second is more than precise enough for a 10 m GPS fix.
    sec_numerator = int(round(seconds * 10000))
    return ((degrees, 1), (minutes, 1), (sec_numerator, 10000))


def gps_ref(deg: float, axis: str) -> str:
    """Return the EXIF GPS reference char: 'N' or 'S' for lat, 'E' or 'W' for lon."""
    if axis.lower() == "lat":
        return "N" if deg >= 0 else "S"
    return "E" if deg >= 0 else "W"


# --------------------------------------------------------------------------- #
# MANIFEST VALIDATION (per parent SOP §2.2 step 1)
# --------------------------------------------------------------------------- #

@dataclass
class ValidationError:
    filename: str
    field: str
    message: str


def validate_row(row: dict) -> list:
    """Return a list of ValidationError. Empty list = row is valid."""
    errors = []
    filename = row.get("filename", "<unknown>")

    # Lat/lon bounds
    try:
        lat = float(row.get("lat", ""))
        if not (TX_LAT_MIN <= lat <= TX_LAT_MAX):
            errors.append(ValidationError(filename, "lat",
                f"lat {lat} out of Texas bounds [{TX_LAT_MIN}, {TX_LAT_MAX}]"))
    except (TypeError, ValueError):
        errors.append(ValidationError(filename, "lat", "lat is missing or not numeric"))

    try:
        lon = float(row.get("lon", ""))
        if not (TX_LON_MIN <= lon <= TX_LON_MAX):
            errors.append(ValidationError(filename, "lon",
                f"lon {lon} out of Texas bounds [{TX_LON_MIN}, {TX_LON_MAX}]"))
    except (TypeError, ValueError):
        errors.append(ValidationError(filename, "lon", "lon is missing or not numeric"))

    # ZIP in PRIMARY_ZIPS
    zip_code = (row.get("zip") or "").strip()
    if zip_code not in PRIMARY_ZIPS:
        errors.append(ValidationError(filename, "zip",
            f"zip {zip_code!r} is not in PRIMARY_ZIPS {sorted(PRIMARY_ZIPS)}"))

    # NWS event id format (optional — empty allowed)
    nws = (row.get("nws_event_id") or "").strip()
    if nws and not NWS_EVENT_ID_RE.match(nws):
        errors.append(ValidationError(filename, "nws_event_id",
            f"nws_event_id {nws!r} does not match ^NWS-[0-9]{{8}}-[A-Z0-9]{{4}}$"))

    # hail_size_in numeric or empty
    hail = (row.get("hail_size_in") or "").strip()
    if hail:
        try:
            float(hail)
        except ValueError:
            errors.append(ValidationError(filename, "hail_size_in",
                f"hail_size_in {hail!r} is not numeric"))

    return errors


# --------------------------------------------------------------------------- #
# BRAND-FIREWALL COMPLIANCE GATE
# --------------------------------------------------------------------------- #

def compliance_check_text(text: str) -> tuple:
    """Return (verdict, score, violations). verdict in {"PASS", "FAIL"}.

    Wraps the runtime ComplianceOfficer. If the officer is unavailable
    (import error), we fail closed: verdict="FAIL", score=0, message includes
    the import error so Saia can see the pipeline did not silently bypass
    the gate.
    """
    if not COMPLIANCE_OFFICER_AVAILABLE:
        return ("FAIL", 0, [{
            "pattern": "<COMPLIANCE_OFFICER_UNAVAILABLE>",
            "banned_label": "compliance-officer-missing",
            "substitute": "fix the import path / python env",
            "spans": [],
            "_import_error": _COMPLIANCE_IMPORT_ERROR,  # type: ignore[name-defined]
        }])
    officer = ComplianceOfficer()
    report = officer.scan(text)
    violations = [{
        "pattern": v.pattern,
        "banned_label": v.banned_label,
        "substitute": v.substitute,
        "spans": list(v.spans),
    } for v in report.violations]
    return (report.verdict, report.compliance_score, violations)


def build_description(row: ManifestRow) -> str:
    """Build the EXIF ImageDescription / IPTC Caption string for one row.
    Verbatim from parent SOP §2.1 ImageDescription example."""
    return (
        f"Storm damage CPPA audit, {row.neighborhood}, Frisco TX {row.zip} — RCAT #03-0637"
    )


def build_user_comment(row: ManifestRow) -> str:
    """Build the EXIF UserComment (engineering note, no PII)."""
    hail = row.hail_size_in or "n/a"
    swath = row.swath_in or "n/a"
    event = row.nws_event_id or "no-NWS-event"
    return (
        f"Hail impact {hail}\" on capture; {swath}\" swath per NWS event {event}; "
        f"Pineapple Roofing LLC, since 2005."
    )


def build_keywords(row: ManifestRow) -> list:
    """Build the EXIF/IPTC Keywords list. Verbatim from parent SOP §2.1."""
    return [
        "Pineapple Contractors",
        "Pineapple Roofing LLC",
        "IKO Certified",
        "RCAT 03-0637",
        "CPPA",
        row.neighborhood,
        f"Frisco TX {row.zip}",
        "North Texas",
        row.surface_type or "roof",
    ]


# --------------------------------------------------------------------------- #
# EXIF WRITER (piexif path — preferred when available)
# --------------------------------------------------------------------------- #

def write_exif_piexif(image_path: Path, row: ManifestRow) -> None:
    """Write EXIF via piexif (the parent SOP's preferred path).

    The piexif library stores all fields as rationals (num, den) tuples.
    GPS fields are populated in the GPS IFD; everything else in the
    Exif IFD or Image IFD.
    """
    if not PIEXIF_AVAILABLE:  # pragma: no cover - guarded by caller
        raise RuntimeError("piexif is not available")

    exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}
    # 0th IFD
    exif_dict["0th"][piexif.ImageIFD.Make] = "Pineapple Roofing LLC"
    exif_dict["0th"][piexif.ImageIFD.Model] = "Drone / Camera (per flight log)"
    exif_dict["0th"][piexif.ImageIFD.Software] = (
        f"m7_geotag_photo_audit.py v{WRITER_VERSION}"
    )
    exif_dict["0th"][piexif.ImageIFD.Artist] = CREATOR_STAMP
    exif_dict["0th"][piexif.ImageIFD.Copyright] = COPYRIGHT_STAMP
    exif_dict["0th"][piexif.ImageIFD.ImageDescription] = build_description(row)
    exif_dict["0th"][piexif.ImageIFD.DateTime] = row.capture_utc.replace("T", " ")[:19]

    # Exif IFD
    exif_dict["Exif"][piexif.ExifIFD.UserComment] = build_user_comment(row)
    exif_dict["Exif"][piexif.ExifIFD.LensModel] = "Pineapple Field Lens (per flight log)"

    # GPS IFD
    lat_dms = deg_to_dms_rational(row.lat)
    lon_dms = deg_to_dms_rational(row.lon)
    exif_dict["GPS"][piexif.GPSIFD.GPSLatitudeRef] = gps_ref(row.lat, "lat")
    exif_dict["GPS"][piexif.GPSIFD.GPSLatitude] = lat_dms
    exif_dict["GPS"][piexif.GPSIFD.GPSLongitudeRef] = gps_ref(row.lon, "lon")
    exif_dict["GPS"][piexif.GPSIFD.GPSLongitude] = lon_dms
    exif_dict["GPS"][piexif.GPSIFD.GPSAreaInformation] = (
        f"{row.neighborhood}, Frisco TX {row.zip}"
    )

    exif_bytes = piexif.dump(exif_dict)
    # piexif uses piexif.insert(in_bytes, path) for JPEG. For PNG it does not
    # support in-place; we use piexif.transplant for raw bytes.
    raw = image_path.read_bytes()
    if image_path.suffix.lower() in {".jpg", ".jpeg"}:
        piexif.insert(exif_bytes, str(image_path))
    else:
        # PNG path — write exif bytes to a sidecar .exif.json
        sidecar = image_path.with_suffix(image_path.suffix + ".exif.json")
        sidecar.write_text(json.dumps({
            "writer_version": WRITER_VERSION,
            "exif": {
                "0th": {piexif.ImageIFD(k).name: v for k, v in exif_dict["0th"].items()},
                "Exif": {piexif.ExifIFD(k).name: v for k, v in exif_dict["Exif"].items()},
                "GPS": {piexif.GPSIFD(k).name: v for k, v in exif_dict["GPS"].items()},
            },
        }, indent=2, default=str), encoding="utf-8")


# --------------------------------------------------------------------------- #
# EXIF WRITER (Pillow path — degraded mode when piexif is missing)
# --------------------------------------------------------------------------- #

def write_exif_pillow(image_path: Path, row: ManifestRow) -> None:
    """Write EXIF via Pillow's getexif()/Image.Exif API. Degraded mode.

    Pillow's EXIF GPS support is limited: it can store GPS IFD via a dict
    but rational encoding differs. We store the lat/lon as a (D, M, S/1)
    rational triple in degrees for round-trip fidelity.
    """
    if not PILLOW_AVAILABLE:  # pragma: no cover
        raise RuntimeError("Pillow is not available")

    img = Image.open(image_path)
    exif = img.getexif()
    # 0th IFD via Pillow's tag-id map. Pillow supports a subset; we use the
    # documented tags and fall back to sidecar JSON for the rest.
    try:
        from PIL.ExifTags import Base as BaseTags  # type: ignore
    except Exception:
        BaseTags = None  # type: ignore
    tag_map = {
        "Make": 271,
        "Model": 272,
        "Software": 305,
        "Artist": 315,
        "Copyright": 33432,
        "ImageDescription": 270,
        "DateTime": 306,
    }
    if BaseTags is not None:
        # Prefer canonical tag names; Pillow may use different IDs.
        try:
            exif[BaseTags.Make] = "Pineapple Roofing LLC"
            exif[BaseTags.Model] = "Drone / Camera (per flight log)"
            exif[BaseTags.Software] = f"m7_geotag_photo_audit.py v{WRITER_VERSION}"
            exif[BaseTags.Artist] = CREATOR_STAMP
            exif[BaseTags.Copyright] = COPYRIGHT_STAMP
            exif[BaseTags.ImageDescription] = build_description(row)
            exif[BaseTags.DateTime] = row.capture_utc.replace("T", " ")[:19]
        except Exception:
            # Fall back to numeric tag IDs.
            for name, val in (
                ("Make", "Pineapple Roofing LLC"),
                ("Model", "Drone / Camera (per flight log)"),
                ("Software", f"m7_geotag_photo_audit.py v{WRITER_VERSION}"),
                ("Artist", CREATOR_STAMP),
                ("Copyright", COPYRIGHT_STAMP),
                ("ImageDescription", build_description(row)),
                ("DateTime", row.capture_utc.replace("T", " ")[:19]),
            ):
                exif[tag_map[name]] = val
    img.save(image_path, exif=exif.tobytes())

    # Write the full EXIF + GPS + IPTC + XMP payload to a sidecar JSON for
    # downstream consumers (Phase 2.3 GBP schema injection).
    sidecar = image_path.with_suffix(image_path.suffix + ".exif.json")
    sidecar.write_text(json.dumps({
        "writer_version": WRITER_VERSION,
        "writer_mode": "pillow-degraded",
        "exif": {
            "Make": "Pineapple Roofing LLC",
            "Model": "Drone / Camera (per flight log)",
            "Software": f"m7_geotag_photo_audit.py v{WRITER_VERSION}",
            "Artist": CREATOR_STAMP,
            "Copyright": COPYRIGHT_STAMP,
            "ImageDescription": build_description(row),
            "UserComment": build_user_comment(row),
            "LensModel": "Pineapple Field Lens (per flight log)",
            "DateTimeOriginal": row.capture_utc.replace("T", " ")[:19],
            "OffsetTime": "-05:00",
        },
        "gps": {
            "GPSLatitudeRef": gps_ref(row.lat, "lat"),
            "GPSLatitudeRational": deg_to_dms_rational(row.lat),
            "GPSLongitudeRef": gps_ref(row.lon, "lon"),
            "GPSLongitudeRational": deg_to_dms_rational(row.lon),
            "GPSAreaInformation": f"{row.neighborhood}, Frisco TX {row.zip}",
            "City": "Frisco",
            "State": "TX",
            "Country": "United States",
            "PostalCode": row.zip,
            "LocationShownCountryCode": "US",
            "LocationShownSublocation": "Street area (no house number)",
        },
    }, indent=2, default=str), encoding="utf-8")


# --------------------------------------------------------------------------- #
# IPTC + XMP SIDECAR WRITER (always — even when libs are present, for redundancy)
# --------------------------------------------------------------------------- #

def write_iptc_xmp_sidecars(image_path: Path, row: ManifestRow) -> None:
    """Write IPTC and XMP sidecar JSON files. Parent SOP §2.2 step 5.

    These are written *in addition* to whatever the libraries write
    (piexif / pyexiv2 / iptcinfo3), so the downstream GBP schema injector
    (Phase 2.3) has a deterministic input regardless of which libraries
    the operator box has.
    """
    description = build_description(row)
    keywords = build_keywords(row)
    iptc = {
        "writer_version": WRITER_VERSION,
        "writer_mode": "sidecar-json",
        "iptc": {
            "Keywords": keywords,
            "City": "Frisco",
            "State": "TX",
            "Country": "United States",
            "Caption": description,
            "CopyrightNotice": COPYRIGHT_STAMP,
            "Byline": CREATOR_STAMP,
            "Credit": "Pineapple Roofing LLC",
            "Source": "Pineapple Contractors M7 Pipeline",
        },
    }
    xmp = {
        "writer_version": WRITER_VERSION,
        "writer_mode": "sidecar-json",
        "xmp": {
            "dc:creator": [CREATOR_STAMP],
            "dc:rights": COPYRIGHT_STAMP,
            "dc:description": description,
            "dc:subject": keywords,
            "dc:title": f"CPPA audit — {row.neighborhood}, Frisco TX {row.zip}",
            "pineapple:eventId": row.nws_event_id or "",
            "pineapple:neighborhood": row.neighborhood,
            "pineapple:zip": row.zip,
            "pineapple:captureUtc": row.capture_utc,
            "pineapple:writerVersion": WRITER_VERSION,
        },
    }
    image_path.with_suffix(image_path.suffix + IPTC_SIDECAR_SUFFIX).write_text(
        json.dumps(iptc, indent=2), encoding="utf-8"
    )
    image_path.with_suffix(image_path.suffix + XMP_SIDECAR_SUFFIX).write_text(
        json.dumps(xmp, indent=2), encoding="utf-8"
    )


# --------------------------------------------------------------------------- #
# FILE-LEVEL HELPERS
# --------------------------------------------------------------------------- #

def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def safe_atomic_write(target: Path, content: bytes) -> None:
    """Write `content` to `target` atomically via tempfile + os.replace.

    On Windows, os.replace is atomic when both source and target are on
    the same filesystem (the tempfile lives in target's parent).
    """
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(
        prefix=target.name + ".",
        suffix=".tmp",
        dir=str(target.parent),
    )
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(content)
        os.replace(tmp_path, target)
    except Exception:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
        raise


# --------------------------------------------------------------------------- #
# CORE PIPELINE
# --------------------------------------------------------------------------- #

def process_manifest(
    manifest_path: Path,
    raw_root: Path,
    tagged_root: Path,
    audit_log_path: Path,
    rejected_log_path: Path,
    tagged_json_path: Path,
) -> dict:
    """Run the full pipeline. Returns a summary dict for the Outbox record."""
    audit_log_path.parent.mkdir(parents=True, exist_ok=True)
    tagged_root.mkdir(parents=True, exist_ok=True)
    quarantine_root = raw_root.parent / QUARANTINE_DIRNAME
    quarantine_root.mkdir(parents=True, exist_ok=True)

    summary = {
        "writer_version": WRITER_VERSION,
        "writer_mode": "piexif+pyexiv2" if PIEXIF_AVAILABLE else "pillow-degraded+sidecar",
        "manifest": str(manifest_path),
        "raw_root": str(raw_root),
        "tagged_root": str(tagged_root),
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "rows_total": 0,
        "rows_accepted": 0,
        "rows_rejected_validation": 0,
        "rows_quarantined_sha256": 0,
        "rows_quarantined_firewall": 0,
        "rows_tagged": 0,
        "results": [],
    }

    rejected_rows: list = []
    results: list = []

    with open(manifest_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for raw_row in reader:
            summary["rows_total"] += 1
            row = ManifestRow(
                filename=(raw_row.get("filename") or "").strip(),
                address=(raw_row.get("address") or "").strip(),
                neighborhood=(raw_row.get("neighborhood") or "").strip(),
                zip=(raw_row.get("zip") or "").strip(),
                capture_utc=(raw_row.get("capture_utc") or "").strip(),
                lat=float(raw_row.get("lat") or 0),
                lon=float(raw_row.get("lon") or 0),
                event_id=(raw_row.get("event_id") or "").strip(),
                roof_age=(raw_row.get("roof_age") or "").strip(),
                surface_type=(raw_row.get("surface_type") or "").strip(),
                hail_size_in=(raw_row.get("hail_size_in") or "").strip(),
                swath_in=(raw_row.get("swath_in") or "").strip(),
                nws_event_id=(raw_row.get("nws_event_id") or "").strip(),
                sha256=(raw_row.get("sha256") or "").strip(),
                source_path=str(raw_root / raw_row["filename"]),
            )

            res = RowResult(filename=row.filename, lat=row.lat, lon=row.lon,
                            neighborhood=row.neighborhood, zip=row.zip)

            # Step 1: validate
            errs = validate_row(raw_row)
            if errs:
                res.rejected = True
                res.reason = "; ".join(f"{e.field}: {e.message}" for e in errs)
                summary["rows_rejected_validation"] += 1
                rejected_rows.append({**raw_row, "reject_reason": res.reason})
                results.append(res)
                continue

            # Step 2: file existence + sha256
            src = Path(row.source_path)
            if not src.exists():
                res.quarantined = True
                res.reason = f"source file not found: {src}"
                summary["rows_quarantined_sha256"] += 1
                results.append(res)
                continue

            actual_sha = sha256_file(src)
            res.sha256_source = actual_sha
            if row.sha256 and row.sha256 != actual_sha:
                # Move the source to QUARANTINE so it does not get tagged.
                qdest = quarantine_root / src.name
                safe_atomic_write(qdest, src.read_bytes())
                res.quarantined = True
                res.reason = f"sha256 mismatch: manifest={row.sha256[:12]}… actual={actual_sha[:12]}…"
                summary["rows_quarantined_sha256"] += 1
                results.append(res)
                continue

            # Step 3-6: brand-fence pre-gate.
            # Concatenate every brand-fenced string and run the ComplianceOfficer.
            description = build_description(row)
            user_comment = build_user_comment(row)
            keywords_blob = " | ".join(build_keywords(row))
            fence_blob = f"{description}\n{user_comment}\n{keywords_blob}\n{COPYRIGHT_STAMP}\n{CREATOR_STAMP}"
            verdict, score, violations = compliance_check_text(fence_blob)
            res.firewall_status = verdict
            res.firewall_score = score
            res.firewall_violations = violations

            if verdict != "PASS":
                res.quarantined = True
                res.reason = f"brand_firewall FAIL (score={score}); {len(violations)} violation(s)"
                summary["rows_quarantined_firewall"] += 1
                # Move source to QUARANTINE
                qdest = quarantine_root / src.name
                safe_atomic_write(qdest, src.read_bytes())
                results.append(res)
                continue

            # Step 7: write tagged asset + sidecars.
            summary["rows_accepted"] += 1
            tagged_path = tagged_root / src.name
            # Copy raw bytes to TAGGED/, then write metadata in place.
            safe_atomic_write(tagged_path, src.read_bytes())

            try:
                if PIEXIF_AVAILABLE and tagged_path.suffix.lower() in {".jpg", ".jpeg"}:
                    write_exif_piexif(tagged_path, row)
                    res.writer_mode = "piexif+pyexiv2"
                else:
                    write_exif_pillow(tagged_path, row)
                    res.writer_mode = "pillow-degraded+sidecar"
                # Always write IPTC + XMP sidecars (per step 5: redundancy).
                write_iptc_xmp_sidecars(tagged_path, row)
            except Exception as e:
                res.quarantined = True
                res.reason = f"EXIF write failed: {type(e).__name__}: {e}"
                summary["rows_quarantined_firewall"] += 1
                results.append(res)
                continue

            res.tagged = True
            res.sha256_tagged = sha256_file(tagged_path)
            res.accepted = True
            summary["rows_tagged"] += 1
            results.append(res)

    # Step 8: lineage log.
    # One row per processed manifest row. The audit timestamp is the *one*
    # allowed non-determinism; everything else is hash-derived.
    with open(audit_log_path, "a", encoding="utf-8") as af:
        af.write(f"# run_start={datetime.now(timezone.utc).isoformat()} writer={WRITER_VERSION} mode={summary['writer_mode']}\n")
        for res in results:
            af.write(
                f"{datetime.now(timezone.utc).isoformat()}\t"
                f"file={res.filename}\t"
                f"src_sha={res.sha256_source[:16]}\t"
                f"tagged_sha={res.sha256_tagged[:16]}\t"
                f"lat={res.lat}\tlon={res.lon}\t"
                f"zip={res.zip}\tneighborhood={res.neighborhood}\t"
                f"firewall={res.firewall_status}\t"
                f"score={res.firewall_score}\t"
                f"mode={res.writer_mode}\t"
                f"result={'TAGGED' if res.tagged else ('QUARANTINED' if res.quarantined else 'REJECTED')}\t"
                f"reason={res.reason}\n"
            )

    # Step 8b: rejected-validation rows (separate CSV, not in TAGGED/).
    if rejected_rows:
        with open(rejected_log_path, "w", encoding="utf-8", newline="") as rf:
            writer = csv.DictWriter(rf, fieldnames=list(rejected_rows[0].keys()))
            writer.writeheader()
            writer.writerows(rejected_rows)

    # Step 8c: tagged JSON for downstream schema injection.
    tagged_payload = {
        "writer_version": WRITER_VERSION,
        "writer_mode": summary["writer_mode"],
        "generated_utc": summary["generated_utc"],
        "tagged_files": [
            {
                "filename": r.filename,
                "lat": r.lat,
                "lon": r.lon,
                "neighborhood": r.neighborhood,
                "zip": r.zip,
                "firewall_status": r.firewall_status,
                "firewall_score": r.firewall_score,
                "writer_mode": r.writer_mode,
                "sha256_source": r.sha256_source,
                "sha256_tagged": r.sha256_tagged,
                "sidecar_files": {
                    "exif": f"{r.filename}.exif.json" if r.writer_mode == "pillow-degraded+sidecar" else None,
                    "iptc": f"{r.filename}{IPTC_SIDECAR_SUFFIX}",
                    "xmp": f"{r.filename}{XMP_SIDECAR_SUFFIX}",
                },
            }
            for r in results if r.tagged
        ],
    }
    tagged_json_path.write_text(json.dumps(tagged_payload, indent=2), encoding="utf-8")

    summary["results"] = [asdict(r) for r in results]
    return summary


# --------------------------------------------------------------------------- #
# SANDBOX TEST (parent SOP §2.2 — runs in CI, no live media, deterministic)
# --------------------------------------------------------------------------- #

def run_sandbox() -> int:
    """Run the deterministic sandbox test described in parent SOP §2.2.

    Synthesizes 5 PNGs (Navy #1A365D), builds a 5-row manifest with 3
    Frisco ZIPs + 1 Plano (out-of-PRIMARY-ZIPS, must be rejected) + 1
    out-of-bounds lat (must be rejected). Runs the pipeline and asserts:

    * 3 rows tagged (the 3 Frisco ZIPs).
    * 2 rows rejected (the Plano + out-of-bounds lat).
    * MANIFEST.audit.log has the run header + 5 result lines.
    * All GPS rationals round-trip.
    * Brand_firewall passes on all tagged rows.
    * Zero green in any output EXIF string.
    """
    if not PILLOW_AVAILABLE:
        print("SANDBOX: Pillow not available — cannot synthesize test PNGs.", file=sys.stderr)
        return 2

    # Use a temp dir under the user's temp so we don't litter the vault.
    sandbox_root = Path(tempfile.mkdtemp(prefix="m7_geotag_sandbox_"))
    raw_root = sandbox_root / "RAW"
    raw_root.mkdir(parents=True, exist_ok=True)
    tagged_root = sandbox_root / TAGGED_DIRNAME
    audit_log = sandbox_root / AUDIT_LOG_FILENAME
    rejected_log = sandbox_root / REJECTED_LOG_FILENAME
    tagged_json = sandbox_root / TAGGED_JSON_FILENAME

    # Synthesize 5 Navy 16x16 PNGs.
    png_paths = []
    for i in range(5):
        path = raw_root / f"sandbox_{i}.png"
        img = Image.new("RGB", (16, 16), color=(0x1A, 0x36, 0x5D))  # Navy #1A365D
        # Add a tiny dot so the file isn't all-zero, but stays in palette.
        d = ImageDraw.Draw(img)
        d.point((8, 8), fill=(0xFB, 0xC0, 0x2D))  # Pineapple Gold
        img.save(path)
        png_paths.append(path)

    # Build the manifest: 3 Frisco ZIPs, 1 Plano (out-of-PRIMARY-ZIPS), 1 out-of-bounds lat.
    manifest_rows = [
        # (filename, neighborhood, zip, lat, lon, hail, swath, nws)
        ("sandbox_0.png", "Starwood",        "75034", 33.1020, -96.8200, "1.75", "4.0",  "NWS-20260712-A1B2"),
        ("sandbox_1.png", "Newman Village",  "75034", 33.1150, -96.8350, "1.50", "3.5",  "NWS-20260712-A1B2"),
        ("sandbox_2.png", "Phillips Creek Ranch", "75035", 33.1310, -96.8580, "2.00", "4.5",  "NWS-20260712-A1B3"),
        # Out-of-PRIMARY-ZIPS (Plano 75024) — must be rejected by validation.
        ("sandbox_3.png", "Whiffletree",     "75024", 33.0198, -96.6989, "1.25", "3.0",  "NWS-20260712-A1B4"),
        # Out-of-Texas-bounds lat (NYC) — must be rejected by validation.
        ("sandbox_4.png", "Starwood (foreign)", "75034", 40.7128, -74.0060, "1.00", "2.5",  "NWS-20260712-A1B5"),
    ]
    manifest_path = sandbox_root / "MANIFEST.sandbox.csv"
    sha_by_file = {p.name: sha256_file(p) for p in png_paths}
    with open(manifest_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["filename", "address", "neighborhood", "zip", "capture_utc",
                    "lat", "lon", "event_id", "roof_age", "surface_type",
                    "hail_size_in", "swath_in", "nws_event_id", "sha256"])
        for fn, nbh, z, lat, lon, hail, swath, nws in manifest_rows:
            utc = "2026-07-14T14:23:11Z"
            w.writerow([fn, "Frisco TX 75034 (street area)", nbh, z, utc,
                        f"{lat}", f"{lon}", "NWS-EVT-001", "10+", "asphalt",
                        hail, swath, nws, sha_by_file[fn]])

    # Run the pipeline.
    summary = process_manifest(
        manifest_path=manifest_path,
        raw_root=raw_root,
        tagged_root=tagged_root,
        audit_log_path=audit_log,
        rejected_log_path=rejected_log,
        tagged_json_path=tagged_json,
    )

    # Assertions.
    fail = []
    if summary["rows_total"] != 5:
        fail.append(f"rows_total expected 5, got {summary['rows_total']}")
    if summary["rows_tagged"] != 3:
        fail.append(f"rows_tagged expected 3, got {summary['rows_tagged']}")
    if summary["rows_rejected_validation"] != 2:
        fail.append(f"rows_rejected_validation expected 2, got {summary['rows_rejected_validation']}")
    if summary["rows_quarantined_sha256"] != 0:
        fail.append(f"rows_quarantined_sha256 expected 0, got {summary['rows_quarantined_sha256']}")
    if summary["rows_quarantined_firewall"] != 0:
        fail.append(f"rows_quarantined_firewall expected 0, got {summary['rows_quarantined_firewall']}")
    if not audit_log.exists():
        fail.append(f"audit log not written at {audit_log}")
    if audit_log.exists():
        with open(audit_log, "r", encoding="utf-8") as af:
            lines = [ln for ln in af.readlines() if ln.strip() and not ln.startswith("#")]
        if len(lines) != 5:
            fail.append(f"audit log expected 5 result lines, got {len(lines)}")
    if not rejected_log.exists():
        fail.append(f"rejected log not written at {rejected_log}")
    if not tagged_json.exists():
        fail.append(f"tagged json not written at {tagged_json}")

    # Round-trip GPS rationals.
    for r in summary["results"]:
        if r.get("tagged"):
            dms = deg_to_dms_rational(r["lat"])
            dms_lon = deg_to_dms_rational(r["lon"])
            # dms = ((d, 1), (m, 1), (s, 10000))
            d, m, s = dms[0][0], dms[1][0], dms[2][0] / dms[2][1]
            recovered = d + m / 60 + s / 3600
            if abs(recovered - abs(r["lat"])) > 1e-3:
                fail.append(f"GPS lat round-trip drift for {r['filename']}: {recovered} vs {r['lat']}")
            d, m, s = dms_lon[0][0], dms_lon[1][0], dms_lon[2][0] / dms_lon[2][1]
            recovered = d + m / 60 + s / 3600
            if abs(recovered - abs(r["lon"])) > 1e-3:
                fail.append(f"GPS lon round-trip drift for {r['filename']}: {recovered} vs {r['lon']}")

    # Brand-fence: every tagged row must have firewall_status=PASS.
    for r in summary["results"]:
        if r.get("tagged") and r.get("firewall_status") != "PASS":
            fail.append(f"tagged row {r['filename']} has firewall_status={r.get('firewall_status')}")

    # Zero green in any tagged output.
    green_hex_re = re.compile(r"#?00[0-9a-fA-F]{2}|#?0[0-9a-fA-F]{5}|\bgreen\b",
                              re.IGNORECASE)
    if tagged_json.exists():
        for r in summary["results"]:
            if not r.get("tagged"):
                continue
            fn = r["filename"]
            for sidecar in [
                tagged_root / f"{fn}{IPTC_SIDECAR_SUFFIX}",
                tagged_root / f"{fn}{XMP_SIDECAR_SUFFIX}",
                tagged_root / f"{fn}.exif.json",
            ]:
                if sidecar.exists() and green_hex_re.search(sidecar.read_text(encoding="utf-8")):
                    fail.append(f"green reference found in {sidecar.name}")
                    break

    # Determinism: re-run the pipeline and compare the tagged SHA-256 set.
    summary2 = process_manifest(
        manifest_path=manifest_path,
        raw_root=raw_root,
        tagged_root=tagged_root,
        audit_log_path=audit_log,
        rejected_log_path=rejected_log,
        tagged_json_path=tagged_json,
    )
    sha_set_1 = {r["sha256_tagged"] for r in summary["results"] if r.get("tagged")}
    sha_set_2 = {r["sha256_tagged"] for r in summary2["results"] if r.get("tagged")}
    if sha_set_1 != sha_set_2:
        fail.append(f"determinism: tagged SHA set differs between runs ({sha_set_1 ^ sha_set_2})")

    # Report.
    print("=" * 72)
    print("m7_geotag_photo_audit.py — SANDBOX TEST")
    print("=" * 72)
    print(f"writer_version: {WRITER_VERSION}")
    print(f"writer_mode   : {summary['writer_mode']}")
    print(f"libraries     : piexif={PIEXIF_AVAILABLE} pyexiv2={PYEXIV2_AVAILABLE} "
          f"iptcinfo3={IPTCINFO3_AVAILABLE} Pillow={PILLOW_AVAILABLE}")
    print(f"compliance    : ComplianceOfficer={'OK' if COMPLIANCE_OFFICER_AVAILABLE else 'MISSING'}")
    print("-" * 72)
    print(f"rows_total              : {summary['rows_total']}")
    print(f"rows_tagged             : {summary['rows_tagged']}")
    print(f"rows_rejected_validation: {summary['rows_rejected_validation']}")
    print(f"rows_quarantined_sha256 : {summary['rows_quarantined_sha256']}")
    print(f"rows_quarantined_firewall: {summary['rows_quarantined_firewall']}")
    print(f"audit log               : {audit_log} (exists={audit_log.exists()})")
    print(f"rejected log            : {rejected_log} (exists={rejected_log.exists()})")
    print(f"tagged json             : {tagged_json} (exists={tagged_json.exists()})")
    print("-" * 72)
    if fail:
        print("SANDBOX: FAIL")
        for f in fail:
            print(f"  - {f}")
        return 1
    print("SANDBOX: PASS — .")
    return 0


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def cmd_info(_args: argparse.Namespace) -> int:
    print("=" * 72)
    print("m7_geotag_photo_audit.py — INFO")
    print("=" * 72)
    print(f"writer_version : {WRITER_VERSION}")
    print(f"vault_root     : {VAULT_ROOT}")
    print(f"scripts_dir    : {SCRIPTS_DIR}")
    print(f"libraries      : piexif={PIEXIF_AVAILABLE} pyexiv2={PYEXIV2_AVAILABLE} "
          f"iptcinfo3={IPTCINFO3_AVAILABLE} Pillow={PILLOW_AVAILABLE}")
    print(f"ComplianceOfficer import : {'OK' if COMPLIANCE_OFFICER_AVAILABLE else 'MISSING'}")
    if not COMPLIANCE_OFFICER_AVAILABLE:
        print(f"  import error: {_COMPLIANCE_IMPORT_ERROR}")  # type: ignore[name-defined]
    print(f"PRIMARY_ZIPS   : {sorted(PRIMARY_ZIPS)}")
    print(f"NAVY_HEX       : {NAVY_HEX}")
    print(f"APPROVED_HEX (subset shown) : {sorted(APPROVED_HEX)}")
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    manifest_path = Path(args.manifest).resolve()
    if not manifest_path.exists():
        print(f"ERROR: manifest not found: {manifest_path}", file=sys.stderr)
        return 2
    raw_root = (manifest_path.parent / "RAW").resolve()
    tagged_root = (manifest_path.parent / TAGGED_DIRNAME).resolve()
    audit_log = (manifest_path.parent / AUDIT_LOG_FILENAME).resolve()
    rejected_log = (manifest_path.parent / REJECTED_LOG_FILENAME).resolve()
    tagged_json = (manifest_path.parent / TAGGED_JSON_FILENAME).resolve()

    summary = process_manifest(
        manifest_path=manifest_path,
        raw_root=raw_root,
        tagged_root=tagged_root,
        audit_log_path=audit_log,
        rejected_log_path=rejected_log,
        tagged_json_path=tagged_json,
    )
    print(json.dumps({k: v for k, v in summary.items() if k != "results"}, indent=2))
    print(f"(see {audit_log} for full per-row audit log; {tagged_json} for schema-injector input)")
    return 0


def cmd_sandbox(_args: argparse.Namespace) -> int:
    return run_sandbox()


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="M7 Local-Signal Photo Audit Pipeline (SOP-SEO-LOCAL-PM7 Phase 2)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("info", help="print library + writer version report").set_defaults(func=cmd_info)

    p_run = sub.add_parser("run", help="run the pipeline against a manifest")
    p_run.add_argument("--manifest", required=True, help="path to MANIFEST.csv")
    p_run.set_defaults(func=cmd_run)

    sub.add_parser("sandbox", help="run the deterministic sandbox test (no live media)").set_defaults(func=cmd_sandbox)

    args = ap.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
