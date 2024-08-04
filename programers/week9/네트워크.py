from collections import deque

def bfs(startNode, visited, graph) :
    queue = deque([startNode])
    path = [startNode]
    
    while queue:
        number = queue.popleft()
        
        for nextNode in graph[number]:
            if nextNode not in visited:
                visited.add(nextNode)
                queue.append(nextNode)
                path.append(nextNode)
            
    return 1


def solution(n, computers):
    answer = 0
    graph = {}
    visited = set([])
    
    for i in range(0, n):
        graph[i] = []

        for j in range(0, len(computers[i])):
             if computers[i][j] == 1 and i != j:
                    graph[i].append(j)

    for g in graph:
        if g not in visited:
            visited.add(g)
            answer += bfs(g, visited, graph)
            

    return answer