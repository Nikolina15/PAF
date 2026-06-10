#zad 2 uz pomoc AI-a
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

kut_deg = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])

T_120 = np.array([0.8020 , 0.8187 , 0.8327 , 0.8660 , 0.8980 , 0.9153 , 0.9293 , 0.9653 ,
 0.9747 , 1.0200 , 1.0373 , 1.1160 , 1.1780 , 1.2733 , 1.4180 , 1.6373 , 1.9100 ,
2.5460])

T_240 = np.array([1.0140 , 1.0320 , 1.0433 , 1.0673 , 1.0840 , 1.1320 , 1.1440 , 1.1720 , 
1.1980 , 1.2293 , 1.2813 , 1.3573 , 1.4200 , 1.5600 , 1.7413 , 1.9840 , 2.4473 ,
3.1573])

g = 9.81

kut_rad = np.radians(kut_deg)

#teorijski
def period(theta, l):
    T = 2*np.pi*np.sqrt(l/(g*np.cos(theta)))
    return T

#njihalo 120mm

popt, pcov = curve_fit(period, kut_rad, T_120, p0=[0.12])      # popt -> optimalan parametar (l)

l_fit_120 = popt[0]
sigma_l_120 = np.sqrt(pcov[0,0])

print(f"l = {l_fit_120:.5f} ± {sigma_l_120:.5f} m")

l_teor_120 = 0.120

rel_pog_120 = abs(l_fit_120-l_teor_120)/l_teor_120*100

print(f"Relativna pogreška = {rel_pog_120:.2f}%")

kut_glatko_120 = np.linspace(0, 85, 200)
kut_glatko_rad_120 = np.radians(kut_glatko_120)
T_fit_120 = period(kut_glatko_rad_120, l_fit_120)

plt.scatter(kut_deg, T_120, label="Mjerenja", color="red")
plt.plot(kut_glatko_120, T_fit_120, label="curve_fit")
plt.xlabel("Kut [°]")
plt.ylabel("Period [s]")
plt.title("Fizikalno njihalo L=120 mm")
plt.grid()
plt.legend()
plt.show()

#njihalo 240mm

popt, pcov = curve_fit(period, kut_rad, T_240, p0=[0.24])      # popt -> optimalan parametar (l)

l_fit_240 = popt[0]
sigma_l_240 = np.sqrt(pcov[0,0])

print(f"l = {l_fit_240:.5f} ± {sigma_l_240:.5f} m")

l_teor_240 = 0.240

rel_pog_240 = abs(l_fit_240-l_teor_240)/l_teor_240*100

print(f"Relativna pogreška = {rel_pog_240:.2f}%")

kut_glatko_240 = np.linspace(0, 85, 200)
kut_glatko_rad_240 = np.radians(kut_glatko_240)
T_fit_240 = period(kut_glatko_rad_240, l_fit_240)

plt.scatter(kut_deg, T_240, label="Mjerenja", color="red")
plt.plot(kut_glatko_240, T_fit_240, label="curve_fit")
plt.xlabel("Kut [°]")
plt.ylabel("Period [s]")
plt.title("Fizikalno njihalo L=240 mm")
plt.grid()
plt.legend()
plt.show()
