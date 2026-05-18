#Vjezbe 4 (uz pomoc AI-a)

import numpy as np
import matplotlib.pyplot as plt

e = 1.602e-19   #elementarni naboj
m_e = 9.109e-31  # masa elektrona

def akceleracija(q, m, v, E, B):
    a = (q/m)*(E+np.cross(v,B))  #np.cross - vektorsko mnozenje
    return a

def simulacija(q, m, E, B, r0, v0, dt, koraci):

    r = np.zeros((koraci, 3))   #matrica, koraci=retci, 3=stupci (za x, y, z)
    v = np.zeros((koraci, 3))

    r[0] = r0
    v[0] = v0

    for i in range(koraci-1):
        a = akceleracija(q, m, v[i], E, B)
        #Eulerova metoda
        v[i+1] = v[i] + a*dt
        r[i+1] = r[i] + v[i+1]*dt
    
    return r, v

#parametri

B = np.array([0, 0, 1e-3])   #magnetsko polje
E = np.array([0, 0, 0])      #elektricno polje
#E = np.array([1e3, 0, 0])

r0 = np.array([0, 0, 0])
v0 = np.array([2e6, 1e6, 1.5e6])
dt = 1e-11
koraci = 6000

#Elektron
r_e, v_e = simulacija(-e, m_e, E, B, r0, v0, dt, koraci)

#Pozitron
r_p, v_p = simulacija(+e, m_e, E, B, r0, v0, dt, koraci)

fig = plt.figure(figsize=(12, 7))
ax = fig.add_subplot(121, projection='3d')
ax.plot(r_e[:,0], r_e[:,1], r_e[:,2])
ax.set_title("Elektron")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot(r_p[:,0], r_p[:,1], r_p[:,2], color='red')
ax2.set_title("Pozitron")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_zlabel("z")

plt.tight_layout()
plt.show()