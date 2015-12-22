import numpy as np
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
from uncertainties import ufloat
import math
from scipy.optimize import curve_fit

unc1 = (0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001)
unc2 = (0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,0.01,0.01,0.01)
unc3 = (0.005/3, 0.005/3,0.005/3, 0.005/3,0.005/3, 0.005/3,0.005/3, 0.005/3,0.005/3)
unc4 = (0.001,0.001,0.001,0.001,0.001)
Tung1 = unp.uarray(np.genfromtxt('data/l2/Tungekoppelt1.txt', unpack = True)/5, unc1)
Tung2 = unp.uarray(np.genfromtxt('data/l2/Tungekoppelt2.txt', unpack = True)/5, unc1)
Tplus = unp.uarray(np.genfromtxt('data/l2/Tplus.txt', unpack = True)/5, unc1)
Tminus = unp.uarray(np.genfromtxt('data/l2/Tminus.txt', unpack = True)/5, unc1)
Tgek1 = unp.uarray(np.genfromtxt('data/l2/Tgekoppelt1.txt', unpack = True)/5, unc4)
Tgek2 = unp.uarray(np.genfromtxt('data/l2/Tgekoppelt2.txt', unpack = True)/3, unc3)
Tgek = np.append(Tgek1, Tgek2)
Tschwebung = unp.uarray(np.genfromtxt('data/l2/Tschwebung.txt', unpack = True)*2, unc2)
l = ufloat(0.502, 0.005)
K = ((Tplus.sum()/10)**2 - (Tminus.sum()/10)**2) / ((Tminus.sum()/10)**2 + (Tplus.sum()/10)**2)
Ttheorie = unp.sqrt(l/9.81)*2*np.pi
Tminustheorie = 2*np.pi/(unp.sqrt(9.81/l + 2*K/l))
Tschwebungtheorie = (Tplus.sum()/10)*(Tminus.sum()/10)/((Tplus.sum()/10)-(Tminus.sum()/10))

print(1-(Tschwebungtheorie)/(Tschwebung.sum()/14))

print('Kopplungskonstante aus T+ und T- errechnet:')
print(K)
#print((unp.sqrt(9.81/l + 2*K/l)))
#print(unp.sqrt(l/9.81)**-1)
print('Mittelwert der Schwingungsdauer des ersten Pendels:' )
print(Tung1.sum()/10)

print('Mittelwert der Schwingungsdauer des zweiten Pendels:' )
print(Tung2.sum()/10)

print('Mittelwert der Schwingungsdauer der phasengleichen Schwingung:' )
print(Tplus.sum()/10)

print('Theoriewert für Schwingungsdauer der einzelnen Pendel sowie phasengleicher Schwingung:')
print(Ttheorie)

print('Mittelwert der Schwingungsdauer der gegenphasigen Schwingung:' )
print(Tminus.sum()/10)
print('Theoriewert für Schwingungsdauer der gegenphasigen Schwingung:')
print(Tminustheorie)

print('Mittelwert der Schwingungsdauer bei gekoppelter Schwingung:' )
print(Tgek.sum()/14)

print('Mittelwert der Schwebungsdauer bei gekoppelter Schwingung:' )
print(Tschwebung.sum()/14)
print('Theoriewert für Schwebungsdauer:')
print(Tschwebungtheorie)
