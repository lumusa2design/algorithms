from concurrent.futures import ProcessPoolExecutor
from sortings_algorithms.insertion_sort import insertion_sort
from auxiliar_functions import disorder_percent
from sortings_algorithms.timsort import timsort
import heapq


def hybrid_adaptative_parallel_sort(arr, num_processes):
    if len(arr) < num_processes:
        return sorted(arr)
    if len(arr) < 1000: 
        return insertion_sort(arr)
    if disorder_percent(arr) < 0.1: 
        return timsort(arr)
    chunk_size = len(arr) // num_processes
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        sorted_chunks = list(executor.map(sorted, chunks))

    return list(heapq.merge(*sorted_chunks))