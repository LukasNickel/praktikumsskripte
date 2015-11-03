import numpy as np
import matplotlib.pyplot as plt

phi, u, low, gain = np.genfromtxt('data\data2.txt', unpack=True)

plt.plot(phi, u, 'rx')
plt.savefig('plot2u.pdf')

plt.clf()

plt.plot(phi, low, 'b--')
plt.savefig('plot2low.pdf')
