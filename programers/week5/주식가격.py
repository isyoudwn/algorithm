from collections import deque

#answer 1
# def solution(prices):
#     deq = deque(prices)
#     answer = []
    
#     while(True):
#         sec = 0
        
#         if len(deq) == 1:
#             answer.append(sec)
#             break
            
#         left = deq.popleft()
        
#         for i in range(0, len(deq)) :
#             if left > deq[i] :
#                 sec = i + 1
#                 break
#             sec = i + 1
                
#         answer.append(sec)
    
#     return answer

#answer 2
def solution(prices):
    deq = deque(prices)
    answer = []
    
    while deq :
        sec = 0
        left = deq.popleft()
        
        for item in deq :
            sec = sec + 1
            if left > item :
                break
            
        answer.append(sec)
    
    return answer