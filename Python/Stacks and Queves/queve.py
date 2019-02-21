class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def enqueue(self, data):
        node = Node(data)
        if not self.first:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1
        return self.length
    
    def dequeue(self):
        if not self.first:
            return None
        current = self.first
        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        self.length -= 1
        return current.data
