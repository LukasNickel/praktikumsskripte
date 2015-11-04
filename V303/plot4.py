import numpy as np
import matplotlib.pyplot as plt

r, low, gain = np.genfromtxt('data\data4.txt', unpack = True)

plt.plot(r, low/gain, 'rx')
plt.ylabel('Tiefpass/???')
plt.xlabel('$r /$ cm')
plt.savefig('plot4.pdf')
plt.clf()
