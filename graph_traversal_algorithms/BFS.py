from non_directed_graph import build_graph
from sys import maxsize
from data_structures.Queue import Queue
import networkx as nx

def BFS(graph, first_node):
    visited, viewed, queue = [], [], Queue()
    viewed.append(first_node)
    queue.enqueue(first_node)
    while not queue.is_empty():
        actual_node = queue.pop()
        if actual_node not in visited:
            visited.append(actual_node)



