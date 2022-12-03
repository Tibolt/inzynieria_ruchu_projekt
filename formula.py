import numpy as np
import matplotlib.pyplot as plt


# funkcja do odczytania danych z pliku


def open_numbers(name, col):
    f = open(name, "r")
    result = []
    for x in f:
        result.append(float(x.split()[col]))
    f.close()
    return result


def open_time(name):
    f = open(name, "r")
    result = []
    for x in f:
        result.append(int(x.split()[0]))
    f.close()
    return result


def calculate(l, h, num):
    # A = l * h
    # suma wszystkich czasow rozmow / dlugosc obserwacji np 1h

    # l -czas trwania polaczenia w ciagu doby, l = [158, 9, 9, 3, 11, 89]
    # h - kolejne minuty doby ,h = [1, 2, 4, 8, 11, 14]
    sum = 0
    for x in l:
        sum += x

    # sredni czas trwania polaczenia
    lt = sum / len(l)

    # ilosc wywolan jakie zarejstrowano w danej minucie doby
    # lambda
    # num = [2.38095e-05, 7.14286e-05, 2.38095e-05, 2.38095e-05, 2.38095e-05, 4.7619e-05]
    out = np.asarray(num) * lt
    hours = np.asanyarray(h) / 60

    plt.plot(hours, out)
    plt.xlabel("kolejne godziny doby")
    plt.ylabel("sredni czas * ilosc wywolan")
    plt.xticks([0, 4, 8, 12, 16, 20, 24])
    plt.show()

# wartosc chwilowa intensywnosci wywolan w poszczegolnych minutach - wzor:
# num[h] / sum(num)

def calculate_avg(avg, h, num):
    # ilosc wywolan jakie zarejstrowano w danej minucie doby
    # lambda
    # num = [2.38095e-05, 7.14286e-05, 2.38095e-05, 2.38095e-05, 2.38095e-05, 4.7619e-05]
    # avg - srenid czas rozmow w danej minucie - array
    # out = np.multiply(np.asarray(num), np.asarray(avg))
    out = np.asarray(num) * np.asarray(avg)
    hours = np.asanyarray(h) / 60

    plt.plot(hours, out)
    plt.xlabel("kolejne godziny doby")
    plt.ylabel("sredni czas * ilosc wywolan")
    # xticks = []
    # for i in range(hours[0], hours[-1:], 6):
    #     xticks.append(int(i))
    # plt.xticks(xticks)
    plt.show()

# wartosc chwilowa intensywnosci wywolan w poszczegolnych minutach - wzor:
# num[h] / sum(num)
