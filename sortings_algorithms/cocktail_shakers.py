def cocktail_shaker_sort(arr):
    start, end = 0, len(arr) -1
    while start < end:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if not swapped:
            break
        end -=1

        for i in range(end, start, -1):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1]= arr[i-1], arr[i]
                swapped = True

        if not swapped:
            break
        start += 1
    return arr
