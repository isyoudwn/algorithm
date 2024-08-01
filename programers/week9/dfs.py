def dfs(curr_node, graph, visited):
    visited.append(curr_node)
    for next_node in graph[curr_node]:
        if next_node not in visited:
            dfs(next_node, graph, visited)
    return visited

def solution():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    visited = []
    dfs('A', graph, visited)
    
    return visited

V = solution()

print(V)