import tkinter
import logging
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from selenium_stock_charm import stockChartsRun, driverInit
from typing import Tuple, Dict
from create_logging import TextAreaLoggerHandler


def createAddWindow(listBox: tkinter.Listbox):
    childWindow = tkinter.Toplevel()
    childWindow.title('Add a symbol')
    childWindow.geometry(newGeometry="+1700+200")

    entry = tkinter.Entry(childWindow)
    entry.grid(row=0, columnspan=3, pady=(20, 10), padx=10)

    def add():
        listBox.insert(tkinter.END, entry.get())
        childWindow.destroy()

    addBtn = tkinter.Button(childWindow, text="add",
                            command=add)
    addBtn.grid(row=1, columnspan=2, sticky="EW", padx=(10, 0), pady=(0, 10))
    cancelBtn = tkinter.Button(
        childWindow, text="cancel", command=childWindow.destroy)
    cancelBtn.grid(row=1, column=2, sticky="EW", padx=(5, 10), pady=(0, 10))


def showDeleteMsgBox(listBox: tkinter.Listbox):
    result = messagebox.askquestion(
        "delet confirmation", "are you sure you want to delete selection?")

    if result == 'yes':
        listBox.delete(listBox.curselection()[0], listBox.curselection()[-1])


def run_selenium(symbols: Tuple[str], page_load_time, logger):
    driver = driverInit(logger)
    for symbol in symbols:
        stockChartsRun(symbol, driver, page_load_time, logger)


def main():
    win = tkinter.Tk()
    win.geometry(newGeometry="+1500+30")
    win.title('open stockchar EMA')

    stockLabel = tkinter.Label(win, text="stock watch list")
    stockLabel.grid(row=0, columnspan=3, sticky="WE", ipady=10)

    listBoxVar = tkinter.Variable()
    lisBox = tkinter.Listbox(
        win, selectmode=tkinter.EXTENDED, listvariable=listBoxVar)
    lisBox.grid(row=1, columnspan=3, rowspan=4,
                sticky='WE', padx=20, pady=(0, 20))

    addBtn = tkinter.Button(text="Add a symbol",
                            command=lambda listBox=lisBox: createAddWindow(listBox=listBox))
    addBtn.grid(row=5, column=0, padx=(20, 0))
    deleteBtn = tkinter.Button(
        text="Delete Selected", command=lambda listBox=lisBox: showDeleteMsgBox(lisBox))
    deleteBtn.grid(row=5, column=1, sticky="W")

    timeoutSetLabel = tkinter.Label(text="set page load out time:")
    timeoutSetLabel.grid(row=6, column=0, sticky="W",
                         padx=(20, 0), pady=20)
    spinBox = tkinter.Spinbox(win, from_=5, to=60, increment=5)
    spinBox.grid(row=6, column=1, sticky="W", padx=(0, 20), pady=20)

    logLevelLabel = tkinter.Label(text="set logging level:")
    logLevelLabel.grid(row=7, column=0, pady=(0, 20))

    loggerLevelComboBox = ttk.Combobox(win)
    loggerLevelComboBox.grid(row=7, column=1, sticky="W", pady=(0, 20))

    loggerComboBoxPairs: Dict[str, int] = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "error": logging.ERROR,
        "critical": logging.CRITICAL
    }

    loggerLevelComboBox['value'] = [val for val in loggerComboBoxPairs.keys()]
    loggerLevelComboBox.current(1)

    loggerTextArea = ScrolledText(win, height=4, bg="#EDEDED")
    loggerTextArea.grid(row=8, columnspan=3, padx=20, pady=(0, 20))

    # logger = create_logging(loggerComboBoxPairs.get(loggerLevelComboBox.get()))
    logger = logging.getLogger('stock logger')
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    ch = TextAreaLoggerHandler(textArea=loggerTextArea)
    ch.setLevel(loggerComboBoxPairs.get(loggerLevelComboBox.get()))
    ch.setFormatter(LOG_FORMAT)
    logger.addHandler(ch)

    startBtn = tkinter.Button(
        text="Start run", command=lambda listBox=lisBox: run_selenium(listBoxVar.get(), page_load_time=int(spinBox.get()), logger=logger))
    startBtn.grid(row=5, column=2, sticky="W", padx=(0, 20))

    win.mainloop()


if __name__ == '__main__':
    main()
