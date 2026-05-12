def detect_runs(arr):
    runs= []
    n = len(arr)

    if n == 0:
        return runs
    start = 0
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            runs.append(arr[start:i])
            start = i
    runs.append(arr[start:n])
    return runs



def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


