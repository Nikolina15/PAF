#test Euler metode(za razlicite dt)
import numpy as np
import matplotlib.pyplot as plt
import Projectile as pro

v0 = 10
theta = np.radians(40)
dt_lista = [0.4, 0.2, 0.1, 0.01, 0.001]

for dt in dt_lista:
    p = pro.Projectile(v0, theta)
    x, y = p.simulate(dt)
    plt.plot(x,y, label= f"dt={dt}")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Eulerova metoda za kosi hitac s razlicitim dt")
plt.legend()
plt.show()