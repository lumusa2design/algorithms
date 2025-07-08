import numpy as np
import random


def roulette_selection(population, fitnesses):
    total_fitness = sum(fitnesses)
    probabilities =   [f/total_fitness for f in fitnesses]
    cumulative_sum = np.cumsum(probabilities)
    random_select = random.random()

    for i, cumulative_probabilities in enumerate(cumulative_sum):
        if random_select <= cumulative_probabilities:
            return population[i]

