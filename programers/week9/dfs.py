def dfs(currentNode, visited, graph) :

    visited.append(currentNode)

    for nextNode in graph[currentNode] :
        if nextNode not in visited:
            dfs(nextNode, visited, graph)
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

    dfs('A', visited, graph)

    return visited

answer = solution()
print(answer)
    
