import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat
import math
from scipy.optimize import curve_fit

t,U = np.genfromtxt('data/f.txt', unpack=True)
x=np.linspace(-0.0000206, 0.00028240, num=1000)
def f(x, a,b):
    return b*np.exp(-a*x)

popt,pcov = curve_fit(f, t, np.fabs(U))

plt.plot(t,U,'kx')
print(popt)
plt.plot(x,f(x,popt[0],popt[1]), 'r-')
plt.savefig('plot5a.pdf')
plt.clf
