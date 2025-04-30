class Node:
    def __init__(self, value, position):
        self.prev_node = None
        self.next_node = None
        self.value = value
        self.position = position

    def __str__(self):
        return f'{self.value}'

class DoubleLinkedList:
    def __init__(self, first_node=None):
        if first_node is None:
            self.first_node = None
            self.last_node = None
            self.length = 0
        else:
            self.first_node = Node(first_node, 0)
            self.last_node = self.first_node
            self.length = 1

    def add_node(self, new_node):
        if self.first_node is None:
            self.first_node = Node(new_node, 0)
            self.last_node = self.first_node
            self.length = 1
            return
        node = Node(new_node, self.length)
        self.last_node.next_node = node
        node.prev_node = self.last_node
        self.last_node = node
        self.length += 1

    def find_node_by_position(self, position):
        if position < 0 or position >= self.length:
            raise IndexError("Posición fuera de rango")
        actual = self.first_node
        for _ in range(position):
            actual = actual.next_node
        return actual

    def remove_node_by_position(self, position):
        if position < 0 or position >= self.length:
            raise IndexError("Posición fuera de rango")
        to_remove = self.find_node_by_position(position)
        prev_n = to_remove.prev_node
        next_n = to_remove.next_node

        if prev_n:
            prev_n.next_node = next_n
        else:
            self.first_node = next_n

        if next_n:
            next_n.prev_node = prev_n
        else:
            self.last_node = prev_n

        self.length -= 1
        return to_remove.value

    def __len__(self):
        return self.length

    def __str__(self):
        if self.length == 0 or self.first_node is None:
            return "List is empty"
        valores = []
        actual = self.first_node
        while actual:
            valores.append(str(actual.value))
            actual = actual.next_node
        return " <-> ".join(valores)


