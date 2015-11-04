import numpy as np
import matplotlib.pyplot as plt

phi, u, low, gain = np.genfromtxt('data\data2.txt', unpack=True)

plt.plot(phi, u, 'rx')
plt.ylabel('$U /$ V')
plt.xlabel('$\phi$ / deg')
plt.savefig('plot2u.pdf')

plt.clf()

plt.plot(phi, low, 'rx')
plt.ylabel('$Lowpass /$ ?')
plt.xlabel('$\phi /$ deg')
plt.savefig('plot2low.pdf')
