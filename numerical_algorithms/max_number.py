def max_number(array_of_numbers):
    maximum = array_of_numbers[0]
    for i in array_of_numbers:
        if i > maximum:
            maximum = i
    return maximum


