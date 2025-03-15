def bubble_sort(lista):
    n_iter = 0
    intercambio=True
    while(intercambio):
        n_iter += 1
        intercambio = False
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1] :
                lista[i], lista[i+1] = lista[i+1], lista[i]
                intercambio = True
    print(f"iteraciones en Bubblesort {n_iter}")
    return lista
