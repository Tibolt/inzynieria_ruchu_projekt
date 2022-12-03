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
# window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)

# label = Label(window, text="Test Program")
# label.place(relx=0.5, rely=0.1, anchor="center")


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


# bt = Button(window, text="Multiply", command=clicked)
# bt.place(relx=0.5, rely=0.25, anchor="center")

# inpx = Entry(window)
# inpx.place(relx=0.5, rely=0.15, anchor="center")
# labelx = Label(window, text="x")
# labelx.place(relx=0.35, rely=0.15, anchor="center")

# inpy = Entry(window)
# inpy.place(relx=0.5, rely=0.20, anchor="center")
# labely = Label(window, text="y")
# labely.place(relx=0.35, rely=0.20, anchor="center")


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


def select_file_average_time():
    global avg_file, average_time_file_label
    filetypes = (("text files", "*.txt"), ("All files", "*.*"))

    filename = fd.askopenfilename(
        title="Open a file", initialdir="~", filetypes=filetypes
    )
    avg_file = filename
    # check if filename is not empty, user could decide to not pick file
    if type(filename) == str:
        average_time_file_label.config(text=os.path.basename(filename))


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

def show_average():
    global h_file, avg_file
    global h, num, avg
    try:
        avg = formula.open_numbers(avg_file,0)
        h = formula.open_numbers(h_file, 0)
        num = formula.open_numbers(h_file, 1)
        formula.calculate_avg(avg, h, num)
    except Exception as e:
        OpenNewWindow("Error", "200x100", "Error with input files")
        # DEBUG
        print(e)

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
    t = Text(window, height=size_y, width=size_x, state="disabled")
    t.grid(row=pos_y, column=pos_x,)
    txt = """Texting end
        New line
    """
    t.insert(END, txt)



def Page2():
    global time_file_label, numbers_file_label
    page = Frame(window)
    page.grid()

    Button(window, text="Open time.txt", command=lambda: select_file_time()).grid(row=4, column=1)
    time_file_label = Label(window, text="Empty")
    time_file_label.grid(row=5, column=1)

    Button(window, text="Open  numbers.txt", command=select_file_numbers).grid(row=4, column=3)
    numbers_file_label = Label(window, text="Empty")
    numbers_file_label.grid(row=5, column=3)

    Button(window, text="show plot", command=show).grid(row=6, column=2)

    NewTextArea("Test_Area", 20, 10, 4, 6, "Test text ...")

    Button(window, text="new window ", command=lambda: OpenNewWindow("Formula", "300x300", "Test text ...")).grid(row=7, column=2)

    Label(window, text="Back to page 1").grid(row=8, column=0)
    Button(window, text="To page 1", command=lambda: ChangePage(1)).grid(row=9, column=0)


def Page1():
    page = Frame(window)
    page.grid()

    label = Label(window, text=" Main Menu")
    label.grid(row=1,column=3)
    # label.grid_columnconfigure(1, weight=1)
    Button(window, text="To page 2", command=lambda: ChangePage(2)).grid(row=2, column=3)
    Button(window, text="To page 3", command=lambda: ChangePage(3)).grid(row=3, column=3)
    NewTextArea("Test_Area", 20, 10, 5, 2, "Main menu text ")


def ChangePage(x):
    for page in window.winfo_children():
        page.destroy()
    if x == 1:
        Page1()
    elif x == 2:
        Page2()
    elif x ==3:
        Page3()
        

def Page3():
    global average_time_file_label, numbers_file_label
    page = Frame(window)
    page.grid()

    Button(window, text="Open avg_time.txt", command=lambda: select_file_average_time()).grid(row=4, column=1)
    average_time_file_label = Label(window, text="Empty")
    average_time_file_label.grid(row=5, column=1)

    Button(window, text="Open  numbers.txt", command=lambda: select_file_numbers()).grid(row=4, column=3)
    numbers_file_label = Label(window, text="Empty")
    numbers_file_label.grid(row=5, column=3)

    Button(window, text="show plot", command=show_average).grid(row=6, column=2)

    NewTextArea("Test_Area", 20, 10, 4, 6, "Test text ...")

    Button(window, text="new window ", command=lambda: OpenNewWindow("Formula", "300x300", "Test text ...")).grid(row=7, column=2)

    Label(window, text="Back to page 1").grid(row=8, column=0)
    Button(window, text="To page 1", command=lambda: ChangePage(1)).grid(row=9, column=0)


Page1()

window.mainloop()
