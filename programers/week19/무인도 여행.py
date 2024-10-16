from collections import deque
visited = []

def bfs(start_x, start_y, sumValue, maps) :
    
    global visited

    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    
    queue = deque([(start_x, start_y)])
    visited.append((start_x, start_y))
    sumValue = int(maps[start_x][start_y])
    
    
    while queue:
        x, y = queue.popleft()

        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]
                
            if (0 <= nx < len(maps)) and (0 <= ny < len(maps[0])) and ((nx, ny) not in visited) and (maps[nx][ny] != 'X'):
                visited.append((nx, ny))
                queue.append((nx, ny))
                sumValue += int(maps[nx][ny])
                
    return sumValue
    
    

def solution(maps):
    answer = []
    global visited
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if (i, j) not in visited and maps[i][j] != 'X':
                answer.append(bfs(i, j, 0, maps))

    
    if not answer:
        return[-1]
    
    answer.sort()
    
    return answer