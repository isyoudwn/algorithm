# O(n)
# 1시간 30분 소요

from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    q1Sum = sum(queue1)
    q2Sum = sum(queue2)
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    targetNumber = (q1Sum + q2Sum) / 2
    
    overflow = 0
    
    while (True) :
        overflow += 1
        
        if q1[0] > targetNumber  or q2[0] > targetNumber:
            return -1
        
        if q1Sum == targetNumber and q2Sum == targetNumber :
            break
            
        if overflow > 300000 :
            return -1
        
        a = abs(q1Sum - q1[0] - targetNumber)
        b = abs(q1Sum + q2[0] - targetNumber)
        
        if a < b :
            q1Sum = q1Sum - q1[0]
            q2Sum = q2Sum + q1[0]
            
            q2.append(q1.popleft())
            
            answer += 1
            
        else :
            q1Sum = q1Sum + q2[0]
            q2Sum = q2Sum - q2[0]
            
            q1.append(q2.popleft())
            
            answer += 1
        
    return answer