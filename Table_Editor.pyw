# ==============================================Import Statements=======================================
import easygui
import os
import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
x = 0
if x ==1:
    easygui.msgbox("hello")
# ==============================================Setting root Window=====================================
window = tk.Tk()  # creates the root window
window.resizable(False, False)  # makes it unable to be resized
window.title("table: ")  # Sets the title in preparation for loading


# ==============================================Functions===============================================
class FileError(Exception):
    """Raised if incorrect file type"""
    pass


def button_make(windowvar, text, command, x, y):  # used to create buttons
    button_temp = tk.Button(
        windowvar,  # Sets the window to display to
        text=text,  # sets text
        command=command  # sets command
    )
    button_temp.place(x=x, y=y)  # sets the x and y co-ordiantes of button
    return button_temp  # returns button variable if needed


def Entry_make(windowvar, input_var, x, y):  # used to create Entry boxes
    Entry_temp = tk.Entry(
        windowvar,  # Sets the window to display to
        textvariable=input_var  # Sets the variable for the text you write
    )
    Entry_temp.place(x=x, y=y)  # Sets x and y co-ordinates
    return Entry_temp  # returns Entry Box Variable


def Label_make(windowvar, text, x, y):  # used to create Labels
    Label_Temp = tk.Label(
        windowvar,  # Sets the window to display to
        text=text  # Sets text
    )
    Label_Temp.place(x=x, y=y)  # Sets x and y Co-ordinates
    return Label_Temp


def show_table():
    global tree, scroll1, scrollbar
    columns = list(testdf2.columns)  # puts the column names into a list
    tree = ttk.Treeview(window, height=10, selectmode="browse")  # makes treeview
    tree.configure(columns=columns)  # sets columns
    tree.column("# 0", anchor="w", width=40)  # sets index column width
    for index in columns:
        tree.column(index, anchor="w", width=100)  # sets the columns
        tree.heading(index, text=index, anchor="w")  # sets name of columns

    for ind, rows in testdf2.iterrows():
        tree.insert("", 0, text=ind, values=list(rows))  # puts all values into the Trreeview table

    scroll1 = ttk.Scrollbar(  # Creates Scrollbar
        window,
        orient="vertical",  # makes it vertical
        command=tree.yview  # makes it change the y position of the table
    )
    tree.configure(yscrollcommand=scroll1.set)  # sets the scroll for the tre eitself

    tree.place(x=100, y=0)  # places tree
    scroll1.place(x=100 + 42 + (100 * len(testdf.columns)), y=0, height=window.winfo_height() + 26)  # places scroll
    window.geometry(str(200 + (100 * len(testdf.columns))) + "x" + str(250))  # makes the window geometry


def new_window():
    def top2():
        def update():
            global testdf2
            testdf.iloc[index_n.get(), col_name.get()] = textvars.get()
            testdf2 = testdf.iloc[::-1]
            tree.destroy()
            scroll1.destroy()
            show_table()
            popup2.destroy()

        textvars = tk.StringVar()  # Tkinter String variable class
        top.destroy()  # removes the previous windpw

        popup2 = tk.Toplevel(window)  # makes new window
        popup2.resizable(False, False)
        popup2.geometry = ("350x100")
        current_val = f"Current cell value = {testdf.iloc[index_n.get(), col_name.get()]}"  # sets string variable

        Label_make(popup2, current_val, 10, 10)  # sets cureent_val string to text in label
        Entry_make(popup2, textvars, 10, 40)
        button_make(popup2, "Update", update, 10, 70)

    top = tk.Toplevel(window)  # new Window
    top.resizable(False, False)
    top.geometry("335x100" + "+" + str(window.winfo_x()) + "+" + str(window.winfo_y() + window.winfo_height() + 50))
    top.title("Change Data")  # Changes title
    index_n = tk.IntVar()  # Tkinter integer variable class
    col_name = tk.IntVar()

    Label_make(top, "Enter the index number of the row:", 10, 10)
    Entry_make(top, index_n, 200, 10)
    Label_make(top, "Enter the column number:", 10, 40)
    Entry_make(top, col_name, 160, 40)
    button_make(top, "Press to view Cell", top2, 10, 70)


def Table_manipulate():
    top = tk.Toplevel()
    top.title("Change the Table")
    top.geometry("200x200" + "+" + str(window.winfo_x()) + "+" + str(window.winfo_y() + window.winfo_height() + 50))
    # sets geometry to put window below root window
    top.resizable(False, False)

    button_make(top, "Add column", col_add, 10, 10)
    button_make(top, "Remove column", col_rmv, 90, 10)
    button_make(top, "Add row", row_add, 10, 50)
    button_make(top, "Remove row", row_rmv, 69, 50)
    button_make(top, "Change column", col_change, 10, 90)


def row_add():
    global testdf2
    testdf.loc[len(testdf.index)] = " "  # Adds blank row
    testdf2 = testdf.iloc[::-1]  # resets the reversed table
    tree.destroy()
    scroll1.destroy()
    show_table()


def row_rmv():
    def rem():
        global testdf, testdf2, tree
        testdf.drop(index=var.get(), inplace=True)  # drops the row form the Pandas data frame
        testdf.reset_index(drop=True, inplace=True)  # resets index values
        testdf2 = testdf.iloc[::-1]  # reverses list for testdf and assigns to testdf2
        tree.destroy()
        scroll1.destroy()
        show_table()

    var = tk.IntVar()
    top = tk.Toplevel()
    top.title("Row removal")
    top.geometry(
        "250x100" + "+" + str(window.winfo_x() + 200) + "+" + str(window.winfo_y() + window.winfo_height() + 50))
    top.resizable(False, False)
    Label_make(top, "Enter Row Num:", 10, 10)
    Entry_make(top, var, 100, 10)
    button_make(top, "Delete", rem, 10, 40)


