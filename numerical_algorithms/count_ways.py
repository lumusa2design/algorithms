def count_ways(number_of_weights):
    if number_of_weights == 0 or number_of_weights==1:
        return 1
    return count_ways(number_of_weights-1) + count_ways(number_of_weights-2)
