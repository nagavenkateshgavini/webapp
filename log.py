import json
import logging
from logging.handlers import RotatingFileHandler
from config import app_config
import constants


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_message = {
            "time": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage()
        }
        if hasattr(record, 'exc_info') and record.exc_info:
            log_message["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_message)


def set_up_logger():
    logger = logging.getLogger(constants.PROJECT_ROOT)

    logger.setLevel(logging.DEBUG)

    # Initialize the JSON formatter
    formatter = JsonFormatter()

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(app_config.LOG_FILE, maxBytes=1024, backupCount=3)
    file_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    return logger


logger = set_up_logger()
