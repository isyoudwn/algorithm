def solution(n):
    answer = 0
    
    #base-case
    A = 1
    B = 2
    C = 0
    
    for i in range(3, n + 1):
        
        C = A + B
        
        A = B
        B = C
        
    answer = C % 1000000007
    
    return answer