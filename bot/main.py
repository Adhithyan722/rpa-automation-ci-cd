from tasks.downloader import download_file
from tasks.process_data import process_data
from tasks.report_gen import generate_report
from utils.logger import get_logger

logger = get_logger()

def run():
    logger.info("RPA Started")

    download_file(
        "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    )
    process_data()
    generate_report()

    logger.info("RPA Completed")

if __name__ == "__main__":
    run()