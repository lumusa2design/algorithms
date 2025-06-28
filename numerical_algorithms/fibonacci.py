def fibonacci(number):
    new = 1
    old = 0
    for i in range(1,number):
        res = old + new
        old = new
        new = res
    return new
