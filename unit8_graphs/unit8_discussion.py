"""
===========================================================
UNIT 8 DISCUSSION: BREADTH-FIRST SEARCH (BFS)
===========================================================

STUDENT INSTRUCTIONS:

This assignment is designed to help you understand how graphs
are traversed using Breadth-First Search (BFS) and how this
applies to real-world systems (e.g., networks, routes,
social connections).

===========================================================
"""

from collections import deque


def bfs(graph, start):
    """
    TODO (Student):
    Implement Breadth-First Search (BFS).

    Requirements:
    - Use a queue to manage traversal order.
    - Track visited nodes to prevent revisiting nodes.
    - Visit nodes level by level.
    - Return the order in which nodes were visited.

    Add comments explaining:
    - Why a queue is used.
    - Why neighbors are added to the queue.
    - How BFS differs from depth-first traversal.
    """

    # If the starting node is not in the graph, return an empty list
    # instead of causing an error.
    if start not in graph:
        return []

    # A set keeps track of nodes that have already been discovered.
    # This prevents BFS from visiting the same node more than once.
    visited = {start}

    # BFS uses a queue because a queue follows FIFO order.
    # The first node added is the first node processed.
    queue = deque([start])

    # This list stores the order in which nodes are visited.
    traversal_order = []

    while queue:
        # Remove the node at the front of the queue.
        current = queue.popleft()
        traversal_order.append(current)

        # Neighbors are added to the back of the queue.
        # This allows BFS to finish one level before moving deeper.
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # Unlike DFS, which follows one path deeply before backtracking,
    # BFS explores nearby nodes level by level.
    return traversal_order


def main():
    print("=== UNIT 8: BREADTH-FIRST SEARCH ===")

    # ===============================
    # TODO (Student): CREATE A GRAPH
    # ===============================
    #
    # Requirements:
    # 1. Create a graph using an adjacency list.
    # 2. Include at least 6 nodes.
    # 3. Include multiple connections between nodes.
    # 4. Clearly display the graph structure.
    # 5. Use comments to explain what the nodes and edges represent.

    print("\n=== GRAPH STRUCTURE ===")

    # This graph represents a streaming recommendation system.
    # Each node represents a content genre.
    # Each edge represents a relationship between similar genres.
    graph = {
        "Action": ["Sci-Fi", "Adventure"],
        "Sci-Fi": ["Action", "Drama", "Thriller"],
        "Adventure": ["Action", "Comedy"],
        "Drama": ["Sci-Fi", "Mystery"],
        "Thriller": ["Sci-Fi"],
        "Comedy": ["Adventure"],
        "Mystery": ["Drama"]
    }

    print("Streaming recommendation graph:")
    for node, neighbors in graph.items():
        print(f"  {node} -> {neighbors}")

    # ===============================
    # TODO (Student): BFS TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Select a starting node.
    # 2. Perform BFS traversal.
    # 3. Display the traversal order.
    # 4. Use comments to explain how BFS visits nodes level by level.
    # 5. Add at least one additional node or edge
    #    and demonstrate the updated traversal.

    print("\n=== BFS TRAVERSAL ===")

    start_node = "Action"

    print("Starting node:", start_node)
    print("BFS traversal order:", bfs(graph, start_node))

    # Starting from Action, BFS first visits genres directly connected
    # to Action before moving to genres farther away.

    # Add a new Documentary node and connect it to Drama.
    graph["Documentary"] = []
    graph["Drama"].append("Documentary")
    graph["Documentary"].append("Drama")

    print("\nAdded Documentary and connected it to Drama.")
    print("Updated BFS traversal:", bfs(graph, start_node))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Start from a different node
    # - Use a disconnected graph
    # - Handle a missing start node safely
    # - Graph containing only one node
    # - Empty graph
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: Missing starting node.
    # The bfs() function safely returns an empty list.
    print("\nMissing starting node:")
    print("BFS from Sports:", bfs(graph, "Sports"))

    # Edge case 2: Graph with only one node.
    # BFS visits the single node and then stops.
    single_node_graph = {
        "Movie": []
    }

    print("\nSingle-node graph:")
    print("BFS traversal:", bfs(single_node_graph, "Movie"))

    # Edge case 3: Empty graph.
    # Since the starting node does not exist, an empty list is returned.
    empty_graph = {}

    print("\nEmpty graph:")
    print("BFS traversal:", bfs(empty_graph, "Action"))

    # Edge case 4: Start from a different node.
    print("\nStarting from Drama:")
    print("BFS traversal:", bfs(graph, "Drama"))


if __name__ == "__main__":
    main()