import matplotlib.pyplot as plt
import numpy as np
import particle as p

p1 = p.Particle(10, 45, 0, 0)
#print(p1.range())
numericko = p1.range()

v0 = 10
theta = np.radians(45)
g = 9.81
domet = ((v0**2)*np.sin(2*theta))/g
analiticko = domet
#print(domet)

odstupanje = abs(numericko - analiticko)        #abs() - apsolutna vrijednost

print(f"Analiticko rijesenje je {analiticko}")
print(f"Numericko rijesenje je {numericko}")
print(f"Odstupanje je {odstupanje}")