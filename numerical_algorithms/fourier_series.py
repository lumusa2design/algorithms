def fourier_series(coefficients, x):
    result = 0.0
    for coeff, n in coefficients:
        if n == 0:
            result += coeff / 2  # a_0 term
        elif coeff[0] == 'a':
            result += coeff * cos(n * x)  # a_n terms
        elif coeff[0] == 'b':
            result += coeff * sin(n * x)  # b_n terms
    return result