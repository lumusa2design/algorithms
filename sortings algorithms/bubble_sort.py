def bubble_sort(lista):
    intercambio=True
    while(intercambio):
        intercambio = False
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1] :
                lista[i], lista[i+1] = lista[i+1], lista[i]
                intercambio = True
    return lista



lista = [5,2,7,6,9,20,1]
print(lista)

print(bubble_sort(lista))