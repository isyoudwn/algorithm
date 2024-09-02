from collections import deque

def solution(order):
    answer = 0
    main = deque([i for i in range(1, len(order) + 1)])
    sub = []
    
    
    for o in order:
        if not main:
            temp = sub.pop()

        elif o == main[0]:
            temp = main.popleft()

        elif o > main[0]:
             while True:
                temp = main.popleft()
                if temp == o:
                    break
                sub.append(temp)
        
        else:
            temp = sub.pop()
    

        if temp == o:
            answer += 1
            
        else:
            break

    
    return answer