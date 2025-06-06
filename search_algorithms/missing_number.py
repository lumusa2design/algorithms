def missing_number(missing_Arr):
    i = 0
    while i < len(missing_Arr):
        if i != missing_Arr[i]:
            return i
        i += 1


