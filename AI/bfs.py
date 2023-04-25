from collections import deque

def bfs(graph, start):
    # Keep track of visited nodes and initialize a queue
    visited = set()
    queue = deque([start])

    while queue:
        # Get the next node from the queue
        node = queue.popleft()

        # If the node has not been visited, mark it as visited and add its neighbors to the queue
        if node not in visited:
            visited.add(node)
            print(node, end=" ")

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

print("BFS Traversal: ", end="")
bfs(graph, 2)
