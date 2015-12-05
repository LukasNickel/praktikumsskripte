import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat
import math
from scipy.optimize import curve_fit


phi, u, low, gain = np.genfromtxt('data\data2.txt', unpack=True)
x=np.linspace(0,360, num=360)

plt.plot(phi, u, 'ko', label=r'$Messwerte$')
plt.ylabel(r'$U_{out} \ / \ \mathrm{V}$')
plt.xlabel(r'$\phi \ / \ \mathrm{deg}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot2u.pdf', bbox_inches='tight', pad_inches=0)


plt.clf()

plt.plot(phi, low, 'ko', label=r'$Messwerte$')
plt.plot(x,np.cos(x/360*2*np.pi)*3,label=r'$3cos(\phi)$')
plt.ylabel(r'$U_{out}\ /\ \mathrm{V}$')
plt.xlabel(r'$\phi \ /\ \mathrm{deg}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot2low.pdf')
