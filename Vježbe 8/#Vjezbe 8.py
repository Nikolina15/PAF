#Vjezbe 8
import numpy as np
import matplotlib.pyplot as plt

def metoda_najmanjih_kvadrata(x,y):

    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xx = np.sum(x**2)
    sum_xy = np.sum(x*y)

    a = (n*sum_xy - sum_x*sum_y) / (n*sum_xx - sum_x**2)
    b = (sum_y - a*sum_x) / n

    y_fit = a*x + b

    #pogreska parametra

    sigma = np.sum((y - y_fit)**2)/(n-2)

    sigma_a = np.sqrt(n*sigma/(n*sum_xx - sum_x**2))
    sigma_b = np.sqrt(sum_xx*sigma/(n*sum_xx - sum_x**2))

    return a, b, sigma_a, sigma_b

def m_najmanjih_kvadrata_kroz_ishodiste(x,y):

    n = len(x)
    sum_xx = np.sum(x**2)
    sum_xy = np.sum(x*y)

    a = sum_xy/sum_xx

    y_fit = a*x

    #pogreska parametra
    sigma = np.sum((y-y_fit)**2)/(n-1)

    sigma_a = np.sqrt(sigma/sum_xx)

    return a, sigma_a

#Zad 1
# a)

h0 = 0.54 # m
m = 0.5257 # kg
r = 4.025e-3 # m
g = 9.81

h = np.array([0.14 , 0.17 , 0.19 , 0.22 , 0.25 , 0.28 , 0.31 , 0.34 , 0.37 , 0.40]) # m
t_mean = np.array([1.740 , 1.793 , 2.043 , 2.190 , 2.280 , 2.417 , 2.540 , 2.640 , 2.670 , 2.813]) # s

s = h

log_s = np.log10(s)
log_t = np.log10(t_mean)

a, b, sigma_a, sigma_b = metoda_najmanjih_kvadrata(log_t, log_s)

print(f"Nagib = {a:.3f} ± {sigma_a:.3f}")
print(f"Odsječak = {b:.3f} ± {sigma_b:.3f}")

t_fit = np.linspace(min(log_t), max(log_t), 100)   #lakse da mi se sirtiraju podatci
s_fit = a*t_fit + b

plt.scatter(log_t, log_s, label="Tocke mjerenja", color="red")
plt.plot(t_fit, s_fit, label = "Odgovarajuci pravac")
plt.title("log(s)- log(t) graf")
plt.xlabel("log(t)")
plt.ylabel("log(s)")
plt.legend()
plt.grid()
plt.show()

#b)

t2 = t_mean**2

a2, sigma_a2 = m_najmanjih_kvadrata_kroz_ishodiste(t2, s)

print(f"Nagib = {a2:.3f} ± {sigma_a2:.3f}")

t2_fit = np.linspace(min(t2), max(t2), 100)
s2_fit = a2*t2_fit

plt.scatter(t2, s, label="Tocke mjerenja", color="red")
plt.plot(t2_fit, s2_fit, label="Odgovarajuci pravac")
plt.title("s-t² graf")
plt.xlabel("t²")
plt.ylabel("s")
plt.legend()
plt.grid()
plt.show()

# c)moment tromosti

a_ef = 2*a2
sigma_a_ef = 2*sigma_a2

Iz = ((m*g*(r**2))/a_ef) - m*(r**2)
sigma_Iz = ((m*g*(r**2))/a_ef**2)*sigma_a_ef

print(f"Moment tromosti = {Iz:.3f} ± {sigma_Iz}")