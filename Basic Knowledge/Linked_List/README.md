# Explanations on LinkedList
![L1](https://user-images.githubusercontent.com/54584388/218909011-929e8381-46fa-4b68-9ced-82cd164f3d09.jpg)
![L2](https://user-images.githubusercontent.com/54584388/218909016-0675f5ad-a257-47ce-b1bd-3e0bdd597871.jpg)

## Benifits of using Linked List over Arrays
- you need a **constant time** O(1) when adding or removing elements from the sequence
- manage memory more efficiently especially when the number of elements is unknown (if arrays you may have to constantly shrink or grow them. Note though that _filled arrays usually take up less memory than Linked Lists._
- you want to insert items in the middle point more efficiently

## Why Linked List?
- **The size of the arrays is fixed**: So we must know the upper limit on the number of elements in advance. Also, generally, the allocated memory is equal to the upper limit irrespective of the usage.

- **Insertion of a new element / Deletion of a existing element in an array of elements is expensive**: The room has to be created for the new elements and to create room existing elements have to be shifted but in Linked list if we have the head node then we can traverse to any node through it and insert new node at the required position.

Example: 
In a system, if we maintain a sorted list of IDs in an array id[] = [1000, 1010, 1050, 2000, 2040]. 
If we want to insert a new ID 1005, then to maintain the sorted order, we have to move all the elements after 1000 (excluding 1000). 

Deletion is also expensive with arrays until unless some special techniques are used. For example, to delete 1010 in id[], everything after 1010 has to be moved due to this so much work is being done which affects the efficiency of the code.

## Drawbacks of Linked List
- Random access is not allowed. We have to access elements sequentially starting from the first node(head node). So we cannot do a binary search with linked lists efficiently with its default implementation. 
- Extra memory space for a pointer is required with each element of the list. 
- Not cache-friendly. Since array elements are contiguous locations, there is the locality of reference which is not there in the case of linked lists.
- It takes a lot of time in traversing and changing the pointers.
- Reverse traversing is not possible in singly linked lists.
- It will be confusing when we work with pointers.
- Direct access to an element is not possible in a linked list as in an array by index.
- Searching for an element is costly and requires O(n) time complexity.
- Sorting of linked lists is very complex and costly.

## Types of Linked List
- **Simple Linked List** – In this type of linked list, one can move or traverse the linked list in only one direction. where the next pointer of each node points to other nodes but the next pointer of the last node points to NULL. It is also called “Singly Linked List”.
- **Doubly Linked List** – In this type of linked list, one can move or traverse the linked list in both directions (Forward and Backward)
- **Circular Linked List** – In this type of linked list, the last node of the linked list contains the link of the first/head node of the linked list in its next pointer.
- **Doubly Circular Linked List** – A Doubly Circular linked list or a circular two-way linked list is a more complex type of linked list that contains a pointer to the next as well as the previous node in the sequence. The difference between the doubly linked and circular doubly list is the same as that between a singly linked list and a circular linked list. The circular doubly linked list does not contain null in the previous field of the first node.
- **Header Linked List** – A header linked list is a special type of linked list that contains a header node at the beginning of the list. 

## Time Complexity
| Time Complexity | Worst Case | Average Case |
|:---------------:|:----------:|:------------:|
| Search          | O(n)       | O(n)         |
| Insertion       | O(1)       | O(1)         |
| Deletion        | O(1)       | O(1)         |

Search is O(n) because as data is not stored in contiguous memory locations so we have to traverse one by one.
Insertion and Deletion are O(1) because we have to just link new nodes for Insertion with the previous and next node and dislink exist nodes for deletion from the previous and next nodes without any traversal.

Auxiliary Space: O(N) [To store dynamic memory]