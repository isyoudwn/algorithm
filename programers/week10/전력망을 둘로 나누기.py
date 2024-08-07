# 50분 소요

from collections import deque

def bfs(start, graph) :
    queue = deque([start])
    visited = set([start])
    nodeNum = 1
    
    while queue:
        currentNode = queue.popleft()
        visited.add(currentNode)
        
        for nextNode in graph[currentNode]:
            if nextNode not in visited:
                visited.add(nextNode)
                queue.append(nextNode)
                nodeNum = nodeNum + 1

    return nodeNum
        

def solution(n, wires):
    answer = -1
    graph = {}
    
    # graph 형태로 만듭니다.
    for w in wires :
        if w[0] not in graph:
            graph[w[0]] = [w[1]]
        else:
            graph[w[0]].append(w[1])
        if w[1] not in graph:
            graph[w[1]] = [w[0]]
        else:
            graph[w[1]].append(w[0])
        
    # wires를 탐색하며 전력망을 끊고, 차이를 구합니다.
    # 만약 차이가 기존 것 보다 작다면 그 수를 answer에 넣습니다.
    for w in wires:
        graph[w[1]].remove(w[0])
        graph[w[0]].remove(w[1])

        result = abs(bfs(w[1], graph) - bfs(w[0], graph))
        
        if answer < 0 :
            answer = result
            
        else :
            if answer > result:
                answer = result
                
        graph[w[1]].append(w[0])
        graph[w[0]].append(w[1])


    return answer