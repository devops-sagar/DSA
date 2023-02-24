# Binary Search Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

node = Node(10)

node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
