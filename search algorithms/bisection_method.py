def bisection_method(func, a, b, tol=1e-9):
    if func(a) < func(b):
        minim,maxim = a,b
    else:
        minim,maxim = b,a
    flag = True
    while(True):
        c = (minim + maxim)/2
        if func(c) < 0:
            minim = c
        if func(c) > 0:
            maxim = c
        if(func(c) == 0):
            return c

def func(x):
    return 2*x - 2

