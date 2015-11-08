import numpy as np
import matplotlib.pyplot as plt

r, low, gain = np.genfromtxt('data\data4.txt', unpack = True)
x=np.linspace(6,186, num=100)
y=x*x

plt.plot(r, low/gain, 'ko', label=r'$Messwerte$')
plt.plot(x, 8.1/y,'b--', label=r'~$1/r^2$')
plt.ylabel(r'$Lowpass\ /\ \mathrm{V}$')
plt.xlabel(r'$r \ /\ \mathrm{cm}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot4.pdf')
plt.clf()
