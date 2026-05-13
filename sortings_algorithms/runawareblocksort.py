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



def run_aware_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    runs = detect_runs(arr)

    while len(runs) > 1:
        new_runs = []

        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                new_runs.append(merge(runs[i], runs[i + 1]))
            else:
                new_runs.append(runs[i])

        runs = new_runs

    return runs[0]


