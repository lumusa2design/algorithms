def cycle_sort(arr):
    writes = 0
    for start in range(len(arr)-1):
        value = arr[start]
        position = start
        for i in range(start+1, len(arr)):
            if arr[i] < value:
                position += 1
        if position == start:
            continue

        while value ==  arr[position]:
            position += 1
        arr[position], value = value, arr[position]
        writes += 1

        while position != start:
            position = start
            for i in range(start +1, len(arr)):
                if arr[i] < value:
                    position+=1

            while value == arr[position]:
                position+=1
            arr[position], value = value, arr[position]
            writes += 1
    return arr
