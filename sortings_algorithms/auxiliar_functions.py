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


def disorder_percent(lista):
    if len(lista) < 2:
        return 0

    roturas = 0

    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            roturas += 1

    return roturas / (len(lista)-1)


def duplicate_percent(lista):
    if not lista:
        return 0

    uniq = len(set(lista))
    return 1 - (uniq / len(lista))

def can_use_counting_sort(arr):
    if not arr:
        return False

    if not all(isinstance(x, int) for x in arr):
        return False

    value_range = max(arr) - min(arr)

    return value_range <= len(arr) * 10