import unittest
from auxiliar_functions import is_order
from merge_sort import merge_sort
from quick_sort import quicksort
from bogo_sort import bogo_sort
from bubble_sort import bubble_sort
class TestSortMethods(unittest.TestCase):
    def test_merge(self):
        arr = [10,9,8,7,6,42,1]
        arr = merge_sort(arr)
        self.assertTrue(is_order(arr))

    def test_quicksort(self):
        arr = [10, 9, 8, 7, 6, 42, 1]
        arr = quicksort(arr)
        self.assertTrue(is_order(arr))

    def test_bogosort(self):
        arr = [10, 9, 8, 7, 6, 42, 1]
        arr = bogo_sort(arr)
        self.assertTrue(is_order(arr))
    def test_bubblesort(self):
        arr = [10, 9, 8, 7, 6, 42, 1]
        arr = bubble_sort(arr)
        self.assertTrue(is_order(arr))

if __name__=='__main__':
    unittest.main()
