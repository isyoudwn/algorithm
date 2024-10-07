import math

def solution(n, stations, w):
    answer = 0
    start = 1
    
    for s in stations:
        front = s - w - start
        start = s + w + 1
        
        answer += math.ceil(front / (w * 2 + 1))

    if start <= n:
        front = n + 1 - start
        answer += math.ceil(front / (w * 2 + 1)) 
        

        
    return answer