# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

## Implementation Summary

I implemented a Binary Search Tree (BST) using recursive insertion, search, and in-order traversal techniques. As a practical example, I used employee IDs and inserted nine values ​​into the tree. Smaller values ​​were placed in the left subtree, while larger values ​​went into the right subtree.

I tested the search functionality using both existing and non existing values. I also demonstrated edge cases by traversing and searching an empty tree and attempting to re-insert an existing value. My implementation ignored duplicate values.

During the in-order traversal, the left subtree, the current node, and the right subtree were visited sequentially. Due to the BST's hierarchical structure, this resulted in the employee IDs being displayed in sorted order.

## Reflection

While working on this task, I learned how recursive insertion, search, and traversal processes work within a binary search tree. The biggest challenge was understanding how to return from a recursive call to the previous node without breaking the tree's continuity. I overcame this by reviewing each comparison and keeping in mind that smaller values ​​move to the left and larger ones to the right.

I also gained an understanding of why in-order traversal produces sorted output. Since the traversal visits the left subtree first, then the current node, and finally the right subtree and a binary search tree places smaller values ​​on the left and larger ones on the right the values ​​are naturally traversed from smallest to largest.

Binary search trees can speed up searches because each comparison eliminates an entire subtree, rather than checking each value individually. A balanced binary search tree allows for efficient search and insertion operations, often in O(log N) time. The insertion order plays a significant role: if values ​​are inserted in already sorted order, the tree can become degenerate (or "skewed") and behave more like a linked list, causing operation execution times to approach O(N).