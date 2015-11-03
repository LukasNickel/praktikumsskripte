import numpy as np
import matplotlib.pyplot as plt

phi, u, low, gain = np.genfromtxt('data\data3.txt', unpack=True)

plt.plot(phi, u, 'rx')
plt.savefig('plot3u.pdf')

plt.clf()

plt.plot(phi, low, 'b--')
plt.savefig('plot3low.pdf')
