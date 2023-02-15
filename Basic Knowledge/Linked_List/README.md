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