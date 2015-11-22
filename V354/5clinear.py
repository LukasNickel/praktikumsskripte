import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat
import math
from scipy.optimize import curve_fit

Uc,U0,f,a = np.genfromtxt('data/5c2.txt', unpack=True)
Urel=Uc/U0
a2 = a*10**-6
f2=f*1000
phi = a*f*360/1000
x=np.linspace(4260,40000,num=100)

print(phi)
plt.plot(f2,Urel,'rx',label='Messwerte')
plt.xlabel(r'$f$ [Hz]')
plt.ylabel(r'$U_{rel}$')
plt.legend(loc='best')
plt.savefig('5c2.pdf')
plt.clf()
plt.plot(f*1000,phi,'rx', label=r'Messwerte')
plt.axhline(y=45,xmin=0,xmax=1,label=r'$\phi = 45$°', color='b')
plt.axhline(y=90,xmin=0,xmax=1,label=r'$\phi = 90$°', color='k')
plt.axhline(y=135,xmin=0,xmax=1,label=r'$\phi = 135$°', color='c')
plt.axvline(x=30000,ymin=0,ymax=1,label=r'$f=30$kHz', color='y')
plt.axvline(x=39000,ymin=0,ymax=1,label=r'$f=39$kHz', color='g')
plt.ylabel(r'$\phi$ [deg]')
plt.xlabel(r'$f$ [Hz]')
plt.legend(loc='best')
plt.savefig('5d2.pdf')
plt.clf()


L = ufloat(10.11*10**-3, 0.03*10**-3)
C = ufloat(2.098*10**-9, 0.006*10**-9)
R1 = ufloat(48.1, 0.1)
R2 = ufloat(509.5, 0.5)
R3 = ufloat(4390.4, 9)
q=1/R2*unp.sqrt(L/C)
print(R2/L)
print(R3/L)
