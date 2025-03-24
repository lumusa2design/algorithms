import random

def uniform_crossover(father, mother):
    if len(father) != len(mother):
        return -1
    son = []
    for i in range(len(father)):
        selection = random.randint(0, 1)
        if selection == 0:
            son.append(father[i])
        if selection == 1:
            son.append(mother[i])
    return son

