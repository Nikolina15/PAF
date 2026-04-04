#Za česticu početne brzine v0 = 10ms i kuta otklona θ = 60o nacrtajte graf ovisnosti relativne pogreške
#numeričkog riješenja o vrijednosti vremenskog koraka ∆t.

import matplotlib.pyplot as plt
import numpy as np
import particle as p

v0 = 10
theta = np.radians(60)
dt_lista = np.linspace(0.001, 0.1, 100)
g = 9.81


analiticko = (v0**2 * np.sin(2*theta)) / g

pogreške = []

for dt in dt_lista:
    p1 = p.Particle(v0, theta)
    numericko = p1.range(dt)

    greska = abs(numericko - analiticko) / analiticko
    pogreške.append(greska)


plt.plot(dt_lista, pogreške)
plt.xlabel("dt")
plt.ylabel("Relativna pogreška")
plt.title("Ovisnost pogreške o vremenskom koraku")
plt.show()