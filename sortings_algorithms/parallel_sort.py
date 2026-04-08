from concurrent.futures import ProcessPoolExecutor
import heapq

def parallel_sort(arr, num_processes):
    if len(arr) < num_processes:
        return sorted(arr)

    chunk_size = len(arr) // num_processes
    chunks = [arr[i:i + chunk_size] for i in range(0, len(arr), chunk_size)]

    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        sorted_chunks = list(executor.map(sorted, chunks))

    return list(heapq.merge(*sorted_chunks))
