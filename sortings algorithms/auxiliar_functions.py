def is_order(lista):
    flag = True
    for i in range(len(lista) -1):
        if lista[i] > lista[i+1]:
            flag = False
    return flag