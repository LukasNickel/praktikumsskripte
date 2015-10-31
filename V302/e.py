import numpy as np
import matplotlib.pyplot as plt

us, v, ubr = np.genfromtxt('V302e.txt', unpack=True)

plt.plot(v, ubr, 'rx')
plt.savefig('plote.pdf')
