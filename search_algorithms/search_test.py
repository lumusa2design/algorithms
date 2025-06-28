import unittest
from lineal_search import linear_search
from binary_search import  binary_search
from search_algoritms_main import f
from numerical_algorithms.bisection_method import bisection_method
class SearchTestMethods(unittest.TestCase):
    def test_lineal_search(self):
        arr = [1,2,3,4,5,6,7]
        search = 5
        result  =  linear_search(arr, search)
        self.assertTrue(result==arr.index(search))
    def test_binary_search(self):
        arr = [1,2,3,4,5,6,7,8]
        search = 5
        result = binary_search(arr, search)
        self.assertTrue(result==arr.index(search))

if __name__=='__main__':
    unittest.main()