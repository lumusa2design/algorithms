import unittest
from sortings_algorithms.auxiliar_functions import is_order
from sortings_algorithms.merge_sort import merge_sort
from sortings_algorithms.quick_sort import quicksort
from sortings_algorithms.bogo_sort import bogo_sort
from sortings_algorithms.bubble_sort import bubble_sort
from sortings_algorithms.counting_sort import counting_sort
from sortings_algorithms.stalin_sort import stalin_sort
from sortings_algorithms.selection_sort import selection_sort
from sortings_algorithms.insertion_sort import insertion_sort

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

    def test_countingsort(self):
        arr = [10, 9, 8, 7, 6, 42, 1]
        arr = counting_sort(arr)
        self.assertTrue(is_order(arr))

    def test_insertionsort(self):
        arr = [10, 9, 8, 7, 6, 42, 1]
        arr = insertion_sort(arr)
        self.assertTrue(is_order(arr))

    def test_staling_sort(self):
        arr = [10, 9, 8, 7, 6, 42, 1]
        arr = stalin_sort(arr)
        self.assertTrue(is_order(arr))

    def test_selection_sort(self):
        arr = [10, 9, 8, 7, 6, 42, 1]
        arr = selection_sort(arr)
        self.assertTrue(is_order(arr))

    def test_insertion_sort(self):
        arr = [10, 9, 8, 7, 6, 42, 1]
        arr = insertion_sort(arr)
        self.assertTrue(is_order(arr))

if __name__=='__main__':
    unittest.main()
