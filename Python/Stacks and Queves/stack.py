class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def append(self, data):
        node = Node(data)
        if not self.first:
            self.first = node
            self.last = node
        else:
            temp = self.first
            self.first = node
            self.first.next = temp
        self.length += 1
        return self
    
    def pop(self):
        if not self.first:
            return None
        temp = self.first
        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        self.length -= 1
        return temp.data
