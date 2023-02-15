''' ************************************************************************
Most basic implementation of linkedlist with adding elements back at each other where here 3 will be the head since we added the number 3 first
and number 5 would not be the tail always as if new number might be added and that will become the tail of the linked list.
source: https://www.educative.io/answers/how-to-create-a-linked-list-in-python
************************************************************************'''

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        
        print(bool(self.head))
        if self.head:
            current = self.head

            while current.next:
                current = current.next
            
            current.next = newNode
        else:
            self.head = newNode
    
    def printLL(self):
        current = self.head
        i = 1
        while current:
            print(f"Node {i}: ", current.data)
            current = current.next
            i += 1

LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()