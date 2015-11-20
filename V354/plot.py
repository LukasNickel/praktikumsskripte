import matplotlib.pyplot as plt
import numpy as np


Uc, U0, f, a = np.genfromtxt('data/data.txt', unpack=True)
phi = a*f
print(phi)

plt.plot(f, phi, 'kx', label='Messwerte')
plt.ylabel(r'$Phi \ / \ \mathrm{deg}$')
plt.xlabel(r'$f \ / \ \mathrm{kHz}$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('build/plot.pdf')
