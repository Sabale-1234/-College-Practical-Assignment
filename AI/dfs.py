def dfs(graph, start, visited=None):
    # If visited is None, create an empty set
    if visited is None:
        visited = set()

    # Add the current node to the visited set
    visited.add(start)

    # Print the current node
    print(start, end=" ")

    # Visit all unvisited neighbors of the current node recursively
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    # Return the visited set
    return visited
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Traversal: ", end="")
dfs(graph, 'A')
