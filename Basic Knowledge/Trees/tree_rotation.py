'''
- Tree rotating algorithm for unbalanced trees
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
    
    def height(self, h = 0):
        left_height = self.left.height(h+1) if self.left else h         # Same code as above but with 3 lines only
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
    
def rotate_right(rot):
    pivot = rot.left
    re_attach_node = pivot.right
    rot.left = re_attach_node
    pivot.right = rot
    return pivot


# l = [50, 25, 75, 67, 100, 80, 120, 92]                         # Also, can use list of items to iterate over instead of inserting multiple times
l_l_imbalanced = [30, 20, 31, 10, 21, 9, 11]                     # Left - Left imbalanced
obj = Node(l_l_imbalanced[0])

for value in l_l_imbalanced:
    obj.insert(value)

obj.print()

obj = rotate_right(obj)

obj.print()                                                     # if there is an error - ignore becase code runs perfectly
