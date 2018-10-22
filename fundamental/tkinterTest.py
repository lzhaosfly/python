import tkinter
from typing import List, Tuple

# main window
win = tkinter.Tk()

# set up title
win.title('tkinter title')

# set up window size newGeometry=widthxheight+x+y
win.geometry(newGeometry="400x400+1500+30")

# # label. fg: text color
# label = tkinter.Label(win, text="label content", width=20, heigh=10,
#                       bg="pink", fg="red", font=("Inconsolata", 20), wraplength=50, justify="left", anchor="se")
# label.pack()

# # entry
# tkVar = tkinter.Variable()
# entry = tkinter.Entry(win, show="*", text=tkVar)
# entry.pack()
# tkVar.set('12345')

# # button
# btn = tkinter.Button(win, text="按钮1", command=lambda: print(entry.get()))
# btn.pack()

# # text (textArea)
# from tkinter.scrolledtext import ScrolledText

# text = ScrolledText(win, width=30, height=4)
# text.pack()
# str1 = """THE PRESIDENT: Hello, everybody! Thank you. Thank you. Thank you, everybody. All right, everybody go ahead and have a seat. How is everybody doing today? (Applause.) How about Tim Spicer? (Applause.) I am here with students at Wakefield High School in Arlington, Virginia. And we've got students tuning in from all across America, from kindergarten through 12th grade. And I am just so glad that all could join us today. And I want to thank Wakefield for being such an outstanding host. Give yourselves a big round of applause. (Applause.) """

# text.insert(tkinter.INSERT, str1)

# # # spin box (number input)
# # sp = tkinter.Spinbox(win, from_=5, to=60, increment=5)
# # sp.pack()

# btn = tkinter.Button(win, text="spValue", command=lambda: print(sp.get()))
# btn.pack()


# List box
listBoxVar = tkinter.Variable()
listBox = tkinter.Listbox(
    win, selectmode=tkinter.EXTENDED, listvariable=listBoxVar)
listBox.pack()

listBox.bind(
    '<Double-Button-1>', lambda event: print(listBox.get(listBox.curselection())))  # bind left moust button double click. 1 menas mouse left key

listBox.bind('<<ListboxSelect>>', lambda event: print(
    listBox.get(first=listBox.curselection()[0], last=listBox.curselection()[-1])))  # bind when select event

for item in ['awdw', 'eee', 'ccc', 'xxx']:
    listBox.insert(tkinter.END, item)  # append to list box

listBox.insert(tkinter.ACTIVE, 'in the head')  # insert to head
# listBox.delete(2)  # delete index 2 item

listBox.select_set(2, 4)  # will select index 2 item, can't be negative number
# listBox.select_clear(2)  # cancel index 2 to 5 selection state

print(listBox.size())  # get size of list box. In this case, it's 5
print(listBox.get(2))  # get the index 2 item.
# get the index 2 item.
print(listBox.get(listBox.curselection()[0], listBox.curselection()[-1]))

# will get the current selection index tuple. It's index, not item!!
print(listBox.curselection())

# check if 2 was selected. In this case, true
print(listBox.select_includes(2))

print(listBoxVar.get())  # get all variable in list box
# listBoxVar.set(('1', '2', '3', '4'))  # set these varaible to list

# # 创建一个菜单
# menubar = tkinter.Menu(win)
# # 菜单选项
# menu1 = tkinter.Menu(menubar, tearoff=False)

# # 给菜单选项添加内容
# for item in ['Python', 'NodeJS', 'Java', 'PHP', '退出']:
#     if item == '退出':
#         menu1.add_separator()
#         menu1.add_command(label=item, command=win.quit)
#     else:
#         menu1.add_command(
#             label=item, command=lambda item=item: print(f'{item} clicked!!!'))

# menubar.add_cascade(label="语言", menu=menu1)

# menu2 = tkinter.Menu(menubar, tearoff=False)
# menu2.add_command(label="red")
# menu2.add_command(label="blue")

# menubar.add_cascade(label="颜色", menu=menu2)

