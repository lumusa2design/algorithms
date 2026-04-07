from concurrent.futures import ProcessPoolExecutor
from sortings_algorithms.insertion_sort import insertion_sort
import heapq


def hybrid_adaptative_parallel_sort(arr, num_processes):
    if len(arr) < num_processes:
        return sorted(arr)
    if len(arr) < 1000: 
        return insertion_sort(arr)
    if len(arr) < 10000:
            return sorted(arr)
    chunk_size = len(arr) // num_processes
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        sorted_chunks = list(executor.map(sorted, chunks))

    return list(heapq.merge(*sorted_chunks))