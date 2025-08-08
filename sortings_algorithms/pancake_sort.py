import random
import time

def flip(array, k):
  left = 0
  while left < k:
    array[left], array[k] = array[k], array[left]
    k -= 1
    left += 1

def max_index (array, k):
    index = 0
    for i in range(k):
        if array[i] > array[index]:
            index = i
    return index

def pancake_sort(array):
    size = len(array)
    while size > 1:
        index = max_index(array, size)
        if index != size:
            flip(array, index)
            flip(array, size-1)
        size-=1
    return array
