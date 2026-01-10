def next_interval(size):
    size = (size * 10) // 13
    return max(1, size)

def comb_sort(arr):
    size = len(arr)
    swapped = True
    while size > 1 or swapped:
        size = next_interval(size)
        swapped = False
        for i in range(len(arr) - size):
            if arr[i] > arr[i + size]:
                arr[i], arr[i + size] = arr[i + size], arr[i]
                swapped = True
    return arr
