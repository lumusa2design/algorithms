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
