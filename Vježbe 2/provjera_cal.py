import matplotlib.pyplot as plt
import numpy as np
#from calculus import derivacija
from calculus import derivacija_interval

def f(x):
    return x**3

x_lista, der_lista = derivacija_interval(f, 1, 5)

analiticka = []
for x in x_lista:
    der_a = 3*(x**2)
    analiticka.append(der_a)

#print(analiticka)

plt.plot(x_lista, der_lista, label = "numericko")
plt.plot(x_lista, analiticka, label = "analiticko")
plt.title("Kubna funkcija")
plt.legend()
plt.xlabel("x")
plt.ylabel("f´(x)")
plt.show()

# print(x_lista)
# print(analiticka)
# print(der_lista)

def f2(x):
    return np.sin(x)

x2_lista, der2_lista = derivacija_interval(f2, 1, 5)

analiticka2 = []
for x in x2_lista:
    der_a2 = np.cos(x)
    analiticka2.append(der_a2)

plt.plot(x2_lista, der2_lista, label = "numericko")
plt.plot(x2_lista, analiticka2, label = "analiticko")
plt.title("Trigonomerijska funkcija (sinus)")
plt.legend()
plt.xlabel("x")
plt.ylabel("f´(x)")
plt.show()