import logging
from io import StringIO

logstream = StringIO()


def create_logging(level=logging.INFO, filename=''):
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
    logging.basicConfig(level=level,
                        format=LOG_FORMAT, datefmt=DATE_FORMAT, stream=logstream)
    return logging
