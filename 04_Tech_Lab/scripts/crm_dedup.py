"""
crm_dedup.py — Google Sheets CRM deduplication by phone number.
Blocks duplicate entries; prints a summary of what was found/removed.
"""

import argparse
import re
import sys

import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.readonly",
]

DEFAULT_CREDS_FILE = "04_Tech_Lab/.env.google_service_account.json"
DEFAULT_TAB = "Leads"
PHONE_COLUMN_HEADER = "Phone"


def normalize_phone(raw: str) -> str:
    digits = re.sub(r"\D", "", str(raw))
    if len(digits) == 11 and digits.startswith("1"):
        digits = digits[1:]
    return digits


def get_sheet(sheet_id: str, tab: str, creds_file: str) -> gspread.Worksheet:
    creds = Credentials.from_service_account_file(creds_file, scopes=SCOPES)
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_key(sheet_id)
    return spreadsheet.worksheet(tab)


def find_phone_column(headers: list[str]) -> int:
    try:
        return headers.index(PHONE_COLUMN_HEADER)
    except ValueError:
        print(f"ERROR: Column '{PHONE_COLUMN_HEADER}' not found in headers: {headers}", file=sys.stderr)
        sys.exit(1)


def find_duplicates(rows: list[list], phone_col: int) -> list[int]:
    seen: set[str] = set()
    duplicate_row_indices: list[int] = []  # 1-based sheet row numbers

    for i, row in enumerate(rows):
        raw = row[phone_col] if phone_col < len(row) else ""
        normalized = normalize_phone(raw)

        if not normalized:
            continue

        if normalized in seen:
            duplicate_row_indices.append(i + 2)  # +1 for header, +1 for 1-based index
        else:
            seen.add(normalized)

    return duplicate_row_indices


def delete_rows(sheet: gspread.Worksheet, row_indices: list[int]) -> None:
    # Delete in reverse order so indices stay valid
    for row_num in sorted(row_indices, reverse=True):
        sheet.delete_rows(row_num)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Deduplicate Google Sheets CRM rows by phone number."
    )
    parser.add_argument("--sheet-id", required=True, help="Google Sheets spreadsheet ID")
    parser.add_argument("--tab", default=DEFAULT_TAB, help=f"Sheet tab name (default: {DEFAULT_TAB})")
    parser.add_argument(
        "--creds",
        default=DEFAULT_CREDS_FILE,
        help=f"Path to service account JSON (default: {DEFAULT_CREDS_FILE})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report duplicates without deleting anything",
    )
    args = parser.parse_args()

    print(f"Connecting to sheet: {args.sheet_id} / tab: {args.tab}")
    sheet = get_sheet(args.sheet_id, args.tab, args.creds)

    all_values = sheet.get_all_values()
    if not all_values:
        print("Sheet is empty.")
        return

    headers = all_values[0]
    rows = all_values[1:]
    phone_col = find_phone_column(headers)

    print(f"Scanning {len(rows)} data rows for duplicate phone numbers...")
    duplicate_indices = find_duplicates(rows, phone_col)

    if not duplicate_indices:
        print("No duplicates found. CRM is clean.")
        return

    print(f"{len(duplicate_indices)} duplicate(s) found at sheet rows: {duplicate_indices}")

    if args.dry_run:
        print("DRY RUN — no rows deleted.")
        for row_num in duplicate_indices:
            row_data = all_values[row_num - 1]
            phone_raw = row_data[phone_col] if phone_col < len(row_data) else "N/A"
            print(f"  Row {row_num}: phone={phone_raw}")
    else:
        print(f"Deleting {len(duplicate_indices)} duplicate row(s)...")
        delete_rows(sheet, duplicate_indices)
        print(f"Done. {len(duplicate_indices)} duplicate(s) removed. CRM synchronized.")


if __name__ == "__main__":
    main()
