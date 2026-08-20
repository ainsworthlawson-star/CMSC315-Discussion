# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

## Implementation Documentation

I completed the Stack and Queue classes by filling in all of the TODO sections in the starter code. For the stack, I used a Python list to store the values. I used append() to push new values onto the stack and pop() to remove the most recently added value. I also added peek() and is_empty() methods and handled cases where the stack was empty.

For the queue, I used deque from Python's collections module. I used append() to add items to the back of the queue and popleft() to remove items from the front. I also added front() and is_empty() methods.

For my real-world example, I used an IT support scenario. The stack represented a technician's action history, while the queue represented incoming support tickets. I also tested empty structures and single-item structures to make sure the program handled those situations correctly.

## Reflection

This assignment helped me understand the difference between stacks and queues by actually using them in a program. Before this assignment, I understood the basic definitions of LIFO and FIFO, but seeing the values added and removed made the difference much clearer. The stack used LIFO because the last technician action added was the first one removed. This makes sense for something like an undo feature. The queue used FIFO because the first support ticket added was the first one processed, which is similar to customers waiting in line.

One challenge I had was making sure I understood which end of each structure should be used when removing data. I handled this by running the program and checking the order of the output. I also tested empty stacks and queues so the program would not fail when there was nothing to remove or view.

The structures use more memory as more items are added. If there are n items stored, the memory needed for the stored data grows approximately with n, or O(n).
