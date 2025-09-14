def quicksort(arr, low=0, high=None):
    if high is None:
        high= len(arr) -1

    if low >= high:
        return
    pivot = partition(arr, low, high)

    quicksort(arr, low, pivot)
    quicksort(arr, pivot +1, high)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, low, high):
    pivot, index_low, index_high = arr[(low + high)//2], low, high

    while True:
        while arr[index_low] < pivot:
            index_low = index_low +1
        while arr[index_high] > pivot :
            index_high = index_high -1
        if index_low >= index_high:
            return index_high
        swap(arr, index_low, index_high)

