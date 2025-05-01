from non_directed_graph import build_graph
from sys import maxsize
from data_structures.Queue import Queue
import networkx as nx

def BFS(graph, first_node):
    visited, viewed, queue = [], set(), Queue()
    viewed.add(first_node)
    queue.enqueue(first_node)

    while not queue.is_empty():
        actual_node = queue.dequeue()
        visited.append(actual_node)
        for neighbour in graph.neighbors(actual_node):
            if neighbour not in viewed:
                viewed.add(neighbour)
                queue.enqueue(neighbour)
    return visited



