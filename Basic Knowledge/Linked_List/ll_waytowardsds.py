''' ************************************************************************

************************************************************************'''

class Node:
    def __init__(self, value, next_node = None, prev_node = None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

class LinkedList:
    def __init__(self, values = None):
        self.head = None
        self.tail = None

        if values is not None:
            self.add_multiple_nodes(values)
    
    def add_node(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    
    def add_multiple_nodes(self, values):
        for value in values:
            self.add_node(value)

obj = LinkedList()
obj.add_node(33)