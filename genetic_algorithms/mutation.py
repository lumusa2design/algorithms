import random

def mutation(arr, space, probability=20):
    for i in range(len(arr)):
        if random.randint(0, 100) < probability:
            arr[i] = random.choice(space)
    return arr

arr = [1,2,3,4,5,6,7,8,9,10]
space = [1,2,3,4,5,6,7,8,9,10]
print(arr)
print(f'{mutation(arr, space)} es el nuevo hijo')