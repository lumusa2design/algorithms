import random

def mutation(arr, space):
    for i in range(arr):
        if random.choice([True, False]):
            arr[i] = random.choice(space)
    return arr

