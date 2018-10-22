import logging
import tkinter
from tkinter.scrolledtext import ScrolledText


def create_logging(level=logging.INFO):
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
    logging.basicConfig(level=level,
                        format=LOG_FORMAT, datefmt=DATE_FORMAT,)
    return logging


class TextAreaLoggerHandler(logging.Handler):
    def __init__(self, textArea: ScrolledText = None) -> None:
        super().__init__()
        self.__textArea = textArea

    def emit(self, record):
        print("***************")
        print(record.getMessage())
        super().emit(record)
        self.__textArea.insert(tkinter.INSERT, record.getMessage() + '\n')
