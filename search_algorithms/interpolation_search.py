def interpolation(unordered_array, key):
    if len(unordered_array) == 0:
        return -1

    low_value = 0
    high_value = len(unordered_array) -1
    while low_value <= high_value and unordered_array[low_value] <= key <= unordered_array[high_value]:
        if unordered_array[high_value] == unordered_array[low_value]:
            if unordered_array[low_value] == key:
                return low_value
            else:
                return -1
        pointer = low_value + int(
            ((key - unordered_array[low_value]) * (high_value - low_value)) /
            (unordered_array[high_value] - unordered_array[low_value])
        )
        if pointer < 0 or pointer >= len(unordered_array):
            return -1

        if unordered_array[pointer] == key:
            return pointer

        elif unordered_array[pointer]  < key:
            low_value = pointer +1
        else:
            high_value = pointer -1

    return -1




