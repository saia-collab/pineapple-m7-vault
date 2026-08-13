import pandas as pd
from datetime import datetime
import os

# Configuration
LOG_FILE = r"C:\Pineapple Contractors M7\04_Tech_Lab\system_logs.csv"
REPORT_DIR = r"C:\Pineapple Contractors M7\01_Command_Center\Compliance_Reports"

def generate_weekly_report():
    if not os.path.exists(REPORT_DIR):
        os.makedirs(REPORT_DIR)
        
    try:
        df = pd.read_csv(LOG_FILE)
        # Filter for the last 7 days of activity
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        weekly_data = df[df['timestamp'] > (datetime.now() - pd.Timedelta(days=7))]
        
        report_date = datetime.now().strftime("%Y-%m-%d")
        report_path = os.path.join(REPORT_DIR, f"Compliance_Report_{report_date}.md")
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f"# 🍍 M7 Weekly Compliance Health Report\n")
            f.write(f"**Generated:** {report_date} 08:30 AM\n\n")
            
            f.write(f"## 📊 Executive Summary\n")
            f.write(f"* **Total Files Audited:** {len(weekly_data)}\n")
            f.write(f"* **Compliance Score:** {100 - (len(weekly_data[weekly_data['status'] == 'Archived']) / len(weekly_data) * 100):.1f}%\n")
            f.write(f"* **Primary Violation:** {weekly_data['violation_type'].mode().iloc[0] if not weekly_data.empty else 'None'}\n\n")
            
            f.write(f"## 🛡️ Archival Detail\n")
            f.write(weekly_data.to_markdown(index=False))
            f.write(f"\n\n*.*")
            
        print(f"✅ Weekly report secured in 01_Command_Center.")
    except Exception as e:
        print(f"⚠️ Report Generation Failed: {e}")

if __name__ == "__main__":
    generate_weekly_report()
