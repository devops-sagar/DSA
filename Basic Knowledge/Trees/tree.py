# Binary Search Tree

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

node = Node(10)

node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(1000)

'''
Line 9 to 18 will generate the following tree:

                                            10(node)
                                           /  \   
                               (node.left)5    15(node.right)
                                         / \   / \
                        (node.left.left)2   6 13  1000 (node.right.right)
                            (node.left.right)(node.right.left)

'''

print(node.right.data)


my_tree = node.left
print(my_tree.data)