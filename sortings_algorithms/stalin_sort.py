def stalin_sort(arr):
    pivot = arr [0]
    res = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] > pivot:
            pivot = arr[i]
            res.append(pivot)
    return res