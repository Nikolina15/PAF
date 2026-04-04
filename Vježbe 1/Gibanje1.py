#Napišite program u kojem korisnik definira iznos sile u N i masu čestice u kg, a program crta x − t, v − t
# i a − t graf za prvih 10 sekundi jednolikog gibanja u jednoj dimenziji. Diferencijalne jednadžbe rješavajte
# numerički. Pripazite na oznake i mjerne jedinice x i y osi na svim grafovima.

import matplotlib.pyplot as plt
import numpy as np
import math

F = float(input("Unesi iznos sile [N]: "))
m = float(input("Unesi masu čestice [kg]: "))

dt = 0.1
t = np.arange(0, 10+dt, dt)          #np.arange(start, stop, step) stvara listu!
a = F/m
a_graf = np.ones(len(t)) * a         #np.ones() stvara niz jedinica duljine kao argument u zagradama  
v = np.zeros(len(t))                 #np.zeros() niz(array) istog tipa kao t ispunjen s nulama.
s = np.zeros(len(t))

for i in range(1, len(t)):            #Euler metoda
    v[i] = v[i-1] + a*dt
    s[i] = s[i-1] + v[i-1]*dt

# v = []
# s = []
# for i in t:
#     v_tren = a*i
#     s_tren = (1/2)*a*(i**2)
#     v.append(v_tren)
#     s.append(s_tren)

#print(v)
#print(s)
#print(len(v), len(t), len(s))

plt.subplot(2,2,1)
plt.plot(t, s)
plt.grid()
plt.xlabel("t[s]")
plt.ylabel("s[m]")
plt.title("s-t graf")

plt.subplot(2,2,2)
plt.plot(t,v)
plt.grid()
plt.xlabel("t[s]")
plt.ylabel("v[m/s]")
plt.title("v-t graf")

plt.subplot(2,2,3)
plt.plot(t,a_graf)
plt.grid()
plt.xlabel("t[s]")
plt.ylabel("a[m/s^2]")
plt.title("a-t graf")

plt.tight_layout()
plt.show()