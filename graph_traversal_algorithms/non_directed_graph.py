import networkx as nx
def build_graph():
    num_nodes, num_edges = map(int, input().split())
    graph = nx.Graph()
    for i in range(1, num_nodes+1):
        graph.add_node(i)
    for i in range(num_edges):
        graph.add_edge(*map(int, input().split()))
    return graph


def build_graph_with_weights():
    num_nodes, num_edges = map(int, input("Número de nodos y aristas: ").split())
    graph = nx.Graph()
    for i in range(1, num_nodes + 1):
        graph.add_node(i)
    print("Introduce las aristas con peso (formato: nodo1 nodo2 peso):")
    for _ in range(num_edges):
        u, v, w = input().split()
        graph.add_edge(int(u), int(v), weight=float(w))  # float(w) por si el peso no es entero
    return graph