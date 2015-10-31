import numpy as np
import uncertainties.unumpy as unp
c4,r2,r3,r4 = np.genfromtxt('V302d18.txt', unpack=True)
#rx=r2*r3/r4
#print(rx)
#print(sum(rx)/len(rx))
#print('mit uncertainties:')
r2err=r2*0.03
r3err=r3*0.03
r4err=r4*0.03
r2unc=unp.uarray(r2, r2err)
r3unc=unp.uarray(r3, r3err)
r4unc=unp.uarray(r4, r4err)
rxunc=r2unc*r3unc/r4unc
lxunc=r2unc*r3unc*c4
print('rx: ')
print(rxunc)
print(sum(rxunc)/len(rxunc))
print('lx: ')
print(lxunc)
print(sum(lxunc)/len(lxunc))
