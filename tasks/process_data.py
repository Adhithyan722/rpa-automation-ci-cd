import pandas as pd
import os
from utils.logger import get_logger

logger = get_logger()

def process_data(file="reports/data.csv"):
    os.makedirs("reports", exist_ok=True)  # 🔥 safety

    df = pd.read_csv(file)
    summary = df.describe()
    summary.to_excel("reports/summary.xlsx")

    logger.info("Data processed successfully")