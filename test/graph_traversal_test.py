import unittest
from graph_traversal_algorithms import BFS
from graph_traversal_algorithms import DFS
from graph_traversal_algorithms import dijkstra_algorithm
import networkx as nx

def build_graph():
    g = nx.Graph()
    g.add_edge('A', 'B', weight=1)
    g.add_edge('A', 'C', weight=5)
    g.add_edge('B', 'C', weight=2)
    g.add_edge('C', 'D', weight=1)
    return g


class TestGraphTraversal(unittest.TestCase):

    def test_bfs(self):
        g = build_graph()
        order = BFS.BFS(g, 'A')
        self.assertEqual(order, ['A', 'B', 'C', 'D'])

    def test_dfs(self):
        g = build_graph()
        order = DFS.DFS(g, 'A')
        self.assertEqual(order[0], 'A')
        self.assertEqual(set(order), {'A', 'B', 'C', 'D'})

    def test_dijkstra(self):
        g = build_graph()
        path = dijkstra_algorithm.dijkstra(g, 'A', 'D')
        self.assertEqual(path, ['A', 'B', 'C', 'D'])

if __name__ == '__main__':
    unittest.main()
