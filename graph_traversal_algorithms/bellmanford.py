import math
from  data_structures.non_directed_graph import *


def bellmanford(graph, first_node):
    if first_node not in graph:
        raise ValueError

    min_distance = {node:math.inf for node in graph.nodes}
    predecesor = {node:None for node in graph.nodes}
    min_distance[first_node] = 0.0

    directed_edges = []
    for u,v, data in graph.edges(data=True):
        weight = float(data.get("weight", 1.0))
        directed_edges.append((u,v, weight))
        if not graph.is_directed():
            directed_edges.append((v,u,weight))

    num_nodes = len(graph.nodes)

    for _ in range(num_nodes-1):
        updated = False
        for u, v, weight in directed_edges:
            if min_distance[u] != math.inf and min_distance[u] + weight < min_distance[v]:
                min_distance[v] = min_distance[u] + weight
                predecesor[v] = u
                updated = True

        if not  updated:
            break

    for u, v, weight in directed_edges:
        if min_distance[u] != math.inf and min_distance[u] + weight < min_distance[v]:
            raise ValueError

    return min_distance, predecesor
