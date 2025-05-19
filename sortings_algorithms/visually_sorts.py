import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from sortings_algorithms.auxiliar_functions import  *
import random

def visually_bubble_sort(lista):
    lista = lista.copy()
    fig, ax = plt.subplots()

    colores = cm.hsv(np.linspace(0, 1, len(lista)))
    bar_rects = ax.bar(range(len(lista)), lista, color=colores, align="edge")

    ax.set_title("Bubble Sort")
    ax.set_xlim(0, len(lista))
    ax.set_ylim(0, max(lista) * 1.1)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    n_iter = 0
    intercambio = True

    def update_bars(arr, i, j):
        for k, (bar, val) in enumerate(zip(bar_rects, arr)):
            bar.set_height(val)
            bar.set_color(cm.hsv(float(val) / float(max(arr))))
        text.set_text(f"Comparando: i={i}, j={j}")
        plt.pause(0.001)

    while intercambio:
        n_iter += 1
        intercambio = False
        for i in range(len(lista) - 1):
            j = i + 1
            update_bars(lista, i, j)
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
                intercambio = True

    print(f"Iteraciones en Bubble Sort: {n_iter}")
    plt.show()
    return lista



def visually_bogo_sort(lista):
    lista = lista.copy()
    fig, ax = plt.subplots()
    colores = cm.hsv(np.linspace(0, 1, len(lista)))
    bar_rects = ax.bar(range(len(lista)), lista, color=colores, align="edge")

    ax.set_title("Bogo Sort")
    ax.set_xlim(0, len(lista))
    ax.set_ylim(0, max(lista) * 1.1)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    n_iter = 0
    def update_bars_bogo(arr):
        for k, (bar, val) in enumerate(zip(bar_rects, arr)):
            bar.set_height(val)
            bar.set_color(cm.hsv(float(val) / float(max(arr))))
        plt.pause(0.001)
    while not is_order(lista):
        n_iter+=1
        random.shuffle(lista)
        update_bars_bogo(lista)
    print(f"iteraciones en Bogosort: {n_iter}")


    return lista



arr = list(range(5, 0, -1))
visually_bubble_sort(arr)
visually_bogo_sort(arr)
