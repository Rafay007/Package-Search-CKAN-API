import logging
from datetime import datetime

def log_config():
    logger = logging.basicConfig(level=logging.INFO, filename=f"./logs/ckan_api_log_{datetime.now()}.log", filemode="w",
                        format="%(asctime)s - %(levelname)s - %(message)s")
    return logger
