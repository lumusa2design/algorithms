def two_point_crossover(first_point, second_point, father, mother):
    father[first_point:second_point],mother[first_point:second_point] = mother[first_point:second_point],father[first_point:second_point]
    return father, mother
