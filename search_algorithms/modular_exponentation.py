def modular_exponentiation(base, exponent, mod):
    c = 1
    for i in range(exponent):
        c *= base
    c =c % mod
    return c


