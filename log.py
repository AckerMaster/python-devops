import os
import sys
import logging
import json

# logs file
LOGS_FILE = "log.txt"

# a costum JSON format
class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage()
        }
        return json.dumps(log)

# function that returns a logger that logs to both terminal and a file
def setup_logging():
    
    # environment variables
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "DEBUG")
    LOG_FORMAT = os.environ.get("LOG_FORMAT", "TEXT")

    logger = logging.getLogger("myapp")
    logger.setLevel(LOG_LEVEL)
    stdout_handler = logging.StreamHandler(sys.stdout)
    
    file_handler = logging.FileHandler(LOGS_FILE)

    if (LOG_FORMAT == "JSON"):
        formatter = JsonFormatter()
    else:
        text_format = "%(asctime)s:%(name)s:%(levelname)s:%(module)s:%(lineno)d:%(funcName)s:%(message)s"
        formatter = logging.Formatter(text_format)
        
    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)
    
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    return logger