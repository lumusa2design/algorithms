import sympy as sp
from auxiliar_functions import distance

def muller_method(func, x0, fail,NiterMax=1000, TOL=1e-9):
    x = sp.symbols('x')
    f_sym = x ** 3 - 4 * x + 1
    fx0 = f_sym.subs(x, x0)
    for i in range(0, NiterMax):
        if fx0 == 0:
            return NiterMax
        diff_fx0 = sp.diff(f_sym, x).subs(x, x0)
        second_diff = sp.diff(f_sym, x, 2).subs(x, x0)
        z1, z2 = polinomios(second_diff/2, diff_fx0, fx0)
        if z1 == 0:
            return fail
        x1 = x0 + z1
        if distance(x0, x1) < TOL:
            x0 = x1
            return x0
        x0 = x1
        fx0 = f_sym.subs(x, x0)
    return -1



def polinomios(a,b,c):
    if a == 0:
        return 0, 0
    dis = b*b - 4*a*c
    if dis < 0:
        return 0, 0
    if dis == 0:
        return 1, 1
    if b > 0:
        z1, z2 = (-b-dis)/(2*a), (-b+dis)/(2*a)
    else:
        z2, z1 = (-b - dis) / (2 * a), (-b + dis) / (2 * a)
    return z1, z2
