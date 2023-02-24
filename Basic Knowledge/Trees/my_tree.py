# Binary Search Tree

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

node = Node(10)

node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(1000)

'''
Line 9 to 18 will generate the following tree:

                                          (node)
                                            10
                                           /  \   
                              (node.left) 5    15 (node.right)
                                         / \   / \
                       (node.left.left) 2   6 13  1000 (node.right.right)
                                           /   \
                            (node.left.right)(node.right.left)

'''

myTree = Tree(node, 'Sagar')        # Create a tree with root node and name of the tree (Meta-Data of a tree)   
print(myTree.root.data)             # Now access the data with myTree.root object instead of node object
print(myTree.root.right.right.data) # likewise access all other nodes in the tree