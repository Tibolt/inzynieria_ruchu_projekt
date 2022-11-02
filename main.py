from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from tkinter.ttk import *
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")


window = Tk()
window.geometry('800x600')

label = Label(window, text="Test Program")
label.place(relx=0.5, rely=0.1, anchor="center")


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


def formula():
    # A = l * h
    l = [158, 9, 9, 3]
    h = [1, 2, 4, 8]
    sum = 0
    for x in l:
        sum += x

    lt = sum / len(l)
    out = lt * h
    print(out)


def test():
    # test wzoru A = l * h
    l = [158, 9, 9, 3]
    h = [1, 2, 4, 8]
    draw(l, h)


bt = Button(window, text="Multiply", command=clicked)
# bt.grid(column=2, row=2)
bt.place(relx=0.5, rely=0.3, anchor="center")

debug_bt = Button(window, text="Debug", command=test)
debug_bt.place(relx=0.5, rely=0.4, anchor="center")

inpx = Entry(window)
inpx.place(relx=0.5, rely=0.15, anchor="center")
labelx = Label(window, text="x")
labelx.place(relx=0.4, rely=0.15, anchor="center")

inpy = Entry(window)
inpy.place(relx=0.5, rely=0.20, anchor="center")
labely = Label(window, text="y")
labely.place(relx=0.4, rely=0.20, anchor="center")


window.mainloop()
