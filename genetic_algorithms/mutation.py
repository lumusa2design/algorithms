import random

def mutation(arr, space, probability=20):
    for i in range(len(arr)):
        if random.randint(0, 100) < probability:
            arr[i] = random.choice(space)
    return arr