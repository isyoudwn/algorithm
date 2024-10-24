from collections import defaultdict, deque

def bfs(start, graph) :
    
    queue = deque([start])
    visited = set([start])
    path = defaultdict(int)
    path[start] = 0
    
    while queue:
        
        now = queue.popleft()
        
        for g in graph[now]:
            if g not in visited:
                queue.append(g)
                visited.add(g)
                path[g] = path[now] + 1
                
    return path
                

def solution(n, edge):
    answer = 0
    graph = defaultdict(list)
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        
    path = bfs(1, graph)
    path = sorted(path.items(), key=lambda x:x[1], reverse=True)

    maxValue = path[0][1]
    
    for p in path:
        if p[1] == maxValue:
            answer += 1
   
    return answer