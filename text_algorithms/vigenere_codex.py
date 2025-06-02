def vigenere_encrypt(message, key):
    index, codex_index = 0, 0
    message, key, codified_message = message.upper(), key.upper(), ""

    while index < len(message):
        if message[index].isalpha():
            codified_message += chr((ord(message[index]) - ord('A') + ord(key[codex_index % len(key)]) - ord('A')) % 26 + ord('A'))
            codex_index +=1
        else:
            codified_message += message[index]
        index += 1
    return codified_message

