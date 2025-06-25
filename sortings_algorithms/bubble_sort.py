def bubble_sort(lista):
    n_iter = 0
    interchange=True
    while(interchange):
        n_iter += 1
        interchange = False
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1] :
                lista[i], lista[i+1] = lista[i+1], lista[i]
                interchange = True
    print(f"Bubble sort iterations {n_iter}")
    return lista
