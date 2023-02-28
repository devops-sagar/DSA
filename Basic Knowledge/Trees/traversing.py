'''
- Simple representation of Insertion of Nodes in Binary Search Tree
- Simple representation of Traversing a Binary Search Tree
    * In order Traversing
    * Pre Order Travesring
    * Post Order Traversing 
'''

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        
        print(self.data, data)                  # This line is for debugging purpose - Can tell you the cuurent values in process
        
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

    def iot(self):                              # In Order Traversing
        if self.left:                           # Left -> Visit -> Right
            self.left.iot()
        print(self.data)
        if self.right:
            self.right.iot()

    def preot(self):                            # Pre Order Traversing
        print(self.data)                        # Visit -> Left -> Right
        if self.left:
            self.left.preot()
        if self.right:
            self.right.preot()

    def posot(self):                            # Post Order Traversing
        if self.left:                           # Left -> Right -> Visit
            self.left.posot()
        if self.right:
            self.right.posot()
        print(self.data)

# root = Node(27)
# root.insert(14)
# root.insert(35)
# root.insert(10)
# root.insert(19)
# root.insert(31)
# root.insert(42)

root = Node(50)
root.insert(25)
root.insert(10)
root.insert(5)
root.insert(13)
root.insert(35)
root.insert(30)
root.insert(42)
root.insert(75)

print(f"-------------------------------------------")
print(f"In-Order Traversing")
print(f"-------------------------------------------")
root.iot()

print(f"-------------------------------------------")
print(f"Pre-Order Traversing")
print(f"-------------------------------------------")
root.preot()

print(f"-------------------------------------------")
print(f"Post-Order Traversing")
print(f"-------------------------------------------")
root.posot()
