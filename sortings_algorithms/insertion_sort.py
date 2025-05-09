def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j -1
        arr[j+1] = key
    return arr


lista = [2,1,8,16,23, 3, 4,6]
print(insertion_sort(lista))