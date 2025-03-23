def distance(a, b):
    return abs(abs(a) -  abs(b))

def derivative(f, x, h=1e-5):
    return (f(x+h)-f(x-h))/(2.*h)

def is_order(lista):
    flag = True
    for i in range(len(lista) -1):
        if lista[i] > lista[i+1]:
            flag = False
    return flag