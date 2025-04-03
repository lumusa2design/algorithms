import string

minusculas = string.ascii_lowercase
mayusculas = string.ascii_uppercase

def letra_a_codigo(letra):
    if letra in minusculas:
        return int(minusculas.index(letra) + 97)
    if letra in mayusculas:
        return int(mayusculas.index(letra) + 65)

clave = "fernando"
a = 0
for _, letra in enumerate(clave):
    a += letra_a_codigo(letra)

print(a)
