import unittest
from auxiliar_functions import is_order
from merge_sort import merge_sort

class TestSortMethods(unittest.TestCase):
    def test_merge(self):
        arr = [10,9,8,7,6,42,1]
        arr = merge_sort(arr)
        self.assertTrue(is_order(arr))

if __name__=='__main__':
    unittest.main()
