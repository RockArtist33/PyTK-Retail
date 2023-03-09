import tkinter as tk
from tkinter import ttk


def button_make(windowvar, text, command, x, y, FontStyle, width, height, bgcolor, fgcolor):  # used to create buttons
    button_temp = tk.Button(
        windowvar,  # Sets the window to display to
        text=text,  # sets text
        font=FontStyle,
        command=command,  # sets command
        bg=bgcolor,
        fg=fgcolor
    )
    button_temp.place(x=x, y=y, width=width, heigh=height)  # sets the x and y co-ordiantes of button
    return button_temp  # returns button variable if needed


def button_make_lambda(windowvar, text, command, x, y, FontStyle, width, height, bgcolor,
                       fgcolor):  # used to create buttons
    button_temp = tk.Button(
        windowvar,  # Sets the window to display to
        text=text,  # sets text
        font=FontStyle,
        command=command,  # sets command
        bg=bgcolor,
        fg=fgcolor
    )
    button_temp.place(x=x, y=y, width=width, heigh=height)  # sets the x and y co-ordiantes of button
    return button_temp  # returns button variable if needed


def Entry_make(windowvar, input_var, x, y, width, height):  # used to create Entry boxes
    Entry_temp = tk.Entry(
        windowvar,  # Sets the window to display to
        textvariable=input_var  # Sets the variable for the text you write
    )
    Entry_temp.place(x=x, y=y, width=width, height=height)  # Sets x and y co-ordinates
    return Entry_temp  # returns Entry Box Variable


def Label_make(windowvar, text, x, y, FontStyle, bgcolor, fgcolor, width, height):  # used to create Labels
    Label_Temp = tk.Label(
        windowvar,  # Sets the window to display to
        text=text,  # Sets text
        font=FontStyle,
        bg=bgcolor,
        fg=fgcolor
    )
    Label_Temp.place(x=x, y=y, width=width, height=height)  # Sets x and y Co-ordinates
    return Label_Temp


class messages_class:
    def __init__(self, window_name, message_list, msg_strng, title):
        self.message_list = message_list
        self.window = window_name
        tree = ttk.Treeview(self.window, height=10, selectmode="browse")
        self.tree = tree
        self.tree.configure()
        self.msg_strng = msg_strng
        self.title = title

    def create_tree(self):
        self.tree["show"] = "headings"
        self.columns = ["TO DO", "Description"]

        self.tree.configure(columns=self.columns)
        for item in range(len(self.columns)):
            self.tree.column(item, anchor="w", width=200)
            self.tree.heading(item, text=self.columns[item], anchor="w")
        self.tree.place(x=150, y=50, width=900, height=400)
        self.tree.column("# 2", anchor="w", width=500)
        scroll1 = ttk.Scrollbar(
            self.window,
            orient="vertical",
            command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=scroll1.set)
        scroll1.place(x=1050,y=50,height= 400)

    def message_create(self):
        self.message_list.append(self.msg_strng.get())
        if (len(self.msg_strng.get()) >= 1):
            self.tree.insert("", tk.END, values=[self.title.get(), self.msg_strng.get()])
