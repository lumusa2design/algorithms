from data_structures import Queue

class Node:
    def __init__(self, value):
        self.father = None
        self.left_son = None
        self.right_son = None
        self.value = value

class BinaryTree:
    def __init__(self, first_value=None):
        if first_value is None:
            self.root = None
            self.length = 0
        else:
            self.root = Node(first_value)
            self.length = 1

    def add_node(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            self.length += 1
            return

        q = Queue.Queue()
        q.enqueue(self.root)

        while not q.is_empty():
            current = q.dequeue()

            if not current.left_son:
                current.left_son = new_node
                new_node.father = current
                self.length += 1
                return
            else:
                q.enqueue(current.left_son)

            if not current.right_son:
                current.right_son = new_node
                new_node.father = current
                self.length += 1
                return
            else:
                q.enqueue(current.right_son)

