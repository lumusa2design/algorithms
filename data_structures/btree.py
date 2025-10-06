class BNode:
    def __init__(self, leaf=True):
        self.key = []
        self.child = []
        self.leaf = leaf

    def __str__(self, level=0):
        result = "  " * level + f"Level {level}: {self.key}\n"
        if not self.leaf:
            for c in self.child:
                result += c.__str__(level + 1)
        return result


class BTree:
    def __init__(self, minimum):
        self.root = BNode(True)
        self.minimum = minimum

    def display(self):
        print(self.root, end="")

    def insert(self, key):
        root = self.root
        t = self.minimum

        if len(root.key) == (2 * t) - 1:
            temp = BNode(False)
            temp.child.append(root)
            self.split_child(temp, 0)
            self.root = temp
            self.insert_non_full(temp, key)
        else:
            self.insert_non_full(root, key)

    def insert_non_full(self, node, value):
        i = len(node.key) - 1
        if node.leaf:
            node.key.append(None)
            while i >= 0 and value < node.key[i]:
                node.key[i + 1] = node.key[i]
                i -= 1
            node.key[i + 1] = value
        else:
            while i >= 0 and value < node.key[i]:
                i -= 1
            i += 1
            if len(node.child[i].key) == (2 * self.minimum) - 1:
                self.split_child(node, i)
                if value > node.key[i]:
                    i += 1
            self.insert_non_full(node.child[i], value)

    def split_child(self, node_parent, index):
        t = self.minimum
        node_to_split = node_parent.child[index]
        new_node = BNode(node_to_split.leaf)
        node_parent.key.insert(index, node_to_split.key[t - 1])
        node_parent.child.insert(index + 1, new_node)
        new_node.key = node_to_split.key[t:]
        node_to_split.key = node_to_split.key[:t - 1]
        if not node_to_split.leaf:
            new_node.child = node_to_split.child[t:]
            node_to_split.child = node_to_split.child[:t]


