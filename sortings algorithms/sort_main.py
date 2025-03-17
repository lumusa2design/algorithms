import bubble_sort
import bogo_sort
import merge_sort
import quick_sort
import stalin_sort
import time


arr_original = [64, 34, 25, 12, 22, 11, 90, 1,50, 23]

print(f"el array original es: {arr_original}")
#Pruebas del Bubble sort
inicio = time.perf_counter_ns()
arr_bubble = bubble_sort.bubble_sort(arr_original.copy())
fin = time.perf_counter_ns()
print(f"El array resultante tras el algoritmo bubble_sort es: {arr_bubble}")

tiempo_algoritmo= fin - inicio
print(f"El tiempo de ejecución ha sido: {tiempo_algoritmo} nanosegundos")

#Prueba Merge sort
inicio = time.perf_counter_ns()
arr_merge, n_iter = merge_sort.merge_sort(arr_original.copy()), merge_sort.count_n_iter()
print(f"el numero de iteraciones de Mergesort fue {n_iter}")
fin = time.perf_counter_ns()
print(f"El array resultante tras el algoritmo Mergesort es: {arr_merge}")

tiempo_algoritmo= fin - inicio
print(f"El tiempo de ejecución ha sido: {tiempo_algoritmo} nanosegundos")

#Pruebas del quick sort
inicio = time.perf_counter_ns()
arr_quick = quick_sort.quicksort(arr_original.copy())
fin = time.perf_counter_ns()
print(f"El array resultante tras el algoritmo quick sort es: {arr_quick}")

tiempo_algoritmo= fin - inicio
print(f"El tiempo de ejecución ha sido: {tiempo_algoritmo} nanosegundos")

#Pruebas staling sort
inicio = time.perf_counter_ns()
arr_stalin = stalin_sort.stalin_sort(arr_original.copy())
fin = time.perf_counter_ns()
print(f"El array resultante tras el algoritmo staling sort es: {arr_stalin}")
#Pruebas Bogo sort
inicio = time.perf_counter_ns()
arr_bogo = bogo_sort.bogo_sort(arr_original.copy())
fin = time.perf_counter_ns()
print(f"El array resultante tras el algoritmo Bogosort es: {arr_bogo}")

tiempo_algoritmo= fin - inicio
print(f"El tiempo de ejecución ha sido: {tiempo_algoritmo} nanosegundos")
