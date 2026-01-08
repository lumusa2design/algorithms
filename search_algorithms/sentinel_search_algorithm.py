def sentinel_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1

    last = arr[-1]
    arr[-1] = target

    i = 0
    while arr[i] != target:
        i += 1
    arr[-1] = last

    if i < n - 1 or arr[-1] == target:
        return i
    else:
        return -1