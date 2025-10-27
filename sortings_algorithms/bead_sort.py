from numerical_algorithms.max_number import max_number
def bead_sort(arr):
    ret = []
    trasposed_arr = [0] * max_number(arr)
    for num in arr:
        trasposed_arr[:num] = [n + 1 for  n in trasposed_arr[:num]]
    for i in range(len(arr)):
        ret.insert(0,(sum(n > i for n in trasposed_arr)))
    return ret
