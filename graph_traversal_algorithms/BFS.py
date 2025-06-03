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

def BFS_find_way(graph, first_node, goal):
    visited, viewed, queue, iter = [], set(), Queue(), 0
    viewed.add(first_node)
    queue.enqueue(first_node)

    while not queue.is_empty() and goal not in visited:
        actual_node = queue.dequeue()
        iter+=1
        visited.append(actual_node)
        for neighbour in graph.neighbors(actual_node):
            if neighbour not in viewed:
                viewed.add(neighbour)
                queue.enqueue(neighbour)
    print(f"Numero de iteraciones: {iter}\n")
    return visited





