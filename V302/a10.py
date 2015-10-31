import numpy as np
r2,r3,r4 = np.genfromtxt('V302a10.txt', unpack=True)
rx=r2*r3/r4
print(rx)
rxm=sum(rx)/len(rx)
print(rxm)
