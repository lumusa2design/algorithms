def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0 or n == 0 or m > n:
        return -1
    bad_char = {}
    for i in range(m):
        bad_char[pattern[i]] = i
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s 
        else:
            shift = max(1, j - bad_char.get(text[s + j], -1))
            s += shift

    return -1  