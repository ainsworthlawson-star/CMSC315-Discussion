# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. How do list operations impact performance in real-world applications?

## Implementation Summary

I completed the insertion, deletion, and search functions using Python lists. I tested insertion at the beginning, middle, and end of a list. I also tested deletion from all three positions and displayed both the removed values and updated lists.

For deletion, I validated the index before removing an item. An invalid index returned None instead of causing an error. I implemented searching as a linear search that checked each list element sequentially and returned the index when the value was found. If the value was not found, the function returned -1.

I also tested several edge cases, including deleting with an invalid index, deleting from an empty list, and inserting into an empty list.

For the real world example, I used a music playlist. Songs were inserted, searched for, and removed from the playlist.

## Reflection

While completing this assignment, I learned how Python lists handle insertion, deletion, and searching. I practiced inserting values at the beginning, middle, and end of a list and saw that items after the insertion point must shift to make room. I also used safe deletion by checking an index before removing an item. This prevented invalid indexes from causing the program to crash. For searching, I implemented a linear search that checked items one at a time until the value was found or the end of the list was reached.

The main challenge was keeping track of indexes after insertions and deletions changed the list. I overcame this by printing the list after each operation and using len() to calculate valid end and middle positions. I also tested edge cases such as deleting with an invalid index, deleting from an empty list, and inserting into an empty list.

These operations affect real world performance because inserting or deleting near the beginning of an array based list may require many elements to shift, while searching may require scanning the entire list.
