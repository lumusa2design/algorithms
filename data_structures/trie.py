

class TrieNode:
    def __init__(self, value):
        self.value = value
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode('')
    def insert(self, word):
        current  = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode(char)
            current = current.children[char]
        current.children['*'] = TrieNode('*')

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return '*' in current.children

    def delete(self, word):
        return self._delete(self.root, word, 0)

    def _delete(self, node, word, index):
        if index == len(word):
            if '*' in node.children:
                del node.children['*']
                return True
            else:
                return False
        else:
            char = word[index]
            if char not in node.children:
                return False
            else:
                child = node.children[char]
                deleted = self._delete(child, word, index + 1)
                if deleted and len(child.children) == 0:
                    del node.children[char]
                return deleted