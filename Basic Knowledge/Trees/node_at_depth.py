'''
- Simple representation of Insertion of Nodes in Binary Search Tree
- Getting all the Nodes from the mentioned depth
'''

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        
        # print(self.data, data)                  # This line is for debuggiing purpose - Can tell you the cuurent values in process
        
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

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.insert(77)

print(f"Nodes at hight 0 : {root.node_at_depth(0)}")
print(f"Nodes at hight 1 : {root.node_at_depth(1)}")
print(f"Nodes at hight 2 : {root.node_at_depth(2)}")
print(f"Nodes at hight 3 : {root.node_at_depth(3)}")