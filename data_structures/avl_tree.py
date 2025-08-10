from data_structures.node import Node

class AVL_Node(Node):
    def __init__(self, value, left = None, right=None, parent=None):
        super().__init__(value, left, right)
        self.parent = parent
        self.height = 1

class AVL_Tree:
    def __init__(self):
        self.root = None
        self.length = 0

    def get_height(self, node):
        return node.height if node else 0
    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left),self.get_height(node.right))
    def get_balance_factor(self, node):
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, root_node):
        new_root = root_node.right
        orphan_subtree = new_root.left

        new_root.left, root_node.right = root_node, orphan_subtree
        new_root.parent, root_node.parent = root_node.parent, new_root
        if orphan_subtree:
            orphan_subtree.parent = root_node

        if new_root.parent is None:
            self.root = new_root
        else:
            if new_root.parent.left is root_node:
                new_root.parent.left = new_root
            else:
                new_root.parent.right = new_root

        self.update_height(root_node)
        self.update_height(new_root)

        return new_root

    def rotate_right(self, root_node):
        new_root = root_node.left
        orphan_subtree = new_root.right

        new_root.right = root_node
        root_node.left = orphan_subtree

        new_root.parent = root_node.parent
        root_node.parent = new_root
        if orphan_subtree:
            orphan_subtree.parent = root_node

        if new_root.parent is None:
            self.root = new_root
        else:
            if new_root.parent.left is root_node:
                new_root.parent.left = new_root
            else:
                new_root.parent.right = new_root

        self.update_height(root_node)
        self.update_height(new_root)

        return new_root

    def rebalance(self, node):
        self.update_height(node)
        balance_factor = self.get_balance_factor(node)
        if balance_factor > 1 and self.get_balance_factor(node.left) >= 0:
            return self.rotate_right(node)
        if balance_factor > 1 and self.get_balance_factor(node.left) < 0:
            node.left = self.rotate_left(node.left)
            node.left.parent = node
            return self.rotate_right(node)
        if balance_factor < -1 and self.get_balance_factor(node.right) <= 0:
            return self.rotate_left(node)
        if balance_factor < -1 and self.get_balance_factor(node.right) > 0:
            node.right = self.rotate_right(node.right)
            node.right.parent = node
            return self.rotate_left(node)
        return node

    def insert(self, value):
        if self.root is None:
            self.root = AVL_Node(value)
            self.size = 1
            return

        def _insert(current_node, value):
            if current_node is None:
                self.size += 1
                return AVL_Node(value)

            if value < current_node.value:
                new_child = _insert(current_node.left, value)
                if current_node.left is not new_child:
                    current_node.left = new_child
                    new_child.parent = current_node
            elif value > current_node.value:
                new_child = _insert(current_node.right, value)
                if current_node.right is not new_child:
                    current_node.right = new_child
                    new_child.parent = current_node
            else:
                return current_node

            return self.rebalance(current_node)

        self.root = _insert(self.root, value)
        self.root.parent = None
    def search(self, value):
        current_node = self.root
        while current_node:
            if value == current_node.value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return None
    def inorder_traversal(self):
        result = []
        def _inorder(node):
            if not node:
                return
            _inorder(node.left)
            result.append(node.value)
            _inorder(node.right)
        _inorder(self.root)
        return result


