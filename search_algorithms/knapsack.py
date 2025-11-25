def knapsack(capacity, weights, values, repetition=True):
    size = len(weights)
    best_value = [0] * (capacity + 1)

    if repetition:
        for i in range(capacity+1):
            for j in range(size):
                if weights[j] <= i:
                    best_value[i] = max(best_value[i], best_value[i - weights[j]] + values[j])
    else:
        for j in range(size):
            for i in range(capacity, weights[j]-1, -1):
                best_value[i] = max(best_value[i], best_value[i - weights[j]] + values[j])

    return best_value[capacity]

