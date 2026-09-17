# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
I learned how Python dictionaries work like hash tables by storing information as key-value pairs.

2. What challenges did you encounter, and how did you overcome them?
One challenge was making sure the program handled missing keys without causing errors.

3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.
Hash tables store data using keys and values. The key is hashed to help determine where the value should be stored internally, which allows fast access to data.



Discussion Board Reflection

While completing this assignment, I learned how Python dictionaries demonstrate the main behavior of hash tables. I used SKU numbers as keys and inventory quantities as values, then practiced inserting, looking up, updating, and deleting entries. The biggest challenge was handling missing keys without causing errors. I solved that by using get() for safe lookups and pop() with a default value for safe deletions. I also tested an empty dictionary so the program covered more than normal inventory operations.

Hash tables improve efficiency because a key is hashed to help locate its value instead of searching every item sequentially. With a good distribution of keys, dictionary insert, lookup, update, and delete operations are O(1) on average. A collision occurs when different keys compete for the same internal location. Python dictionaries resolve collisions internally, but frequent collisions can require additional work and reduce performance. For an inventory system, dictionaries are useful because SKU values provide unique identifiers and allow quantities to be retrieved or updated quickly as the number of products grows.