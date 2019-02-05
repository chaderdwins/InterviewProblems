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
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
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
        current_head = self.head
        self.head = current_head.next
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return current_head

    def addHead(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = self.head
        new_node.next = self.head
        self.head = new_node
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
        found_node = self.get(index)
        if found_node:
            found_node.data = data
            return True
        return False

    def insert(self, index, data):
        if index < 0 or index > self.length:
            return False
        if index == self.length:
            return self.append(data)
        if index == 0:
            return self.addHead(data)
        new_node = Node(data)
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = new_node
        new_node.next = temp
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.removeHead()
        if index == self.length - 1:
            return self.pop()
        previous_node = self.get(index - 1)
        removed = previous_node.next
        previous_node.next = removed.next
        self.length -= 1
        return removed

    def reverse(self):
        node = self.head
        self.head = self.tail
        self.tail = node
        prev = None
        for i in range(self.length):
            next = node.next
            node.next = prev
            prev = node
            node = next
        return self

    def print(self):
        li = ''
        current = self.head
        while current:
            li = li + str(current.data) + '->'
            current = current.next
        return li
