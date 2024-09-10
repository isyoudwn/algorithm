from collections import deque

def bfs(start_x, start_y, end_x, end_y, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n, m = len(graph), len(graph[0])
    
    visited = set([(start_x, start_y)])
    queue = deque([(start_x, start_y, 0)])

    while queue:
        x, y, distance = queue.popleft()

        if x == end_x and y == end_y:
            return distance
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if (nx, ny) not in visited:
                    if graph[nx][ny] != 'X':
                        visited.add((nx, ny))
                        queue.append((nx, ny, distance + 1))
                        
    return -1  
    

def solution(maps):
    answer = 0
    graph = []
    
    start_x = 0
    start_y = 0
    
    labber_x = 0
    labber_y = 0
    
    end_x = 0
    end_y = 0
    
    for m in maps:
        graph.append(list(m))
        
    for i in range(0, len(graph)):
        for j in range(0, len(graph[0])):
            if graph[i][j] == 'S':
                start_x = i
                start_y = j
                
            elif graph[i][j] == 'L':
                labber_x = i
                labber_y = j
                
            elif graph[i][j] == 'E':
                end_x = i
                end_y = j
    
    distance_labber = bfs(start_x, start_y, labber_x, labber_y, graph)
    distance_end = bfs(labber_x, labber_y, end_x, end_y, graph)
    
    if distance_labber == -1 or distance_end == -1 :
        return -1
    
    answer = distance_labber + distance_end

    
    return answer