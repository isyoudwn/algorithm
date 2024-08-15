from collections import deque
path = []
N = 1



def dfs(current, graph, temp) :
    global path, N
    
    if current not in graph:
        return
    
    for nextNode in graph[current]:
        if nextNode[1] != 1:
            nextNode[1] = 1
            temp.append(nextNode[0])
            dfs(nextNode[0], graph, temp)
            
            if len(temp) == N:
                path.append(temp.copy())
            temp.pop()
            nextNode[1] = 0
    return
        
    

def solution(tickets):
    global path, N
    
    answer = []
    graph = {}
    
    for t in tickets:
        if t[0] not in graph:
            graph[t[0]] = []
    
    for t in tickets:
        graph[t[0]].append([t[1], 0])
        
    N = N + len(tickets)
        
    
    dfs("ICN", graph, ["ICN"])

    path.sort()
    answer = path[0]
        
    return answer