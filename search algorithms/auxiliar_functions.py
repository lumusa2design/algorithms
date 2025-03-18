def distance(a, b):
    return abs(abs(a) -  abs(b))

def derivative(f, x, h=1e-5):
    return (f(x+h)-f(x-h))/(2.*h)