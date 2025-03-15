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
        if(self.length == 0):
            return True

    def head(self):
        return self.elements[-1]

    def tail(self):
        return self.elements[0]

    def clear_queue(self):
        self.elements = []

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



cola = Queue()
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
print(cola)
print(cola.dequeue())
print(cola)

