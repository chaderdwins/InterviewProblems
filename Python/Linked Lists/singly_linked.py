# reference: https://www.youtube.com/watch?v=Bd1L64clh34
#https://github.com/joeyajames/Python

# implementing a singly linked list using python 3
class Node:
    #constructor
    def __init__(self, data, next_node=None):
        self.data = data #data value for the node
        self.next_node = next_node #optional pointer for next Node

    #this class method will return the pointer to the next node
    def get_next(self):
        return self.next_node

    #this method will set the pointer to the next node
    def set_next(self, next_node):
        self.next_node = next_node

    #this method returns the data from the node
    def get_data(self):
        return self.data

    #this method will set the data for the node
    def set_data(self, data):
        self.data = data

class LinkedList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0 #this variable tracks the size of our linked list

    #this function returns the size of our linked list
    def get_size(self):
        return self.size

    #this function will add a node to our linked list at the very beginning
    def add(self, data):
        #self.root is the next node that this new node will point to
        new_node = Node(data, self.root) #creating a new node with the passed in data
        self.root = new_node #set the new root to this new_node
        self.size += 1 #increment the size of our linked list by 1

    #this function will search for and remove a node
    def remove(self, find_data): #data is what we want to remove
        current_node = self.root #we start our search at the root node
        prev_node = None #previous is initially none since we begin at root

        while current_node != None: #while we are not at the end of list
                if current_node.get_data() == find_data:
                    if prev_node != None: #check if we are in root node
                        #bypassing current node and setting previous node pointer
                        #to match the next node (from current)
                        prev_node.set_next(current_node.get_next())
                    else: # we are in the root node
                        self.root = current_node.get_next() #set root pointer to next Node
                    self.size -= 1 #decrement the linked list size
                    return True #mission complete
                else: #couldn't find the data so we traverse the list by incrementing
                    prev_node = current_node #shifting down the list
                    current_node = current_node.get_next()
        return False #data not in the linked list

    def find(self, find_data):
        current_node = self.root
        while current_node != None:
            if current_node.get_data() == find_data: #check if data in current node
                return find_data
            elif current_node.get_next() == None: #check if we are at tail
                return False
            else:
                current_node = current_node.get_next() #traverse the list, increment

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
