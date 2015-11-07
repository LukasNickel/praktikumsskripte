import numpy as np
import matplotlib.pyplot as plt


phi, u, low, gain = np.genfromtxt('data\data2.txt', unpack=True)

plt.plot(phi, u, 'rx')
plt.ylabel('$U /$ V')
plt.xlabel('$\phi$ / deg')
plt.tight_layout(pad=0)
plt.savefig('plot2u.pdf', bbox_inches='tight', pad_inches=0)


plt.clf()

plt.plot(phi, low, 'rx')
plt.ylabel('$Lowpass /$ ?')
plt.xlabel('$\phi /$ deg')
plt.savefig('plot2low.pdf')
