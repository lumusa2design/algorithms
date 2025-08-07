from insertion_sort import *
from merge_sort import *
from numba import njit

@njit
def tim_sort(array, min_run=32):
    size, runs = len(array), []
    for start in range(0, size, min_run):
        sublist = array[start:min(start + min_run, size)]
        sorted_run = insertion_sort(sublist)
        runs.append(sorted_run)

    while len(runs) > 1:
        new_runs = []
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                merged =  merge(runs[i], runs[i+1])
                new_runs.append(merged)
            else:
                new_runs.append(runs[i])
        runs = new_runs

    if runs:
        sorted_arr = runs[0]
        for i in range(size):
            array[i] = sorted_arr[i]

