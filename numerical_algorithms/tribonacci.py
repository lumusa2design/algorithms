def dynamic_programming_tribonacci(num):
    tribo_numbers = [0]*num
    tribo_numbers[2] = 1

    for i in range(3, num):
        tribo_numbers[i] = tribo_numbers[i-1] + tribo_numbers[i-2] + tribo_numbers[i-3]

    return tribo_numbers


