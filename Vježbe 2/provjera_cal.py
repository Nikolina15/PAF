import matplotlib.pyplot as plt
import numpy as np
#from calculus import derivacija
from calculus import derivacija_interval

def f(x):
    return x**3

x_lista, der_lista = derivacija_interval(f, 1, 5)
xe2_lista, dere2_lista = derivacija_interval(f, 1, 5, 100, 0.1)
xe3_lista, dere3_lista = derivacija_interval(f, 1, 5, 100, 0.01)

analiticka = []
for x in x_lista:
    der_a = 3*(x**2)
    analiticka.append(der_a)

# analiticka_e2 = []
# for x2 in xe2_lista:
#     der_e2 = 3*(x**2)
#     analiticka_e2.append(der_e2)

# analiticka_e3 = []

#print(analiticka)
plt.title("Kubna funkcija")
plt.scatter(x_lista, analiticka, label = "analiticko", s=20, color="black", alpha=10)
plt.scatter(x_lista, der_lista, label = "numericko(eps=1)", s=10)
plt.scatter(xe2_lista, dere2_lista, label = "numericko2(eps=0.1)", s=10)
plt.scatter(xe3_lista, dere3_lista, label = "numericko3(eps=0.01)", s=10)
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