import matplotlib.pyplot as plt
import numpy as np

def derivacija(f, x, eps=1, metoda="three-step"):                   # 1e-5 je isto kao i 1 * 10^{-5}, h je mali pomak u x-u!
    
    if metoda == "three-step":
        der3 = (f(x+eps) - f(x-eps))/(2*eps)
        return der3
    elif metoda =="two-step":
        der2 = (f(x+eps) - f(x)) / eps
    else:
       raise ValueError("Nepoznata metoda")     #raise ValueError(...) = “korisnik je dao krivi argument

def derivacija_interval(f, a, b, N=100, eps=1, metoda="three-step"):        #N nije potreban ali daje korisniku mogucnost za promijeniti
    x_vrijednosti = np.linspace(a, b, N)
    der_vrijednosti = []

    for x in x_vrijednosti:
        der = derivacija(f, x, eps, metoda)
        der_vrijednosti.append(der)

    return x_vrijednosti, der_vrijednosti

def pravokutna_aproks_integrala(f, a, b, N=50):

    dx = (b-a)/N
    x = np.linspace(a, b, N+1)

    donja_suma = 0
    gornja_suma = 0

    for i in range(N):
        donja_suma += f(x[i])
        gornja_suma = f(x[i+1])

    donja_suma *= dx
    gornja_suma *= dx

    return donja_suma, gornja_suma

def trapezna_metoda_integracije(f, a, b, N=50):

    dx = (b-a)/N
    x = np.linspace(a, b, N+1)

    suma = 0

    for i in range(1, N):
        suma += f(x[i])

    integral = (f(x[0]) + 2*suma + f(x[N])) * (dx/2)

    return integral