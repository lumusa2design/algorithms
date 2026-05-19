from concurrent.futures import ProcessPoolExecutor
from pyexpat import features
from insertion_sort import insertion_sort
from auxiliar_functions import disorder_percent
from runawareblocksort import run_aware_merge_sort
from tim_sort import tim_sort
from auxiliar_functions import duplicate_percent
from three_way_quicksort import three_way_quicksort
from auxiliar_functions import can_use_counting_sort
from counting_sort import counting_sort
from parallel_sort import parallel_sort
from auxiliar_functions import analyze_array_sample
import heapq


def hybrid_adaptive_parallel_sort(arr, num_processes):
    features = analyze_array_sample(arr)

    n = features["n"]

    if n <= 1:
        return arr, "trivial"

    if features["can_counting"] and (
        n < 1_000 or features["duplicates"] > 0.25 or n > 100_000
    ):
        return counting_sort(arr), "counting_sort"

    if features["disorder"] < 0.1:
        return run_aware_merge_sort(arr), "run_aware_block_sort"

    if features["duplicates"] > 0.3:
        three_way_quicksort(arr, 0, n - 1)
        return arr, "three_way_quicksort"

    if n > 1_000_000:
        return parallel_sort(arr, num_processes), "parallel_sort"

    tim_sort(arr)
    return arr, "tim_sort_fallback"

import random
import time

def test_algorithm():
    tests = {
        "pequeña": [5, 2, 9, 1, 5, 6],
        "casi ordenada": list(range(10000)),
        "muchos duplicados": [random.randint(0, 5) for _ in range(10000)],
        "aleatoria": [random.randint(0, 100000) for _ in range(10000)],
        "inversa": list(range(10000, 0, -1)),
    }

    for name, arr in tests.items():
        original = arr.copy()

        start = time.perf_counter()
        result = hybrid_adaptive_parallel_sort(arr, num_processes=4)
        end = time.perf_counter()

        expected = sorted(original)

        print(f"\nTest: {name}")
        print(f"Correcto: {result == expected}")
        print(f"Tiempo: {end - start:.6f} segundos")
        print(f"Primeros 10: {result[:10]}")

if __name__ == "__main__":
    test_algorithm()