# Partition
# Write code to partition a linked list around a value x, such that all nodes less than x co
# before all nodes greater than or equal to x If x is contained within the list, the values of x only n
# to be after the elements less than x is below). The partition element x can appear anywhere in the
# right partition it does not need to appear between the left and right partitions

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


def partition(link,z):
    dust = LinkedList()
    li = []
    for i in range(link.length):
        li.append(link.get(i).data)
    li.sort()
    left = li[:z]
    right = li[z:]
    for item in left:
        dust.append(item)
    for item in right:
        dust.append(item)
    return dust



link = LinkedList()
for i in range(r(1,20)):
    link.append(i)
for i in range(r(1,20)):
    link.append(i)
for i in range(r(1,20)):
    link.append(i)
print(f"list before partition: {link.print()}")
z = r(1,20)
print(f"partition number is: {z}")

link = partition(link,z)
print(f"The partitioned linked list is: {link.print()}")
