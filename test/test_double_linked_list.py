import unittest
from data_structures.double_linked_list import DoubleLinkedList

class TestDoubleLinkedList(unittest.TestCase):
    def test_add_and_remove(self):
        dl = DoubleLinkedList(1)
        dl.add_node(2)
        dl.add_node(3)
        self.assertEqual(str(dl), '1 <-> 2 <-> 3')
        removed = dl.remove_node_by_position(1)
        self.assertEqual(removed, 2)
        self.assertEqual(len(dl), 2)
        self.assertEqual(str(dl), '1 <-> 3')
        self.assertEqual(dl.find_node_by_position(1).value, 3)

if __name__ == '__main__':
    unittest.main()
