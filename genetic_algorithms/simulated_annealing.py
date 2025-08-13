import math
import random


def simulated_annealing(function, initial_tuple, temp0=1.0, temp_min=1e-3, max_evals=50000, alpha=0.98,step=0.1, seed=42):
    random.seed(seed)
    x = list(initial_tuple)
    fx = function(x)
    best_x, best_fx = list(x), fx
    T = temp0
    evals = 1

    def neighbor(vector, temperature):
        return [xi + random.gauss(0, step) * (temperature / temp0) for xi in vector]

    while T > temp_min and evals < max_evals:
        y = neighbor(x, T)
        fy = function(y); evals += 1
        delta = fy -fx
        if delta <= 0 or random.random() < math.exp(-delta/T):
            x, fx = y, fy
            if fx < best_fx:
                best_x, best_fx = list(x), fx
        T *= alpha
    return best_x, best_fx
