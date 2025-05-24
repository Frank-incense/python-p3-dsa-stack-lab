class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = []
        self.limit = limit
        for item in items:
            self.items.append(item)

    def isEmpty(self):
        return False if len(self.items) else True

    def push(self, item):
        if self.limit > self.size():
            self.items.append(item)

    def pop(self):
        if self.items:
           return self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        return self.size() == self.limit

    def search(self, target):
        count = 0
        found = False
        if target not in self.items:
            return -1
        for item in self.items:
            if found:
                count += 1
            elif target == item:
                found = True
            
        return count