import random

def create_individual_real(length, min_value, max_value):
    return [random.uniform(min_value, max_value) for _ in range(length)]


def create_population_real(population_size, genom_length, min_value, max_value):
    return [create_individual_real(genom_length, min_value, max_value) for i in range(population_size)]

def evaluate(individual):
    object1 = sum(individual) / len(individual)
    object2 = sum(x**2 for x in individual) / len(individual)
    return object1, object2




