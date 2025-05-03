from data_structures.stack import Stack
import networkx as nx
def DFS(graph, first_node):
    visited, viewed, stack = [], set(), Stack()
    viewed.add(first_node)
    stack.insert(first_node)

    while not stack.is_empty():
        actual_node = stack.pop()
        visited.append(actual_node)
        for neighbour in graph.neighbors(actual_node):
            if neighbour not in viewed:
                viewed.add(neighbour)
                stack.insert(neighbour)
    return visited


g = nx.Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('C', 'E')

visited_nodes = DFS(g, 'A')
print(visited_nodes)
