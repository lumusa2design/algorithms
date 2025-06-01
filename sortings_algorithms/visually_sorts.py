import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from sortings_algorithms.auxiliar_functions import  *
import random
from sortings_algorithms.auxiliar_functions import find_max

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
    plt.show()


    return lista


def visually_counting_sort(lista):
    arr = lista.copy()
    fig, ax = plt.subplots()
    colores = cm.hsv(np.linspace(0, 1, len(arr)))
    bar_rects = ax.bar(range(len(arr)), arr, color=colores, align="edge")

    ax.set_title("Counting Sort")
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, max(arr) * 1.1)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    def update_bars(arr, step_desc=""):
        for k, (bar, val) in enumerate(zip(bar_rects, arr)):
            bar.set_height(val)
            bar.set_color(cm.hsv(float(val) / float(max(arr)) if max(arr) > 0 else 0))
        text.set_text(step_desc)
        plt.pause(0.1)

    max_val = max(arr)
    count = [0] * (max_val + 1)

    for i in range(len(arr)):
        count[arr[i]] += 1
        update_bars(arr, f"Contando: valor {arr[i]}")

    index = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[index] = i
            update_bars(arr, f"Insertando: {i} en posición {index}")
            index += 1
            count[i] -= 1

    plt.show()
    return arr



def visually_insertion_sort(lista):
    arr = lista.copy()
    fig, ax = plt.subplots()
    colores = cm.hsv(np.linspace(0, 1, len(arr)))
    bar_rects = ax.bar(range(len(arr)), arr, color=colores, align="edge")

    ax.set_title("Insertion Sort")
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, max(arr) * 1.1)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    def update_bars(arr, step_desc=""):
        for k, (bar, val) in enumerate(zip(bar_rects, arr)):
            bar.set_height(val)
            bar.set_color(cm.hsv(float(val) / float(max(arr)) if max(arr) > 0 else 0))
        text.set_text(step_desc)
        plt.pause(0.1)

    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j -1
            update_bars(arr)
        arr[j+1] = key
    return arr

def visually_merge_sort(lista):
    arr = lista.copy()
    fig, ax = plt.subplots()
    colores = cm.hsv(np.linspace(0, 1, len(arr)))
    bar_rects = ax.bar(range(len(arr)), arr, color=colores, align="edge")

    ax.set_title("Merge Sort")
    ax.set_xlim(0, len(arr))
    ax.set_ylim(0, max(arr) * 1.1)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    def update_bars(arr, step_desc=""):
        for k, (bar, val) in enumerate(zip(bar_rects, arr)):
            bar.set_height(val)
            bar.set_color(cm.hsv(float(val) / float(max(lista))))
        text.set_text(step_desc)
        plt.pause(0.2)

    def merge_sort(arr, left, right):
        if left < right:
            middle = (left + right) // 2
            merge_sort(arr, left, middle)
            merge_sort(arr, middle + 1, right)
            merge(arr, left, middle, right)
            update_bars(arr, f"Fusionando: {left}-{right}")

    def merge(arr, left, middle, right):
        n1 = middle - left + 1
        n2 = right - middle
        L = arr[left:left+n1]
        R = arr[middle+1:middle+1+n2]

        i = j = 0
        k = left

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    merge_sort(arr, 0, len(arr)-1)
    plt.show()
    return arr

def visually_quick_sort(arr):
    lista = arr.copy()
    fig, ax = plt.subplots()
    colores = cm.hsv(np.linspace(0, 1, len(lista)))
    bar_rects = ax.bar(range(len(lista)), lista, color=colores, align="edge")
    ax.set_title("Quick Sort")
    ax.set_xlim(0, len(lista))
    ax.set_ylim(0, max(lista) * 1.1)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    def update_bars(data, step_desc=""):
        for k, (bar, val) in enumerate(zip(bar_rects, data)):
            bar.set_height(val)
            bar.set_color(cm.hsv(float(val) / float(max(lista))))
        text.set_text(step_desc)
        plt.pause(0.01)

    def quick_sort_in_place(data, low, high):
        if low < high:
            pivot_index = partition(data, low, high)
            quick_sort_in_place(data, low, pivot_index - 1)
            quick_sort_in_place(data, pivot_index + 1, high)

    def partition(data, low, high):
        pivot = data[high]
        i = low - 1
        for j in range(low, high):
            if data[j] <= pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
                update_bars(lista, f"Swapped {data[i]} and {data[j]}")
        data[i + 1], data[high] = data[high], data[i + 1]
        update_bars(lista, f"Moved pivot {data[i+1]}")
        return i + 1

    quick_sort_in_place(lista, 0, len(lista) - 1)
    plt.show()
    return lista

def visually_selection_sort(arr):
    lista = arr.copy()
    fig, ax = plt.subplots()
    colores = cm.hsv(np.linspace(0, 1, len(lista)))
    bar_rects = ax.bar(range(len(lista)), lista, color=colores, align="edge")
    ax.set_title("Selection Sort")
    ax.set_xlim(0, len(lista))
    ax.set_ylim(0, max(lista) * 1.1)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    def update_bars(arr, i, j):
        for k, (bar, val) in enumerate(zip(bar_rects, arr)):
            bar.set_height(val)
            bar.set_color(cm.hsv(float(val) / float(max(arr))))
        text.set_text(f"Comparando: i={i}, j={j}")
        plt.pause(0.001)

    for i in range(len(arr)):
        minimo = i
        for j in range(i+1, len(arr)):
            if arr[minimo] > arr[j]:
                minimo = j
            update_bars(arr, i, j)
        arr[i], arr[minimo] = arr[minimo], arr[i]

    return arr

def visually_stalin_sort(arr):
    original = arr.copy()
    fig, ax = plt.subplots()
    colores = cm.hsv(np.linspace(0, 1, len(original)))
    bar_rects = ax.bar(range(len(original)), original, color=colores, align="edge")

    ax.set_title("Stalin Sort")
    ax.set_xlim(0, len(original))
    ax.set_ylim(0, max(original) * 1.1)
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)

    def update_bars(current_arr, highlight_index=None, removed_index=None):
        for i, bar in enumerate(bar_rects):
            if i < len(current_arr):
                bar.set_height(current_arr[i])
                if i == highlight_index:
                    bar.set_color('green')
                elif i == removed_index:
                    bar.set_color('red')
                else:
                    bar.set_color(cm.hsv(float(current_arr[i]) / float(max(original))))
            else:
                bar.set_height(0)
                bar.set_color('white')
        plt.pause(0.5)

    pivot = arr[0]
    result = [pivot]
    current_arr = arr.copy()
    update_bars(current_arr, highlight_index=0)

    for i in range(1, len(arr)):
        if arr[i] >= pivot:
            pivot = arr[i]
            result.append(pivot)
            update_bars(current_arr, highlight_index=i)
        else:
            update_bars(current_arr, removed_index=i)
            current_arr[i] = 0


arr = list(range(18, 0, -1))
#visually_bubble_sort(arr)
#visually_bogo_sort(arr)
#visually_counting_sort(arr)
#visually_insertion_sort(arr)
#visually_merge_sort(arr)
#visually_quick_sort(arr)
#visually_selection_sort(arr)
visually_stalin_sort(arr)
