from datetime import datetime
import os

def generate_report():
    os.makedirs("reports", exist_ok=True)

    with open("reports/final_report.txt", "w") as f:
        f.write("RPA Execution Report\n")
        f.write(f"Generated at: {datetime.now()}\n")