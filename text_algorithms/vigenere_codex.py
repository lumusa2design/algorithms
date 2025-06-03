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


def vigenere_decrypt(codified_message, key):
    index, code_index = 0, 0
    codified_message, key, decodified_message = codified_message.upper(), key.upper(), ""
    while index < len(codified_message):
        if codified_message[index].isalpha():
            decodified_message += chr((ord(codified_message[index]) - ord('A') - (ord(key[code_index % len(key)]) - ord('A'))) % 26 + ord('A'))
            code_index += 1
        else:
            decodified_message += codified_message[index]
        index += 1
    return decodified_message
