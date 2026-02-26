import requests
from utils.logger import get_logger

logger = get_logger()

def download_file(url, output="reports/data.csv"):
    try:
        r = requests.get(url)
        with open(output, "wb") as f:
            f.write(r.content)
        logger.info("File downloaded successfully")
    except Exception as e:
        logger.error(f"Download failed: {e}")