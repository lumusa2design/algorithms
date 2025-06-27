def pow_method(number, exponent):
    if number ==0:
        return 1

    res = 1
    for i in range(exponent):
        res*=number
    return res