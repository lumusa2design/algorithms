from sortings_algorithms.bogo_sort import bogo_sort
import random
import time

def auto_timer(size):
    arr_of_elements = random.sample(range(0, 10000), 10)
    start = time.time()
    sorted_arr = bogo_sort(arr_of_elements)
    end = time.time()
    temporizer = end - start
    return temporizer


print(f'the time to order 10 elements using bogosort is: {auto_timer(10)} seconds')
print(f'the time to order 100 elements using bogosort is: {auto_timer(100)} seconds')
print(f'the time to order 1000 elements using bogosort is: {auto_timer(1000)} seconds')
arr_of_elements = random.sample(range(0, 100000), 10)
start = time.time()
sorted_arr = sorted(arr_of_elements)
end = time.time()
temporizer = end - start
print(f'but the time with generic algorithm  to 100000 of python is:{temporizer} seconds ')
