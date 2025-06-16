import auxiliar_functions

def regula_falsi(f, a, b, Max_iter, TOL= 1e-9):
    xr1 = 0
    if f(a) * f(b) > 0:
        raise ValueError
    for i in range(Max_iter):
        xr = a - (b-a)/(f(b)- f(a)) * f(a)
        fx = f(xr)
        if fx * f(b) < 0:
            a = xr
        else:
            b = xr
        if fx == 0 or auxiliar_functions.distance(xr, xr1) < TOL:
            return xr
        xr1 = xr
    return -1



def f(x):
    return x**3 - 4*x + 1  # Ejemplo de fun
