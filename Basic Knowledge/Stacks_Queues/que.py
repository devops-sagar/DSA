''' ************************************************************************
Start of simple Implementation - just to show how to push and pop in a queue
************************************************************************'''
# from collections import deque

# # create a new empty deque object that will function as a queue
# queue = deque()

# # add some items to the queue
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.append(4)

# # print the queue contents
# print(queue)

# # pop an item off the front of the queue
# x = queue.popleft()
# print(x)
# print(queue)

''' ************************************************************************
End of simple Implementation - just to show how to push and pop in a queue
************************************************************************'''


# Although its stack variable .pop(0) makes it act like queue
stack = []
  
stack.append('a')
stack.append('b')
stack.append('c')
  
print("Initial queue")
print(stack)
  
print("\nElements dequeued from queue")
print(stack.pop(0))
print(stack.pop(0))
print(stack.pop(0))
  
print("\nQueue after removing elements")
print(stack)
  
# ------------------------------------------------------------------------------------------------

# Python program to
# demonstrate implementation of
# queue using queue module


from queue import Queue

q = Queue(maxsize = 3)

print(q.qsize())

q.put('a')
q.put('b')
q.put('c')

print("\nFull: ", q.full())

print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())

print("\nEmpty: ", q.empty())

q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())