def bisection_method(func, a, b, tol=1e-9):
    if func(a) < 0:
        minim,maxim = a,b
    else:
        minim,maxim = b,a
    while(True):
        c = (minim + maxim)/2
        if func(c) < 0:
            minim = c
        if func(c) > 0:
            maxim = c
        if(func(c) == 0):
            return c

