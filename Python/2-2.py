#Return Kth to Last
#Implement an algorithm to find the nth to last element in a linked list
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


def get_nth(k):
    if k > link.length:
        return None
    if k == link.length:
        return link.removeHead().data
    if k == 0:
        return link.pop().data

    index = link.length -1 - k
    return link.get(index).data

link = LinkedList()
for i in range(r(1,15)):
    link.append(i)
print(f"link is: {link.print()}")
z = r(0,5)
print(f"k is: {z}")
j = get_nth(z)
print(f"the {z}th to last element is: {j}")
