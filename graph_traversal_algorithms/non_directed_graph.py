import networkx as nx
import matplotlib.pyplot as plt
def build_graph():

    num_nodes, num_edges = map(int, input().split())

    graph = nx.Graph()
    for i in range(1, num_nodes+1):
        graph.add_node(i)

    for i in range(num_edges):
        graph.add_edge(*map(int, input().split()))

    return graph


G = build_graph()

pos = nx.spring_layout(G)

node_values = list(G.nodes())

plt.figure(figsize=(6,6))
nx.draw(
    G,
    pos,
    node_color=node_values,
    cmap=plt.cm.viridis,
    node_size=300,
    width=2,
    with_labels=True,
)
plt.axis('off')
plt.show()
