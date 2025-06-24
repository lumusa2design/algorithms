import bubble_sort
import bogo_sort
import merge_sort
import quick_sort
import stalin_sort
import time


arr_original = [64, 34, 25, 12, 22, 11, 90, 1,50, 23]

print(f"the original list is: {arr_original}")
#Pruebas del Bubble sort
inicio = time.perf_counter_ns()
arr_bubble = bubble_sort.bubble_sort(arr_original.copy())
fin = time.perf_counter_ns()
print(f"Thr result is: {arr_bubble}")

tiempo_algoritmo= fin - inicio
print(f"Execution Time: {tiempo_algoritmo} ns")

#Prueba Merge sort
inicio = time.perf_counter_ns()
arr_merge, n_iter = merge_sort.merge_sort(arr_original.copy()), merge_sort.count_n_iter()
print(f"The number of iterations of merge sort is: {n_iter}")
fin = time.perf_counter_ns()
print(f"The result of merge sort is: {arr_merge}")

tiempo_algoritmo= fin - inicio
print(f"Execution time: {tiempo_algoritmo} ns")

#Pruebas del quick sort
inicio = time.perf_counter_ns()
arr_quick = quick_sort.quicksort(arr_original.copy())
fin = time.perf_counter_ns()
print(f"The result after quicksort is: {arr_quick}")

tiempo_algoritmo= fin - inicio
print(f"Execution time: {tiempo_algoritmo} ns")

#Pruebas staling sort
inicio = time.perf_counter_ns()
arr_stalin = stalin_sort.stalin_sort(arr_original.copy())
fin = time.perf_counter_ns()
print(f"the result of stalin sort was: {arr_stalin}")
#Pruebas Bogo sort
inicio = time.perf_counter_ns()
arr_bogo = bogo_sort.bogo_sort(arr_original.copy())
fin = time.perf_counter_ns()
print(f"the result of bogo sort was {arr_bogo}")

tiempo_algoritmo= fin - inicio
print(f"Execution time: {tiempo_algoritmo} ns")
