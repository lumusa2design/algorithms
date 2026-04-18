from concurrent.futures import ProcessPoolExecutor
from sortings_algorithms.insertion_sort import insertion_sort
from auxiliar_functions import disorder_percent
from sortings_algorithms.tim_sort import tim_sort
from sortings_algorithms.auxiliar_functions import duplicate_percent
from sortings_algorithms.three_way_quicksort import three_way_quicksort
import heapq


def hybrid_adaptative_parallel_sort(arr, num_processes):
    if len(arr) <= 1:
        return arr

    if len(arr) < num_processes:
        return sorted(arr)

    if len(arr) < 1000:
        return insertion_sort(arr)

    if disorder_percent(arr) < 0.1:
        tim_sort(arr)
        return arr

    if duplicate_percent(arr) > 0.5:
        three_way_quicksort(arr, 0, len(arr) - 1)
        return arr

    if len(arr) < 10000 and can_use_counting_sort(arr):
        return counting_sort(arr)

    return parallel_sort(arr, num_processes)