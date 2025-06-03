import unittest
from data_structures.stack import Stack

class TestStack(unittest.TestCase):
    def test_basic_operations(self):
        s = Stack()
        self.assertTrue(s.is_empty())
        s.insert(1)
        s.insert(2)
        self.assertEqual(len(s), 2)
        self.assertEqual(s.head(), 2)
        self.assertEqual(s.tail(), 1)
        self.assertEqual(repr(s), '1 ->2')
        self.assertEqual(s.pop(), 2)
        self.assertEqual(len(s), 1)
        s.clear_stack()
        self.assertTrue(s.is_empty())

if __name__ == '__main__':
    unittest.main()
