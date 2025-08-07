from numba import njit

n_iter = 0

@njit
def merge_sort(unsorted_list):
    if len(unsorted_list) > 1:
        mid = len(unsorted_list) // 2
        left = unsorted_list[0:mid]
        right = unsorted_list[mid:len(unsorted_list)]
        left = merge_sort(left)
        right = merge_sort(right)
        res =merge(left, right)
        return res
    return unsorted_list

@njit
def merge(left, right):
    res = []
    i, j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return  res

