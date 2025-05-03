class Stack:
    def __init__(self):
        self.length = 0
        self.elements = []

    def insert(self, e):
        self.elements.append(e)
        self.length+=1

    def pop(self):
        self.length-=1
        return self.elements.pop()

    def __len__(self):
        return self.length

    def is_empty(self):
        if(self.length == 0):
            return True
        return False
    def clear_stack(self):
        self.elements = []
        self.length = 0

    def head(self):
        return self.elements[-1]

    def tail(self):
        return self.elements[0]
    def __repr__(self):
        repre = ""
        for i in range(len(self)):
            if(i < len(self)-1):
                repre += f"{self.elements[i]} ->"
            else:
                repre += f"{self.elements[i]}"
        return repre

