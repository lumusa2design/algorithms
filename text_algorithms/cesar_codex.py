def cesar_codex(text, num_code):
    ans = ''
    for i in range(len(text)):
        character = text[i]
        if character == " ":
            ans+= character
        elif character.isupper():
            ans += chr((ord(character) + num_code - 65) % 26 + 65)
        else:
            ans += chr((ord(character) + num_code-97) % 26 + 97)
    return ans

print(f"la contraseña es {cesar_codex('hello world', 4)}")

