from collections import deque

def bfs(start_x, start_y, graph) :
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(start_x, start_y)])
    visited = set([(start_x, start_y)])
    distance = {(start_x,start_y) : 1}
    
    while queue:
        x, y = queue.popleft()
        
        if x == len(graph) - 1 and y == len(graph[0]) - 1 :
            return distance[(x, y)]
        
        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if (nx, ny) not in visited :
                    if graph[nx][ny] == 1:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
                        distance[(nx, ny)] = distance[(x, y)] + 1
    
    return -1
                    

def solution(maps):
    answer = 0
    answer = bfs(0,0,maps)

    return answer