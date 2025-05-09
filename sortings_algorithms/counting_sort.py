from sortings_algorithms.auxiliar_functions import find_max

def counting_sort(arr):
    maxim = find_max(arr)
    count = [0] * (maxim +1)
    res = []
    for i in range(len(arr)):
        count[arr[i]] += 1

    for i in range(len(count)):
        while count[i] > 0:
            res.append(i)
            count[i] -= 1
    return res




