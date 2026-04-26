import random

def three_way_quicksort(arr, low, high):
    if low < high:
        lt, gt = partition(arr, low, high)
        three_way_quicksort(arr, low, lt - 1)
        three_way_quicksort(arr, gt + 1, high)

def partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[low], arr[pivot_index] = arr[pivot_index], arr[low]

    pivot = arr[low]

    lt = low
    gt = high
    i = low + 1

    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1

    return lt, gt
