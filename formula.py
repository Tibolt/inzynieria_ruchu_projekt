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
    #Średnie natęzenie ruchu
    # A = l * h
    # l - sredia liczba zgloszen na jednostke czasu
    # h - sredni czas trwania polaczenia

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

    # srednia ilosc wywolan
    connections_sum = 0
    for x in num:
        connections_sum += x
    
    connections_avg = connections_sum / len(num)
    result = connections_avg * lt


    plt.plot(hours, out)
    plt.xlabel("kolejne godziny doby")
    plt.ylabel("natężenie ruchu")
    plt.xticks([0, 4, 8, 12, 16, 20, 24])
    plt.show()
    return result

# wartosc chwilowa intensywnosci wywolan w poszczegolnych minutach - wzor:
# num[h] / sum(num)

def calculate_avg(avg, h, num):
    # ilosc wywolan jakie zarejstrowano w danej minucie doby
    # lambda
    # num = [2.38095e-05, 7.14286e-05, 2.38095e-05, 2.38095e-05, 2.38095e-05, 4.7619e-05]
    # avg - sredni czas rozmow w danej minucie - array
    out = np.asarray(num) * np.asarray(avg)
    hours = np.asanyarray(h) / 60

    plt.plot(hours, out)
    plt.xlabel("kolejne godziny doby")
    plt.ylabel("natężenie ruchu")
    # xticks = []
    # for i in range(hours[0], hours[-1:], 6):
    #     xticks.append(int(i))
    # plt.xticks(xticks)
    plt.show()

    sum = 0
    for x in avg:
        sum += x

    # sredni czas trwania polaczenia
    lt = sum / len(avg)

    # srednia ilosc wywolan
    connections_sum = 0
    for x in num:
        connections_sum += x

    connections_avg = connections_sum / len(num)
    result = connections_avg * lt
    return result

def calculate_v2(con_time, h):
    # suma wszystkich czasow rozmow / dlugosc obserwacji np 1h
    # wartosc chwilowa intensywnosci wywolan w poszczegolnych minutach - wzor:
    # gdzie suma od 1 do liczby zestawionych polaczen w przedziale czasu h
    # sum(connection_time) / h
    sum = 0
    for x in con_time:
        sum += x

    observation_time = []
    for i in range(1, len(con_time)+1):
        observation_time.append(i)
        
    out = sum / h

    # TODO: Zapytac o wykres, co rysowac
    # TODO: FIX x and y must have same first dimension, but have shapes (59,) and (40,) error 

    return out