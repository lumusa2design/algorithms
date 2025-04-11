import unittest
import queue


class TestSortMethods(unittest.TestCase):
    def test_queue(self):
        cola = queue.Queue()
        cola.queue.enqueue(1)
        cola.queue.enqueue(2)
        cola.queue.enqueue(3)
        self.assertTrue(cola.queue.dequeue() == 1)
        print(cola)

if __name__ == "__main__":
    unittest.main()