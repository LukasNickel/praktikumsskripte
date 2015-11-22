import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat
import math
from scipy.optimize import curve_fit

Uc,U0,f,a = np.genfromtxt('data/data.txt', unpack=True)
Urel=Uc/U0
phi = a*f*360/1000

plt.plot(f*1000,Urel,'rx',label=r'$Messwerte$')
plt.xscale('log')
plt.xlabel(r'$f$ [Hz]')
plt.ylabel(r'$U_{rel}$')
plt.legend(loc='best')
plt.savefig('5c.pdf')
plt.clf()
plt.plot(f*1000,phi,'rx', label=r'Messwerte')
plt.xscale('log')
plt.ylabel(r'$\phi$ [deg]')
plt.xlabel(r'$f$ [Hz]')
plt.legend(loc='best')
plt.savefig('5d.pdf')
plt.clf()
