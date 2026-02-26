from datetime import datetime

def generate_report():
    with open("reports/final_report.txt", "w") as f:
        f.write(f"RPA Execution Report\n")
        f.write(f"Generated at: {datetime.now()}\n")