import unittest
from data_structures.Queue import Queue

class TestQueue(unittest.TestCase):
    def test_is_empty(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue(1)
        self.assertFalse(q.is_empty())
        q.clear_queue()
        self.assertTrue(q.is_empty())

    def test_enqueue_dequeue(self):
        q = Queue()
        q.enqueue('a')
        q.enqueue('b')
        self.assertEqual(len(q), 2)
        self.assertEqual(q.dequeue(), 'a')
        self.assertEqual(len(q), 1)
        self.assertEqual(q.dequeue(), 'b')
        self.assertTrue(q.is_empty())

if __name__ == '__main__':
    unittest.main()
