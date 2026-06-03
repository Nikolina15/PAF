#Vjezbe 7 uz pomoc AI-a
import numpy as np
import matplotlib.pyplot as plt

np. random . seed (42)
mase_ciste = np.random.normal(loc =2.06 , scale =0.05 , size =57).tolist()
mase = mase_ciste + [6.0 , 1.2 , 3.2 , 4.5 , 8.5 , 7.8 , 0.08 , 0.02] # pogreske pri redukciji podataka

#1 zad.
def histogram(podatci, k):
    min_p = min(podatci)
    max_p = max(podatci)

    h = (max_p-min_p)/k

    frekv = [0]*k   #lista s nulama za popunit
    rubovi = []
    
    for i in range(k+1):
        rubovi.append(min_p + (i*h))

    for x in podatci:            
        index = int((x-min_p)/h)
        if index == k:
            index = k-1
        
        frekv[index] += 1
    
    for i in range(k):
        print(f"[{rubovi[i]:.3f}, {rubovi[i+1]:.3f}) : {frekv[i]}")

    return rubovi, frekv

rubovi, frekvencija = histogram(mase_ciste, 10)

sirina = rubovi[1] - rubovi[0]

plt.bar(rubovi[:-1], frekvencija, width=sirina, edgecolor="black", align="edge")
plt.xlabel("Masa")
plt.ylabel("Broj mjerenja")
plt.title("Histogram masa Sirius A")
plt.show()


#zad 2 gotovi moduli

k = 10
#k2 = 5

#aritmeticka sredina
sredina = np.mean(mase_ciste)
#medijan
medijan_np = np.median(mase_ciste)

plt.hist(mase_ciste, bins=k, edgecolor="black", color="red")
plt.axvline(sredina, color="blue", label="Sredina")
plt.axvline(medijan_np, color="green", label="Medijan")
plt.xlabel("Masa")
plt.ylabel("Broj mjerenja")
plt.title("Histogram koristeci gotove module")
plt.legend()
plt.show()

#usporedba frekvencija
n, bins, patches = plt.hist(mase_ciste, bins=10)   # n=frekv, bins=rubovi, patches= stupci u grafu

print("Frekvencije iz zad.1")
print(frekvencija)

print("Fekvencije iz zad.2") #plt.hist() vraca numpy array vraca elemente tipa float
print(n)


#zad 3 funkcija za racunanje medijana

def medijan(podatci):
    sortirani_pod = sorted(podatci)
    n = len(sortirani_pod)

    if n % 2 == 0:
        return ((sortirani_pod[int(n/2)-1] + sortirani_pod[int(n/2)]) /2)       #po indekcima trazis sredinu 
    else:
        return sortirani_pod[int(n/2)]      
    
a = [3,1,4,1,5,9,2,6]       #paran
b = [3,1,4,1,5,9,2,6,5]     #neparan

print(f"Medijan a = {medijan(a)}")
print(f"Medijan b = {medijan(b)}")

moj_medijan = medijan(mase)
np_medijan = np.median(mase)

print(f"Medijan = {moj_medijan}")
print(f"NumPy medijan = {np_medijan}")


#4 zadatak

#aritmeticka sredina i medijan za sve podatke
a_sredina1 = np.mean(mase)
medijan1 = medijan(mase)
razlika1 = abs(a_sredina1-medijan1)

print("Za sve podatke:")
print(f"    Aritmeticka sredina = {a_sredina1:.3f}")
print(f"    Medijan = {medijan1:.3f}")
print(f"    Razlika = {razlika1:.3f}")

# bez velikih odstupanja

#mase_ciste = np.random.normal(loc =2.06 , scale =0.05 , size =57).tolist()
# tocke su raspodjeljene oko 2.06
# standardna devijacija je 0.05
# granice min i max iz mase_ciste!!!

mase2 = []

for x in mase:
    if min(mase_ciste) < x < max(mase_ciste):
        mase2.append(x)

a_sredina2 = np.mean(mase2)
medijan2 = medijan(mase2)
razlika2 = abs(a_sredina2-medijan2)

print("Za vrijednosti bez znacajnog odstupanja:")
print(f"    Aritmeticka sredina = {a_sredina1:.3f}")
print(f"    Medijan = {medijan1:.3f}")
print(f"    Razlika = {razlika1:.3f}")

razlika_sredine = abs(a_sredina1 - a_sredina2)
promjena_m = abs(medijan1 - medijan2)

print(f"Promjena sredine = {razlika_sredine:.3f}")
print(f"Promijena medijana = {promjena_m:.3f}")

plt.hist(mase, bins=10, edgecolor= "black", color="green")

plt.axvline(a_sredina1, label="Sredina (sve)", color="blue")
plt.axvline(medijan1, label="Medijan (sve)", color="lightblue")

plt.axvline(a_sredina2, label="Sredina (bez odstupanja)", color="pink")
plt.axvline(medijan2, label="Medijan (bez odstupanja)", color= "lightpink")

plt.xlabel("Masa")
plt.ylabel("Broj mjerenja")
plt.title("Utjecaj odstupajućih vrijednosti")

plt.legend()
plt.show()