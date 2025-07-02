import binary_search

def exponential_search(ordered_list, key):
    length_list = len(ordered_list)
    if length_list == 0:
        return -1

    bound = 1

    while bound < length_list and ordered_list[bound] < key:
        bound *= 2

    left = bound // 2
    right = min(bound, length_list)

    result = binary_search.binary_search(ordered_list[left:right], key)

    if result == -1:
        return -1
    else:
        return left + result
