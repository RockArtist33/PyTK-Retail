import os
import easygui
import matplotlib
import multiprocessing
import tkinter as tk
import sys
import tkinter.ttk as ttk
import pandas as pd
import tkinter_objects as TE
import subprocess

easygui.msgbox("Hello, world!")

root = tk.Tk()
root.geometry("1200x900")
root.title("Main Menu")
Messagevar = tk.StringVar()

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Boarddf = pd.DataFrame({
    "TO DO": [],
    "Description": []
})

message_list = []


def TEload():
    """
    unfortunately certain restrictions on the college systems disallow the use of subprocesses
    """
    subprocess.Popen(["python",resource_path("./Table_Editor.pyw")],shell=False) # Activates a subprocess that runs this script
    #os.system("python "+resource_path("./Table_Editor.pyw"))

def Gload():
    """
        unfortunately certain restrictions on the college systems disallow the use of subprocesses
    """
    subprocess.Popen(["python", resource_path("./plot_test.pyw")], shell=False)
    #os.system("python "+resource_path("./plot_test.pyw"))


def Main_UI():
    print("test")
    MsgVar = tk.StringVar()
    msg_box = TE.messages_class(root, message_list, Messagevar, MsgVar)
    msg_box.create_tree()
    TE.button_make(root, "Table Editor", TEload, 100, 700, ("Arial", "40"), 500, 100, "#cccccc", "black")
    TE.button_make(root, "Graph Viewer", Gload, 600, 700, ("Arial", "40"), 500, 100, "#cccccc", "black")
    TE.button_make(root, "Press to type", msg_box.message_create, 250, 500, ("Arial", 16), 175, 90, "#cccccc", None)
    TE.Entry_make(root, MsgVar, 550, 500, 400, 40)
    TE.Entry_make(root, Messagevar, 550, 550, 400, 40)
    TE.Label_make(root, "TODO:", 480, 500, ("Arial"), None, None, None, None)
    TE.Label_make(root, "Description:", 450, 550, ("Arial"), None, None, None, None)


x = 0

Main_UI()
root.mainloop()



































































































































































































































































































































































































































































































































































print(
    "Muhammed is the best teacher that I have ever had. Ronaldo is better than Messi. Man Utd are winning the prem "
    "this year.")