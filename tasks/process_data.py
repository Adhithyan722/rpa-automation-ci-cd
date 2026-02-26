import pandas as pd
from utils.logger import get_logger

logger = get_logger()

def process_data(file="reports/data.csv"):
    df = pd.read_csv(file)
    summary = df.describe()
    summary.to_excel("reports/summary.xlsx")
    logger.info("Data processed successfully")