# Explanations on Tress
- One tree, One root node / One root node, One tree
- node can have 0 or more children. 0 children node called as leaf
- Each node links exactly to one parent. Any Node can not have 2 parents, otherwise it will generate the loops and **trees don't have loops**
- Node can not be its own parent
- Nodes are associated with data in it
- Nodes are arranged based on the data it have

## Binary Search Tree
Binary trees are useful for storing data in an organized manner so that it can be quickly retrieved, inserted, updated, and deleted. This arrangement of nodes allows each comparison to skip about half of the rest of the tree, so each operation as a whole is lightning fast.  

To be precise, binary search trees **provide an average Big-O complexity of O(log(n)) for search, insert, update, and delete operations.** log(n) is much faster than the linear O(n) time required to find elements in an <ins>unsorted array</ins>. Many popular production databases such as PostgreSQL and MySQL use binary trees under the hood to speed up CRUD operations.  

- Each node can have only 2 children and all nodes contains numeric value in it
- childredn to their left must have the lessaer value and right one must have the higher value than their parents
- No deplicate values allowed, **all must be unique**  
![bst](https://user-images.githubusercontent.com/54584388/221265887-cdebfcd8-cb5e-4c2c-a202-32b1ab76de31.gif)


### Pros
- When balanced, a BST provides lightning-fast O(log(n)) insertions, deletions, and lookups.  

| Operation | Average Case | Worst Case |
|:---------:|:------------:|:----------:|
| Space     | O(n)         | O(n)       |
| Access    | O(log n)     | O(n)       |
| Search    | O(log n)     | O(n)       |
| Insertion | O(log n)     | O(n)       |
| Removal   | O(log n)     | O(n)       |


### Cons
- Slow for a brute-force search. If you need to iterate over each node, you might have more success with an array.
- When the tree becomes unbalanced, all fast **O(log(n)) operations quickly degrade to O(n)**.
- Since pointers to whole objects are typically involved, a BST can require quite a bit more memory than an array, although this depends on the implementation.

### Where would you use a binary search tree in real life?
There are many applications of binary search trees in real life, and one of the most common use cases is in storing indexes and keys in a database.  

For example, in MySQL or PostgreSQL when you create a primary key column, what you’re really doing is creating a binary tree where the keys are the values of the column, and those nodes point to database rows. This lets the application easily search database rows by providing a key. For example, getting a user record by the email primary key.  

Other common uses include:
- Pathfinding algorithms in video games (A*) use BSTs
- File compression using a Huffman encoding scheme uses a binary search tree
- Rendering calculations - Doom (1993) was famously the first game to use a BST
- Compilers for low-level coding languages parse syntax using a BST
- Almost every database in existence uses BSTs for key lookups

### What’s the difference between a Binary Tree and a Linked List?
While binary trees and linked lists both use pointers to keep track of nodes, binary trees are more efficient for searching. In fact, linked lists are **O(n)** when used to search for a specific element - that’s pretty bad! Linked lists excel at removing and inserting elements quickly in the middle of the list.
