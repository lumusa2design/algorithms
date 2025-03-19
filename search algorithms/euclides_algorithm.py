def euclides(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1

    res = num1 % num2

    while res != 0:
        num1, num2 = num2, res
        res = num1 % num2
    return num2

a,b = 2366, 273
mcd = euclides(a, b)

print(f"El maximo comun divisor de {a} y {b} es {mcd}")