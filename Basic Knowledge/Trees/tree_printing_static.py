'''
Printing Tree Horizontally - Generated by chatGPT
'''

# class Node:
#     def __init__(self, value):
#         self.left = None
#         self.right = None
#         self.value = value

# def insert(root, value):
#     if root is None:
#         root = Node(value)
#     elif value < root.value:
#         root.left = insert(root.left, value)
#     else:
#         root.right = insert(root.right, value)
#     return root

# def print_tree(root, level=0):
#     if root is not None:
#         print_tree(root.right, level + 1)
#         print('  -   ' * level, end='')
#         print(root.value)
#         print_tree(root.left, level + 1)

# # Example usage
# root = Node(7)
# root = insert(root, 3)
# root = insert(root, 12)
# root = insert(root, 1)
# root = insert(root, 5)
# root = insert(root, 9)
# root = insert(root, 15)

# print_tree(root)


'''
General code:
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def getNodesAtDepth(self, depth, nodes=[]):
        if depth == 0:
            nodes.append(self.data)
            return nodes

        if self.left:
            self.left.getNodesAtDepth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))
        
        if self.right:
            self.right.getNodesAtDepth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))
        return nodes

    def height(self, h=0):
        leftHeight = self.left.height(h+1) if self.left else h 
        rightHeight = self.right.height(h+1) if self.right else h
        return max(leftHeight, rightHeight)


class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def _nodeToChar(self, n, spacing):
        if n is None:
            return 'x'+(' '*spacing)
        spacing = spacing-len(str(n))+1
        return str(n)+(' '*spacing)

    # def print(self, label=''):
    def print(self):
        # print(self.name+'#'+label)
        print('')
        print(f"self.root = {self.root.data}")
        height = self.root.height()
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
            row = self.root.getNodesAtDepth(depth, [])
            print((' '*offset)+''.join([self._nodeToChar(n, spacing) for n in row]))
            spacing = offset+1
            offset = int(offset/2) - 1
        print('')


tree = Tree(Node(50))
tree.root.left = Node(25)
tree.root.right = Node(75)
tree.root.left.left = Node(13)
tree.root.left.right = Node(35) 
tree.root.left.right.right = Node(37)
tree.root.right.left = Node(55)
tree.root.right.right = Node(103)
tree.root.left.left.left = Node(2)
tree.root.left.left.right = Node(20)
tree.root.right.left = Node(55)
tree.root.right.right.right = Node(256)

tree.print()