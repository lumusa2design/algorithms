class segment_tree:
    def __init__(self, data, func=min, default=float('inf')):
        self.n = len(data)
        self.func = func
        self.default = default
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [default] * (2 * self.size)
        self.build(data)

    def build(self, data):
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, index, value):
        # Update the leaf node
        pos = index + self.size
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.func(self.tree[2 * pos], self.tree[2 * pos + 1])

    def query(self, left, right):
        res = self.default
        left += self.size
        right += self.size

        while left < right:
            if left % 2 == 1:
                res = self.func(res, self.tree[left])
                left += 1
            if right % 2 == 1:
                right -= 1
                res = self.func(res, self.tree[right])