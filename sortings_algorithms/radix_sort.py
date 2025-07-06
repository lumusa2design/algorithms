from numerical_algorithms.max_number import max_number
from sortings_algorithms.counting_sort import counting_sort


def radix_sort(unordered_array):
    result =unordered_array[:]
    max_number_of_array = max_number(result)
    exponent = 1

    while max_number_of_array // exponent > 0:
        buckets = [[] for i in range(10)]

        for number in result:
            digit = (number//exponent) % 10
            buckets[digit].append(number)

        for i in range(10):
            if buckets[i]:
                buckets[i] = counting_sort(buckets[i])

        result = [num for bucket in buckets for num in bucket]

        exponent *= 10
    return result
