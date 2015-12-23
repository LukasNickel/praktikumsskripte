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
errphi = 0.01
erru = 0.05
errf = 500
p1=ufloat(108.86,0.005)
p2=ufloat(125.86, 0.005)
p3=ufloat(141.12,0.005)
f1=36000
f2=38000
f3=40000
x=np.linspace(4000,40500, num=1000)
p1=(2, 1.009138e-07, 2.1210779999999998e-11,0)

def g():
    return (-np.arctan(-w*R*C/(1-L*C*w**2)))
    #return(np.arctan(f))

def k(y,A,B,C,D):
    return(A*np.arctan(B*(y-C))+D)

def m(y,A1,RC,LC,b):
    return(A1*np.arctan((-y*RC)/(1-LC*y**2))+b)

#params, covariance = curve_fit(k,w,phi)
#print(params)
params2, covariance2 = curve_fit(m,w,phi,p0=p1)
print(params2)

plt.errorbar(f, phi, xerr= errf, yerr=errphi,fmt='o',label=r'Messwerte')
#plt.plot(f,phi,'rx', label=r'Messwerte')
plt.plot(f,g(),'k-', label=r'Theorie')

#plt.plot(x,k(x*2*np.pi, params[0],params[1],params[2],params[3]),'r-', label=r'Fit')

plt.plot(x,m(x*2*np.pi, params2[0],params2[1],params2[2],params2[3]),'r-', label=r'Fit')

plt.xscale('log')
plt.ylabel(r'$\phi$ [deg]')
plt.xlabel(r'$f$ [Hz]')
plt.legend(loc='best')
plt.savefig('5d.pdf')
plt.clf()
