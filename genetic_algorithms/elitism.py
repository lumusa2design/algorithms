def elitism(population, fitnesses, num_elites=1):
    sorted_index = sorted(range(len(fitnesses)), key=lambda i: fitnesses[i], reverse=True)
    elites =  [population[i] for i in sorted_index[:num_elites]]
    return elites

