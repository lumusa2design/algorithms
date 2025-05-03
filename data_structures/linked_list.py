class Node:
    def __init__(self, value, position=0):
        self.value = value
        self.next_node = None
        self.position = position

    def __str__(self):
        return f'{self.value}'

class Simple_Linked_List:
    def __init__(self, first_node):
        self.first_node = Node(first_node)
        self.len = 1
        self.last_node = self.first_node

    def add_node(self, new_node):
        new_node = Node(new_node, self.len)
        self.last_node.next_node = new_node
        self.last_node=new_node
        self.len+=1
    def find_node_by_position(self, position):
        if position < 0 or position > self.len:
            pass
        actual = self.first_node
        for i in range(position):
            actual = actual.next_node
        return actual
    def remove_node_by_position(self, position):
        self.len -= 1
        if position == 0:
            if self.first_node == self.last_node:
                self.last_node = None
                self.first_node = None
            else:
                self.first_node = self.first_node.next_node
        else:
            actual = self.first_node
            for i in range(position -1):
                actual = actual.next_node
            next_node = actual.next_node
            actual.next_node = next_node.next_node

            self.reorder()
    def reorder(self):
        position = 0
        actual = self.first_node
        while actual is not None:
            actual.position = position
            actual = actual.next_node
            position += 1
        self.last_node = self.find_node_by_position(self.len - 1) if self.len > 0 else None

    def insert_by_position(self, position, value):
        if position > self.len:
            return "No es tan grande"
        actual = self.first_node
        for i in range(position -1):
            print(i)

    def __str__(self):
        actual = self.first_node
        lista_str = ""
        while actual is not None:
            lista_str += str(actual) + ", "
            actual = actual.next_node
        return lista_str.strip(", ")

    def __len__(self):
        return self.len



lista_encadenada = Simple_Linked_List(5)
lista_encadenada.add_node(1)
lista_encadenada.add_node(2)
lista_encadenada.add_node(3)
lista_encadenada.add_node(4)
lista_encadenada.add_node(6)
lista_encadenada.add_node(7)
print(lista_encadenada.find_node_by_position(2).value)
print(lista_encadenada.find_node_by_position(len(lista_encadenada)-1))
print(lista_encadenada)
lista_encadenada.remove_node_by_position(len(lista_encadenada)-1)
print(lista_encadenada)
print(lista_encadenada.find_node_by_position(len(lista_encadenada)-1))
print(lista_encadenada)
lista_encadenada.remove_node_by_position(len(lista_encadenada)-1)
print(lista_encadenada)

