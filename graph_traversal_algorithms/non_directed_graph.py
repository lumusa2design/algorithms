import networkx as nx
def build_graph():
    num_nodes, num_edges = map(int, input().split())
    graph = nx.Graph()
    for i in range(1, num_nodes+1):
        graph.add_node(i)
    for i in range(num_edges):
        graph.add_edge(*map(int, input().split()))
    return graph