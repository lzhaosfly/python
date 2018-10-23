import tkinter
import logging
import pickle
import os
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from selenium_stock_charm import stockChartsRun, driverInit
from typing import Tuple, Dict
from create_logging import TextAreaLoggerHandler
from threading import Thread


def createAddWindow(listBox: tkinter.Listbox):
    childWindow = tkinter.Toplevel()
    childWindow.title('Add a symbol')
    # childWindow.geometry(newGeometry="+1700+200")

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


def run_selenium(loggerTextArea: ScrolledText, symbols: Tuple[str], page_load_time, logger):
    loggerTextArea.delete(1.0, tkinter.END)
    driver = driverInit(driver_logging=logger)
    for symbol in symbols:
        stockChartsRun(symbol, driver, page_load_time, stock_logging=logger)


def saveListAndQuit(listBoxVar: tkinter.Variable, win: tkinter.Tk):
    if len(listBoxVar.get()) > 0:
        with open(os.path.join(os.path.dirname(__file__), 'watch_list.pickle'), 'wb') as pickleFile:
            pickle.dump(listBoxVar.get(), pickleFile)
    win.destroy()


def main():
    win = tkinter.Tk()
    # win.geometry(newGeometry="+1500+30")
    win.title('open stockchar EMA')

    stockLabel = tkinter.Label(win, text="stock watch list")
    stockLabel.grid(row=0, columnspan=3, sticky="WE", ipady=10)

    listBoxVar = tkinter.Variable()

    if os.path.exists(os.path.join(os.path.dirname(__file__), 'watch_list.pickle')):
        with open(os.path.join(os.path.dirname(__file__), 'watch_list.pickle'), 'rb') as pickleFile:
            initialList = pickle.load(pickleFile)
            listBoxVar.set(initialList)

    listBox = tkinter.Listbox(
        win, selectmode=tkinter.EXTENDED, listvariable=listBoxVar)
    listBox.grid(row=1, columnspan=3, rowspan=4,
                 sticky='WE', padx=20, pady=(0, 20))

    addBtn = tkinter.Button(text="Add a symbol",
                            command=lambda listBox=listBox: createAddWindow(listBox=listBox))
    addBtn.grid(row=5, column=0, padx=(20, 0))
    deleteBtn = tkinter.Button(
        text="Delete Selected", command=lambda listBox=listBox: showDeleteMsgBox(listBox))
    deleteBtn.grid(row=5, column=1, sticky="W")

    timeoutSetLabel = tkinter.Label(text="set page load out time:")
    timeoutSetLabel.grid(row=6, column=0, sticky="W",
                         padx=(20, 0), pady=20)
    spinBoxDefault = tkinter.StringVar()
    spinBox = tkinter.Spinbox(
        win, from_=5, to=60, increment=5, textvariable=spinBoxDefault)
    spinBoxDefault.set('10')
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

    logger = logging.getLogger('stock logger')
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logger.setLevel(loggerComboBoxPairs.get(loggerLevelComboBox.get()))
    ch = TextAreaLoggerHandler(textArea=loggerTextArea)
    ch.setLevel(loggerComboBoxPairs.get(loggerLevelComboBox.get()))
    ch.setFormatter(LOG_FORMAT)
    logger.addHandler(ch)

    loggerLevelComboBox.bind('<<ComboboxSelected>>', lambda event: ch.setLevel(
        loggerComboBoxPairs.get(loggerLevelComboBox.get())))

    startBtn = tkinter.Button(
        text="Start run", command=lambda listBox=listBox: Thread(target=run_selenium, args=(loggerTextArea, listBoxVar.get(), int(spinBox.get()), logger)).start())

    startBtn.grid(row=5, column=2, sticky="W", padx=(0, 20))

    win.protocol('WM_DELETE_WINDOW', lambda listBoxVar=listBoxVar,
                 win=win: saveListAndQuit(listBoxVar=listBoxVar, win=win))

    win.mainloop()


if __name__ == '__main__':
    main()
