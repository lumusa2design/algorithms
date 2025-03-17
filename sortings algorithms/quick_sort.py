def quicksort(arr):
    if not arr:
        return []
    if len(arr) == 1:
        return arr
    left = []
    right=[]
    pivot = arr[-1]
    for i in arr[:-1]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)
    res = quicksort(left) + [pivot] + quicksort(right)
    return res
