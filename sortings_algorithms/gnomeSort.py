def gnome_sort(arr):
    pos = 1
    n = len(arr)

    while pos < n:
        if arr[pos] >= arr[pos - 1]:
            pos += 1
        else:
            arr[pos], arr[pos - 1] = arr[pos - 1], arr[pos]
            pos -= 1
            if pos == 0:
                pos = 1

    return arr

