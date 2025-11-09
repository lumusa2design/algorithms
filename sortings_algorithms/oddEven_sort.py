from auxiliar_functions import is_order
def odd_even_sort(lista):
    arr = lista.copy()
    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    while not is_order(arr):
        for i in range(1,len(arr) -1, 2):
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1)
        for i in range(0, len(arr)-1, 2):
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1)
    return arr

if __name__ == "__main__":
    arr = [2,1,8,6,4,7]
    print(odd_even_sort(arr))
    print(arr)