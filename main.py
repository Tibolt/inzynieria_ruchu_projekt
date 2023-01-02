from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd
import matplotlib
import formula
import os

matplotlib.use("TkAgg")

window = Tk()
window.geometry("800x600")
window.minsize(800, 600)
window.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)


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
    global l_file, h_file, result_label
    global l, h, num
    try:
        l = formula.open_time(l_file)
        h = formula.open_numbers(h_file, 0)
        num = formula.open_numbers(h_file, 1)
        result = formula.calculate(l, h, num)
        result_txt = "Wynik: " +str(result)
        result_label.config(text=result_txt)
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


def show_version2():
    global h_file, text_time
    global h, con_time
    try:
        h = text_time.get(1.0, END).split()[0]
        con_time = formula.open_numbers(h_file,0)
        formula.calculate_v2(con_time, int(h))
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
    txt = """
        Texting end
        New line
    """
    t.insert(END, txt)


def ChangePage(x):
    for page in window.winfo_children():
        page.destroy()
    if x == 1:
        Page1()
    elif x == 2:
        Page2()
    elif x == 3:
        Page3()
    elif x == 4:
        Page4()


def Page1():
    page = Frame(window)
    page.grid()

    label = Label(window, text=" Main Menu")
    label.grid(row=1,column=3)
    # label.grid_columnconfigure(1, weight=1)
    Button(window, text="Średnia natężenia ruchu", command=lambda: ChangePage(2)).grid(row=3, column=3)
    Button(window, text="Średnia natęzenia ruchu 2", command=lambda: ChangePage(3)).grid(row=4, column=3)
    Button(window, text="Wartość chwilowa intensywności wywołań", command=lambda: ChangePage(4)).grid(row=5, column=3)

    txt = """
        Aplikacja do wyświetlenia i obliczenia
        średniego czasu ruchu telekom.
        
    """
    descr = Label(window, text=txt)
    descr.grid(row=2, column=5,)

    instruction_txt = """
        Rozszerzona instrukcja ...
        ...
        ...
        ...
        Opis aplikacji ...
    """
    Button(window, text="Więcej...", command=lambda: OpenNewWindow("Formula", "300x300", instruction_txt)).grid(row=3, column=5)
 

def Page2():
    global time_file_label, numbers_file_label, result_label
    page = Frame(window)
    page.grid()

    label = Label(window, text="Średnie natęzenie ruchu")
    label.grid(row=1, column=3)

    spacer1 = Label(window, text="")
    spacer1.grid(row=2, column=0)

    Button(window, text="Open time.txt", command=lambda: select_file_time()).grid(row=3, column=1)
    time_file_label = Label(window, text="Empty")
    time_file_label.grid(row=4, column=1)

    Button(window, text="Open  numbers.txt", command=select_file_numbers).grid(row=3, column=3)
    numbers_file_label = Label(window, text="Empty")
    numbers_file_label.grid(row=4, column=3)

    Button(window, text="show plot", command=show).grid(row=5, column=2)

    result_label = Label(window, text="Wynik: ")
    result_label.grid(row=6, column=2)

    txt = """
        Średnie natezenie ruchu telekom
        Wzor: A = lambda * h
        gdzie: 
            lambda - średnia liczba zgloszen na jednostke czasu
            h - średni czas trwania polaczenia

        Za pomoca przycisków wybrac pliki
    """
    descr = Label(window, text=txt)
    descr.grid(row=5, column=4)

    Button(window, text="Więcej ...", command=lambda: OpenNewWindow("Formula", "300x300", "Test text ..."))\
        .grid(row=6, column=4)

    spacer2 = Label(window, text="")
    spacer2.grid(row=7, column=0, pady=100)

    Label(window, text="Back to page 1").grid(row=8, column=0)
    Button(window, text="To page 1", command=lambda: ChangePage(1)).grid(row=9, column=0)


def Page3():
    global average_time_file_label, numbers_file_label
    page = Frame(window)
    page.grid()

    label = Label(window, text="Średnie natęzenie ruchu 2")
    label.grid(row=1,column=3)

    spacer1 = Label(window, text="")
    spacer1.grid(row=2, column=0)

    Button(window, text="Open avg_time.txt", command=lambda: select_file_average_time()).grid(row=3, column=1)
    average_time_file_label = Label(window, text="Empty")
    average_time_file_label.grid(row=4, column=1)

    Button(window, text="Open  numbers.txt", command=lambda: select_file_numbers()).grid(row=3, column=3)
    numbers_file_label = Label(window, text="Empty")
    numbers_file_label.grid(row=4, column=3)

    Button(window, text="show plot", command=show_average).grid(row=5, column=2)

    txt = """
        Srednie natezenie ruchu telekom
        Wzor: A = lambda * h
        gdzie: 
            lambda - średnia liczba zgloszen na jednostke czasu 
            h - czas trwania połączenia w danej minucie

        Za pomoca przyciskow wybrac pliki
    """
    descr = Label(window, text=txt)
    descr.grid(row=5, column=4,)

    Button(window, text="new window ", command=lambda: OpenNewWindow("Formula", "300x300", "Test text ...")).grid(row=6, column=4)

    spacer2 = Label(window, text="")
    spacer2.grid(row=7, column=0, pady=100)

    Label(window, text="Back to page 1").grid(row=8, column=0)
    Button(window, text="To page 1", command=lambda: ChangePage(1)).grid(row=9, column=0)

def Page4():
    global numbers_file_label, text_time
    page = Frame(window)
    page.grid()

    label = Label(window, text="Wzór 2")
    label.grid(row=1, column=3)

    spacer1 = Label(window, text="")
    spacer1.grid(row=2, column=0)

    # Button(window, text="Open avg_time.txt", command=lambda: select_file_average_time()).grid(row=4, column=1)
    text_time = Text(window, height=1, width=3 )
    text_time.grid(row=3, column=1)
    text_time.insert(END, "1")
    
    desc = """
    Czas obserwacji
    w minuatch 
    (liczba calkowita)
    """

    Label(window, text=desc, width=10).grid(row=4, column=1, ipadx=30)

    Button(window, text="Open connection_time.txt", command=lambda: select_file_numbers()).grid(row=3, column=3)
    numbers_file_label = Label(window, text="Empty")
    numbers_file_label.grid(row=4, column=3)

    Button(window, text="show plot", command=show_version2).grid(row=5, column=2)

    txt = """
        Wartosc chwilowa intensywnosci wywolan
        Wzor: suma wszystkich czasow/dlugosc obserwacji

        Za pomoca przyciskow wybrac pliki
        I wpisac liczbe calkowita czasu obserwacji
    """
    descr = Label(window, text=txt)
    descr.grid(row=5, column=4)

    Button(window, text="new window ", command=lambda: OpenNewWindow("Formula", "300x300", "Test text ..."))\
        .grid(row=6, column=4)

    spacer2 = Label(window, text="")
    spacer2.grid(row=7, column=0, pady=80)

    Label(window, text="Back to page 1").grid(row=8, column=0)
    Button(window, text="To page 1", command=lambda: ChangePage(1)).grid(row=9, column=0)


Page1()

window.mainloop()
