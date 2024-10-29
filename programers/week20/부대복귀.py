from collections import defaultdict, deque

def bfs(start, graph) :
    
    visited = set([start])
    queue = deque([start])
    path = defaultdict(int)
    
    while queue:
        
        now = queue.popleft()

        for next_node in graph[now]:
            if next_node not in visited:
                visited.add(next_node)
                path[next_node] = path[now] + 1
                
        
                queue.append(next_node)
                
        
    return path
                
            


def formatting(roads) :
    graph = defaultdict(list)
    
    for r in roads:
        graph[r[0]].append(r[1])
        graph[r[1]].append(r[0])
        
    return graph

def solution(n, roads, sources, destination):
    answer = []
    graph = formatting(roads)
    result = bfs(destination, graph)

    for s in sources:
        if s in result:
            answer.append(result[s])
        else:
            answer.append(-1)

    
    return answer