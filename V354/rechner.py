import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat
import math
from scipy.optimize import curve_fit

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
print(urelminus)
print(urelplus)
print(q)
print(q1/q)
