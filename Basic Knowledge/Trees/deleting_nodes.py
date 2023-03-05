'''
- Hard to understand the printing of tree as it consist of lot many calculations and formulae
- Deleting Nodes from the tree using RTMM (Right Tree Find Minimum) for two child Node, one child node and zero child node
'''

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        
        # print(self.data, data)                                           # This line is for debuggiing purpose - Can tell you the cuurent values in process
        
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
    
    def node_at_depth(self, depth, nodes = []):
        if depth == 0:
            nodes.append(self.data)
            return nodes
        
        if self.left:
            self.left.node_at_depth(depth - 1, nodes)
        else:
            nodes.extend([None] * 2 ** (depth - 1))

        if self.right:
            self.right.node_at_depth(depth - 1, nodes)
        else:
            nodes.extend([None] * 2 ** (depth - 1))
        
        return nodes
    
    def height(self, h = 0):
        left_height = self.left.height(h+1) if self.left else h          # Same code as above but with 3 lines only
        right_height = self.right.height(h+1) if self.right else h
        return max(left_height, right_height)
    
    def _nodeToChar(self, n, spacing):
        if n is None:
            return 'x'+(' '*spacing)
        spacing = spacing-len(str(n))+1
        return str(n)+(' '*spacing)
    
    def print(self):
        # print(self.name+'#'+label)
        print('')
        print(f"self.root = {self.data}")
        height = self.height()
        print(f"Height = {height}")
        spacing = 3
        width = int((((2**height)-1) * (spacing+1)) + 1)
        print(f"Width = {width}")
        # Root offset
        offset = int((width-1)/2)
        print(f"Offset = {offset}")
        print('')
        for depth in range(0, height+1):
            if depth > 0:
                # print directional lines
                print(' '*(offset+1)  + (' '*(spacing+2)).join(['/' + ('-'*(spacing-2)) + '\\']*(2**(depth-1))))
            row = self.node_at_depth(depth, [])
            print((' '*offset)+''.join([self._nodeToChar(n, spacing) for n in row]))
            spacing = offset+1
            offset = int(offset/2) - 1
        print('')
    
    def findmin(self):                                                   # Helper function for deleting nodes
        if self.left:
            return self.left.findmin()
        return self
    
    def delete(self, target):

        if self.data == target:
            if self.right and self.left:                                 # RTFM - Right Tree Find Minimum
                minValue = self.right.findmin()
                self.data = minValue.data
                self.right = self.right.delete(minValue.data)
                return self
            else:
                return self.right or self.left
        
        if self.right and target > self.data:
            self.right = self.right.delete(target)
        
        if self.left and target < self.data:
            self.left = self.left.delete(target)
        
        return self
    
    def isBalanced(self):
        left_height = self.left.height() + 1 if self.left else 0
        right_height = self.right.height() + 1 if self.right else 0
        return abs(left_height - right_height) < 2


# obj = None
l = [50, 25, 75, 67, 100, 80, 120, 92]                                   # Also, can use list of items to iterate over instead of inserting multiple times
root = Node(l[0])

for value in l:
    root.insert(value)

root.print()

dnode = 75                                                               # Node you want to delete
if dnode in l:
    root.delete(dnode)
    print(f"Found the node {dnode}\nDeletion in progress...\nNode {dnode} Deleted!")
    root.print()
    print(f"Tree balanced from {root.data}? {root.isBalanced()}")
    print(f"Tree balanced from {root.left.data}? {root.left.isBalanced()}")     # Ignore the warnings and errors in this line as of now. However, the code is running as expected
else:
    print(f"Node {dnode} you are trying to delete is not in the given tree")