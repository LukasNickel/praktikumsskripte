import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

r, low, gain = np.genfromtxt('data\data4.txt', unpack = True)
x=np.linspace(6,186, num=100)
y=x*x
low2=low/gain-(0.2/1000)
lnr = np.log(r)
lnu = np.log(low2)

def f(lnr, a,b):
    return a*r+b

def g(x,c,d):
    return c*x**d

#popt, pcov = curve_fit(g,r, low2, p0=(5,-2))

#print(popt)
#print(pcov)

plt.plot(r, low2, 'ko', label=r'$Messwerte$')
#plt.plot(x, g(x,popt[0],popt[1],popt[2]), 'r-', label='Fit')
plt.plot(x,g(x,5.288,-1.876),label='Fit')

plt.xscale('log')
plt.yscale('log')
plt.ylabel(r'$U_{out}\ /\ \mathrm{V}$')
plt.xlabel(r'$r \ /\ \mathrm{cm}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot4.pdf')
plt.clf()
