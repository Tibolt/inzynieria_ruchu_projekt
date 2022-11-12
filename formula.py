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


# A = l * h

# suma wszystkich czasow rozmow / dlugosc obserwacji np 1h

# czas trwania polaczenia w ciagu doby
# l = [158, 9, 9, 3, 11, 89]
l = open_time("time.txt")

# kolejne minuty doby
# h = [1, 2, 4, 8, 11, 14]
h = open_numbers("numbers.txt", 0)

sum = 0
for x in l:
    sum += x

# sredni czas trwania polaczenia
lt = sum / len(l)

# ilosc wywolan jakie zarejstrowano w danej minucie doby
# lambda
# num = [2.38095e-05, 7.14286e-05, 2.38095e-05, 2.38095e-05, 2.38095e-05, 4.7619e-05]
num = open_numbers("numbers.txt", 1)

# wartosc chwilowa intensywnosci wywolan w poszczegolnych minutach - wzor:
# num[h] / sum(num)


out = np.asarray(num) * lt
print(out)

hours = np.asanyarray(h) / 60

plt.plot(hours, out)
plt.xlabel("kolejne godziny doby")
plt.ylabel("sredni czas * ilosc wywolan")
plt.xticks([0, 4, 8, 12, 16, 20, 24])
plt.show()
