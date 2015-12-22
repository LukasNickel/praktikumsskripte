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
phi = a*f*2*np.pi/1000/1000
w=2*np.pi*f

print(phi)
def g():
    return (-np.arctan(-w*R*C/(1-L*C*w**2)))
    #return(np.arctan(f))
p1=ufloat(108.86,0.005)
p2=ufloat(125.86, 0.005)
p3=ufloat(141.12,0.005)
f1=36000
f2=38000
f3=40000

plt.plot(f,phi,'rx', label=r'Messwerte')
plt.plot(f,g(),'k-', label=r'Theorie')

plt.xscale('log')
plt.ylabel(r'$\phi$ [deg]')
plt.xlabel(r'$f$ [Hz]')
plt.legend(loc='best')
plt.savefig('5d.pdf')
plt.clf()
