# Sum Lists
# You have two numbers represented by a linked list, where each node contains a single
# dialt. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list
# EXAMPLE
# Input: (7-> 1->6) + (5-> 9 > 2). That is, 617 +295
# Output: 2 -> 1 -> 9. That is, 912

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

def summation(link, zinc):
    li , zi = [] , []
    for i in range(link.length):
        li.append(link.get(i).data)
    for i in range(zinc.length):
        zi.append(zinc.get(i).data)
    li = li[::-1]
    zi = zi[::-1]
    for i in range(len(li)):
        li[i] = str(li[i])
    for i in range(len(zi)):
        zi[i] = str(zi[i])
    almost_there = str(int(''.join(li)) + int(''.join(zi)))[::-1]
    final = LinkedList()
    for item in almost_there:
        final.append(int(item))
    return final

link = LinkedList()
zinc = LinkedList()
for i in range(1, r(1,10)):
    link.append(i)
for i in range(1,r(1,10)):
    zinc.append(i)
print(f"link before summation: {link.print()}")
print(f"zinc before summation: {zinc.print()}")


link = summation(link, zinc)
print(f"The sum linked list is: {link.print()}")
