import auxiliar_functions
def newton_raphson(f, x0, MaxIter, TOL=1e-9):
    fx0 = f(x0)
    for i in range(MaxIter):
        x1 = x0 - (fx0/auxiliar_functions.derivative(f, x0))
        if fx0 == 0 or auxiliar_functions.distance(x0, x1)< TOL:
            print(i)
            return x0
        x0 = x1
        fx0 = f(x0)

    return -1


