from insertion_sort import insertion_sort

def bucket_sort(array):
    size = len(array)
    buckets = [[] for i in range(size)]

    for num in array:
        bi = int(size * num)
        buckets[bi].append(num)

    for bucket in buckets:
        insertion_sort(bucket)

    index = 0
    for bucket in buckets:
        for num in bucket:
            array[index] = num
            index +=1
