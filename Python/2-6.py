# Palindrome
# Implement a function that checks if a linked list is a palindrome

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

def palindrome(link):
    li = []
    for i in range(link.length):
        li.append(link.get(i).data)
    return li == li[::-1]

link = LinkedList()
for i in range(10):
    link.append(i)
for i in range(10,-1,-1):
    link.append(i)
# link.append('h')
# link.append('h')
# link.append('l')
# link.append('l')
# link.append('o')
# link.append('o')
# link.append('h')
print(f"link is: {link.print()}")
print(palindrome(link))
