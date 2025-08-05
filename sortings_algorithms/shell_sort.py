def shell_sort(array, gap=None):
    size = len(array)
    if gap is None:
        gap = size//2

    while gap > 0:
        for i in range(gap, size):
            temp =  array[i]
            j = i

            while j  >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2