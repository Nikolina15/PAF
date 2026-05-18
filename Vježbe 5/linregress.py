import math
import numpy as np
import matplotlib.pyplot as plt

M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336]
kut = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]

xy_lista = []
x2_lista = []

for i in range(len(M)):
    a = M[i]*kut[i]
    xy_lista.append(a)

print(xy_lista)

for i in kut:
    b = i**2
    x2_lista.append(b)

xy = sum(xy_lista)
x2 = sum(x2_lista)

a = xy/x2

y2_lista = []

for j in M:
    c = j**2
    y2_lista.append(c)

y2 = sum(y2_lista)

sigma = math.sqrt((1/len(M))*((y2/x2) - a**2))

print(f"Model torzije aluminijske šipke Dt : {a}")
print(f"Standardna devijacija je {sigma}")

x = np.linspace(0, 1.2, 100)
y = a*x

plt.scatter(kut, M, label= "Podatci", color="red")
plt.plot(x, y, label="linerana regresija")
plt.legend()
plt.xlabel("M [Nm]")
plt.ylabel("φ [rad]")
plt.show()