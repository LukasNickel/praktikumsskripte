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
R = 48.1
f=f1*1000
U1 = 1.44
f0=34000
my=ufloat(784,27)
R1=ufloat(48.1,0.1)
Runc = ufloat(48.1, 0.1)

u0=ufloat(1.38,0.005)
umax=ufloat(5.52,0.005)
uminus=ufloat(4.28,0.005)
uplus=ufloat(4.08,0.005)
wplus=ufloat(38,1)
wminus=ufloat(30,1)
wres = ufloat(34,1)
u0plus=ufloat(1.44,0.005)
u0minus=ufloat(1.52,0.005)
q1 = ufloat(4,0.015)

urelminus = uminus/u0minus
urelplus = uplus / u0plus
q = wres/(wplus-wminus)


print(L*C)
