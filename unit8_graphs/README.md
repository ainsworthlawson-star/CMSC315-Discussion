# Unit 8 Discussion: Breadth-First Search (BFS)

## Overview

This assignment explores graph traversal using Breadth-First Search (BFS).

## Learning Objectives

- Represent graphs using adjacency lists
- Implement BFS
- Use queues in graph traversal
- Analyze graph traversal behavior

## Requirements

1. Create a graph.
2. Perform BFS traversal.
3. Add nodes or edges.
4. Demonstrate edge cases.
5. Analyze BFS behavior.
6. Create a real-world graph example.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare BFS and DFS conceptually and describe real-world applications and use cases.

While working on this task I learned how graphs can be represented using adjacency lists and how the Breadth First Search (BFS) algorithm uses a queue to traverse connected nodes. I also understood why BFS operates on the FIFO principle, nodes discovered first are processed first allowing the algorithm to explore the graph level by level. I practiced using Python dictionaries, lists, sets and deques while creating a streaming recommendation graph.

One challenge was ensuring that nodes were not visited more than once. Since various genres were interconnected there was a risk of adding a node repeatedly. I resolved this by using a set of visited nodes and marking each node as visited as soon as it was added to the queue. To handle cases where starting nodes were missing, I chose to return an empty list. Both BFS and DFS traverse graphs but they function differently. BFS explores nearby nodes before moving further away whereas DFS follows a path in depth before backtracking. BFS is suitable for finding the shortest paths in unweighted graphs as well as for analyzing social connections and recommendation systems. DFS can be useful for exploring mazes, dependency relationships or paths that require deeper investigation.