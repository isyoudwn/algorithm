from collections import defaultdict

visited = []
path = []

def dfs(graph, st, p):
    if st >= len(graph):
        temp = sorted(p.copy())
        if temp not in path:
            path.append(temp)
        return
    
    for g in graph[st]:
        if g not in visited:
            visited.append(g)
            p.append(g)
            dfs(graph, st + 1, p)
            visited.pop()
            p.pop()
    
    

def solution(user_id, banned_id):
    answer = 0
    
    graph = []

    for idx, value in enumerate(banned_id):
        graph.append([])
        for u in user_id:
            if len(u) == len(value):
                for i in range(0, len(value)):
                    if value[i] != u[i] and value[i] != '*':
                        break
                else:
                    graph[idx].append(u) 

    
    dfs(graph, 0, [])
    
    answer = len(path)
    
    return answer