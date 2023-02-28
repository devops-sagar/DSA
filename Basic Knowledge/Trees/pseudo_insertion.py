'''
Pseudo code for insertion of Node in BST
run in log(n) time complexity
'''

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

class BST(Node):

    def __init__(self, start):
        self.root = None

    def insert(self, current, data):
        
        if self.root == None:
            self.root = Node(data)

        else:
            if current < current.data:
                if current.left == None:
                    current.left = Node(data)
                else:
                    self.insert(current.left, data)             # Recursion in place to loop through Nodes which are in the way
            else:
                if current.right == None:
                    current.right = Node(data)
                else:
                    self.insert(current.right, data)            # Recursion in place to loop through Nodes which are in the way

