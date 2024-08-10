# 35분 소요

from collections import deque

def bfs(start, graph) :
    queue = deque([start])
    visited = set([start])
    distance = { start : 0 }
    
    while queue:
        
        currentNode = queue.popleft()
        
        for nextNode in graph[currentNode] :
            if nextNode not in visited:
                queue.append(nextNode)
                visited.add(nextNode)
                distance[nextNode] = distance[currentNode] + 1
                
    return distance

def formattingGraph(n, edge) :
    
    graph = {}
        
    for i in range(1, n + 1) :
        graph[i] = []
        
    for v in edge :
        graph[v[1]].append(v[0])
        graph[v[0]].append(v[1])
        
    return graph
                
            
def solution(n, edge):
    answer = 0
    
    graph = formattingGraph(n, edge)
    
    distance = bfs(1, graph)
    
    maxdistance = max(distance.values())
    
    for key, value in distance.items():
        if value == maxdistance:
            answer += 1
    
    return answer