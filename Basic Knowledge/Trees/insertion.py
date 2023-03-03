'''
- Simple representation of Insertion of Nodes in Binary Search Tree
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

# root = Node(27)
# root.insert(14)
# root.insert(35)
# root.insert(10)
# root.insert(19)
# root.insert(31)
# root.insert(42)

obj = None
l = [7, 3, 12, 1, 5, 9, 15]                     # Also, can use list of items to iterate over instead of inserting multiple times
root = Node(l[0])

for value in l:
    obj = root.insert(value)