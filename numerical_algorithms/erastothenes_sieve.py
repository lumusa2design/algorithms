from math import sqrt

def erastothenes_sieve(num):
    is_prime = [True] * (num + 1)

    for i in range(2, int(sqrt(num)) + 1):
        if is_prime[i]:
            j = i * i
            while j <= num:
                is_prime[j] = False
                j += i

    return is_prime

