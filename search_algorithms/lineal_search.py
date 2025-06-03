def linear_search(arr, search):
    for i in range(len(arr)):
        if arr[i] == search:
            return i

    return -1


