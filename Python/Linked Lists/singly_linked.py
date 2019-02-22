class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1
        return self

    def pop(self):
        if not self.head:
            return None
        current = self.head
        new_tail = current
        while current.next:
            new_tail = current
            current = current.next
        self.tail = new_tail
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return current

    def removeHead(self):
        if not self.head:
            return None
        current = self.head
        self.head = current.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return current

    def addHead(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.tail = self.head
        node.next = self.head
        self.head = node
        self.length += 1
        return self

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        counter = 0
        current = self.head
        while counter != index:
            current = current.next
            counter += 1
        return current

    def set(self, index, data):
        found = self.get(index)
        if found:
            found.data = data
            return True
        return False

    def insert(self, index, data):
        if index < 0 or index > self.length:
            return False
        if index == self.length:
            return self.append(data)
        if index == 0:
            return self.addHead(data)
        node = Node(data)
        prev = self.get(index - 1)
        current = prev.next
        prev.next = node
        node.next = current
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.removeHead()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        current = prev.next
        prev.next = current.next
        self.length -= 1
        return current

    def reverse(self):
        current = self.head
        self.head = self.tail
        self.tail = current
        prev = None
        for i in range(self.length):
            next = current.next
            current.next = prev
            prev = current
            current = next
        return self
