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


def analyze_array(arr):
    n = len(arr)

    if n == 0:
        return {
            "n": 0,
            "duplicates": 0,
            "disorder": 0,
            "can_counting": False
        }

    is_int = True
    min_value = arr[0]
    max_value = arr[0]
    disorder_breaks = 0
    seen = set()

    previous = arr[0]

    for i, value in enumerate(arr):
        seen.add(value)

        if not isinstance(value, int):
            is_int = False

        if value < min_value:
            min_value = value

        if value > max_value:
            max_value = value

        if i > 0 and previous > value:
            disorder_breaks += 1

        previous = value

    unique = len(seen)
    duplicates = 1 - unique / n
    disorder = disorder_breaks / (n - 1) if n > 1 else 0

    value_range = max_value - min_value if is_int else None

    can_counting = (
        is_int
        and value_range is not None
        and value_range <= n * 10
    )

    return {
        "n": n,
        "duplicates": duplicates,
        "disorder": disorder,
        "can_counting": can_counting
    }