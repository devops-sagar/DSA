class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
           
    def search(self, goal):
        if self.data == goal:
            print("Found", goal)
            return self
        elif self.left and self.data > goal:
            print("Going left")
            return self.left.search(goal)
        elif self.right and self.data < goal:
            print("Going right")
            return self.right.search(goal)
        else:
            print("Element Not found in tree")
    
    def pre_order(self):
        print(self.data)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()

    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.data)
        if self.right:
            self.right.in_order()

    def post_order(self):
        if self.left:
            self.left.post_order()
        if self.right:
            self.right.post_order()
        print(self.data)

class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name
    
    def search(self, goal):
        return self.root.search(goal)
    
    def pre_order(self):
        self.root.pre_order()

    def in_order(self):
        self.root.in_order()

    def post_order(self):
        self.root.post_order()

node = Node(10)

node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(1000)

'''
Line 44 to 53 will generate the following tree:

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
# print(myTree.root.data)             # Now access the data with myTree.root object instead of node object
# print(myTree.root.right.right.data) # likewise access all other nodes in the tree

try:
    found = myTree.search(12)    # Search for an element in the tree
    print(found.data)
except AttributeError as e:
    # print(e)
    print("Element not found")

print("Pre Order:------------")
myTree.pre_order()

print("In Order:-------------")
myTree.in_order()

print("Post Order:-----------")
myTree.post_order()