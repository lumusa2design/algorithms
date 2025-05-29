import random

def mutation(arr, space, probability=20):
    for i in range(len(arr)):
        if random.randint(0, 100) < probability:
            arr[i] = random.choice(space)
    return arr

def smart_mutation(individual, puzzle, probability=20, space=81):
    for i in range(space):
        if puzzle[i] == 0 and random.randint(0, 100) < probability:
            row = i // 9
            row_vals = individual[row*9:(row+1)*9]
            possible = [n for n in range(1, 10) if n not in row_vals or n == individual[i]]
            individual[i] = random.choice(possible)
    return individual