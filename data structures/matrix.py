def create_matrix(col, row):
    arr = []
    for i in range(col):
        arr.append([])
        for j in range(row):
            arr[i].append(0)
    print(arr)
    fill_matrix(arr)
    return arr
def fill_matrix(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] = input(f'introduzca el valor para la posicion{i},{j}: ')

arr = create_matrix(12,12)
print(arr)
