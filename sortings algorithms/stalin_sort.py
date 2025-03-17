def stalin_sort(arr):
    for i in reversed(range(1, len(arr))):
        if arr[i] <= arr[i-1]:
            arr.pop(i)
    return arr