from collections import defaultdict
def dfs(start, path, graph, N) :
    if len(path) == N:
        return path
    
    for g in graph[start]:
        if g[1] != True:
            path.append(g[0])
            g[1] = True
            path = dfs(g[0], path, graph, N)
            
            if len(path) < N:
                path.pop()
                g[1] = False
                
    return path


def solution(tickets):
    answer = []
    graph = defaultdict(list)
    N = len(tickets) + 1
        
    for t in tickets :
        graph[t[0]].append([t[1], False])
    
    for key, value in graph.items() :
        value.sort()
    
    return dfs("ICN", ["ICN"], graph, N)