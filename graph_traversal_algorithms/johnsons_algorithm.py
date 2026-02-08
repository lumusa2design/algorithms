import networkx as nx
import heapq
from graph_traversal_algorithms.dijkstra_algorithm import dijkstra_all
from graph_traversal_algorithms.bellmanford import bellmanford


def johnson(graph):
    G = graph.copy()
    q = "__q__"
    G.add_node(q)
    for v in graph.nodes(q):
        G.add_edge(q, v, weight=0)
    try:
        h, _ = bellmanford(G, q)
    except ValueError:
        raise ValueError("El grafo contiene un ciclo negativo")
    G.remove_node(q)
    G_reweighted = G.copy()

    for u, v, data in G_reweighted.edges(data=True):
        w = data.get("weight", 1.0)
        data["weight"] = w + h[u] - h[v]
    all_pairs_paths = {}
    all_pairs_distances = {}

    for u in G_reweighted.nodes:
        distances, previous = dijkstra_all(G_reweighted, u)
        all_pairs_distances[u] = {
            v: distances[v] - h[u] + h[v]
            for v in distances
        }
    return all_pairs_distances, all_pairs_paths
