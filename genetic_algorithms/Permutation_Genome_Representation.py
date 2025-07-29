import random

def create_individual_permutation(length):
    individual = list(range(length))
    random.shuffle(individual)
    return  individual

def create_population_permutation(population_size, genome_length):
    return [create_individual_permutation(genome_length) for _ in range(population_size)]

def evaluate(individual):
    total = 0
    for i in range(len(individual) - 1):
        total += abs(individual[i] - individual[i + 1])
    return total, 0
