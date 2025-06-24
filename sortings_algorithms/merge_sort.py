n_iter = 0

def merge_sort(unsorted_list):
    global n_iter
    if len(unsorted_list) > 1:
        n_iter +=1
        mid = len(unsorted_list) // 2
        left = unsorted_list[0:mid]
        right = unsorted_list[mid:len(unsorted_list)]
        left = merge_sort(left)
        right = merge_sort(right)
        res =merge(left, right)
        return res
    return unsorted_list


def merge(left, right):
    global n_iter
    res = []
    i, j = 0,0
    while i < len(left) and j < len(right):
        n_iter +=1
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return  res

def count_n_iter():
    return n_iter