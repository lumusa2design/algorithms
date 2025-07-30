def linear_dynamic_mutation_rate(current_generation, max_generation, start=0.3, end=0.01):
    return start - (start - end) * (current_generation/max_generation)

def inverse_dynamic_mutation_rate(current_generation, max_generation):
    return 1.0 / (current_generation + 1)

