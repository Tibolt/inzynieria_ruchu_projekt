import numpy as np
import matplotlib.pyplot as plt


# A = l * h

# suma wszystkich czasow rozmow / dlugosc obserwacji np 1h

# czas trwania polaczenia w ciagu doby
l = [158, 9, 9, 3, 11, 89]

# kolejne minuty doby
h = [1, 2, 4, 8, 11, 14]

sum = 0
for x in l:
    sum += x

# sredni czas trwania polaczenia
lt = sum / 4

# ilosc wywolan jakie zarejstrowano w danej minucie doby
# lambda
num = [
    2.38095E-05,
    7.14286E-05,
    2.38095E-05,
    2.38095E-05,
    2.38095E-05,
    4.7619E-05]

# wartosc chwilowa intensywnosci wywolan w poszczegolnych minutach - wzor:
# num[h] / sum(num)


out = np.asarray(num) * lt
print(out)


plt.plot(h, out)
plt.xlabel('kolejne minuty doby')
plt.ylabel('sredni czas * ilosc wywolan')
plt.show()
