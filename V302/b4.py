import numpy as np
import uncertainties.unumpy as unp
c2,r2,r3,r4 = np.genfromtxt('V302b4.txt', unpack=True)
#rx=r2*r3/r4
#print(rx)
#print(sum(rx)/len(rx))
#print('mit uncertainties:')
r34=r3/r4
r34err=r34*0.005
r34unc=unp.uarray(r34, r34err)
cxunc=c2/r34unc
print(cxunc)
print(sum(cxunc)/len(cxunc))
