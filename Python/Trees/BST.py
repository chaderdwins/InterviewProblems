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
        while current:
            if data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right
            else:
                return True
        return False
    
    def find(self, data):
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
                found = True
        if not found:
            return None
        return current
    
    def BFS(self):
        node = self.root
        li, queue = [], []
        queue.append(node)
        while queue:
            node = queue.pop(0)
            li.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return li
    
    def DFSPreOrder(self):
        li = []
        def traverse(node):
            li.append(node.data)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return li

    def DFSPostOrder(self):
        li = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            li.append(node.data)
        traverse(self.root)
        return li
    
    def DFSInOrder(self):
        li = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            li.append(node.data)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return li
            