class Heap:
    def __init__(self):
        self.heap = []
    @staticmethod
    def _father(value):
        return (value - 1)//2

    @staticmethod
    def _left( value):
        return 2 * value + 1

    @staticmethod
    def _right( value):
        return 2 * value +2

    def __len__(self):
        return len(self.heap)

    def _float_function(self, value):
        while value > 0 and self.heap[value] < self.heap[self._father(value)]:
            self.heap[value], self.heap[self._father(value)] = self.heap[self._father(value)], self.heap[value]
            value = self._father(value)
    def _sink(self, index):
        smallest = index
        left = self._left(index)
        right = self._right(index)

        if left < len(self) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._sink(smallest)

    def insert(self, value):
        self.heap.append(value)
        self._float_function(len(self)-1)

    def extract(self):
        if not self:
            return None

        if len(self) ==1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink(0)
        return root

    def peek(self):
        return self.heap[0] if self else None
