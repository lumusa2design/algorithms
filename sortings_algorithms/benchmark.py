import random
import time
import copy

from hybrid_adaptative_parallel_sort import hybrid_adaptative_parallel_sort
from tim_sort import tim_sort
from three_way_quicksort import three_way_quicksort
from counting_sort import counting_sort
from parallel_sort import parallel_sort


def benchmark_algorithm(name, algorithm, arr):
    data = arr.copy()

    start = time.perf_counter()
    result = algorithm(data)
    end = time.perf_counter()

    if result is None:
        result = data

    return {
        "algorithm": name,
        "correct": result == sorted(arr),
        "time": end - start
    }


def benchmark_all():
    test_cases = {
        "pequeña": [random.randint(0, 100) for _ in range(100)],
        "casi ordenada": list(range(10000)),
        "muchos duplicados": [random.randint(0, 5) for _ in range(10000)],
        "aleatoria": [random.randint(0, 100000) for _ in range(10000)],
        "inversa": list(range(10000, 0, -1)),
    }

    algorithms = [
        ("Python sorted", lambda arr: sorted(arr)),
        ("Hybrid Adaptive Parallel Sort", lambda arr: hybrid_adaptative_parallel_sort(arr, 4)),
        ("Tim Sort propio", lambda arr: tim_sort(arr)),
        ("Three-Way QuickSort", lambda arr: three_way_quicksort(arr, 0, len(arr) - 1)),
        ("Counting Sort", lambda arr: counting_sort(arr)),
        ("Parallel Sort", lambda arr: parallel_sort(arr, 4)),
    ]

    for case_name, arr in test_cases.items():
        print(f"\n=== Caso: {case_name} ===")

        for alg_name, alg_func in algorithms:
            try:
                result = benchmark_algorithm(alg_name, alg_func, arr)
                print(
                    f"{result['algorithm']:<30} "
                    f"Correcto: {result['correct']} "
                    f"Tiempo: {result['time']:.6f}s"
                )
            except Exception as e:
                print(f"{alg_name:<30} ERROR: {e}")


if __name__ == "__main__":
    benchmark_all()