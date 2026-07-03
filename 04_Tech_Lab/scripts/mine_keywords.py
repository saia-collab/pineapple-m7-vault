import os

# Define paths
ROOT_DIR = r"C:\Pineapple-Mana-Global"
TECH_LAB = os.path.join(ROOT_DIR, "04_Tech_Lab")
INPUT_TERMS = os.path.join(TECH_LAB, "daily_search_terms.txt")
OUTPUT_NEGATIVES = os.path.join(TECH_LAB, "output", "negative_keywords_to_block.txt")

# Strict Corporate Elite Banned Triggers
BANNED_TRIGGERS = ["free", "cheap", "discount", "diy", "how to", "bargain", "affordable", "wholesale"]


def run_overnight_keyword_mining():
    print("🛡️ Activating Overnight Money Shield Keyword Miner...")
    os.makedirs(os.path.dirname(OUTPUT_NEGATIVES), exist_ok=True)

    # Create a mock file if it doesn't exist yet so the user can test
    if not os.path.exists(INPUT_TERMS):
        with open(INPUT_TERMS, "w") as f:
            f.write("certified roof repair frisco\nfree roof inspection\ncheap shingles near me\nrcat roofing contractors\nhow to patch a roof hole\n")
        print(f"📝 Created sample file at {INPUT_TERMS}. Run the script again to see it analyze!")
        return

    bleeders_found = []

    with open(INPUT_TERMS, "r") as f:
        terms = f.readlines()

    for term in terms:
        cleaned_term = term.strip().lower()
        if not cleaned_term:
            continue

        # Check if the search term contains any banned low-integrity words
        for banned in BANNED_TRIGGERS:
            if banned in cleaned_term:
                bleeders_found.append(term.strip())
                break

    # Save the budget bleeders to your blocking sheet
    with open(OUTPUT_NEGATIVES, "w") as f:
        for bleeder in bleeders_found:
            f.write(f"{bleeder}\n")

    print(f"🚨 Audit Complete! Found {len(bleeders_found)} budget-bleeding terms.")
    print(f"📥 Saved to block list: {OUTPUT_NEGATIVES}")


if __name__ == "__main__":
    run_overnight_keyword_mining()
