#Napišite svoj modul "kinematika.py" koji će sadržavati funckiju jednoliko_gibanje(). Neka funkcije kao
# ulazne parametre primaju sve podatke neophodne za izračun (iznos sile, masa, ...) i neka crta iste grafove
# kao i u prošlom zadatku. Napravite novi program u kojem ćete uključiti razvijeni modul i pozvati funkciju.

import matplotlib.pyplot as plt
import numpy as np

def jednoliko_gibanje(F, m, v0, s0, vrijeme):
    dt = 0.1
    t = np.arange(0, vrijeme+dt, dt)

    a_konst = F/m
    a = np.ones(len(t)) * a_konst

    v = []
    s = []
    for i in t:
        v_tren = v0*i + a_konst*i
        s_tren = s0 + v0*i + (1/2)*a_konst*(i**2)
        v.append(v_tren)
        s.append(s_tren)

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
    plt.plot(t,a)
    plt.grid()
    plt.xlabel("t[s]")
    plt.ylabel("a[m/s^2]")
    plt.title("a-t graf")

    plt.tight_layout()
    plt.show()

