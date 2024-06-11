from collections import defaultdict, deque

def shortest_path_dag(n, edges, source, target):
    # Initialize the graph
    graph = defaultdict(list)
    for u, v, weight in edges:
        graph[u].append((v, weight))
    
    # Initialize distances
    dp = {i: float('inf') for i in range(n)}
    dp[target] = 0
    
    # Topological sort using Kahn's algorithm
    in_degree = [0] * n
    for u in graph:
        for v, _ in graph[u]:
            in_degree[v] += 1
            
    queue = deque([target])
    topological_order = []
    
    while queue:
        node = queue.popleft()
        topological_order.append(node)
        for neighbor, _ in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Reverse topological order
    topological_order.reverse()
    
    # Compute shortest paths
    for u in topological_order:
        for v, weight in graph[u]:
            dp[u] = min(dp[u], weight + dp[v])
    
    return dp[source]

# Example usage
n = 8  # Number of vertices
edges = [
    (0, 1, 2),
    (0, 2, 4),
    (1, 2, 1),
    (1, 3, 7),
    (2, 4, 3),
    (3, 5, 1),
    (4, 3, 2),
    (4, 5, 6)
]
source = 0
target = 5

print("Shortest path from {} to {} is: {}".format(source, target, shortest_path_dag(n, edges, source, target)))
