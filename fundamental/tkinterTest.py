import tkinter

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


# # List box
# listBoxVar = tkinter.Variable()
# listBox = tkinter.Listbox(
#     win, selectmode=tkinter.EXTENDED, listvariable=listBoxVar)
# listBox.pack()

# listBox.bind(
#     '<Double-Button-1>', lambda event: print(listBox.get(listBox.curselection())))  # bind left moust button double click. 1 menas mouse left key

# listBox.bind('<<ListboxSelect>>', lambda event: print(
#     listBox.get(first=listBox.curselection()[0], last=listBox.curselection()[-1])))  # bind when select event

# for item in ['awdw', 'eee', 'ccc', 'xxx']:
#     listBox.insert(tkinter.END, item)  # append to list box

# listBox.insert(tkinter.ACTIVE, 'in the head')  # insert to head
# # listBox.delete(2)  # delete index 2 item

# listBox.select_set(2, 4)  # will select index 2 item, can't be negative number
# # listBox.select_clear(2)  # cancel index 2 to 5 selection state

# print(listBox.size())  # get size of list box. In this case, it's 5
# print(listBox.get(2))  # get the index 2 item.

# # will get the current selection index tuple. It's index, not item!!
# print(listBox.curselection())

# # check if 2 was selected. In this case, true
# print(listBox.select_includes(2))

# print(listBoxVar.get())  # get all variable in list box
# # listBoxVar.set(('1', '2', '3', '4'))  # set these varaible to list

# 创建一个菜单
menubar = tkinter.Menu(win)
# 菜单选项
menu1 = tkinter.Menu(menubar, tearoff=False)

# 给菜单选项添加内容
for item in ['Python', 'NodeJS', 'Java', 'PHP', '退出']:
    if item == '退出':
        menu1.add_separator()
        menu1.add_command(label=item, command=win.quit)
    else:
        menu1.add_command(
            label=item, command=lambda item=item: print(f'{item} clicked!!!'))

menubar.add_cascade(label="语言", menu=menu1)

menu2 = tkinter.Menu(menubar, tearoff=False)
menu2.add_command(label="red")
menu2.add_command(label="blue")

menubar.add_cascade(label="颜色", menu=menu2)

win.config(menu=menubar)  # window menu

# bind to right click meanu, Mac is <Button-2>, but windows and linux is <Button-3>
win.bind("<Button-2>", lambda event: menubar.post(event.x_root, event.y_root))


win.mainloop()
