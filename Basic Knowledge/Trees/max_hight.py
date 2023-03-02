'''
- Simple representation of Insertion of Nodes in Binary Search Tree
- getting the maximum height of a tree
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
    
    def height(self, h=0):

        # if self.left:
        #     left_height = self.left.height(h+1)
        # else:
        #     left_height = h

        # if self.right:
        #     right_height = self.right.height(h+1)
        # else:
        #     right_height = h

        # return max(left_height, right_height)
        
        left_height = self.left.height(h+1) if self.left else h         # Same code as above but with 3 lines only
        right_height = self.right.height(h+1) if self.right else h
        return max(left_height, right_height)
    
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)

print(root.height())