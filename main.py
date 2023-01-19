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
window.title("Kalkulator średniej wartości natęzenia ruchu telekomunkacjynego")
window.geometry("950x750")
window.minsize(950, 750)
window.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)

l_file, h_file, avg_file, connection_file = None, None, None, None

# Actual program
def select_file_time():
    global l_file, time_file_label
    filetypes = (("text files", "*.txt"), ("All files", "*.*"))

    filename = fd.askopenfilename(
        title="Open a file", initialdir=os.curdir, filetypes=filetypes
    )
    # check if filename is not empty, user could decide to not pick file
    if filename:
        time_file_label.config(text=os.path.basename(filename))
        l_file = filename


def select_file_numbers():
    global h_file, numbers_file_label
    filetypes = (("text files", "*.txt"), ("All files", "*.*"))

    filename = fd.askopenfilename(
        title="Open a file", initialdir=os.curdir, filetypes=filetypes
    )
    # check if filename is not empty, user could decide to not pick file
    if filename:
        numbers_file_label.config(text=os.path.basename(filename))
        h_file = filename


def select_file_average_time():
    global avg_file, average_time_file_label
    filetypes = (("text files", "*.txt"), ("All files", "*.*"))

    filename = fd.askopenfilename(
        title="Open a file", initialdir=os.curdir, filetypes=filetypes
    )
    # check if filename is not empty, user could decide to not pick file
    if filename:
        average_time_file_label.config(text=os.path.basename(filename))
        avg_file = filename


def select_connection_time():
    global connection_file, connection_file_label
    filetypes = (("text files", "*.txt"), ("All files", "*.*"))

    filename = fd.askopenfilename(
        title="Open a file", initialdir=os.pardir, filetypes=filetypes
    )
    # check if filename is not empty, user could decide to not pick file
    if filename:
        connection_file_label.config(text=os.path.basename(filename))
        connection_file = filename

def show():
    global l_file, h_file, result_label
    global l, h, num
    try:
        l = formula.open_time(l_file)
        h = formula.open_numbers(h_file, 0)
        num = formula.open_numbers(h_file, 1)
        result = round(formula.calculate(l, h, num), 3)
        result_txt = "Wynik: " + str(result) + " [Erlang]"
        result_label.config(text=result_txt)
    except:
        OpenNewWindow("Error", "200x100", "Błędne pliki/dane")
        # DEBUG
        print("Error with files")

def show_average():
    global h_file, avg_file, result_label_p3
    global h, num, avg
    try:
        avg = formula.open_numbers(avg_file,0)
        h = formula.open_numbers(h_file, 0)
        num = formula.open_numbers(h_file, 1)
        result = round(formula.calculate_avg(avg, h, num), 3)
        result_txt = "Wynik: " + str(result) + " [Erlang]"
        result_label_p3.config(text=result_txt)
    except Exception as e:
        OpenNewWindow("Error", "200x100", "Błędne pliki/dane")
        # DEBUG
        print(e)


def show_version2():
    global connection_file, text_time, result_label_p4
    global h, con_time
    try:
        h = text_time.get(1.0, END).split()[0]
        con_time = formula.open_numbers(connection_file,0)
        result = round(formula.calculate_v2(con_time, int(h)), 3)
        result_txt = "Wynik: " + str(result) + " [Erlang]"
        result_label_p4.config(text=result_txt)
    except Exception as e:
        OpenNewWindow("Error", "200x100", "Błędne pliki/dane")
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
    min_size = size.split("x")
    newWindow.minsize(min_size[0], min_size[1])

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

    label = Label(window, text="Menu główne")
    label.grid(row=0, column=4, pady=20)

    spacer2 = Label(window, text="")
    spacer2.grid(row=1, column=0, pady=30)
    # label.grid_columnconfigure(1, weight=1)
    Button(window, text="1. Przycisk", command=lambda: ChangePage(2)).grid(row=2, column=3, ipadx=5, ipady=5)
    Label(window, text="Średnie natężenie 1 wzór").grid(row=3, column=3)

    Button(window, text="2. Przycisk", command=lambda: ChangePage(3)).grid(row=4, column=3, ipadx=5, ipady=5)
    Label(window, text="Średnie natężenie 1 wzór").grid(row=5, column=3)

    Button(window, text="3. Przycisk", command=lambda: ChangePage(4)).grid(row=6, column=3, ipadx=5, ipady=5)
    Label(window, text="Średnie natężenie 2 wzór").grid(row=7, column=3)

    txt = """
        W programie możemy obliczyć średnie natęzenie 
        ruchu telekomunikacyjnego i wyświetlić wykres
        natężenia w danej godzinie. 
        
        W menu można wybrać sposób użyty do wyznaczenia
        średniego natężenia:
        1 przycisk - średnia liczba zgłoszeń i średni
            czas trwania połączenia.
        2 przycisk - średnia liczba zgłoszeń i czas
            trwania połączenia w danej minucie.
            (różni się wykresem)
        3 przycisk - suma czasów trwania połączeń
            i okres obserwacji.
    
        
    """
    descr = Label(window, text=txt, borderwidth=3, relief="groove")
    descr.grid(row=2, column=5, ipadx=10, rowspan=6)

    instruction_txt = """
        Średnia wartość natężenia ruchu telekomunikacyjnego
        to iloczyn średniego czasu trwania połączenia
        i średniej ilości zgłoszeń. Jednostką jest erlang.
        
        Dla danego systemu telekomunikacyjnego 
        składającego się z 1 linii 
        i czasu obserwacji równego 1 godzinie, jeśli linia 
        ta zajęta jest całą godzinę, 
        to natężenie ruchu wynosi 1 erlang.
    """
    Button(window, text="Więcej...", command=lambda: OpenNewWindow("Formula", "450x450", instruction_txt))\
        .grid(row=8, column=5, pady=10)
 

