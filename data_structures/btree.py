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

    def


