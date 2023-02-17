# Explanation on Stacks
- LIFO way to push and pop the elements
- Can not randomly access elements in stack unlike list
- Good standard insertion and deletion can be done with **O(1) time complexity.**
- built in list type is used to implement stack in python, due to this fact list is the most flexible thing in python and not every push requires the resize of whole stack as its built upon a list that's why it takes O(1) time
- If you are using .insert() method instead of .push() or .append(), you are no longer in the performance range of O(1). Also, it considers as violetting rules of stack in python

## The functions associated with stack are:
- empty() – Returns whether the stack is empty – **Time Complexity: O(1)**
- size() – Returns the size of the stack – **Time Complexity: O(1)**
- top() / peek() – Returns a reference to the topmost element of the stack – **Time Complexity: O(1)**
- push(a) – Inserts the element ‘a’ at the top of the stack – **Time Complexity: O(1)**
- pop() – Deletes the topmost element of the stack – **Time Complexity: O(1)**

## How to implement the stack
### Implementing using List
Python’s built-in data structure list can be used as a stack. Instead of push(), append() is used to add elements to the top of the stack while pop() removes the element in LIFO order. Unfortunately, the list has a few shortcomings. The biggest issue is that it can run into speed issues as it grows. The items in the list are stored next to each other in memory, if the stack grows bigger than the block of memory that currently holds it, then Python needs to do some memory allocations. This can lead to some append() calls taking much longer than other ones.

```
    stack = []

    stack.append('a')
    stack.append('b')
    stack.append('c')
    
    print('Initial stack')
    print(stack)

    print('\nElements popped from stack:')
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    
    print('\nStack after elements are popped:')
    print(stack)
```

Output

    Initial stack
    ['a', 'b', 'c']

    Elements popped from stack:
    c
    b
    a

    Stack after elements are popped:
    []

### Implementation using collections.deque:
Python stack can be implemented using the deque class from the collections module. Deque is preferred over the list in the cases where we need quicker append and pop operations from both the ends of the container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity. 

```
from collections import deque
  
stack = deque()
  
stack.append('a')
stack.append('b')
stack.append('c')
  
print('Initial stack:')
print(stack)

print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
  
print('\nStack after elements are popped:')
print(stack)

```

Output

    Initial stack:
    deque(['a', 'b', 'c'])

    Elements popped from stack:
    c
    b
    a

    Stack after elements are popped:
    deque([])

### Implementation using queue module:
Queue module also has a LIFO Queue, which is basically a Stack. Data is inserted into Queue using the put() function and get() takes data out from the Queue. 

There are various functions available in this module: 

- maxsize – Number of items allowed in the queue.
- empty() – Return True if the queue is empty, False otherwise.
- full() – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
- get() – Remove and return an item from the queue. If the queue is empty, wait until an item is available.
- get_nowait() – Return an item if one is immediately available, else raise QueueEmpty.
- put(item) – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
- put_nowait(item) – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
- qsize() – Return the number of items in the queue.

```
from queue import LifoQueue
  
# Initializing a stack
stack = LifoQueue(maxsize=3)
  
# qsize() show the number of elements
# in the stack
print(stack.qsize())
  
# put() function to push
# element in the stack
stack.put('a')
stack.put('b')
stack.put('c')
  
print("Full: ", stack.full())
print("Size: ", stack.qsize())
  
# get() function to pop
# element from stack in
# LIFO order
print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())
  
print("\nEmpty: ", stack.empty())

```

Output

    0
    Full:  True
    Size:  3

    Elements popped from the stack
    c
    b
    a

    Empty:  True

## Advantages of Stack:

- Stacks are simple data structures with a well-defined set of operations, which makes them easy to understand and use.
- _Stacks are efficient for adding and removing elements, as these operations have a time complexity of O(1)._
- In order to reverse the order of elements we use the stack data structure.
- Stacks can be used to implement undo/redo functions in applications.

## Drawbacks of Stack:

- Restriction of size in Stack is a drawback and if they are full, you cannot add any more elements to the stack.
- Stacks do not provide fast access to elements other than the top element.
- _Stacks do not support efficient searching, as you have to pop elements one by one until you find the element you are looking for._