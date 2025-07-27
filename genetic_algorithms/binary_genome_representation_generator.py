import random

def create_individual(length):
    return [random.randint(0,1) for i in range(length)]

def create_population(population_size, genome_length):
    return [create_individual(genome_length) for _ in range(population_size)]

def evaluate(individual):
    object1 = sum(individual)/len(individual)
    return object1, 1 -object1