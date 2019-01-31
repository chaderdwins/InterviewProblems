class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

class LinkedList:
    def __init__(self, root=None):
        self.root = root
        if root != None:
            self.size = 1
        else:
            self.size = 0

    def get_size(self):
        return self.size

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, find_data):
        current_node = self.root
        prev_node = None

        while current_node != None:
                if current_node.get_data() == find_data:
                    if prev_node != None:
                        prev_node.set_next(current_node.get_next())
                    else:
                        self.root = current_node.get_next()
                    self.size -= 1
                    return True
                else:
                    prev_node = current_node
                    current_node = current_node.get_next()
        return False

    def find(self, find_data):
        current_node = self.root
        while current_node != None:
            if current_node.get_data() == find_data:
                return find_data
            elif current_node.get_next() == None:
                return False
            else:
                current_node = current_node.get_next()

myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)
print("size="+str(myList.get_size()))
print(myList.remove(7))
print("size="+str(myList.get_size()))
print(myList.remove(12))
print("size="+str(myList.get_size()))
print(myList.find(5))
