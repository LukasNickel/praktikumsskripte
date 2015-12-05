import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat
import math
from scipy.optimize import curve_fit

Uc,U0,f,a = np.genfromtxt('data/data.txt', unpack=True)
Urel=Uc/U0
phi = a*f*360/1000
errphi = 2
erru = 0.05
errf = 500


#plt.plot(f*1000,Urel,'rx',label=r'Messwerte')
plt.errorbar(f*1000, Urel, xerr= errf, yerr=erru,fmt='o',label=r'Messwerte')
plt.xlim(4000, 50000)
plt.ylim(0,4.1)
plt.xscale('log')
plt.xlabel(r'$f$ [Hz]')
plt.ylabel(r'$U_{rel}$')
plt.legend(loc='best')
plt.savefig('5c.pdf')
plt.clf()


#plt.plot(f*1000,phi,'rx', label=r'Messwerte')
plt.errorbar(f*1000, phi, xerr= errf, yerr=errphi,fmt='o',label=r'Messwerte')
plt.xlim(4000, 100000)
plt.ylim(0,160)
plt.xscale('log')
plt.ylabel(r'$\phi$ [deg]')
plt.xlabel(r'$f$ [Hz]')
plt.legend(loc='best')
plt.savefig('5d.pdf')
plt.clf()
