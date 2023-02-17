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