def is_order(lista):
    flag = True
    for i in range(len(lista) -1):
        if lista[i] > lista[i+1]:
            flag = False
    return flag

def find_max(arr):
    maxim = arr[0]
    for i in range(1,len(arr)):
        if arr[i] > maxim:
            maxim = arr[i]
    return maxim


def disorder_percent(lista):
    if len(lista) < 2:
        return 0

    roturas = 0

    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            roturas += 1

    return roturas / (len(lista)-1)


def duplicate_percent(lista):
    if not lista:
        return 0

    uniq = len(set(lista))
    return 1 - (uniq / len(lista))

def can_use_counting_sort(arr):
    if not arr:
        return False

    if not all(isinstance(x, int) for x in arr):
        return False

    value_range = max(arr) - min(arr)

    return value_range <= len(arr) * 10


def analyze_array_sample(arr, sample_size=10_000):
    n = len(arr)

    if n == 0:
        return {
            "n": 0,
            "duplicates": 0,
            "disorder": 0,
            "can_counting": False,
        }

    if n <= sample_size:
        sample = arr
    else:
        step = n // sample_size
        sample = arr[::step][:sample_size]

    is_int = all(isinstance(x, int) for x in sample)

    disorder_breaks = 0
    for i in range(len(sample) - 1):
        if sample[i] > sample[i + 1]:
            disorder_breaks += 1

    disorder = disorder_breaks / max(1, len(sample) - 1)

    unique = len(set(sample))
    duplicates = 1 - unique / len(sample)

    if is_int:
        value_range = max(sample) - min(sample)
        can_counting = value_range <= n * 10
    else:
        can_counting = False

    return {
        "n": n,
        "duplicates": duplicates,
        "disorder": disorder,
        "can_counting": can_counting,
    }
