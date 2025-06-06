def missing_number(missing_Arr):
    i = 0
    while i < len(missing_Arr):
        if i != missing_Arr[i]:
            return i
        i += 1


arr = [0,1,2,3,4,5,6,8,9, 10]

print(missing_number(arr))
