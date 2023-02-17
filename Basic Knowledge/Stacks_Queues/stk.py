
''' ************************************************************************
Start of simple Implementation - just to show how to push and pop
************************************************************************'''

# from collections import deque

# stack = deque()
# # stack = []


# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.append(4)

# print(stack)

# x = stack.pop()
# print(x)
# print(stack)

''' ************************************************************************
end of simple Implementation 
below you will see different operations using queue module
************************************************************************'''

from queue import LifoQueue

stack = LifoQueue(maxsize=2)

print(stack.qsize())

print("Before: ",stack)

stack.put('a')
stack.put('b')
stack.put('c')
# stack.put('d')
# stack.put('e')
# stack.put('f')

print("After: ",stack)

print("Stack Full T/F: ", stack.full())
print("Size of stack: ", stack.qsize())

print(stack.get())
print(stack.get())
print(stack.get())

print("Stack Empty T/F: ",stack.empty())