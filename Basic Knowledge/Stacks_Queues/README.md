# Explanation on Stacks
- LIFO way to push and pop the elements
- Can not randomly access elements in stack unlike list
- Good standard insertion and deletion can be done with **O(1) time complexity.**
- built in list type is used to implement stack in python, due to this fact list is the most flexible thing in python and not every push requires the resize of whole stack as its built upon a list that's why it takes O(1) time
- If you are using .insert() method instead of .push() or .append(), you are no longer in the performance range of O(1). Also, it considers as violetting rules of stack in python
- You can not add elements using .push() operation if you are using the by default list as a stack. You have to use the .append() method to add the element just like a list method. If you want to forcefully use the .push() function to add elements, you can refer the below given code with importing third party library.

```
from pythonds.basic import Stack

s=Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
```

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
Python stack can be implemented using the deque class from the collections module. Deque is preferred over the list in the cases where we need quicker append and pop operations from both the ends of the container, as deque provides an O(1) time complexity for append and pop operations as compared to ::list which provides O(n) time complexity.:: 

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
- __Stacks are efficient for adding and removing elements, as these operations have a time complexity of O(1).__
- In order to reverse the order of elements we use the stack data structure.
- Stacks can be used to implement undo/redo functions in applications.

## Drawbacks of Stack:

- Restriction of size in Stack is a drawback and if they are full, you cannot add any more elements to the stack.
- Stacks do not provide fast access to elements other than the top element.
- __Stacks do not support efficient searching, as you have to pop elements one by one until you find the element you are looking for.__


------------------------------------------------------------------------------------------------------------------------------------------------


# Explanation on Queues
Operations associated with queue are: 
 
- **Enqueue**: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – **Time Complexity : O(1)**
- **Dequeue**: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition – **Time Complexity : O(1)**
- **Front**: Get the front item from queue – **Time Complexity : O(1)**
- **Rear**: Get the last item from queue – **Time Complexity : O(1)**

## How to implement the Queue
### Implementing using List
List is a Python’s built-in data structure that can be used as a queue. Instead of enqueue() and dequeue(), append() and pop() function is used. However, **lists are quite slow for this purpose because inserting or deleting an element at the beginning requires shifting all of the other elements by one, requiring O(n) time.**

 ```
# Initializing a queue
queue = []
  
# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')
  
print("Initial queue")
print(queue)
  
# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
  
print("\nQueue after removing elements")
print(queue)
 ```

 ## Implementation using collections.deque
 Queue in Python can be implemented using deque class from the collections module. Deque is preferred over list in the cases where we need **quicker append and pop operations from both the ends of container, as deque provides an O(1) time complexity for append and pop operations as compared to list which provides O(n) time complexity. Instead of enqueue and deque, append() and popleft() functions are used.**
 ```
 from collections import deque
  
# Initializing a queue
q = deque()
  
# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')
  
print("Initial queue")
print(q)
  
# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())
  
print("\nQueue after removing elements")
print(q)
 ```

 ## Implementation using queue.Queue
Queue is built-in module of Python which is used to implement a queue. queue.Queue(maxsize) initializes a variable to a maximum size of maxsize. A maxsize of zero ‘0’ means a infinite queue. This Queue follows FIFO rule. 
There are various functions available in this module: 
 
- **maxsize** – Number of items allowed in the queue.
- **empty()** – Return True if the queue is empty, False otherwise.
- **full()** – Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
- **get()** – Remove and return an item from the queue. If queue is empty, wait until an item is available.
- **get_nowait()** – Return an item if one is immediately available, else raise QueueEmpty.
- **put(item)** – Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
- **put_nowait(item)** – Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
- **qsize()** – Return the number of items in the queue.