import sympy
import numpy as np

def error(f, err_vars=None):
    from sympy import Symbol, latex
    s = 0
    latex_names = dict()

    if err_vars == None:
        err_vars = f.free_symbols

    for v in err_vars:
        err = Symbol('latex_std_' + v.name)
        s += f.diff(v)**2 * err**2
        latex_names[err] = '\\sigma_{' + latex(v) + '}'

    return latex(sympy.sqrt(s), symbol_names=latex_names)

w, l, k, g, t1, t2= sympy.var('\omega l K g T_+ T_-')

w = sympy.sqrt(g/l)
T = 2*sympy.pi*sympy.sqrt(l/g)
T2 = 2*sympy.pi/sympy.sqrt(g/l+2*K/l)
k = (t1**2-t2**2)/(t1**2+t2**2)
T3 = (t1*t2)/(t1-t2)
print(error(w))
print()
print(error(T))
print()
print(error(k))
print()
print((error(T3)))
