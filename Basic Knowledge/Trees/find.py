'''
- Simple representation of Insertion of Nodes in Binary Search Tree
- Simple representation of searching of specific node in Binary search tree
'''

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        
        print(self.data, data)                  # This line is for debuggiing purpose - Can tell you the cuurent values in process
        
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    
    def search(self, goal):
        print("------------------------Searching  Starts Here---------------------------")
        print(self.data, goal)                  # This line is for debuggiing purpose - Can tell you the cuurent values in process

        if self.data == goal:
            print("Found", goal)
            return self
        
        elif self.left and self.data > goal:
            print("Going left")                 # This line is for debuggiing purpose - To see which stage we are on
            return self.left.search(goal)
        
        elif self.right and self.data < goal:
            print("Going right")                # This line is for debuggiing purpose - To see which stage we are on
            return self.right.search(goal)
        
        else:
            print("Element Not found in tree")

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

root.search(31)
root.search(20)