# usporedba Eulerove metode i RK4 za dt = 0.01

import numpy as np
import matplotlib.pyplot as plt
import Projectile as pro

v0 = 10
theta = np.radians(55)
dt = 0.01

cestica = pro.Projectile(v0, theta)

#Euler
x1, y1 = cestica.simulate(dt)

#RK4
x2, y2 = cestica.simulate_RK4(dt)

plt.plot(x1, y1, label="Euler metoda")
plt.plot(x2, y2, label= "RK4")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()