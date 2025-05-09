def is_order(lista):
    flag = True
    for i in range(len(lista) -1):
        if lista[i] > lista[i+1]:
            flag = False
    return flag

def find_max(arr):
    maxim = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > maxim:
            maxim = arr[i]
    return maxim
