from sortings_algorithms.auxiliar_functions import  *
import random
def bogo_sort(lista):
    n_iter = 0
    while not is_order(lista):
        n_iter+=1
        random.shuffle(lista)
    print(f"iteraciones en Bogosort: {n_iter}")
    return lista

