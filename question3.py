def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    
    # Mark the current vertex as visited
    visited.add(vertex)
    print(vertex)  # Process the vertex (e.g., print it)

    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS Traversal (Recursive):")
dfs_recursive(graph, 'A')

def dfs_iterative(graph, start_vertex):
    visited = set()
    stack = [start_vertex]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)  # Process the vertex (e.g., print it)
            # Add all unvisited neighbors to the stack
            stack.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

# Example usage:
print("DFS Traversal (Iterative):")
dfs_iterative(graph, 'A')
