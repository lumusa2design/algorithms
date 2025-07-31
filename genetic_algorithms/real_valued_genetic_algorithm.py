import random
def create_individual_real_valued(length, min_value, max_value):
    return [random.uniform(min_value, max_value) for _ in range(length)]


def create_population_real(population_size, gene_length, min_value, max_value):
    return [create_individual_real_valued(gene_length, min_value, max_value) for _ in range(population_size)]

def arithmetic_crossover(parent1, parent2, alpha=0.5):
    child1 = [(1 - alpha) * x + alpha * y for x, y in zip(parent1, parent2)]
    child2 = [alpha * x + (1 - alpha) * y for x, y in zip(parent1, parent2)]
    return child1, child2

def mutation_real(individual, min_value, max_value, prob=0.1, sigma=0.1):
    for i in range(len(individual)):
        if random.random() < prob:
            individual[i] += random.gauss(0, sigma)
            individual[i] = min(max(individual[i], min_value), max_value)
    return individual