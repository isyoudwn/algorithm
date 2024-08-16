def solution(dirs):
    
    
    answer = 0
    N = len(dirs)
    visited = []
    directions = {
        'U' : (0, 1),
        'L' : (-1, 0),
        'R' : (1, 0),
        'D' : (0, -1)
    }
    
    now = [0,0]
    
    for i in range(0, N):
        d = dirs[i]
        temp_x = directions[d][0] + now[0]
        temp_y = directions[d][1] + now[1]
        
        if (temp_x <= 5 and temp_y <= 5) and (temp_x >= -5 and temp_y >= -5):
            
            if [(temp_x, temp_y), (now[0], now[1])] not in visited:
                visited.append([(temp_x, temp_y), (now[0], now[1])])
                visited.append([(now[0], now[1]), (temp_x, temp_y)])
                answer += 1
                
            now[0] = temp_x
            now[1] = temp_y
            
        else:
            continue
        
    
    return answer