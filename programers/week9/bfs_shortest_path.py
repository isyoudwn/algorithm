from collections import deque

def bfs_shortest_path(startNode, targetNode, graph) :
    queue = deque([startNode])
    visited = set([startNode])
    path = {startNode : [startNode]}

    while queue:
        currentNode = queue.popleft()
        if  currentNode == targetNode:
            return path[currentNode]
        
        for nextNode in graph[currentNode]:
            if nextNode not in visited:
                visited.add(nextNode)
                queue.append(nextNode)
                path[nextNode] = path[currentNode] + [nextNode]
    return -1


def solution() :
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    startNode = 'A'
    endNode = 'F'

    return bfs_shortest_path(startNode, endNode, graph)

print(solution())

