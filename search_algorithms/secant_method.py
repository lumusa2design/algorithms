from auxiliar_functions import distance
def secant_method(f, x0, x1, TOL=1e-9, max_iter = 100000):
    for i in range(max_iter):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        if x0 == 0 or distance(x1, x2) <= TOL or x1==x0:
            return x0
        x0, x1 = x1, x2
    return -1

