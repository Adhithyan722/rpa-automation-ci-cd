import requests
import os
from utils.logger import get_logger

logger = get_logger()

def download_file(url, output="reports/data.csv"):
    try:
        os.makedirs(os.path.dirname(output), exist_ok=True)  # 🔥 FIX
        r = requests.get(url)
        with open(output, "wb") as f:
            f.write(r.content)
        logger.info("File downloaded successfully")
    except Exception as e:
        logger.error(f"Download failed: {e}")
        raise