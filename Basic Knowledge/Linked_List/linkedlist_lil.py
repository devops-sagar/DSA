
''' ************************************************************************
Start of simple Implementation - just to show how to make nodes
This is the most basic way to implement the LinkedList in which Script will add the elements 5, 10, 15, 20 on top of each other. At the end of the 
program 20 will be the Head node and 5 will be the tail node
************************************************************************'''

# class Node(object):
#     def __init__(self, value):
#         self.value = value
#         self.next = None

#     def set_next(self, next):
#         self.next = next

#     def get_data(self):
#         return self.value
    
#     def get_next(self):
#         return self.next

# class LinkedList(object):
#     def __init__(self, head = None):
#         self.head = head

#     def insert(self, data):
#         new_node = Node(data)
#         new_node.set_next(self.head)
#         self.head = new_node

#     def dump(self):
#         temp = self.head
#         i = 1
#         while(temp != None):
#             print(f"Node {i}: ", temp.get_data())
#             temp = temp.get_next()
#             i += 1

# obj = LinkedList()
# obj.insert(5)
# obj.insert(10)
# obj.insert(15)
# obj.insert(20)

# obj.dump()


''' ************************************************************************
end of simple Implementation - just to show how to make nodes
below you will see different operations on the linkedlist like counting nodes, searching elements in the nodes
and deletion of specific nodes. These all can implemtnt on the existing codebase develop for making nodes and 
assigning some values to it which is given above
************************************************************************'''


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
        self.count = 0
    
    def get_count(self):        #to count the number of Nodes
        return self.count

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1         #increasing with every call

    def find(self, value):      #function to find the item
        item = self.head
        while(item != None):
            if(item.get_data() == value):
                print(f"{item.get_data()} found at memory location: {item}")
                # break
                return None
            else:
                item = item.get_next()
                if item == None:
                    print(f"{value} is not available in linked list")
        return None
    
    def delete(self, index):            # Function to remove the element from the linkedlist - basically we are skipping the element in the list
        if index > self.count or self.head == None:
            return
        else:
            temp_index = 0
            node = self.head
            while (temp_index < index - 1):
                node = node.get_next()
                temp_index += 1
            node.set_next(node.get_next().get_next())
            self.count -= 1


    def dump(self):
        temp = self.head
        i = 0
        while(temp != None):
            print(f"Node {i}: ", temp.get_data())
            temp = temp.get_next()
            i += 1

obj = LinkedList()

obj.insert(10)
obj.insert(9)
obj.insert(8)
obj.insert(7)
obj.insert(6)
obj.insert(5)
obj.insert(4)
obj.insert(3)
obj.insert(2)
obj.insert(1)
obj.insert(0)

obj.dump()

print("Totoal Number of Nodes before Deletion: ", obj.get_count())  #showing total count before deletion

obj.find(10)              #finding item in nodes
obj.find(-5)              #finding item in nodes
obj.find(50)              #finding item in nodes
obj.find(50-5)              #finding item in nodes

obj.delete(0)   # This case will not gonna delete the 0th element in ll as the function is not able to get the 0th element ...this need to be optimised
obj.delete(2)   # Skip the element which resides on the index-2
obj.delete(6)   # Skip the element which resides on the index-6
print("Totoal Number of Nodes after Deletion: ", obj.get_count())  #showing total count after deletion

obj.dump()
