class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        node = Node(data)
        if not self.root:
            self.root = node
            return self
        current = self.root
        while True:
            if data == current.data:
                return None
            if data < current.data:
                if current.left == None:
                    current.left = node
                    return self
                current = current.left
            else:
                if current.right == None:
                    current.right = node
                    return self
                current = current.right
    
    def contains(self, data):
        if not self.root:
            return False
        current = self.root
        found = False
        while current and not found:
            if data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right
            else:
                return True
        return False