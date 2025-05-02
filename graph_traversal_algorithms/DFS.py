from data_structures.stack import Stack

def DFS(graph, first_node):
    visited, viewed, queue = [], set(), Stack()
    viewed.add(first_node)