# win.config(menu=menubar)  # window menu

# # bind to right click meanu, Mac is <Button-2>, but windows and linux is <Button-3>
# win.bind("<Button-2>", lambda event: menubar.post(event.x_root, event.y_root))


# create a new window

# # main window label
# labelVar = tkinter.StringVar()
# label = tkinter.Label(win, textvariable=labelVar)
# label.pack()


# def createChildWindow():
#     childWindow = tkinter.Toplevel()
#     childWindow.title('child window')
#     childWindow.geometry('200x100+1600+150')

#     entry = tkinter.Entry(childWindow)
#     entry.pack()

#     def add():
#         labelVar.set(entry.get())
#         childWindow.destroy()

#     addBtn = tkinter.Button(childWindow, text="add",
#                             command=add)
#     cancelBtn = tkinter.Button(
#         childWindow, text="cancel", command=childWindow.destroy)
#     addBtn.pack()
#     cancelBtn.pack()


# btn = tkinter.Button(win, text='show a child window',
#                      command=createChildWindow)
# btn.pack()


# create message box
# def createMessageBox():
#     result = messagebox.askquestion(
#         'message box tile', 'are you sure?')
#     if result == 'yes':
#         print('yes clicked!!!')
#     else:
#         print('no clicked!!')

# btn = tkinter.Button(win, text='show a child window',
#                      command=createMessageBox)
# btn.pack()


# comboBox
# comboBox = ttk.Combobox(win)
# comboBox.pack()

# comboBox['value'] = ("CA", "NY", "TA")
# comboBox.current(0)  # set selection

# comboBox.bind('<<ComboboxSelected>>', lambda event: print(comboBox.get()))

# checkBoxInputs: List[Tuple[str, tkinter.BooleanVar]] = [
#     ('Money', tkinter.BooleanVar()),
#     ('Power', tkinter.BooleanVar()),
#     ('People', tkinter.BooleanVar()),
# ]

# result: List[str] = []


# def update():
#     result.clear()
#     for item in checkBoxInputs:
#         if item[1].get() and item[0] not in result:
#             result.append(item[0])
#     print(result)


# for value in checkBoxInputs:
#     checkBtn = tkinter.Checkbutton(
#         win, text=value[0], variable=value[1], command=update)
#     checkBtn.pack()

# # grid layout
# tkinter.Label(win, text="Find:").grid(row=0, column=0, sticky='e')
# tkinter.Entry(win, width=60).grid(row=0, column=1,
#                                   padx=2, pady=20, sticky='we', columnspan=9)
# tkinter.Label(win, text="Replace:").grid(row=1, column=0, sticky='e')
# tkinter.Entry(win).grid(row=1, column=1, padx=2, pady=2, sticky='we',
#                         columnspan=9)
# tkinter.Button(win, text="Find").grid(
#     row=0, column=10, sticky='e' + 'w', padx=2, pady=2)
# tkinter.Button(win, text="Find All").grid(
#     row=1, column=10, sticky='e' + 'w', padx=2)
# tkinter.Button(win, text="Replace").grid(row=2, column=10, sticky='e' +
#                                          'w', padx=2)
# tkinter.Button(win, text="Replace All").grid(
#     row=3, column=10, sticky='e' + 'w', padx=2)
# tkinter.Checkbutton(win, text='Match whole word only').grid(
#     row=2, column=1, columnspan=4, sticky='w')
# tkinter.Checkbutton(win, text='Match Case').grid(
#     row=3, column=1, columnspan=4, sticky='w')
# tkinter.Checkbutton(win, text='Wrap around').grid(
#     row=4, column=1, columnspan=4, sticky='w')
# tkinter.Label(win, text="Direction:").grid(row=2, column=6, sticky='w')
# tkinter.Radiobutton(win, text='Up', value=1).grid(
#     row=3, column=6, columnspan=6, sticky='w')
# tkinter.Radiobutton(win, text='Down', value=2).grid(
#     row=3, column=7, columnspan=2, sticky='e')


win.mainloop()
