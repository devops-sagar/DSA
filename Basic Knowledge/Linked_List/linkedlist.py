class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def set_next(self, next):
        self.next = next

    def get_data(self):
        return self.value
    
    def get_next(self):
        return self.next

class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def dump(self):
        temp = self.head
        i = 1
        while(temp != None):
            print(f"Node {i}: ", temp.get_data())
            temp = temp.get_next()
            i += 1

obj = LinkedList()
obj.insert(5)
obj.insert(10)
obj.insert(15)
obj.insert(20)

obj.dump()