def solution(n):
    answer = 0
    
    for i in range(1, n + 1):
        temp = i
        
        if temp == n:
            answer = answer + 1
            continue
        
        for j in range(i + 1, n + 1):
            
            if temp == n:
                answer = answer + 1
                break
            
            elif temp > n:
                break
                
            else:
                temp = temp + j
                
    
    return answer