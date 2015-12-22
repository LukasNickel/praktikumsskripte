import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat
import math
from scipy.optimize import curve_fit
Uc,U0,f1,a = np.genfromtxt('data/data.txt',unpack=True)
Urel=Uc/U0
L = 10.11*10**-3
C = 2.098*10**-9
R = 509.5
f=f1*1000
U1 = 1
w=2*np.pi*f
errphi = 2
erru = 0.05
errf = 50
x=np.linspace(0,40000, num=1000)
p = (2.1e-11, 1e-7, 1, 34000*2*np.pi, 1)

def g(y):
    return (U1/np.sqrt((1-L*C*y**2)**2+(y**2*R**2*C**2)))

def k(w,A,B,C,D,E):
    return(E/np.sqrt((1-A*(w-D)**2)**2+((w-D)**2*B**2))) + C

params, covariance = curve_fit(k,w,Urel,p0=p)

plt.xscale('log')
plt.xlim(4000, 50000)
plt.errorbar(f, Urel, xerr= errf, yerr=erru,fmt='o',label=r'Messwerte')
plt.plot(x,g(x*2*np.pi),'k-',label=r'Resonanzkurve aus Theorie')
print(params)
plt.plot(x,k(x*2*np.pi, params[0],params[1],params[2],params[3],params[4]),'r-', label=r'Fit')
plt.xlabel(r'$f$ [Hz]')
plt.ylabel(r'$U_{rel}$')
plt.legend(loc='best')
plt.savefig('5cfit.pdf')
plt.clf()
#print(1/np.sqrt((1-L*C*(2*np.pi*34000)**2)**2+((np.pi*2*34000)**2*R**2*C**2)))
