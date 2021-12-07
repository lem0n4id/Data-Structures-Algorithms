## Linked List

Linked List can be defined as collection of objects 
called **nodes** that are randomly stored in the memory.

A node contains two fields i.e. data stored at that 
particular address and the pointer which contains the address of the next node in the memory.

The last node of the list contains pointer to the null.

```py

LinkedList:object
Node:object
    
# Start with the empty list
llist = LinkedList()

llist.head = Node(1)
second = Node(2)
third = Node(3)

'''
Three nodes have been created.
We have references to these three blocks as head,
second and third

    llist.head        second              third
        |                |                  |
        |                |                  |
+----+------+     +----+------+     +----+------+
| 1  | None |     | 2  | None |     |  3 | None |
+----+------+     +----+------+     +----+------+
'''

llist.head.next = second; # Link first node with second

'''
Now next of first Node refers to second.  So they
both are linked.

    llist.head        second              third
        |                |                  |
        |                |                  |
+----+------+     +----+------+     +----+------+
| 1  |  o-------->| 2  | null |     |  3 | null |
+----+------+     +----+------+     +----+------+
'''

second.next = third; # Link second node with the third node

'''
Now next of second Node refers to third.  So all three
nodes are linked.

    llist.head        second              third
        |                |                  |
        |                |                  |
+----+------+     +----+------+     +----+------+
| 1  |  o-------->| 2  |  o-------->|  3 | null |
+----+------+     +----+------+     +----+------+
'''
```
### Arrays vs Linked List 

(Here Arrays are not dynamic like how python lists work, more on this later)

_Arrays_ store elements in **contiguous memory locations**, resulting in easily calculable addresses for the elements stored and this allows faster access to an element at a specific index. 

Linked lists are less rigid in their storage structure and elements are usually **not stored in contiguous locations**, hence they need to be stored with additional tags giving a reference to the next element. 

This difference in the data storage scheme decides which data structure would be more suitable for a given situation. 

#### Major Differences

- **Size:** Since data can only be stored in contiguous blocks of memory in an array, its size cannot be altered at runtime due to the risk of overwriting other data. However, in a linked list, each node points to the next one such that data can exist at scattered (non-contiguous) addresses; this allows for a dynamic size that can change at runtime.

- **Memory allocation:** For arrays at compile time and at runtime for linked lists. but, a dynamically allocated array also allocates memory at runtime.

- **Memory efficiency:** For the same number of elements, linked lists use more memory as a reference to the next node is also stored along with the data. However, size flexibility in linked lists may make them use less memory overall; this is useful when there is uncertainty about size or there are large variations in the size of data elements; 

memory equivalent to the upper limit on the size has to be allocated while using arrays, whereas _linked lists can increase their sizes_ step-by-step proportionately to the amount of data.

- **Execution time:** Any element in an array can be directly accessed with its index; however in the case of a linked list, all the previous elements must be traversed to reach any element. Also, better cache locality in arrays can significantly improve performance. 

As a result, some operations (such as modifying a certain element) are faster in arrays, while some others (such as inserting/deleting an element in the data) are faster in linked lists.


#### Advantages of Linked Lists

1. Dynamic size
2. Ease of insertion/deletion

#### Drawbacks of Linked Lists

1. Random access is not allowed (Since elements aren't indexed)
2. 
2. Extra memory required for the pointer/reference to next node
3. takes a lot of time in traversing and changing the pointers


### Linked List operations

- Insertion
    - [Inserting a node](https://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/)

- Delete a node
    - algorithm i used:
    ```md
    1. find the node to be deleted
    2. link the nodes before and after the deleted node
    3. check if the head is shifted (if deleted node is first one)
    ```

    - [delete the first occurrence of data](https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/)
    - [Delete a Linked List node at a given position](https://www.geeksforgeeks.org/delete-a-linked-list-node-at-a-given-position/)

### Resources used

- [GFG](https://www.geeksforgeeks.org/linked-list-set-1-introduction/) - [from](https://www.geeksforgeeks.org/data-structures/linked-list/)
- [javaTpoint](https://www.javatpoint.com/singly-linked-list)

---

- [LeetCode](https://leetcode.com/tag/linked-list/)


### Futher Reading

- [github repo w some common programs in cpp?](https://github.com/whoparthgarg/Data-Structures-and-Algorithms/tree/main/10.%20Linked%20List)
---
- https://realpython.com/linked-lists-python/
- https://realpython.com/python-data-structures/
- https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm
