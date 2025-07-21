def rabin_karp(pattern, text):
    alphabet_size, prime, pattern_length, text_length, pattern_hash, window_hash = 256, 101, len(pattern), len(text),0,0
    high_order_multiplier, occurrences = 1, []

    for _ in range(pattern_length -1):
        high_order_multiplier = (high_order_multiplier * alphabet_size) % prime

    for i in range(pattern_length):
        pattern_hash = (alphabet_size * pattern_hash + ord(pattern[i])) % prime
        window_hash = (alphabet_size * window_hash + ord(text[i])) % prime

    for i in range(text_length - pattern_length + 1):
        if pattern_hash == window_hash:
            match = True
            for j in range(pattern_length):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                occurrences.append(i + 1)
        if i < text_length - pattern_length:
            window_hash = (alphabet_size * (window_hash - ord(text[i]) * high_order_multiplier) + ord(text[i + pattern_length])) % prime
            if window_hash < 0:
                window_hash += prime

    return occurrences