def col_rmv():
    def rem():
        global testdf, testdf2, tree
        testdf.drop(testdf.columns[var.get()], inplace=True, axis=1)  # removes column
        testdf.reset_index(drop=True, inplace=True)  # resets index just in case
        testdf2 = testdf.iloc[::-1]  # reverse list and assigns to testdf2
        tree.destroy()
        scroll1.destroy()
        show_table()

    var = tk.IntVar()
    top = tk.Toplevel()
    top.title("Column removal")
    top.geometry(
        "250x100" + "+" + str(window.winfo_x() + 200) + "+" + str(window.winfo_y() + window.winfo_height() + 50))
    top.resizable(False, False)
    Label_make(top, "Enter Column Num:", 10, 10)
    Entry_make(top, var, 130, 10)
    button_make(top, "Delete", rem, 10, 40)


def col_add():
    def add_complete():
        global testdf2
        testdf[entryvar.get()] = " "
        testdf2 = testdf.iloc[::-1]
        tree.destroy()
        scroll1.destroy()
        show_table()

    new_window = tk.Toplevel()
    new_window.title("Add Column")
    new_window.geometry(
        "220x100" + "+" + str(window.winfo_x() + 200) + "+" + str(window.winfo_y() + window.winfo_height() + 50))
    new_window.resizable(False, False)
    entryvar = tk.StringVar()

    Label_make(new_window, "Add column", 10, 10)
    Entry_make(new_window, entryvar, 90, 10)
    button_make(new_window, "Update", add_complete, 10, 40)


def col_change():
    def add_complete():
        def change_column():
            global testdf, testdf2

            x = entryvar2.get()
            testdf.rename(columns={testdf.columns[x]: entryvar.get()}, inplace=True)  # renames the selected column
            testdf2 = testdf.iloc[::-1]  # copies testdf,reverses it and puts it into testdf2
            tree.destroy()
            scroll1.destroy()
            show_table()

        new_window.destroy()  # removes previous window
        new_window1 = tk.Toplevel()  # cretaes new window
        new_window1.title("Add Column")  # sets window title
        new_window1.geometry(
            "300x100" + "+" + str(window.winfo_x() + 200) + "+" + str(window.winfo_y() + window.winfo_height() + 50))
        new_window1.resizable(False, False)
        Label_make(new_window1, "Change column name", 10, 10)
        Entry_make(new_window1, entryvar, 140, 10)
        button_make(new_window1, "Update", change_column, 10, 40)

    new_window = tk.Toplevel()
    new_window.title("Add Column")
    new_window.geometry(
        "300x100" + "+" + str(window.winfo_x() + 200) + "+" + str(window.winfo_y() + window.winfo_height() + 50))
    new_window.resizable(False, False)
    entryvar = tk.StringVar()
    entryvar2 = tk.IntVar()
    Label_make(new_window, "Enter column num:", 10, 10)
    Entry_make(new_window, entryvar2, 120, 10)
    button_make(new_window, "Enter", add_complete, 10, 40)


def save():
    try:
        file = easygui.filesavebox(msg="Save to the intended file", title="Save File",
                                   filetypes=['*.csv', "All files", "*"],
                                   default="*.csv")  # opens a file saving box
        file_ext = os.path.splitext(file)  # splits file into path and ext
        """
        Checks if the name of teh file has the ".csv" file extension or not
        If it does, it doesnt change the name,
        If it does It adds the extension
        """
        if file_ext[1] == ".csv":  # checks extension
            testdf.to_csv(file, index=False)  # if correct, changes nothing
        else:
            testdf.to_csv(file + ".csv", index=False)  # if incorrect, adds .csv to end of file name
    except TypeError:
        raise TypeError("The file has not been saved, perhaps you cancelled?")


def load1():
    global testdf, testdf2
    try:
        file = easygui.fileopenbox(msg="Open the intended file", title="Load File", filetypes=['*.csv'],
                                   default="*.csv")  # loads a file open box
        file_check = os.path.splitext(file)
        if file_check[1] == ".csv":  # checks the file extension

            window.title("table: " + file)  # sets the title to the file name
            testdf = pd.read_csv(file)  # sets the csv file to a pandas dataframe
            testdf2 = testdf.iloc[::-1]
        else:
            raise FileError("this file is not of a compatible File type e.g. '.csv'")
    except TypeError:
        raise TypeError("The the program stopped, perhaps you cancelled loading?")


def load():
    global tree, testdf, testdf2
    try:
        file = easygui.fileopenbox(msg="Open the intended file", title="Load File", filetypes=['*.csv'],
                                   default="*.csv")
        file_check = os.path.splitext(file)
        if file_check[1] == ".csv":  # checks file extension
            window.title("table: " + file)
            testdf = pd.read_csv(file)
            testdf2 = testdf.iloc[::-1]
            tree.destroy()
            scroll1.destroy()
            show_table()
        else:
            raise FileError("this file is not of a compatible File type e.g. '.csv'")
    except TypeError:
        raise TypeError("The file has not been loaded, perhaps you cancelled?")


load1()
button_make(window, "Edit Table", Table_manipulate, 20, 10)
button_make(window, "Edit Data", new_window, 20, 50)
button_make(window, "Load file", load, 20, 90)
button_make(window, "Save to file", save, 20, 130)
show_table()
window.mainloop()
