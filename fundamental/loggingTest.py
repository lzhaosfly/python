import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(filename='', level=logging.DEBUG,
                    format=LOG_FORMAT, datefmt=DATE_FORMAT)

logging.debug("This is a debug info")
logging.info("This is a info info")
