import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'graph_traversal_algorithms'))
import BFS
import DFS
import dijkstra_algorithm
import networkx as nx

class TestGraphTraversal(unittest.TestCase):
    def build_graph(self):
        g = nx.Graph()
        g.add_edge('A', 'B', weight=1)
        g.add_edge('A', 'C', weight=5)
        g.add_edge('B', 'C', weight=2)
        g.add_edge('C', 'D', weight=1)
        return g

    def test_bfs(self):
        g = self.build_graph()
        order = BFS.BFS(g, 'A')
        self.assertEqual(order, ['A', 'B', 'C', 'D'])

    def test_dfs(self):
        g = self.build_graph()
        order = DFS.DFS(g, 'A')
        self.assertEqual(order[0], 'A')
        self.assertEqual(set(order), {'A', 'B', 'C', 'D'})

    def test_dijkstra(self):
        g = self.build_graph()
        path = dijkstra_algorithm.dijkstra(g, 'A', 'D')
        self.assertEqual(path, ['A', 'B', 'C', 'D'])

if __name__ == '__main__':
    unittest.main()
