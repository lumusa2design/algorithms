def selection_sort(arr):
    for i in range(len(arr)):
        minimo = i
        for j in range(i+1, len(arr)):
            if arr[minimo] > arr[j]:
                minimo = j
        arr[i], arr[minimo] = arr[minimo], arr[i]
    return arr

lista = [2,1,8,16,23, 3, 4,6]
print(selection_sort(lista))