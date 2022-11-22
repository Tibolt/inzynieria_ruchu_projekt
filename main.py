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
    global l_file, time_file_label
    filetypes = (("text files", "*.txt"), ("All files", "*.*"))

    filename = fd.askopenfilename(
        title="Open a file", initialdir="~", filetypes=filetypes
    )
    l_file = filename
    # check if filename is not empty, user could decide to not pick file
    if type(filename) == str:
        time_file_label.config(text=os.path.basename(filename))


def select_file_numbers():
    global h_file, numbers_file_label
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
        OpenNewWindow("Error", "200x100", "Error with input files")
        # DEBUG
        print("Error with files")


# function to open a new window
def OpenNewWindow(title, size, text):

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


def NewTextArea(title, size_x, size_y, pos_x, pos_y, text):
    newText = Text(window, height=size_y, width=size_x)
    newLabel = Label(newText, text=text)

    newText.place(relx=pos_x, rely=pos_y, anchor="center")
    newLabel.place(relx=pos_x - 0.3, rely=pos_y, anchor="center")


def Page1():
    global time_file_label, numbers_file_label
    page = Frame(window)
    page.grid()
    Label(window, text="Back to page 2").grid(row=0)
    Button(window, text="To page 2", command=ChangePage).grid(row=1)

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

    NewTextArea("Test_Area", 20, 10, 0.8, 0.3, "Test text ...")

    new_window_button = Button(window, text="new window ", command=lambda: OpenNewWindow("Formula", "300x300", "Test text ..."))
    new_window_button.place(relx=0.2, rely=0.7, anchor="center")

def Page2():
    page = Frame(window)
    page.grid()
    Label(window, text="Back to page 1").grid(row=0)
    Button(window, text="To page 1", command=ChangePage).grid(row=2, column=1)


def ChangePage():
    global page_num
    for page in window.winfo_children():
        page.destroy()
    if page_num == 1:
        Page2()
        page_num = 2
    elif page_num == 2:
        Page1()
        page_num = 1

page_num = 1
Page1()

window.mainloop()
