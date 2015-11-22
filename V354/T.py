import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat
import math
L = ufloat(10.11*10**-3, 0.03*10**-3)
C = ufloat(2.098*10**-9, 0.006*10**-9)
R1 = ufloat(48.1, 0.1)
R2 = ufloat(509.5, 0,5)
T1 = (1/L/C - (R1**2)/4/(L**2))
print(T1)
T2=unp.sqrt(T1)
print(T2)
print(2*np.pi/T2)
print(1/1.35/(10**3))
print(1/(2*np.pi/T2))
print(1/(1/(2*np.pi/T2)))

R=unp.sqrt(4*L/C)
print('R:')
print(R)
print(R/L)
print(1/unp.sqrt(L*C))
