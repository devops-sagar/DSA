# Explanation on Quick sort
* <ins>Devide and Conquer</ins> algorithm also uses <ins>recursion</ins> for sorting
* Even though **Perform Better than Merge Sort**
* Does not need extra memory to do work like merge sort
* <ins>Worst case</ins> would be the **quadratic Time Complexity O(n2)**, when data is mostly sorted which is also not comman

## Method
* **Pivot** is something in between the higher range and lower range. Consider it as a middle point of entire sorted array. If we are goiing to assume the first element as pivot then we are going to compare the rest of the data with it either the data is less then pivot or greater then pivot.  

* Left pointer <ins>should always be less then pivot</ins> **(L[i] < pivot)**
* If **(L[i] > pivot)** then it will triggered itself to swap with the right element which triggered itself in 4th step explanation to swap with this left element
* Right pointer <ins>shpould always be greater then pivot</ins> **(L[i] > pivot)**
* If **(L[i] < pivot)** then it will triggered itself to swap with the left element which triggred itself in 2nd step explanation.  

