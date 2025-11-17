def compare(value1, value2):
    return ((1.0 * value2[0])/value2[1]) - ((1.0 * value1[0])/value1[1])

def fractional_knapsack(values, weight, capacity):
    length = len(values)
    items = [[values[i], weight[i]] for i in range(length)]
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    res, current_capacity = 0.0, capacity

    for i in range(length):
        if items[i][1] <= current_capacity:
            res += items[i][0]
            current_capacity -= items[i][1]

        else:
            res += (1.0 * items[i][0] / items[i][1]) * current_capacity
            break
    return res
