from pow_method import pow_method
from factorial import  factorial


def taylor_polynomial(number, grade):
    expansion = 1
    for i in range(1, grade):
        term = pow_method(number, i)/factorial(i)
        expansion += term
    return expansion