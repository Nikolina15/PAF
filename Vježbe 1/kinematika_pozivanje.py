#nastavak za Gibanje zadatak 2

from kinematika import jednoliko_gibanje

F = float(input("Upiši iznos sile[N]: "))
m = float(input("Upiši masu[kg]: "))
v0 = float(input("Upiši pocetnu brzinu[m/s]: "))
s0 = float(input("Upiši pocetni put[m]: "))
t = float(input("Upiši vrijeme promatranog gibanja [s]: "))

jednoliko_gibanje(F, m, v0, s0, t)