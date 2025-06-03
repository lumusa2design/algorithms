import unittest
import sys
import os

from search_algorithms.binary_conversion import dec_to_binary
from search_algorithms.lineal_search import linear_search

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'search_algorithms'))
from search_algorithms import binary_search, lineal_search, fibonacci, bisection_method, newton_raphson_method, secant_method, lineal_search

class TestSearchAlgorithms(unittest.TestCase):
    def test_linear_and_binary_search(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(linear_search(arr, 4), 3)
        self.assertEqual(binary_search.binary_search(arr, 4), 3)
        self.assertEqual(binary_search.binary_search([3,1,2], 2), -1)

    def test_fibonacci(self):
        self.assertEqual(fibonacci.fibonacci(5), 5)
        self.assertEqual(fibonacci.fibonacci(1), 1)

    def test_binary_conversion(self):
        self.assertEqual(dec_to_binary(10), '1010')
        self.assertEqual(dec_to_binary(0), '0')

    def test_root_methods(self):
        f = lambda x: x**2 - 4
        self.assertAlmostEqual(bisection_method.bisection_method(f, 0, 3), 2, places=6)
        self.assertAlmostEqual(secant_method.secant_method(f, 1, 3), 2, places=6)
        nr = newton_raphson_method.newton_raphson(f, 1.0, 100)
        self.assertAlmostEqual(nr, 2, places=6)

if __name__ == '__main__':
    unittest.main()
