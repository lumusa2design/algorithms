def lucas_number(number):
    a,b  =2,1

    if(number==0):
        return a

    for i in range(2, number+1):
        b,a = a+b, b

    return b

