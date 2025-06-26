def min_number(array_of_numbers):
    min_number = array_of_numbers[0]
    for i in array_of_numbers:
        if i < min_number:
            min_number = i
    return  min_number
