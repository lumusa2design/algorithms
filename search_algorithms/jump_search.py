import math

def jump_search(array, search):
    jump = round(math.sqrt(len(array)))
    position, prev, back = 0, -1, True
    while 0 <= array[position] != search :
        if array[position] > search and back:
            prev, jump, back = position - jump, -1, False
        if position < prev:
            return -1
        position += jump
        if position >= len(array):
            return -1
    return position

arr = [2, 4, 6, 8, 10, 12, 14, 16]
print(jump_search(arr, 5))