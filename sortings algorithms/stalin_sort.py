import auxiliar_functions
def stalin_sort(arr):
    flag = True
    while flag:
        for i in reversed(range(1, len(arr))):
            if arr[i] <= arr[i-1]:
                arr.pop(i)
            if auxiliar_functions.is_order(arr):
                flag = False
    return arr