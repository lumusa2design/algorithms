from .bellmanford import bellmanford


def extend_graph_for_johnson(graph):
    extended = graph.copy()
    q = 0  # nodo ficticio (no usado por el usuario)
    extended.add_node(q)

    for node in graph.nodes:
        extended.add_edge(q, node, weight=0.0)

    return extended, q


def reweight_graph(graph, h):
    reweighted = graph.copy()
    for u, v, data in graph.edges(data=True):
        w = data.get("weight", 1.0)
        reweighted[u][v]["weight"] = w + h[u] - h[v]
    return reweighted


def dijkstra_distance(graph, source):
    distances = {node: float('inf') for node in graph.nodes}
    distances[source] = 0
    visited = set()

    while len(visited) < len(graph.nodes):
        min_node = None
        min_dist = float('inf')

        for node in graph.nodes:
            if node not in visited and distances[node] < min_dist:
                min_dist = distances[node]
                min_node = node

        if min_node is None:
            break

        visited.add(min_node)

        for neighbor in graph.neighbors(min_node):
            if neighbor in visited:
                continue
            w = graph[min_node][neighbor].get("weight", 1)
            if distances[min_node] + w < distances[neighbor]:
                distances[neighbor] = distances[min_node] + w

    return distances


def johnson(graph):
    extended_graph, q = extend_graph_for_johnson(graph)
    h, _ = bellmanford(extended_graph, q)

    reweighted = reweight_graph(graph, h)

    all_pairs = {}
    for u in graph.nodes:
        dist = dijkstra_distance(reweighted, u)
        all_pairs[u] = {
            v: dist[v] - h[u] + h[v]
            for v in dist
        }

    return all_pairs

from data_structures.non_directed_graph import build_graph_with_weights
graph = build_graph_with_weights()

distances = johnson(graph)

print("\nAll-pairs shortest paths:")
for u in distances:
    print(f"From {u}: {distances[u]}")