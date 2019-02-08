#Delete Middle Node
# implement an algorithm to delete a node in the middle(i.e. any node but the head or tail)
# of a singly linked list.
from random import randint as r
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
            self.tail = new_node
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
            self.head = None
            self.tail = None
        return current_head

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        counter = 0
        current = self.head
        while counter != index:
            current = current.next
            counter += 1
        return current

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == self.length:
            return self.pop()
        if index == 0:
            return self.removeHead()
        previous_node = self.get(index-1)
        removed = previous_node.next
        previous_node.next = removed.next
        self.length -= 1
        return removed

    def print(self):
        s = ''
        current = self.head
        while current:
            s = s + str(current.data) + '->'
            current = current.next
        return s


link = LinkedList()
for i in range(r(1,15)):
    link.append(i)
print(f"list before removal: {link.print()}")
z = r(1,link.length-2)
print(f"index is: {z}")
link.remove(z)
print(link.print())
