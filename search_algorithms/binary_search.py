from auxiliar_functions import is_order


def binary_search(arr, search):
    if not is_order(arr):
        return -1

    left = 0
    right = len(arr) - 1


    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == search:
            return mid
        elif arr[mid] < search:
            left = mid + 1
        else:
            right = mid - 1

    return -1
