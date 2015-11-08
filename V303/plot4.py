import numpy as np
import matplotlib.pyplot as plt

r, low, gain = np.genfromtxt('data\data4.txt', unpack = True)

plt.plot(r, low/gain, 'rx', label=r'$Messwerte$')
plt.ylabel(r'$Lowpass\ /\ \mathrm{V}$')
plt.xlabel(r'$r \ /\ \mathrm{cm}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot4.pdf')
plt.clf()
