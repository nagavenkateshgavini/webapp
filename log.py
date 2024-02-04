import logging
from logging.handlers import RotatingFileHandler

from config import app_config
import constants


def set_up_logger():
    logger = logging.getLogger(constants.PROJECT_ROOT)

    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(app_config.LOG_FILE, maxBytes=1024, backupCount=3)
    file_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger


logger = set_up_logger()
