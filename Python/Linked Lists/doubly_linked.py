class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        node = Node(data)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length += 1
        return self

    def pop(self):
        if not self.head:
            return None
        current = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = current.prev
            self.tail.next = None
            current.prev = None
        self.length -= 1
        return current

    def removeHead(self):
        if self.length == 0:
            return None
        current = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = current.next
            self.head.prev = None
            current.next = None
        self.length -= 1
        return current

    def addHead(self, data):
        node = Node(data)
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.length += 1
        return self

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        count = 0
        current = self.head
        if index <= self.length / 2:
            count = 0
            current = self.head
            while count != index:
                current = current.next
                count += 1
        else:
            count = self.length -1
            current = self.tail
            while count != index:
                current = current.prev
                count -= 1
        return current

    def set(self, index, data):
        found = self.get(index)
        if found != None:
            found.data = data
            return True
        return False

    def insert(self, index, data):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.addHead(data)
        if index == self.length:
            return self.append(data)
        node = Node(data)
        prev = self.get(index-1)
        next_node = prev.next

        prev.next = node
        node.prev = prev

        node.next = next_node
        next_node.prev = node

        self.length += 1
        return True

    def reverse(self):
        node = self.head
        while node != None:
            next_node = node.next
            node.next = node.prev
            node.prev = next_node
            node = next_node
        self.head, self.tail = self.tail, self.head
        return self
