class FenwickTree:
    def __init__(self, values: list[int]):
        self.values = values[:]
        self.size = len(values)
        self.tree = [0] * (self.size + 1)

        for i, value in enumerate(values):
            self._add(i + 1, value)

    def _add(self, index: int, delta: int) -> None:
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def add(self, index: int, delta: int) -> None:
        self.values[index - 1] += delta
        self._add(index, delta)

    def set(self, index: int, value: int) -> None:
        delta = value - self.values[index - 1]
        self.values[index - 1] = value
        self._add(index, delta)

    def prefix_sum(self, index: int) -> int:
        result = 0

        while index > 0:
            result += self.tree[index]
            index -= index & -index

        return result

    def range_sum(self, left: int, right: int) -> int:
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

