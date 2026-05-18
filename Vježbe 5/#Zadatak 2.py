#Zadatak 2
# Napišite funkciju koja uzima broj iteracija N te N puta zbraja 1/3 pa zatim N puta oduzima 1/3 broju 5.
# Ispišite konačni rezultat za 200, 2000 i 20000 iteracija. Objasnite rezultat koji ste dobili.

N1 = 200
N2 = 2000
N3 = 20000

a = 1/3
b = 5

def zbroj(broj, N):
    zbroj = 0
    for i in range(N):
        zbroj += broj
    
    return zbroj

def oduzimanje(umanjenik, umanjitelj, N):
    for i in range(N):
        umanjenik -= umanjitelj
    
    return umanjenik

zbroj_N1 = zbroj(a, N1)
zbroj_N2 = zbroj(a, N2)
zbroj_N3 = zbroj(a, N3)

razlika_N1 = oduzimanje(b, a, N1)
razlika_N2 = oduzimanje(b, a, N2)
razlika_N3 = oduzimanje(b, a, N3)

print(f"Zbroj:\n    za N = 200: {zbroj_N1}\n    za N = 2000: {zbroj_N2}\n    za N = 20000: {zbroj_N3}")
print(f"Razlika:\n    za N = 200: {razlika_N1}\n    za N = 2000: {razlika_N2}\n    za N = 20000: {razlika_N3}")


# Obajsnjenje zadatka:
# računala ne pohranjuju decimalne brojeve potpuno točno (binarni zapis)
# numeričke pogreške rastu s brojem operacija