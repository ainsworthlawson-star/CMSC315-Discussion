# Unit 7 Discussion: Sorting Algorithms

## Overview

This assignment compares Bubble Sort and Merge Sort.

## Learning Objectives

- Implement Bubble Sort
- Implement Merge Sort
- Understand divide-and-conquer
- Compare algorithm efficiency

## Requirements

1. Test Bubble Sort and Merge Sort.
2. Use multiple datasets.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world sorting example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:



1. What concepts or skills did you learn while completing this assignment?

I learned how the bubble sort algorithm compares adjacent values ​​and how the merge sort algorithm uses recursion to split lists before merging them. Implementing both methods helped me grasp the concept of stable sorting, understand differences in time complexity and verify the results using Python's sorted() function. I also practiced leaving the original input data unmodified.


2. What challenges did you encounter, and how did you overcome them?

The merge phase was the most complex as it required tracking positions in two separate lists and copying the remaining elements. I carefully analyzed the comparisons selecting the left element first in the event of identical values and tested scenarios such as empty lists, duplicates, reverse order and already sorted values. Assertions helped me identify errors before comparing performance.


3. Compare and constrast each sorting algorithm based on efficiency differences, tradeoffs made, and when to each.

Compare the algorithms in terms of efficiency, advantages and disadvantages and their respective use cases. The bubble sort algorithm was easier to understand and its ability to terminate early proved advantageous for small playlists that were already largely sorted, its execution time in average and worst case scenarios was O(n²). The merge sort algorithm required more code and O(n) additional memory but offered an execution time of O(n log n) making it better suited for large frequently updated lists. Both implementations preserved the original order of tracks with the same rating. For extensive streaming recommendations I would prefer the merge sort algorithm as its predictable performance and ability to sort the two halves of the data independently are beneficial.