#Zadatak 5

import math
import numpy as np

import numpy as np

# 5 mjerenja temperature vrenja vode [u stupnjevima Celzijusa ]
malo_n = [99.8 , 100.1 , 99.9 , 100.2 , 100.0]

# 10000 mjerenja istog eksperimenta ( simulacija )
np.random.seed (42)
veliko_n = np.random.normal(loc =100.0 , scale =0.2 , size =10000).tolist()

def srednja_vrijednost(lista):
    x = sum(lista)/len(lista)
    return x

def sigma_n(lista):
    lista_kvadrata = []

    for i in lista:
        a = (i - srednja_vrijednost(lista))**2
        lista_kvadrata.append(a)

    sigma = math.sqrt(sum(lista_kvadrata)/len(lista))
    return sigma

def s(lista):
    lista_kvadrata = []

    for i in lista:
        a = (i - srednja_vrijednost(lista))**2
        lista_kvadrata.append(a)

    a = math.sqrt(sum(lista_kvadrata)/(len(lista)-1))
    return a

def sigma_s_v(lista):
    sigma = s(lista)/math.sqrt(len(lista))
    return sigma

#malo_n

n_sigma_n = sigma_n(malo_n)
n_s = s(malo_n)
n_sigma_s_v = sigma_s_v(malo_n)
n_rel_razlika = abs(n_sigma_n-n_s)/n_s * 100

print("Malo n:")
print(f"σ_n = {n_sigma_n:.3f}")
print(f"s = {n_s:.3f}")
print(f"σ_x̄ = {n_sigma_s_v:.3f}")
print(f"Relativna razlika σ_n i s = {n_rel_razlika:.3f} %")

#veliko n
N_sigma_n = sigma_n(veliko_n)
N_s = s(veliko_n)
N_sigma_s_v = sigma_s_v(veliko_n)
N_rel_razlika = abs(N_sigma_n-N_s)/N_s * 100

print("Veliko n:")
print(f"σ_n = {N_sigma_n:.3f}")
print(f"s = {N_s:.3f}")
print(f"σ_x̄ = {N_sigma_s_v:.3f}")
print(f"Relativna razlika σ_n i s = {N_rel_razlika:.3f} %")

#(a)
# Kako se mijenja s kada povećamo broj mjerenja, a kako σx̄?
# s ostaje približno ista jer opisuje raspršenje podataka.
# σx̄ se smanjuje jer dijelimo s: sqrt(n)	​
# što znači da srednja vrijednost postaje preciznija.

# (b)
# Kolika je relativna razlika između σₙ i s?
# Za mali skup razlika je primjetna.
# Za veliki skup razlika postaje gotovo zanemariva.

# (c)
# np.std() po defaultu dijeli s n, kada je to ispravno koristiti?
# Ispravno je koristiti kada:
# imaš cijelu populaciju podataka
# ne procjenjuješ iz uzorka.