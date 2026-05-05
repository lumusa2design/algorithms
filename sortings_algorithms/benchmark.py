import random
import time

from hybrid_adaptative_parallel_sort import hybrid_adaptive_parallel_sort
from tim_sort import tim_sort
from three_way_quicksort import three_way_quicksort
from counting_sort import counting_sort
from parallel_sort import parallel_sort


REPETITIONS = 10


def benchmark_algorithm(name, algorithm, arr):
    total_time = 0
    final_result = None
    chosen = None

    for _ in range(REPETITIONS):
        data = arr.copy()

        start = time.perf_counter()
        result = algorithm(data)
        end = time.perf_counter()

        if isinstance(result, tuple):
            result, chosen = result

        if result is None:
            result = data

        final_result = result
        total_time += end - start

    return {
        "algorithm": name,
        "chosen": chosen,
        "correct": final_result == sorted(arr),
        "time": total_time / REPETITIONS
    }


def benchmark_all():
    test_cases = {
        "pequeña": [random.randint(0, 100) for _ in range(100)],
        "casi ordenada": list(range(10_000)),
        "muchos duplicados": [random.randint(0, 5) for _ in range(10_000)],
        "aleatoria": [random.randint(0, 100_000) for _ in range(10_000)],
        "inversa": list(range(10_000, 0, -1)),

        "floats aleatorios": [random.random() for _ in range(10_000)],
        "strings": [str(random.randint(0, 100_000)) for _ in range(10_000)],
        "enteros rango enorme": [
            random.randint(0, 10_000_000)
            for _ in range(10_000)
        ],
        "aleatoria gigante": [
    random.randint(0, 1000000)
    for _ in range(1_000_000)
],
"duplicados gigantes": [
    random.randint(0, 100)
    for _ in range(1_000_000)
]
    }

    algorithms = [
        ("Python sorted", lambda arr: sorted(arr)),
        ("Hybrid Adaptive Parallel Sort", lambda arr: hybrid_adaptive_parallel_sort(arr, 4)),
        ("Tim Sort propio", lambda arr: tim_sort(arr)),
        ("Three-Way QuickSort", lambda arr: three_way_quicksort(arr, 0, len(arr) - 1)),
        ("Counting Sort", lambda arr: counting_sort(arr)),
        ("Parallel Sort", lambda arr: parallel_sort(arr, 4)),
    ]

    global_scores = {
        name: 0 for name, _ in algorithms
    }

    for case_name, arr in test_cases.items():
        print(f"\n=== Caso: {case_name} (n={len(arr):,}) ===")

        results = []

        for alg_name, alg_func in algorithms:
            try:
                result = benchmark_algorithm(alg_name, alg_func, arr)

                chosen_text = (
                    f" Elegido: {result['chosen']:<20}"
                    if result["chosen"]
                    else ""
                )

                print(
                    f"{result['algorithm']:<30} "
                    f"Correcto: {str(result['correct']):<5} "
                    f"Tiempo medio: {result['time']:.6f}s"
                    f"{chosen_text}"
                )

                if result["correct"]:
                    results.append(result)

            except Exception as e:
                print(f"{alg_name:<30} ERROR: {e}")

        podium = sorted(results, key=lambda x: x["time"])[:3]

        print("\n🏆 Podio:")
        medals = ["🥇", "🥈", "🥉"]
        points = [3, 2, 1]

        for i, result in enumerate(podium):
            global_scores[result["algorithm"]] += points[i]

            print(
                f"{medals[i]} {result['algorithm']} "
                f"- {result['time']:.6f}s"
            )

    print("\n=== CLASIFICACIÓN GENERAL ===")

    ranking = sorted(
        global_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    medals = ["🥇", "🥈", "🥉"]

    for i, (algorithm, score) in enumerate(ranking):
        medal = medals[i] if i < 3 else "  "
        print(f"{medal} {algorithm:<30} {score} pts")


if __name__ == "__main__":
    benchmark_all()