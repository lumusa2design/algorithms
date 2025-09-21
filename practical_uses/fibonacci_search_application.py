from search_algorithms.fibonacci_search import fibonacci_search
from search_algorithms.lineal_search import linear_search
import random
import time

dataset = random.sample(range(0, 10000000), 10000000)
search_value = dataset[1000]



t0 = time.perf_counter()
lx = linear_search(dataset, search_value)
t1 = time.perf_counter()
print(f"finded the value {search_value} at the position {lx} in {t1 - t0:.6f} seconds")

start_fibo = time.perf_counter()
fx = fibonacci_search(dataset, search_value)
end_fibo = time.perf_counter()

print(f"finded the value {search_value} at the position {fx} in {end_fibo - start_fibo:.6f} seconds")



