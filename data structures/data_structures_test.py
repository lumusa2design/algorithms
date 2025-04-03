import unittest
import queue
from queue import Queue


class TestSortMethods(unittest.TestCase):
    def Queue_test(self):
        cola = Queue()
        cola.enqueue(1)
        cola.enqueue(2)
        cola.enqueue(3)
        self.assertTrue(cola.dequeueu)
        print(cola)

if __name__ == "__main__":
    unittest.main()