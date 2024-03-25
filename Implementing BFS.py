from collections import deque

def bfs(graph, start):
    visited = set()  # Set to keep track of visited nodes
    queue = deque([start])  # Queue for BFS traversal

    while queue:
        node = queue.popleft()  # Dequeue a node from the front of the queue
        if node not in visited:
            print(node)  # Process the node
            visited.add(node)  # Mark the node as visited

            # Enqueue all adjacent nodes that have not been visited
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example graph represented as a dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Breadth-First Search Traversal:")
bfs(graph, 'A')  # Starting BFS traversal from node 'A'
