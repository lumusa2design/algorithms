import random

def ternary_search(arr, search):
    left, right = 0, len(arr) - 1
    while left <= right:
        middle1, middle2 = left + (right - left) // 3, right - (right - left) // 3
        if arr[middle1] == search:
            return middle1
        elif arr[middle2] == search:
            return middle2
        elif search < arr[middle1]:
            right = middle1 - 1
        elif search > arr[middle2]:
            left = middle2 + 1
        else:
            left, right = middle1 + 1, middle2 - 1

    return -1
