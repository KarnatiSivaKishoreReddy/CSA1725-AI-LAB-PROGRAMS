def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Set to keep track of visited nodes

    print(start)  # Process the current node
    visited.add(start)  # Mark the current node as visited

    # Recursively visit all adjacent nodes that have not been visited
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example graph represented as a dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Depth-First Search Traversal:")
dfs(graph, 'A')  # Starting DFS traversal from node 'A'
