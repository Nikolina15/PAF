#Zadatak 1
# (a) Oduzmite 5.0 i 4.935. Koji rezultat očekujete? Koji rezultat dobijete koristeći Python? Objasnite.
# (b) Provjerite iznosi li suma brojeva 0.1, 0.2 i 0.3 broj 0.6. Objasnite rezultat koji ste dobili.

#Oduzimanje
ocekivano = 0.065
python_rj = 5.0 - 4.935
print(f"Oduzimanje\n  Ocekivano : {ocekivano} \n  Rjesenje u pythonu: {python_rj}") 

#Suma
ocekivano2 = 0.6
python_rj_zbroj = 0.1+0.2+0.3
print(f"Suma\n  Ocekivano : {ocekivano2} \n  Rjesenje u pythonu:{python_rj_zbroj}") 


# Python u memoriji zapisuje brojeve koristeci binarni zapis. Vecina decimalnih brojeva se ne mogu tocno
# prikazati pomocu binarnog sustava, zbog toga dolazi do malih gresaka kao u primjeru. 