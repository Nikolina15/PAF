#Vježbe 6

import math
import numpy as np
import matplotlib.pyplot as plt

#Dijametar[mm]
R1 = [19.98, 20.18, 20.10, 20.08, 19.74]
R2 = [19.92, 19.82, 19.96, 19.98, 19.88]
R3 = [24.96, 24.98, 24.98, 24.92, 24.94]

#Duljine[mm]
L1 = [49.80, 49.00, 50.48, 49.80, 49.96]
L2 = [52.56, 52.50, 52.62, 52.58, 52.54]
L3 = [55.34, 55.40, 55.30, 55.44, 55.48]

#Masa[g]
m1 = [138.92, 138.98, 139.20, 138.90, 138.92]
m2 = [128.65, 128.60, 128.65, 128.35, 128.50]
m3 = [71.89, 71.90, 71.79, 71.85, 71.70]


def srednja_vrijednost(lista):
    x = sum(lista)/len(lista)
    return x

def standardno_odstupanje(lista):
    lista_kvadrata = []

    for i in lista:
        a = (i - srednja_vrijednost(lista))**2
        lista_kvadrata.append(a)

    sigma = math.sqrt(sum(lista_kvadrata)/(len(lista)*(len(lista)-1)))
    return sigma

def volumen(r, L):
    V = (r**2)*math.pi*L
    return V 

def gustoca(m, V):
    rho = m/V
    return rho
    
#Propagacije pogreške za funkcije
def sigma_volumena(r, sigma_r, L, sigma_L):
    dV_dr = 2*r*math.pi*L
    dV_dL = (r**2)*math.pi

    sigma_V = math.sqrt((dV_dr*sigma_r)**2 + (dV_dL*sigma_L)**2)
    return sigma_V

def sigma_gustoce(m, sigma_m, V, sigma_V):
    drho_dm = 1/V
    drho_dV = -m/(V**2)

    sigma_rho = math.sqrt((drho_dm*sigma_m)**2 + (drho_dV*sigma_V)**2)
    return sigma_rho

#Relativna pogreška u usporedbi s literaturom(gustoća)
def relativna_pogreska(rho, rho_lit):
    delta = (abs(rho-rho_lit)/rho_lit)*100
    return delta

#Racun

dijametri = [R1, R2, R3]
duljina = [L1, L2, L3]
masa = [m1, m2, m3]

radijus = []
for i in range(3):
    r_lista = []
    radijus.append(r_lista)
    for j in dijametri[i]:
        r = j/2
        r_lista.append(r)

#print(radijus)

gustoca_valjaka = []

for i in range(3):

    print(f"VALJAK {i+1}")

    #srednja vrjednost
    #dijametar
    R_s = srednja_vrijednost(dijametri[i])
    sigma_R = standardno_odstupanje(dijametri[i])

    #radijus
    r_s = srednja_vrijednost(radijus[i])
    sigma_r = standardno_odstupanje(radijus[i])

    #duljina
    L_s = srednja_vrijednost(duljina[i])
    sigma_L = standardno_odstupanje(duljina[i])

    #masa
    m_s = srednja_vrijednost(masa[i])
    sigma_m = standardno_odstupanje(masa[i])

    #pretvorba mm -> cm
    r_cm = r_s/10
    sigma_r_cm = sigma_r/10
    L_cm = L_s/10
    sigma_L_cm = sigma_L/10

    #Volumen
    V = volumen(r_cm, L_cm)
    sigma_V = sigma_volumena(r_cm, sigma_r_cm, L_cm, sigma_L_cm)

    #Gustoca
    rho = gustoca(m_s, V)
    gustoca_valjaka.append(rho)
    sigma_rho = sigma_gustoce(m_s, sigma_m, V, sigma_V)

    print(f"R = {R_s:.3f} ± {sigma_R:.3f} mm")
    print(f"L = {L_s:.3f} ± {sigma_L:.3f} mm")
    print(f"m = {m_s:.3f} ± {sigma_m:.3f} g")

    print(f"V = {V:.3e} ± {sigma_V:.3e} cm^3")
    print(f"ρ = {rho:.3e} ± {sigma_rho:.3e} g/cm^3")

print(gustoca_valjaka)

#gustoca iz lit
rho_bakra = 8.96
rho_zeljeza = 7.87
rho_aluminija = 2.70

rho_lit = [rho_bakra, rho_zeljeza, rho_aluminija]
materijal = ["Bakar","Zeljezo", "Aluminiji"]

for i in range(3):
    print(f"Valjak {i+1} = {materijal[i]}")

    r_p = relativna_pogreska(gustoca_valjaka[i], rho_lit[i])
    print(f"Relativna pogreska: {r_p:.3f}%")
