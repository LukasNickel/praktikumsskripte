import numpy as np
import matplotlib.pyplot as plt

phi, u, low, gain = np.genfromtxt('data\data3.txt', unpack=True)

plt.plot(phi, u, 'rx')
plt.ylabel('$U /$ V')
plt.xlabel('$\phi$ / deg')
plt.savefig('plot3u.pdf')

plt.clf()

plt.plot(phi, low, 'rx')
plt.ylabel('$Lowpass /$ ?')
plt.xlabel('$\phi /$ deg')
plt.savefig('plot3low.pdf')
print(phi)
