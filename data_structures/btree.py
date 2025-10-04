class BNode():
    def __init__(self, leaf=True):
        self.key = []
        self.child = []
        self.leaf = True
        length = 0

    def __str__(self, level=0):
        print(f"Level {level}: {self.key}")
        if not self.leaf:
            for child in self.child:
                child.display(level + 1)

class BTree:
    def __init__(self, minimum):
        self.root = BNode(True)
        self.minimum = minimum

    def display(self):
        print(self.root)

    def insert(self, key):
        root = self.root
        if len(root.key) == (2 * self.minimum) - 1:
            temp = BNode()
            self.root = temp
            temp.child.append(root)
            self.split_child(temp, 0)

    def split_child(self, node_child,key_len ):
        i = len(node_child.key) -1
        if node_child.leaf:
            node_child.key.append(None)




