def one_point_crossover(point, father, mother):
    father[:point], mother[:point] = mother[:3], father[:point]
    return father, mother
