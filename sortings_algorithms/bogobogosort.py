from auxiliar_functions import is_order
from bogo_sort import bogo_sort
import random
def bogobogosort(arr):
    array_list = arr.copy()
    counter = 0
    while not is_order(array_list):
        if counter > 0:
            random.shuffle(array_list)
        element = array_list.pop()
        bogo_sort(array_list)
        array_list.append(element)
        counter +=1
    return  array_list
