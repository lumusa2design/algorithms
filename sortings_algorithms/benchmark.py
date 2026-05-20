import random
import time

from hybrid_adaptative_parallel_sort import hybrid_adaptive_parallel_sort
from tim_sort import tim_sort
from three_way_quicksort import three_way_quicksort
from counting_sort import counting_sort
from parallel_sort import parallel_sort
from runawareblocksort import run_aware_merge_sort


SMALL_REPETITIONS = 10
LARGE_REPETITIONS = 3
NUM_PROCESSES = 4


def benchmark_algorithm(name, algorithm, arr, repetitions):
    total_time = 0
    final_result = None
    chosen = None
    expected = sorted(arr)

    for _ in range(repetitions):
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
        "correct": final_result == expected,
        "time": total_time / repetitions,
    }


def get_algorithms():
    return [
        ("Python sorted", lambda arr: sorted(arr)),
        ("Hybrid Adaptive Parallel Sort", lambda arr: hybrid_adaptive_parallel_sort(arr, NUM_PROCESSES)),
        ("Tim Sort propio", lambda arr: tim_sort(arr)),
        ("Run-Aware Block Sort", lambda arr: run_aware_merge_sort(arr)),
        ("Three-Way QuickSort", lambda arr: three_way_quicksort(arr, 0, len(arr) - 1)),
        ("Counting Sort", lambda arr: counting_sort(arr)),
        ("Parallel Sort", lambda arr: parallel_sort(arr, NUM_PROCESSES)),
    ]


def create_scoreboard(algorithms):
    return {
        name: 0
        for name, _ in algorithms
    }


def print_ranking(title, scores):
    print(f"\n=== {title} ===")

    ranking = sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    medals = ["🥇", "🥈", "🥉"]

    for i, (algorithm, score) in enumerate(ranking):
        medal = medals[i] if i < 3 else "  "
        print(f"{medal} {algorithm:<30} {score} pts")


def run_benchmark_group(group_name, test_cases, repetitions):
    algorithms = get_algorithms()
    scores = create_scoreboard(algorithms)

    print("\n" + "=" * 60)
    print(f"{group_name}")
    print(f"Repeticiones por algoritmo: {repetitions}")
    print("=" * 60)

    for case_name, arr in test_cases.items():
        print(f"\n=== Caso: {case_name} (n={len(arr):,}) ===")

        results = []

        for alg_name, alg_func in algorithms:
            try:
                result = benchmark_algorithm(
                    alg_name,
                    alg_func,
                    arr,
                    repetitions
                )

                chosen_text = (
                    f" Elegido: {result['chosen']:<22}"
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

        print("\n🏆 Podio del caso:")

        medals = ["🥇", "🥈", "🥉"]
        points = [3, 2, 1]

        for i, result in enumerate(podium):
            scores[result["algorithm"]] += points[i]

            print(
                f"{medals[i]} {result['algorithm']} "
                f"- {result['time']:.6f}s"
            )

    print_ranking(f"CLASIFICACIÓN {group_name}", scores)

    return scores


def merge_scores(*scoreboards):
    total = {}

    for scoreboard in scoreboards:
        for algorithm, score in scoreboard.items():
            total[algorithm] = total.get(algorithm, 0) + score

    return total


def benchmark_all():
    small_medium_tests = {
        "pequeña": [
            random.randint(0, 100)
            for _ in range(100)
        ],

        "casi ordenada": list(range(10_000)),

        "muchos duplicados": [
            random.randint(0, 5)
            for _ in range(10_000)
        ],

        "aleatoria": [
            random.randint(0, 100_000)
            for _ in range(10_000)
        ],

        "inversa": list(range(10_000, 0, -1)),

        "floats aleatorios": [
            random.random()
            for _ in range(10_000)
        ],

        "strings": [
            str(random.randint(0, 100_000))
            for _ in range(10_000)
        ],

        "enteros rango enorme": [
            random.randint(0, 10_000_000)
            for _ in range(10_000)
        ],

        "runs largas": (
            list(range(0, 2_500))
            + list(range(2_500, 5_000))
            + list(range(7_500, 10_000))
            + list(range(5_000, 7_500))
        ),

        "runs mezcladas": (
            list(range(0, 2_000))
            + list(range(4_000, 6_000))
            + list(range(2_000, 4_000))
            + list(range(6_000, 10_000))
        ),
    }

    large_tests = {
        "aleatoria gigante": [
            random.randint(0, 1_000_000)
            for _ in range(1_000_000)
        ],

        "duplicados gigantes": [
            random.randint(0, 100)
            for _ in range(1_000_000)
        ],

        "casi ordenada gigante": list(range(1_000_000)),

        "inversa gigante": list(range(1_000_000, 0, -1)),
    }

    small_scores = run_benchmark_group(
        "TESTS PEQUEÑOS Y MEDIANOS",
        small_medium_tests,
        SMALL_REPETITIONS
    )

    large_scores = run_benchmark_group(
        "TESTS GRANDES",
        large_tests,
        LARGE_REPETITIONS
    )

    total_scores = merge_scores(small_scores, large_scores)

    print_ranking("CLASIFICACIÓN GLOBAL TOTAL", total_scores)


if __name__ == "__main__":
    benchmark_all()