def Page2():
    global time_file_label, numbers_file_label, result_label, l_file, h_file
    page = Frame(window)
    page.grid()

    label = Label(window, text="Średnie natęzenie ruchu")
    label.grid(row=1, column=3, pady=20)

    spacer1 = Label(window, text="")
    spacer1.grid(row=2, column=0)


    Button(window, text="Otwórz 1", command=lambda: select_file_time()).grid(row=3, column=1)
    time_file_label = Label(window, text="Pusty")
    time_file_label.grid(row=4, column=1)

    if l_file:
        time_file_label.config(text=os.path.basename(l_file))

    Button(window, text="Otwórz  2", command=select_file_numbers).grid(row=3, column=3)
    numbers_file_label = Label(window, text="Pusty")
    numbers_file_label.grid(row=4, column=3)

    if h_file:
        numbers_file_label.config(text=os.path.basename(h_file))

    Button(window, text="Pokaż wykres", command=show).grid(row=5, column=2, ipadx=10)

    result_label = Label(window, text="Wynik: ")
    result_label.grid(row=6, column=2)

    txt = """
            Średnie natężenie ruchu telekomunikacyjnego
                            Wzór: A = lambda * h
    gdzie: 
        lambda - średnia liczba zgłoszeń na jednostke czasu
        h - średni czas trwania połączenia

    Za pomocą przycisków "Otwórz" wybrać odpowiednie pliki
        otwórz 1 - plik z czasami trwania połączeń
        otwórz 2 - plik z licznościami wywołań jakie zarejstrowano
        w danej minucie
        
    Kliknij "więcej" aby dowiedzieć się o zawartości plików.
    """
    descr = Label(window, text=txt, borderwidth=3, relief="groove")
    descr.grid(row=5, column=4, ipadx=10)
    instruction_txt = """
            Instrukcja:
        1 plik w formacie txt 
            w kolumnie wpisać czasy trwania połączeń[s].
            
            Przykładowy plik o nazwie "time.txt",
            przykładowe dwa pierwsze wiersze pliku:
            23
            51
            
        2 plik w formacie txt
            w pierwszej kolumnie wpisać 
            poszczególne minuty doby,
            w drugiej kolumnie wpisać średnią 
            liczbe zgłoszeń w danej minucie.
            Kolumny odzielić tabulatorem.
            
            Przykładowy plik o nazwie "numbers.txt",
            przykładowe dwa pierwsze wiersze pliku
            1   510
            3   670
                
        Pliki z danymi znajdują się w
        folderze "przykłady".
        Wynik średniego natężenia wyświetli się 
        po zamknięciu okna z wykresem.
        """
    Button(window, text="Więcej ...", command=lambda: OpenNewWindow("Formula", "450x500", instruction_txt))\
        .grid(row=6, column=4)

    spacer2 = Label(window, text="")
    spacer2.grid(row=7, column=0, pady=100)

    Button(window, text="Cofnij", command=lambda: ChangePage(1)).grid(row=9, column=0)


