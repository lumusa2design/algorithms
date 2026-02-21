def rot13(text):
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            rotated = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            result.append(rotated)
        elif 'A' <= char <= 'Z':
            rotated = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
            result.append(rotated)
        else:
            result.append(char)
    return ''.join(result)