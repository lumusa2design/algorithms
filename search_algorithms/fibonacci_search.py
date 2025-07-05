def fibonacci_search(sorted_array, key):
    size = len(sorted_array)
    fibo1,fibo2, fibo3 = 0, 1,1
    while fibo3 < size:
        fibo1, fibo2 = fibo2, fibo3
        fibo3 = fibo1+fibo2

    offset = -1

    while fibo3 > 1:
        i = min(offset + fibo1, size-1)
        if sorted_array[i] < key:
            fibo3 = fibo2
            fibo2 = fibo2 - fibo1
            fibo1 = fibo3 - fibo2
            offset = i
        else:
            return i
    if fibo2 and sorted_array[offset + 1] == key:
        return offset +1
    return -1

