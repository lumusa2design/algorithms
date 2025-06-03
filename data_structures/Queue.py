class Queue:
    def __init__(self):
        self.length = 0
        self.elements = []

    def enqueue(self, e):
        self.elements.insert(0, e)
        self.length +=1

    def dequeue(self):
        self.length -=1
        return self.elements.pop()

    def is_empty(self):
        return self.length == 0

    def head(self):
        return self.elements[-1]

    def tail(self):
        return self.elements[0]

    def clear_queue(self):
        self.elements = []
        self.length = 0

    def __len__(self):
        return self.length

    def __repr__(self):
        repre = ""
        for i in range(len(self)):
            if(i < len(self)-1):
                repre += f"{self.elements[i]} ->"
            else:
                repre += f"{self.elements[i]}"
        return repre




