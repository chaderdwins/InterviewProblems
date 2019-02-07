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
        new_node = Node(data)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return self

    def pop(self):
        if not self.head:
            return None
        pop_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = pop_node.prev
            self.tail.next = None
            pop_node.prev = None
        self.length -= 1
        return pop_node

    def removeHead(self):
        if self.length == 0:
            return None
        old_head = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = old_head.next
            self.head.prev = None
            old_head.next = None
        self.length -= 1
        return old_head

    def addHead(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
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
        found_node = self.get(index)
        if found_node != None:
            found_node.data = data
            return True
        return False

    def insert(self, index, data):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.addHead(data)
        if index == self.length:
            return self.append(data)
        new_node = Node(data)
        b4_node = self.get(index-1)
        after_node = b4_node.next

        b4_node.next = new_node
        new_node.prev = b4_node

        new_node.next = after_node
        after_node.prev = new_node

        self.length += 1
        return True

    def reverse(self):
        node = self.head
        while node != None:
            next = node.next
            node.next = node.prev
            node.prev = next
            node = next
        self.head, self.tail = self.tail, self.head
        return self
