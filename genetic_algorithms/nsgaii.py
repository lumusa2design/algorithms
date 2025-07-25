import random
from random import randint
from mutation import mutation
from tournament_selection import tournament_selection
from two_point_crossover import *
import matplotlib.pyplot as plt

def plot_pareto(population, fitnesses):
    f1 = [f[0] for f in fitnesses]
    f2 = [f[1] for f in fitnesses]

    plt.figure(figsize=(8, 6))
    plt.scatter(f1, f2, c='blue', label='Soluciones')
    plt.xlabel('Objetivo 1')
    plt.ylabel('Objetivo 2')
    plt.title('Frente de Pareto - NSGA-II')
    plt.grid(True)
    plt.legend()
    plt.show()

def evaluate(population):
    objetive = sum(population) / len(population)
    return objetive, 1 - objetive

def domination(individual1, individual2):
    return all(x <= y for x, y in zip(individual1, individual2)) and any(x < y for x, y in zip(individual1, individual2))

def non_dominated_sort(population, fitnesses):
    fronts = [[]]
    domination_count = [0 for _ in population]
    dominated = [[] for _ in population]
    rank = [0 for _ in population]

    for i, fit_i in enumerate(fitnesses):
        for j, fit_j in enumerate(fitnesses):
            if i == j:
                continue
            if domination(fit_i, fit_j):
                dominated[i].append(j)
            elif domination(fit_j, fit_i):
                domination_count[i] += 1

        if domination_count[i] == 0:
            rank[i] = 0
            fronts[0].append(i)

    current = 0
    while fronts[current]:
        next_front = []
        for i in fronts[current]:
            for j in dominated[i]:
                domination_count[j] -= 1
                if domination_count[j] == 0:
                    rank[j] = current + 1
                    next_front.append(j)
        current += 1
        fronts.append(next_front)

    return fronts[:-1], rank

def crowding_distance(front, fitnesses):
    n = len(front)
    distances = [0.0] * n
    num_objectives = len(fitnesses[0])

    for m in range(num_objectives):
        sorted_idx = sorted(range(n), key=lambda i: fitnesses[front[i]][m])
        distances[sorted_idx[0]] = distances[sorted_idx[-1]] = float('inf')
        min_val = fitnesses[front[sorted_idx[0]]][m]
        max_val = fitnesses[front[sorted_idx[-1]]][m]
        if max_val == min_val:
            continue
        for i in range(1, n - 1):
            prev = fitnesses[front[sorted_idx[i - 1]]][m]
            next = fitnesses[front[sorted_idx[i + 1]]][m]
            distances[sorted_idx[i]] += (next - prev) / (max_val - min_val)

    return distances

def elitism_nsga2(population, fitnesses, fronts, num_elites=1):
    front0 = fronts[0]
    sorted_indices = sorted(front0, key=lambda i: sum(fitnesses[i]), reverse=True)
    elites = [population[i] for i in sorted_indices[:num_elites]]
    return elites

def nsga2(pop_size, generations, gene_length, gene_space, crossover_func, num_elites=1):
    population = [[random.choice(gene_space) for _ in range(gene_length)] for _ in range(pop_size)]

    for gen in range(generations):
        fitnesses = [evaluate(ind) for ind in population]
        fronts, rank = non_dominated_sort(population, fitnesses)

        crowding = [0] * len(population)
        for front in fronts:
            distances = crowding_distance(front, fitnesses)
            for i, idx in enumerate(front):
                crowding[idx] = distances[i]

        elites = elitism_nsga2(population, fitnesses, fronts, num_elites)

        combined_fitness = [sum(f) for f in fitnesses]
        selected = [tournament_selection(population, combined_fitness, size_tournament=2) for _ in
                    range(len(population))]

        offspring = []
        for i in range(0, len(selected), 2):
            if i+1 < len(selected):
                child1, child2 = crossover_func(random.randint(1, gene_length - 2), selected[i][:], selected[i + 1][:])
                offspring.extend([mutation(child1, gene_space), mutation(child2, gene_space)])

        combined = elites + offspring
        combined_fitness = [evaluate(ind) for ind in combined]
        fronts, _ = non_dominated_sort(combined, combined_fitness)

        new_population = []
        for front in fronts:
            if len(new_population) + len(front) > pop_size:
                distances = crowding_distance(front, combined_fitness)
                sorted_front = [x for _, x in sorted(zip(distances, front), reverse=True)]
                new_population.extend([combined[i] for i in sorted_front[:pop_size - len(new_population)]])
                break
            new_population.extend([combined[i] for i in front])

        population = new_population

    fitnesses = [evaluate(ind) for ind in population]
    plot_pareto(population, fitnesses)
    return population



def crossover_wrapper(point, parent1, parent2):
    p1 = randint(1, len(parent1) - 2)
    p2 = randint(p1 + 1, len(parent1) - 1)
    return lambda_two_point_crossover(p1, p2, parent1, parent2)

if __name__ == "__main__":

    def crossover_wrapper(point, parent1, parent2):
        p1 = random.randint(1, len(parent1) - 2)
        p2 = random.randint(p1 + 1, len(parent1) - 1)
        return lambda_two_point_crossover(p1, p2, parent1, parent2)

    final_population = nsga2(
        pop_size=30,
        generations=50,
        gene_length=10,
        gene_space=[0, 1],
        crossover_func=crossover_wrapper,
        num_elites=2
    )
