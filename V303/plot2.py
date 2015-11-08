import numpy as np
import matplotlib.pyplot as plt


phi, u, low, gain = np.genfromtxt('data\data2.txt', unpack=True)
x=np.linspace(0,360, num=360)

plt.plot(phi, u, 'rx', label=r'$Messwerte$')
plt.ylabel(r'$U \ / \ \mathrm{V}$')
plt.xlabel(r'$\phi \ / \ \mathrm{deg}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot2u.pdf', bbox_inches='tight', pad_inches=0)


plt.clf()

plt.plot(phi, low, 'rx', label=r'$Messwerte$')
plt.plot(x,np.cos(x/360*2*np.pi)*3,label=r'$3cos(\phi)$')
plt.ylabel(r'$Lowpass\ /\ \mathrm{V}$')
plt.xlabel(r'$\phi \ /\ \mathrm{deg}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('plot2low.pdf')
