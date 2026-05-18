import math

brojevi = []

print("Unesi 10 brojeva:")

for i in range(10):
    x = float(input(f"Broj {i+1}: "))
    brojevi.append(x)


#Aritmeticka sredina

suma = 0

for i in brojevi:
    suma += i

aritm_sredina = suma / len(brojevi)

#Standardna devijacija

suma_kvadrata = 0

for i in brojevi:
    suma_kvadrata += (i - aritm_sredina)**2

sigma = math.sqrt(suma_kvadrata/(len(brojevi)*(len(brojevi)-1)))

print(f"Aritmeticka sredina: {aritm_sredina}")
print(f"Standardna devijacija: {sigma}")


#Korištenje gotovih modula (statistics)

import statistics

#Aritmeticka sredina
a_s = statistics.mean(brojevi)

#Standardna devijacija
s_d = statistics.stdev(brojevi)     # koristi u nazivniku samo n-1

print("Koristenjem gotovih modula")
print(f"    Aritmeticka sredina: {a_s}")
print(f"    Standardna devijacija: {s_d}")