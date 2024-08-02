from collections import deque

def bfs_shortest_distance(startNode, targetNode, graph) :
    queue = deque([startNode])
    visited = set([startNode])
    distance = {startNode : 0}
    
    while queue:
        currentNode = queue.popleft()
        if currentNode == targetNode :
            return distance[currentNode]

        for nextNode in graph[currentNode] :
            if nextNode not in visited :
                visited.add(nextNode)
                queue.append(nextNode)
                distance[nextNode] = distance[currentNode] + 1
            

def solution() :
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    print(bfs_shortest_distance('A', 'F', graph))

solution()