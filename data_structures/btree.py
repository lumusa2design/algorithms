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
            self.insert_non_full(temp)


    def split_child(self, node_child,key_len ):
        minimum = self.minimum
        y = node_child.child[key_len]
        z = BNode(leaf=y.leaf)
        node_child.insert(key_len, y.key[minimum -1])
        z.key = y.key[minimum: (2*minimum) - 1]
        y.key = y.key[0:minimum-1]

        if not y.leaf:
            z.child = y.child[minimum: 2 * minimum]
            y.child = y.child[0: minimum - 1]
        node_child.child.insert(key_len + 1, z)




