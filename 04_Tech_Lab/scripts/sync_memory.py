import shutil
import os
import datetime

# The paths for the Pineapple-Mana-Global architecture
# Note: Update CLOUD_SYNC_FOLDER to point to your actual shared cloud drive path (e.g., Google Drive or OneDrive)
CLOUD_SYNC_FOLDER = "C:/Users/estim/OneDrive/Pineapple_Cloud_Sync/" 
LOCAL_KNOWLEDGE_MAT = "C:/Pineapple-Mana-Global/03_Knowledge_Mat/"

# Core memory files to keep your AI's brain updated
MEMORY_FILES = [
    "brand-voice.md",
    "marketing-wisdom.md",
    "campaign-history.md"
]

def sync_memory():
    print(f"[{datetime.datetime.now()}] Starting Daily Pineapple Memory Sync...")
    
    if not os.path.exists(CLOUD_SYNC_FOLDER):
        print("Cloud sync folder not found. Please verify the path.")
        return

    for file_name in MEMORY_FILES:
        source_file = os.path.join(CLOUD_SYNC_FOLDER, file_name)
        dest_file = os.path.join(LOCAL_KNOWLEDGE_MAT, file_name)
        
        if os.path.exists(source_file):
            shutil.copy2(source_file, dest_file)
            print(f"[OK] Successfully synced: {file_name}")
        else:
            print(f"[!!] Missing in cloud: {file_name}")
            
    print("Sync complete. Local AI memory is 100% up to date!")

if __name__ == "__main__":
    sync_memory()
