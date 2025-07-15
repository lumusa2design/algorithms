import random


def tournament_selection(population, fitness, size_tournament):
    selected_indexes = random.sample(range(len(population)), size_tournament)
    best_index = max(selected_indexes, key=lambda i:fitness[i])
    return population[best_index]


