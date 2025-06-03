import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'data_structures'))
import linked_list

class TestLinkedList(unittest.TestCase):
    def test_operations(self):
        ll = linked_list.Simple_Linked_List(1)
        ll.add_node(2)
        ll.add_node(3)
        self.assertEqual(len(ll), 3)
        self.assertEqual(str(ll), '1, 2, 3')
        self.assertEqual(ll.find_node_by_position(1).value, 2)
        ll.remove_node_by_position(1)
        self.assertEqual(len(ll), 2)
        self.assertEqual(str(ll), '1, 3')
        self.assertEqual(ll.find_node_by_position(1).value, 3)

if __name__ == '__main__':
    unittest.main()
