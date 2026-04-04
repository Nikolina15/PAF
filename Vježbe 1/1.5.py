#Unaprijedite kod iz prethodnog zadatka koristeći modul matplotlib.pyplot tako da nacrtate 
#unesene koordinate i pravac koji prolazi kroz njih. Ponudite u funkciji opciju da se graf prikaže na ekranu ili da se spremi
#kao PDF. Dopustite korisniku da bira ime pod kojim će se spremiti graf.

import matplotlib.pyplot as plt
import numpy as np

def jednadžba_pravca(x1, y1, x2, y2, opcija):
    if x1 == x2:
        print(f"Jenadžba pravca je x = {x1}")
        plt.scatter([x1, x2], [y1, y2])
        plt.axvline(x=x1)

    else: 
        k = round((y2-y1)/(x2-x1))
        l = round(y1-(k*x1))
        print(f"Jednadžba pravac je y = {k}x + {l}")
        x = [x1, x2]
        y = [k*x1 + l, k*x2 + l]

        plt.scatter([x1, x2], [y1, y2])
        plt.plot(x, y)

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Prikaz prvaca kroz dvije točke")

    if opcija == "PRIKAŽI":
        plt.show()

    elif opcija == "SPREMI":
        ime = input("Unesite ime datoteke: ")
        plt.savefig(ime + ".pdf")
        print(f"Graf je spremljen kao {ime}.pdf")

x1 = int(input("unsi x koordinatu prve točke: "))
y1 = int(input("unsi y koordinatu prve točke: "))
x2 = int(input("unsi x koordinatu druge točke: "))
y2 = int(input("unsi y koordinatu druge točke: "))

opcija = input("Upiši PRIKAŽI za prikazati graf ili SPREMI za spremiti graf kao PDF: ")

jednadžba_pravca(x1, y1, x2, y2, opcija)