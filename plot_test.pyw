# =============================================Imports======================================
import pandas as pd
import easygui
import tkinter as tk
import tkinter_objects as TE
import matplotlib.pyplot as plt
x = 0
if x ==1:
    easygui.msgbox("hello")
    matplotlib.pyplot.plot([1],[1])

# =============================================Variables====================================
root = tk.Tk()
root.geometry("900x600")
root.title("Load graphs")

columnnamevar = tk.StringVar()
row_number = tk.IntVar()
xlabel = tk.StringVar()
ylabel = tk.StringVar()
start_row = tk.IntVar()
end_row = tk.IntVar()
df = pd.DataFrame({})
filename = ""

# =============================================Functions====================================
"""
The reroute functions exist to allow the passing of parameters without using lambda.
"""


def Button_reroute_line():
    tempplt1 = PlottingData(df, xlabel.get(), ylabel.get(), columnnamevar, row_number, start_row.get(),
                            end_row.get())  # Class Variable
    tempplt1.plot_data_line()


def Button_reroute_bar():
    tempplt1 = PlottingData(df, xlabel.get(), ylabel.get(), columnnamevar, row_number, start_row.get(),
                            end_row.get())  # Class Variable
    tempplt1.plot_data_bar()


def load_files():
    global df, filename, Graph1, Graph2
    filename = easygui.fileopenbox(msg="Find your file", title="Find CSV file", default="*.csv",
                                   filetypes=[".csv"])  # opens a file loading box
    df = pd.read_csv(filename)  # sets csv file indicated by the file path to a DataFrame
    Graph1["state"] = tk.ACTIVE  # sets button as active
    Graph2["state"] = tk.ACTIVE  # sets button as active


class PlottingData:
    def __init__(self, dataFrame, x_label, y_label, column_name, row_number, start_row, end_row):
        self.dataFrame = dataFrame
        self.colname = column_name.get()
        self.row_num = row_number.get()
        self.x_label = x_label
        self.y_label = y_label
        self.start_row_index = start_row
        self.end_row_index = end_row

    def plot_data_line(self):
        """
        The DataFrame is loaded to allow for easy retrieval and displaying of data in a graph format. The x value is
        a set of index values from one point to another set by the start_row_index variable and the end_row_index
        variable.
        The y values is similar, but it gets the column first before calling the values

        """
        plt.plot(self.dataFrame.index.values[self.start_row_index:self.end_row_index],
                 self.dataFrame[self.colname].iloc[self.start_row_index:self.end_row_index])
        plt.xlabel(self.x_label)  # sets the x-axis label
        plt.ylabel(self.y_label)  # sets the y-axis label
        plt.title(filename)  # sets the title for the graph to the file path
        plt.show()  # shows it
        plt.close()  # ensures it closes

    def plot_data_bar(self):
        """
        The column names are set by getting the list of column names in the dataFrame through using dataFrame.columns
        the height is then set by getting an individual row set by the row_num variable and the width of teh bars is
        set by a float
        """
        plt.bar(self.dataFrame.columns, self.dataFrame.iloc[self.row_num], 0.8)
        plt.xlabel(self.x_label)  # sets x-axis label
        plt.ylabel(self.y_label)  # sets y-axis variable
        plt.title(filename)  # sets title to file path
        plt.show()  # shows the graph
        plt.close()  # ensure sit closes


# tkinter objects from tkinter_object.py
TE.Label_make(root, "LINE GRAPH OPTIONS", 10, 70, ("Arial", 20), None, None, None, None)
TE.Label_make(root, "BAR GRAPH OPTIONS", 550, 70, ("Arial", 20), None, None, None, None)
TE.Label_make(root, "X axis title", 10, 120, ("Arial"), None, None, None, None)
TE.Label_make(root, "Y axis title", 10, 160, ("Arial"), None, None, None, None)
TE.Label_make(root, "X axis title", 550, 120, ("Arial"), None, None, None, None)
TE.Label_make(root, "Y axis title", 550, 160, ("Arial"), None, None, None, None)
TE.Label_make(root, "What column are you analysing?", 10, 200, ("Arial"), None, None, None, None)
TE.Label_make(root, "What row are you analysing?", 550, 200, ("Arial"), None, None, None, None)
TE.Label_make(root, "Start row index number:", 10, 250, ("Arial"), None, None, None, None)
TE.Label_make(root, "End row index number:", 10, 280, ("Arial"), None, None, None, None)

TE.Entry_make(root, xlabel, 100, 120, None, None)
TE.Entry_make(root, ylabel, 100, 160, None, None)
TE.Entry_make(root, xlabel, 640, 120, None, None)
TE.Entry_make(root, ylabel, 640, 160, None, None)
TE.Entry_make(root, columnnamevar, 250, 203, None, None)
TE.Entry_make(root, row_number, 760, 203, None, None)
TE.Entry_make(root, start_row, 200, 253, None, None)
TE.Entry_make(root, end_row, 200, 283, None, None)

TE.button_make_lambda(root, "Load File", load_files, 25, 480, ("Arial", 40), 425, 100, "#cccccc", "black")
Graph1 = TE.button_make_lambda(root, "Load Line Graph", Button_reroute_line, 455, 480, ("Arial", 10), 425, 50,
                               "#cccccc", "black")
Graph2 = TE.button_make_lambda(root, "Load Bar Graph", Button_reroute_bar, 455, 530, ("Arial", 10), 425, 50,
                               "#cccccc", "black")

# Sets the buttons as disabled on initial startup
Graph1["state"] = tk.DISABLED
Graph2["state"] = tk.DISABLED

root.mainloop()
