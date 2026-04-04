import numpy as np
import matplotlib.pyplot as plt
import calculus as calc

def f(x):
    return x**2

a = 0
b = 5

analiticko = 125/3

koraci = np.arange(1, 100, 2)

p_donje = []
p_gornje = []
trap = []

for N in koraci:
    donja, gornja = calc.pravokutna_aproks_integrala(f, a, b, N)
    t_integral = calc.trapezna_metoda_integracije(f, a, b, N)

    p_donje.append(donja)
    p_gornje.append(gornja)
    trap.append(t_integral)

plt.plot(koraci, p_donje, label="donja suma")
plt.plot(koraci, p_gornje, label="gornja suma")
plt.plot(koraci, trap, label="trapezna")
plt.axhline(analiticko, label="analitičko", color="black")

plt.xlabel("N (broj podjela)")
plt.ylabel("Vrijednost integrala")
plt.title("Usporedba numeričkih metoda integracije")
plt.legend()
plt.show()