class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def insert(root, value):
    if root is None:
        root = Node(value)
    elif value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def print_tree(root, level=0):
    if root is not None:
        print_tree(root.right, level + 1)
        print('  -   ' * level, end='')
        print(root.value)
        print_tree(root.left, level + 1)

# Example usage
root = Node(7)
root = insert(root, 3)
root = insert(root, 12)
root = insert(root, 1)
root = insert(root, 5)
root = insert(root, 9)
root = insert(root, 15)

print_tree(root)
