import unittest
from lineal_search import linear_search
class SearchTestMethods(unittest.TestCase):
    def linear_Search_test(self):
        arr = [1,2,3,4,5,6,7]
        search = 5
        result  =  linear_search(arr, 5)
        print(result)
        self.assertTrue(result==4)
if __name__=='__main__':
    unittest.main()