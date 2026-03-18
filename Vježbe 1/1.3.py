# Napišite program koji će korisnika tražiti da upiše (x, y) koordinate za dvije točke. 
# Ako korisnik pogriješi prilikom unosa koordinate opomenite ga da ponovi upis. Nakon što je korisnik uspješno upisao dvije koordinate
# ispišite na ekran jednadžbu pravca koji prolazi kroz te dvije točke.

import matplotlib.pyplot as plt
import numpy as np
import math

while True:
    try:
        print("Upiši koordinate za prvu točku.")
        x1 = int(input("Upiši x koordinatu: "))
        y1 = int(input("Upiši y koordinate: "))
        break
    except ValueError:
        print("Pogrešan unos! Upišite broj!")

while True:
    try:
        print("Upiši koordinate za drugu točku.")
        x2 = int(input("Upiši x koordinatu: "))
        y2 = int(input("Upiši y koordinate: "))
        break
    except ValueError:
        print("Pogrešan unos! Upišite broj!")

# jed. pravca je y = k*x + l

if x1 == x2:
    print("Pravac je vertikalan na x os")
    print(f"Jednadžba pravca je x = {x1}")
elif y1 == y2:
    print("Pravac je horizontalan s osi x")
    print(f"Jednadzba pravca je y = {y1}")
else:
    k = round((y2 - y1)/(x2 - x1))
    l = round(y1 - (k*x1))
    print(f"Jednadžba pravaca je y = {k}x + {l}")