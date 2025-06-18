def two_point_crossover(first_point, second_point, father, mother):
    father[first_point:second_point],mother[first_point:second_point] = mother[first_point:second_point],father[first_point:second_point]
    return father, mother

lambda_two_point_crossover = lambda first_point, second_point, father, mother: (mother[:first_point] + father[first_point:second_point] + mother[second_point:], father[:first_point] + mother[first_point:second_point] + father[second_point:])
