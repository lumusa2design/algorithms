import unittest
import queue


class TestSortMethods(unittest.TestCase):
    def test_queue(self):
        my_queue = queue.Queue()
        my_queue.queue.enqueue(1)
        my_queue.queue.enqueue(2)
        my_queue.queue.enqueue(3)
        self.assertTrue(my_queue.queue.dequeue() == 1)
        print(my_queue)

if __name__ == "__main__":
    unittest.main()