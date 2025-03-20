def one_point_crossover(point, father, mother):
    father[:point], mother[:point] = mother[:point], father[:point]
    return father, mother
