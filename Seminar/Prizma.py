#Modul za lom svijetlosti na prizmu

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Funkcija za racunanje devijacije zrake na prizmi
# 1. Snellov zakon na prvoj plohi
# 2. Geometrija prizme
# 3. Snellov zakon na izlasku
# 4. Ukupna devijacija: δ = i + e - A

def devijacija_prizme(upadni_kut_deg, vrsni_kut_prizme_deg, indeks_loma_materijala):

    i = np.radians(upadni_kut_deg)
    A = np.radians(vrsni_kut_prizme_deg)
    n = indeks_loma_materijala

    validni_kutovi = []
    devijacije = []

    for kut in i:
        r1 = np.arcsin(np.sin(kut)/n)
        r2 = A - r1

        #provjera izlazne zrake
        if abs(n*np.sin(r2)) <= 1:
            e = np.arcsin(n*np.sin(r2))
            delta_rad = kut + e - A
            delta_deg = np.degrees(delta_rad)

            validni_kutovi.append(np.degrees(kut))
            devijacije.append(delta_deg)

        else:
            continue

    return validni_kutovi, devijacije

# MINIMALANA DEVIJACIJA

def minimalna_devijacija(vrsni_kut_prizme_deg, indeks_loma_materijala):
    A = vrsni_kut_prizme_deg
    n = indeks_loma_materijala

    upadni_kutovi = np.linspace(1, 89, 2000)

    kutovi, devijacije = devijacija_prizme(upadni_kutovi, A, n)

    min_devijacija = min(devijacije)
    indeks = devijacije.index(min_devijacija)
    min_kut = kutovi[indeks]

    return min_kut, min_devijacija

# RASPAD BIJELE SVIJETLOSTI
# CAUCHIJEVA JEDNADŽBA
# indeks loma ovisi o valnoj duljini
# ova ovisnos uzrokuje disprerziju

def cauchijev_indeks(valna_duljina_nm):     #valna duljina izrazena je u mikrometrima

    valna_duljina_μm = valna_duljina_nm / 1000
    
    # konstante
    A = 1.5046
    B = 0.00420

    x = A + B/ valna_duljina_μm**2

    return x 

# DISPERZIJA
# za svaku valnu duljinu racunamo indeks loma i devijaciju

def disperzija(valna_duljina_nm, ulazni_kut_deg, vrsni_kut_prizme_deg):

    A = np.radians(vrsni_kut_prizme_deg)
    i = np.radians(ulazni_kut_deg)

    disperzije = []

    for valna_duljina in valna_duljina_nm:
        n = cauchijev_indeks(valna_duljina)

        r1 = np.arcsin(np.sin(i)/n)
        r2 = A - r1

        #provjera izlazne zrake
        if abs(n*np.sin(r2)) <= 1:
            e = np.arcsin(n*np.sin(r2))
            delta_rad = i + e - A
            delta_deg = np.degrees(delta_rad)
            disperzije.append(delta_deg)

        else:
            continue
    
    return disperzije

# PARAMETRI PRIZME
vrsni_kut_przme = 60   # stupnjevi
n = 1.52               # indeks loma

# GRAF 1: DEVIJACIJA I UPADNI KUT I MINIMALNA DEVIJACIJA

ulazni_kutovi = np.linspace(1, 80, 500)

kutovi, devijacija = devijacija_prizme(ulazni_kutovi, vrsni_kut_przme, n)
min_kut, min_dev = minimalna_devijacija(vrsni_kut_przme, n)

print("Minimalna devijacija:")
print(f"Upadni kut = {min_kut:.2f}°")
print(f"Devijacija = {min_dev:.2f}°")

plt.plot(kutovi, devijacija)
plt.scatter(min_kut, min_dev, color = "red", label= "Minimalna devijacija")
plt.title("Devijacija zrake u ovisnosti o upadnom kutu")
plt.xlabel("Upadni kut [°]")
plt.ylabel("Devijacija [°]")
plt.legend()
plt.grid()
plt.show()

# GRAF 2: DISPERZIJA SVIJETOSTI U OVISNOSTI O VALNOJ DULJUNU

valna_duljina = np.linspace(400, 700, 300)

disp = disperzija(valna_duljina, 45, vrsni_kut_przme)

fig, ax = plt.subplots(figsize=(8,5))
norm = mpl.colors.Normalize(vmin=400, vmax=700)
cmap = plt.cm.nipy_spectral

# crtanje segment po segment (svaka boja = λ)
for i in range(len(valna_duljina) - 1):

    ax.plot(valna_duljina[i:i+2], disp[i:i+2], color=cmap(norm(valna_duljina[i])), linewidth=2)

ax.set_xlabel("Valna duljina λ (nm)")
ax.set_ylabel("Devijacija δ (°)")
ax.set_title("Disperzija svjetlosti na prizmi (Spektralni prikaz)")
ax.grid(True)
plt.show()


# GRAF 3: USPOREDBA MATERIJALA

materijali = {"Voda": 1.333, "Akril": 1.49, "Staklo": 1.52, "Flint staklo": 1.66}

ulazni_kutovi2 = np.linspace(1, 89, 500)

for key, value in materijali.items():
    kutovi2, delta = devijacija_prizme(ulazni_kutovi2, 60, value)

    plt.plot(kutovi2, delta, label=key)

plt.title("Utjecaj indeksa loma na devijaciju")
plt.xlabel("Upadni kut i (°)")
plt.ylabel("Devijacija δ (°)")
plt.legend()
plt.grid()
plt.show()

# GRAF 4: UTJECAJ VRŠNOG KUTA PRIZME

vrsni_kutovi = [30, 45, 60, 75]

upadni_kutovi = np.linspace(1, 80, 500)

for A in vrsni_kutovi:

    kutovi, devijacije = devijacija_prizme(upadni_kutovi,A,1.52)

    plt.plot(kutovi,devijacije,label=f"A = {A}°")

plt.title("Utjecaj vršnog kuta prizme na devijaciju")
plt.xlabel("Upadni kut i (°)")
plt.ylabel("Devijacija δ (°)")
plt.legend()
plt.grid()
plt.show()