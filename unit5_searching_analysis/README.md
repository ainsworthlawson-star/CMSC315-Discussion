# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

I learned that the choice of search algorithm depends on how the data is organized and how frequently it needs to be searched. I used the example of an inventory with product identifiers because quickly locating an item is a practical problem. Linear search was easier to implement because it checks each value sequentially. With binary search, I had to pay closer attention to the lower, upper, and middle indices. I worked on boundary adjustments step-by-step and tested various cases such as empty lists, single element lists, missing values, and positions at the beginning and end to verify the logic.

2. What challenges did you encounter, and how did you overcome them?

The number of comparisons highlighted the difference in performance. In my test with 10,000 elements, linear search checked 10,000 values ​​to find the last element, whereas binary search required only 14 comparisons. Linear search has a worst case runtime of O(n), as it may require checking every element. Binary search has a runtime of O(log n) because it halves the remaining search range at each step.

3. Explain when to use linear versus binary search, including tradeoffs in real world scenarios.

I would use linear search for small or unsorted datasets. Binary search is better suited for large, sorted collections that are queried frequently, sorting requires some initial setup time. It requires an ordering that allows half of the remaining values ​​to be excluded during each search step.