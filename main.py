from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import matplotlib
import matplotlib.pyplot as plt
import formula
import os

matplotlib.use("TkAgg")

window = Tk()
window.geometry("800x600")


label = Label(window, text="Test Program")
label.place(relx=0.5, rely=0.1, anchor="center")


# For testing and learning
def clicked():
    try:
        x = float(inpx.get())
        y = float(inpy.get())
        output = x * y
        label.configure(text=str(output))
        figure = Figure(figsize=(4, 3), dpi=100)
        plot = figure.add_subplot(1, 1, 1)

        plot.plot(x, y, color="red", marker="o", linestyle="")

        canvas = FigureCanvasTkAgg(figure, window)
        canvas.get_tk_widget().place(relx=0.5, rely=0.7, anchor="center")
        # plt.plot([0, inpx.get()], [0, inpy.get()])
        # plt.show()
    except:
        label.configure(text="Error, enter numbers")


def draw(x, y):
    plt.plot(x, y)
    plt.show()


bt = Button(window, text="Multiply", command=clicked)
# bt.grid(column=2, row=2)
bt.place(relx=0.5, rely=0.25, anchor="center")

inpx = Entry(window)
inpx.place(relx=0.5, rely=0.15, anchor="center")
labelx = Label(window, text="x")
labelx.place(relx=0.35, rely=0.15, anchor="center")

inpy = Entry(window)
inpy.place(relx=0.5, rely=0.20, anchor="center")
labely = Label(window, text="y")
labely.place(relx=0.35, rely=0.20, anchor="center")


# Actual program
def select_file_time():
    global l_file
    filetypes = (("text files", "*.txt"), ("All files", "*.*"))

    filename = fd.askopenfilename(
        title="Open a file", initialdir="~", filetypes=filetypes
    )
    l_file = filename
    # check if filename is not empty, user could decide to not pick file
    if type(filename) == str:
        time_file_label.config(text=os.path.basename(filename))


def select_file_numbers():
    global h_file
    filetypes = (("text files", "*.txt"), ("All files", "*.*"))

    filename = fd.askopenfilename(
        title="Open a file", initialdir="~", filetypes=filetypes
    )
    h_file = filename
    if type(filename) == str:
        numbers_file_label.config(text=os.path.basename(filename))


def show():
    global l_file, h_file
    global l, h, num
    try:
        l = formula.open_time(l_file)
        h = formula.open_numbers(h_file, 0)
        num = formula.open_numbers(h_file, 1)
        formula.calculate(l, h, num)
    except:
        openNewWindow("Error", "200x100", "Error with input files")
        # DEBUG
        print("Error with files")


# function to open a new window
def openNewWindow(title, size, text):

    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(window)

    # sets the title of the
    # Toplevel widget
    newWindow.title(title)

    # sets the geometry of toplevel
    newWindow.geometry(size)

    # A Label widget to show in toplevel
    Label(newWindow, text=text).pack()


# open button
open_button = Button(window, text="Open time.txt", command=lambda: select_file_time())
open_button.place(relx=0.2, rely=0.35, anchor="center")
time_file_label = Label(window, text="Empty")
time_file_label.place(relx=0.2, rely=0.4, anchor="center")

open_button = Button(window, text="Open  numbers.txt", command=lambda: select_file_numbers())
open_button.place(relx=0.5, rely=0.35, anchor="center")
numbers_file_label = Label(window, text="Empty")
numbers_file_label.place(relx=0.5, rely=0.4, anchor="center")

open_button = Button(window, text="show plot", command=show)
open_button.place(relx=0.35, rely=0.45, anchor="center")

window.mainloop()
