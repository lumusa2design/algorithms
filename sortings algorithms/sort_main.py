import bubble_sort
import time


arr_original = [64, 34, 25, 12, 22, 11, 90, 1,50, 23]
print(f"el array original es: {arr_original}")
inicio = time.perf_counter_ns()
arr_bubble = bubble_sort.bubble_sort(arr_original)
fin = time.perf_counter_ns()
print(f"El array resultante tras el algoritmo bubble_sort es: {arr_bubble}")

tiempo_algoritmo= fin - inicio
print(f"El tiempo de ejecución ha sido: {tiempo_algoritmo} nanosegundos")