def Page3():
    global average_time_file_label, numbers_file_label, result_label_p3, h_file, avg_file
    page = Frame(window)
    page.grid()

    label = Label(window, text="Średnie natęzenie ruchu 2")
    label.grid(row=1,column=3, pady=20)

    spacer1 = Label(window, text="")
    spacer1.grid(row=2, column=0)

    Button(window, text="Otwórz 1", command=lambda: select_file_average_time()).grid(row=3, column=1)
    average_time_file_label = Label(window, text="Pusty")
    average_time_file_label.grid(row=4, column=1)

    if avg_file:
       average_time_file_label.config(text=os.path.basename(avg_file))
    Button(window, text="Otwórz 2", command=lambda: select_file_numbers()).grid(row=3, column=3)
    numbers_file_label = Label(window, text="Pusty")
    numbers_file_label.grid(row=4, column=3)

    if h_file:
        numbers_file_label.config(text=os.path.basename(h_file))

    Button(window, text="Oblicz", command=show_average).grid(row=5, column=2)

    result_label_p3 = Label(window, text="Wynik: ")
    result_label_p3.grid(row=6, column=2)

    txt = """
            Średnie natężenie ruchu telekomunikacyjnego
                            Wzór: A = lambda * h
    gdzie: 
        lambda - średnia liczba zgłoszeń na jednostke czasu 
        h - średni czas trwania połączenia

    Za pomocą przycisków "Otwórz" wybrać odpowiednie pliki
        otwórz 1 - plik z czasami trwania połączeń dla danego 
        wywołania
        otwórz 2 - plik z licznościami wywołan jakie zarejstrowano
        w danej minucie
        
    Kliknij "więcej" aby dowiedzieć sie o zawartości plików.
    """
    descr = Label(window, text=txt, borderwidth=3, relief="groove")
    descr.grid(row=5, column=4, ipadx=10)
    instruction_txt = """
            Instrukcja:
        1 plik w formacie txt 
            w kolumnie wpisać czas trwania połączenia
            dla danej liczby zgłoszeń.
            Ilośc wierszy powinna być taka sama jak 
            w drugim pliku.
                
            Przykładowy plik o nazwie "avg_time.txt"m
            przykładowe dwa pierwsze wiersze pliku:
            23
            51
                
        2 plik w formacie txt
            w pierwszej kolumnie wpisać 
            poszczególną minute doby,
            w drugiej kolumnie wpisać średnią 
            liczbe zgłoszeń dla danej minuty.
            Kolumny odzielić tabulatorem.
            
            Przykładowy plik o nazwie "numbers.txt",
            przykładowe dwa pierwsze wiersze pliku:
            1   510
            3   670
            
        Pliki z danymi znajdują się w
        folderze "przykłady".
        Wynik średniego natężenia wyświetli się 
        po zamknięciu okna z wykresem.
        """
    Button(window, text="Instrukcja", command=lambda: OpenNewWindow("Formula", "450x500", instruction_txt)).grid(row=6, column=4)

    spacer2 = Label(window, text="")
    spacer2.grid(row=7, column=0, pady=100)

    Button(window, text="Cofnij", command=lambda: ChangePage(1)).grid(row=9, column=0)

def Page4():
    global connection_file_label, text_time, result_label_p4, connection_file
    page = Frame(window)
    page.grid()

    label = Label(window, text="Wzór 2")
    label.grid(row=1, column=3, pady=20)

    spacer1 = Label(window, text="")
    spacer1.grid(row=2, column=0)

    # Button(window, text="Open avg_time.txt", command=lambda: select_file_average_time()).grid(row=4, column=1)
    text_time = Text(window, height=1, width=7)
    text_time.grid(row=3, column=1, ipadx=5)
    text_time.insert(END, "60")
    
    desc = """
        Czas obserwacji
        w minuatch 
        (liczba calkowita)
    """

    Label(window, text=desc, width=10).grid(row=4, column=1, ipadx=30)

    Button(window, text="Otwórz", command=lambda: select_connection_time()).grid(row=3, column=3)
    connection_file_label = Label(window, text="Pusty")
    connection_file_label.grid(row=4, column=3)

    if connection_file:
        connection_file_label.config(text=os.path.basename(connection_file))

    Button(window, text="Oblicz", command=show_version2).grid(row=5, column=2)

    result_label_p4 = Label(window, text="Wynik: ")
    result_label_p4.grid(row=6, column=2)

    txt = """
            Średnie natężenie ruchu telekomunikacyjnego (2 wzór)
        Wzór: AT = suma czasów trwania połączeń/okres obserwacji
    
    W polu "czas obserwacji" wpisać okres obserwacji
    w minutach jako liczbę całkowitą.
    Za pomocą przycisku "Otwórz" wybrać odpowiednie pliki
        Otwórz - plik z czasami trwania połączeń
    
    Kliknij "więcej" aby dowiedzieć sie o zawartości plików.
    """
    descr = Label(window, text=txt, borderwidth=3, relief="groove")
    descr.grid(row=5, column=4, ipadx=10)
    instruction_txt = """
            Instrukcja:
        1 okienko liczba całkowita
            wpisać czas obserwacji rozmów
        2 plik w formacie txt 
            Przykładowy plik o nazwie "connection_time.txt",
            w kolumnie wpisać czas trwania k-tego połączenia
            przykładowe dwa pierwsze wiersze pliku:
            23
            51
            ...
                    
        Pliki z danymi znajdują się w
        folderze "przykłady".
        """
    Button(window, text="Instrukcja", command=lambda: OpenNewWindow("Formula", "450x400", instruction_txt)).grid(row=6, column=4)

    spacer2 = Label(window, text="")
    spacer2.grid(row=7, column=0, pady=100)

    Button(window, text="Confij", command=lambda: ChangePage(1)).grid(row=9, column=0)



Page1()

window.mainloop()
