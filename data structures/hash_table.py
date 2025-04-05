import string

class hash_table:
    def __init__(self, module):
        self.size = module
        self.table = [[None] for _ in range(module)]

    def own_hash(self, key):
        minusculas = string.ascii_lowercase
        mayusculas = string.ascii_uppercase
        num = 0
        for letra in key:
            if letra in minusculas:
                num += int(minusculas.index(letra) + 97)
            if letra in mayusculas:
                num += int(mayusculas.index(letra) + 65)
        print(num)
        return num
    def insert(self, key, value):
        position = self.own_hash(key) % self.size
        if self.table[position][0] == None:
            self.table[position][0] = (key, value)
        elif key not in self.table[position]:
            self.table[position].append((key, value))
        print(self.table)


    def get(self, key):
        position = self.own_hash(key) % self.size
        if len(self.table[position]) == 1:
            return self.table[position][0][0]
        elif len(self.table[position]) > 1:
            for i in self.table[position]:
                if i[0] == key:
                    return i[1]
        else:
            return "nada majo"

clave = "fernando"
ht = hash_table(5)
ht.insert(clave,"nombre")
clave2 = "carlos"
ht.insert(clave2, "otro nombre")
clave3 = "ofdnanref"
clave4 = "pablo"
clave5= "paco"
clavo6 = "miranda"
ht.insert(clave3, "valor")
ht.insert(clave4, "valor2")
ht.insert(clave5, "valor3")
ht.insert(clavo6, "valor4")
print(ht.get(clave5))
